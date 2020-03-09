# -*- coding: utf-8 -*-
"""
Created on Wed Mar 04 16:15 2020
Somatic Membrane Impedance Measurement
@author: Andrew Brughera 
"""
from brian2 import cm, um, mV, pA, uF, ohm, siemens, ms, second, Hz
#from brian2 import SpikeGeneratorGroup, SpatialNeuron, Soma, Cylinder, Synapses
from brian2 import SpatialNeuron, Soma, Cylinder
#from brian2 import SpikeMonitor, StateMonitor, Network, run
from brian2 import StateMonitor, run
from brian2 import defaultclock
from math import exp
import numpy as np
import matplotlib.pyplot as plt

defaultclock.dt=0.02*ms # for better precision

# Morphology of the model MSO soma only
# soma:
# morpho = Cylinder(length=40*um, diameter=20*um, n=2)
morpho = Soma(diameter=30.*um)
# contralateral dendrite:
morpho.cDend = Cylinder(length=150.*um, diameter=3.5*um, n=20)
# ipsilateral dendrite:
morpho.iDend = Cylinder(length=150.*um, diameter=3.5*um, n=20)
# axon:
morpho.axon = Cylinder(length=400.*um, diameter=2.*um, n=51)

temp_degC = 37.  # temperature in degree celcius
# Temperature-dependent rate increase of ion-channels
q10 = 3. ** ((temp_degC - 22) / 10.)
# Membrane Parameters
# (capacitance/area is defined in the SpatialNeuron)
EK = -106. * mV
ENa = 62.1 * mV
EH = -43. * mV
# Passive channels
EL = -65. * mV
gL = 0.00005 * siemens/cm**2

# Ion-channel and Circuit Equations  
# Na channel from Scott et al. 2010
eqs_Na = """
dm/dt=q10*(minf-m)/mtau : 1
dh/dt=q10*(hinf-h)/htau : 1
minf = 1./(1+exp((v/mV + 46.) / (-11.))) : 1
hinf = 1./(1+exp((v/mV + 62.5) / 7.77)) : 1
mtau = ((0.141 + (-0.0826 / (1 + exp((-20.5 - v/mV) / 10.8)))) / 3.)*ms : second
htau = ((4. + (-3.74 / (1 + exp((-40.6 - v/mV) / 5.05)))) / 3.)*ms : second
gNabar : siemens/meter**2
"""

# KLT channel (low threshold K+) from Mathews et al. 2010
eqs_Klt = """
dw/dt=q10*(winf-w)/wtau : 1
dz/dt=q10*(zinf-z)/ztau : 1
winf = 1./(1+exp((v/mV + 57.34)/(-11.7))) : 1
k = 0.27 : 1
zinf = ((1.- k)/(1+exp((v/mV+67.)/6.16))) + k : 1
wtau = ((21.5/((6.*exp((v/mV+60.)/7.))+(24.*exp(-1*(v/mV+60.)/50.6))))+0.35)*ms : second
ztau = ((170./(5.*exp((v/mV+60.)/10.)+exp((v/mV+70.)/8.)))+10.7)*ms : second
gKltbar : siemens/meter**2
"""

# Hyperpolarizarion-activated cyclic nucleotide (HCN, iH) channel, non-inactivating
# from Rothman and Manis 2003
eqs_H = """
dr/dt=q10*(rinf-r)/rtau : 1
rinf = 1. / (1+exp((v/mV + 76.) / 7.)) : 1
rtau = ((100000. / (237.*exp((v/mV+60.) / 12.) + 17.*exp(-(v/mV+60.) / 14.))) + 25.)*ms : second
gHbar : siemens/meter**2
"""

# Synaptic inputs work with the full model - soma, dendrites, axon
#eqs= """
#Im = gNabar*m**4*((0.993*h) + 0.007)*(ENa-v) + gKltbar*w**4*z*(EK-v) + gHbar*r*(EH-v) + gL*(EL-v) : amp/meter**2
#Is_eCo = gs_eCo * (Es_e - v) : amp (point current)
#dgs_eCo/dt = -gs_eCo/taus_e : siemens
#Is_eIp = gs_eIp * (Es_e - v) : amp (point current)
#dgs_eIp/dt = -gs_eIp/taus_e : siemens
#"""

## For membrane impedance measurement, inject a current containing a frequency sweep
eqs= """
Im = gNabar*m**4*((0.993*h) + 0.007)*(ENa-v) + gKltbar*w**4*z*(EK-v) + gHbar*r*(EH-v) + gL*(EL-v) : amp/meter**2
I : amp (point current)
"""

eqs += eqs_Na + eqs_Klt + eqs_H


nrn = SpatialNeuron(morphology=morpho, model=eqs, Cm=1.*uF/cm**2, Ri=150.*ohm*cm, method='exponential_euler')

# Local Membrane Parameters; nrn.main is the soma
nrn.main.gNabar = 0.0432 * siemens/cm**2  # 0.072
nrn.main.gKltbar = 0.0324 * siemens/cm**2 # 0.054
nrn.main.gHbar = 0.01296 * siemens/cm**2 # 0.021

nrn.cDend.gNabar = 0.0 * siemens/cm**2
nrn.cDend.gKltbar = 0.00132 * siemens/cm**2 # 0.0022
nrn.cDend.gHbar = 0.00066 * siemens/cm**2 # 0.0011

nrn.iDend.gNabar = 0.0 * siemens/cm**2
nrn.iDend.gKltbar = 0.00132 * siemens/cm**2 # 0.0022
nrn.iDend.gHbar = 0.00066 * siemens/cm**2 # 0.0011

nrn.axon.gNabar = 0.25 * siemens/cm**2
nrn.axon.gKltbar = 0.0595 * siemens/cm**2
nrn.axon.gHbar = 0.0025 * siemens/cm**2

# Initialize to a resting state 
vRestSoma = -60.5222*mV
vRestDend = -60.5285*mV
vRestAxon = -64.3498*mV
# Soma 
nrn.main.v = vRestSoma
nrn.main.m = 1./(1+exp((vRestSoma/mV + 46.) / (-11.)))
nrn.main.h = 1./(1+exp((vRestSoma/mV + 62.5) / 7.77))
nrn.main.w = 1./(1+exp((vRestSoma/mV + 57.34)/(-11.7)))
k_init = 0.27
nrn.main.z = ((1.- k_init)/(1+exp((vRestSoma/mV+67.)/6.16))) + k_init
nrn.main.r = 1. / (1+exp((vRestSoma/mV + 76.) / 7.))
# ContraLateral Denrite
nrn.cDend.v = vRestDend
nrn.cDend.m = 1./(1+exp((vRestDend/mV + 46.) / (-11.)))
nrn.cDend.h = 1./(1+exp((vRestDend/mV + 62.5) / 7.77))
nrn.cDend.w = 1./(1+exp((vRestDend/mV + 57.34)/(-11.7)))
nrn.cDend.z = ((1.- k_init)/(1+exp((vRestDend/mV+67.)/6.16))) + k_init
nrn.cDend.r = 1. / (1+exp((vRestDend/mV + 76.) / 7.))
# IpsiLateral Denrite
nrn.iDend.v = vRestDend
nrn.iDend.m = 1./(1+exp((vRestDend/mV + 46.) / (-11.)))
nrn.iDend.h = 1./(1+exp((vRestDend/mV + 62.5) / 7.77))
nrn.iDend.w = 1./(1+exp((vRestDend/mV + 57.34)/(-11.7)))
nrn.iDend.z = ((1.- k_init)/(1+exp((vRestDend/mV+67.)/6.16))) + k_init
nrn.iDend.r = 1. / (1+exp((vRestDend/mV + 76.) / 7.))
# Axon
nrn.axon.v = vRestAxon
nrn.axon.m = 1./(1+exp((vRestAxon/mV + 46.) / (-11.)))
nrn.axon.h = 1./(1+exp((vRestAxon/mV + 62.5) / 7.77))
nrn.axon.w = 1./(1+exp((vRestAxon/mV + 57.34)/(-11.7)))
nrn.axon.z = ((1.- k_init)/(1+exp((vRestAxon/mV+67.)/6.16))) + k_init
nrn.axon.r = 1. / (1+exp((vRestAxon/mV + 76.) / 7.))

msoSomaState = StateMonitor(nrn.main, ['v','I'], record=True)
#msoAxonState = StateMonitor(nrn, ['v','I'], record=morpho.axon[200*um])
#msocDendState = StateMonitor(nrn, ['v','I'], record=morpho.cDend[75*um])
#msoiDendState = StateMonitor(nrn, ['v','I'], record=morpho.iDend[75*um])

# Current input / Zap frequency-sweep parameters
sweepdur = 1.0*second
#sweepdur_ms = 960*ms
f_max = 2000*Hz
f_min = 1*Hz
m2000 = (f_max - f_min)/(2*(sweepdur - defaultclock.dt))
t_settle = 100*ms
t_bias = 900*ms
I_Bias = 900*pA
I_Zap_Max = 250*pA

# Initialize the injected current to zero - probably redundant
nrn.I = 0.0*pA
# Settle the membrane
run(t_settle, report='text')  # Go to rest

# Set the injected current in the soma to the bias current
nrn.I[0] = I_Bias
run(t_bias, report='text')  # Equilibrate to I_Bias
IBiasStr = 'IBias' + str(int(I_Bias/pA)) + 'pA'


# Add the "zap" frequency-sweep current to the injected current in the soma
sweepNsamples = round(sweepdur/defaultclock.dt)
for k in range(sweepNsamples):
    t1 = (k * defaultclock.dt)
    nrn.I[0] = I_Bias + I_Zap_Max * np.sin(2*np.pi*(m2000*t1 + f_min) * t1)
    run(defaultclock.dt, report='text')

IZapMaxStr = 'IZapMax' + str(int(I_Zap_Max/pA)) + 'pA'

# Remove the frequency-sweep current
nrn.I[0] = I_Bias
run(100*ms, report='text')

# Remove the bias current
nrn.I[0] = 0*pA
run(100*ms, report='text')

plt.plot(msoSomaState.t / ms, msoSomaState.v[0] / mV)
plt.xlabel('t (ms)')
plt.ylabel('v (mV)')
#plt.ylim((-65,-45))
plt.show()

fftStart = round((t_settle + t_bias)/defaultclock.dt)
fftStop = round((t_settle + t_bias + sweepdur)/defaultclock.dt)
Vfft = np.fft.fft(msoSomaState.v[0][fftStart:fftStop])
Ifft = np.fft.fft(msoSomaState.I[0][fftStart:fftStop])
Zfft = np.divide(Vfft, Ifft)

plt.semilogx(range(10,1000),abs(Vfft[10:1000])) # For now, 1-Hz resolution, drop 0 Hz (large DC)
plt.show()

plt.semilogx(range(10,1000),abs(Ifft[10:1000])) # For now, 1-Hz resolution, drop 0 Hz (large DC)
plt.show()

timeVmemFileStr = 'timeVmemMsoSomaEfn3_' + IBiasStr + '_' + IZapMaxStr + '.txt'
file9 = open(timeVmemFileStr,'w')
for index in range(len(msoSomaState.t)):
    file9.write(str(msoSomaState.t[index] / ms) + " " + str(msoSomaState.v[0][index] / mV) + '\n')
file9.close()

Zfft_CoreFileStr = 'ZfftMsoSomaEfn3_' + IBiasStr + '_' + IZapMaxStr
absZfft_CoreFileStr = 'absZfftMsoSomaEfn3_' + IBiasStr + '_' + IZapMaxStr
file10 = open(Zfft_CoreFileStr  + '.txt','w')
file11 = open(absZfft_CoreFileStr  + '.txt','w')
for index in range(len(Zfft)):
    file10.write(str((index/len(Zfft)) * (1/defaultclock.dt)/Hz) + " " + str(Zfft[index]) + '\n')
    file11.write(str((index/len(Zfft)) * (1/defaultclock.dt)/Hz) + " " + str(abs(Zfft[index])) + '\n')
file10.close()
file11.close()

fig_absZ_MsoEfn3, ax = plt.subplots(1, 1)
ax.set_title('model MsoEfn3 (900ms 900pA bias, 250pA Sweep)', fontsize=16)
ax.set_ylabel('impedance (MOhm)', fontsize=16)
ax.set_xlabel('frequency (Hz)', fontsize=16)
ax.set_ylim((0,8))
ax.tick_params(axis='both', which='major', labelsize=16)
ax.semilogx(range(10,2000),abs(Zfft[10:2000])/1e6, linewidth=2.0)
fig_absZ_MsoEfn3.tight_layout()
fig_absZ_MsoEfn3.savefig(absZfft_CoreFileStr + '.png', dpi=300)
