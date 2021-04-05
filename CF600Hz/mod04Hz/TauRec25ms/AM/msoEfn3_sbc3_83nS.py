# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 10:08:16 2018

@author: Andrew Brughera 
"""
from __future__ import division
# from __future__ import division, absolute_import, print_function

#import numpy as np
#import random
#import pandas as pd

#import brian2
#from brian2 import *
#from brian2.units import cm, um, mV, amp, uF, ohm, siemens, nS, ms, second
from brian2 import cm, um, mV, amp, uF, ohm, siemens, nS, ms, second
from brian2 import SpikeGeneratorGroup, SpatialNeuron, Soma, Cylinder, Synapses
from brian2 import SpikeMonitor, StateMonitor, Network, run
from brian2 import defaultclock
from math import exp
import numpy as np
import matplotlib.pyplot as plt

def mkmsoEn(inputSpkFileTuple, temp_degC=37):
    
    defaultclock.dt=0.02*ms # for better precision
    #v_init = -63.* mV     	
    
    #def make_mso_neuron(NrnGrpsContra, NrnGrpsIpsi, 
    #                    gEco=18.*1e-9, gEip=18.*1e-9,
    #                    gIco=2.*1e-9, gIip=0.4*1e-9, 
    #                    temp_degC=37.):
    #
    
    
#    nGbcsCo = 4
#    nGbcsIp = 4
    nSbcsCo = 4
    nSbcsIp = 4
    
    # Start with an ipsilateral-leading IPD of 90 degrees at the beginning of 
    # the amplitude modulation cycle:
    #sbCoSpkFile = 'sb3SpTMmsCF600HzCa616HzStPhsN090AMBB32Hz75dBsplMdSpSpec3.txt'
    #sbIpSpkFile = 'sb3SpTMmsCF600HzCa584HzStPhs000AMBB32Hz75dBsplMdSpSpec3.txt'
    #gbCoSpkFile = 'gbSpTMmsCF600HzCa616HzStPhsN090AMBB32Hz75dBsplMdSpSpec3.txt'
    #gbIpSpkFile = 'gbSpTMmsCF600HzCa584HzStPhs000AMBB32Hz75dBsplMdSpSpec3.txt'
    sbCoSpkFile = inputSpkFileTuple[0]
    sbIpSpkFile = inputSpkFileTuple[1]
#    gbCoSpkFile = inputSpkFileTuple[2]
#    gbIpSpkFile = inputSpkFileTuple[3]
    
    sbCoIdxSpktimeArray = np.loadtxt(sbCoSpkFile)
    sbCoCellIndices = sbCoIdxSpktimeArray[:, 0].astype(int)
    sbCoSpkTimes = sbCoIdxSpktimeArray[:, 1] * ms
    sbCoSpkGenGrp = SpikeGeneratorGroup(nSbcsCo, sbCoCellIndices, sbCoSpkTimes)
    
    sbIpIdxSpktimeArray = np.loadtxt(sbIpSpkFile)
    sbIpCellIndices = sbIpIdxSpktimeArray[:, 0].astype(int)
    sbIpSpkTimes = sbIpIdxSpktimeArray[:, 1] * ms
    sbIpSpkGenGrp = SpikeGeneratorGroup(nSbcsIp, sbIpCellIndices, sbIpSpkTimes)
    
#    gbCoIdxSpktimeArray = np.loadtxt(gbCoSpkFile)
#    gbCoCellIndices = gbCoIdxSpktimeArray[:, 0].astype(int)
#    gbCoSpkTimes = gbCoIdxSpktimeArray[:, 1] * ms
#    gbCoSpkGenGrp = SpikeGeneratorGroup(nGbcsCo, gbCoCellIndices, gbCoSpkTimes)
#    
#    gbIpIdxSpktimeArray = np.loadtxt(gbIpSpkFile)
#    gbIpCellIndices = gbIpIdxSpktimeArray[:, 0].astype(int)
#    gbIpSpkTimes = gbIpIdxSpktimeArray[:, 1] * ms
#    gbIpSpkGenGrp = SpikeGeneratorGroup(nGbcsIp, gbIpCellIndices, gbIpSpkTimes)
    
    
    # Morphology of the model MSO Neuron
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
    # Synaptic parameters
    Es_e = 0.*mV
#    Es_i = -90.*mV
    taus_e = 0.4*ms
#    taus_i = 1.*ms
    '''Variables for synaptic weights are unitless according to Brian2.
    The effective unit is siemens for use amp*siemens=volt eqns.
    So we multiply w_eCo,w_eIp,w_iCo,w_iIp  by unit siemens when adding each
    to g on_pre synaptic spikes. We use these local variables for synaptic weight, 
    and not the standard w because...
    The synapses'synaptic weight (e.g., Syn_eCo.w) references the Same State Variable
    as klt activation w for it's SpatialNeuron (nrn.w here) or NeuronGroup. 
    This way klt activation and synaptic weight are identical and quite ridiculous.
    We used local variables w_iCo and w_iIp (other than w) for synaptic weights of 
    summed synapses, but had to use constant for the synapses that target
    individual compartments of the dendrites.'''
    w_eCo=36.e-9
    w_eIp=36.e-9
    #w_iCo=2.e-9
    #w_iIp=0.4e-9
#    w_iCo=0.e-9
#    w_iIp=0.e-9
    
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
    wtau = ((21.5/((6.*exp((v/mV+60.)/7.))+(24.*exp(-(v/mV+60.)/50.6))))+0.35)*ms : second
    ztau = ((170./(5.*exp((v/mV+60.)/10.)+exp(-(v/mV+70.)/8.)))+10.7)*ms : second
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
    
    #eqs= """
    #Im = gNabar*m**4*((0.993*h) + 0.007)*(ENa-v) + gKltbar*w**4*z*(EK-v) + gHbar*r*(EH-v) + gL * (EL - v) - Cm*dv/dt : amp/meter**2
    #Is_eCo = gs_eCo * (Es_e - v) : amp (point current)
    #dgs_eCo/dt = -gs_eCo/taus_e : siemens/second
    #Is_eIp = gs_eIp * (Es_e - v) : amp (point current)
    #dgs_eIp/dt = -gs_eIp/taus_e : siemens/second
    #Is_iCo = gs_iCo * (Es_i - v) : amp (point current)
    #gs_iCo : siemens
    #Is_iIp = gs_iIp * (Es_i - v) : amp (point current)
    #gs_iIp : siemens
    #"""
#    eqs= """
#    Im = gNabar*m**4*((0.993*h) + 0.007)*(ENa-v) + gKltbar*w**4*z*(EK-v) + gHbar*r*(EH-v) + gL*(EL-v) : amp/meter**2
#    Is_eCo = gs_eCo * (Es_e - v) : amp (point current)
#    dgs_eCo/dt = -gs_eCo/taus_e : siemens
#    Is_eIp = gs_eIp * (Es_e - v) : amp (point current)
#    dgs_eIp/dt = -gs_eIp/taus_e : siemens
#    Is_iCo = gs_iCo * (Es_i - v) : amp (point current)
#    gs_iCo : siemens
#    Is_iIp = gs_iIp * (Es_i - v) : amp (point current)
#    gs_iIp : siemens
#    """
    eqs= """
    Im = gNabar*m**4*((0.993*h) + 0.007)*(ENa-v) + gKltbar*w**4*z*(EK-v) + gHbar*r*(EH-v) + gL*(EL-v) : amp/meter**2
    Is_eCo = gs_eCo * (Es_e - v) : amp (point current)
    dgs_eCo/dt = -gs_eCo/taus_e : siemens
    Is_eIp = gs_eIp * (Es_e - v) : amp (point current)
    dgs_eIp/dt = -gs_eIp/taus_e : siemens
    """
    
    eqs += eqs_Na + eqs_Klt + eqs_H
    
    '''threshold_location: for the midpoint of the axon,
    threshold_location = 'morpho.axon[200.*um]' caused an 'axon' not resolved error.
    threshold_location = morpho.axon[200.*um] caused
    TypeError: "object of type 'numpy.int64' has no len()" 
    So used the compartment number 66 (in morpho, indexing begins with 0),
    66 = index 0 (soma) + 20 cDend) + 20 (iDend) + 26 (26th of 51 axon compartments)
    '''
    nrn = SpatialNeuron(morphology=morpho, model=eqs, method='exponential_euler',
                        threshold='v > -20.*mV',
                        threshold_location=66,
                        refractory='v > -35.*mV',
                        Cm = 1.*uF/cm**2, Ri = 150.*ohm*cm)
                        #threshold_location=morpho.axon[200.*um])
    
    #nrn = SpatialNeuron(morphology=morpho, model=eqs, method='exponential_euler',
    #                    threshold='v > -20.*mV',
    #                    threshold_location=,
    #                    refractory='v > -35.*mV',morpho.axon[200.*um]
    #                    Cm = 1.*uF/cm**2, Ri = 150.*ohm*cm)
    #                    #threshold_location=morpho.axon[200.*um])
    
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
    
    # Synapses
    # Could not resolve local variable w_eCo in gs_eCo eqn
    # So entered synaptic weight as numerical value
    # 'gs_eCo += 21.e-9*siemens' for 600 Hz
    Syn_eCo = Synapses(sbCoSpkGenGrp, nrn, on_pre='gs_eCo += w_eCo*siemens')
    Syn_eCo.connect(i=0, j=morpho.cDend[150.*(0.4 + 0.025)*um])
    Syn_eCo.connect(i=1, j=morpho.cDend[150.*(0.45 + 0.025)*um])
    Syn_eCo.connect(i=2, j=morpho.cDend[150.*(0.5 + 0.025)*um])
    Syn_eCo.connect(i=3, j=morpho.cDend[150.*(0.55 + 0.025)*um])
    
    # Could not resolve local variable w_eIp in gs_eCo eqn
    # So entered numerical value
    Syn_eIp = Synapses(sbIpSpkGenGrp, nrn, on_pre='gs_eIp += w_eIp*siemens')
    Syn_eIp.connect(i=0, j=morpho.iDend[150.*(0.4 + 0.025)*um])
    Syn_eIp.connect(i=1, j=morpho.iDend[150.*(0.45 + 0.025)*um])
    Syn_eIp.connect(i=2, j=morpho.iDend[150.*(0.5 + 0.025)*um])
    Syn_eIp.connect(i=3, j=morpho.iDend[150.*(0.55 + 0.025)*um])
        
#    Syn_iCo = Synapses(gbCoSpkGenGrp, nrn.main, 
#                       model='''dg/dt = -g/taus_e : siemens (clock-driven)
#                                gs_iCo_post = g : siemens (summed)''',
#                       on_pre='g += w_iCo*siemens')
#    Syn_iCo.connect(True)
#    
#    Syn_iIp = Synapses(gbIpSpkGenGrp, nrn.main, 
#                       model='''dg/dt = -g/taus_e : siemens (clock-driven)
#                                gs_iIp_post = g : siemens (summed)''',
#                       on_pre='g += w_iIp*siemens')
#    Syn_iIp.connect(True)
    
    # Initialize synaptic g's
    #    gs_eCo0 = 0
    #    gs_eCo1 = 0.
    #    gs_eCo2 = 0.
    #    gs_eCo3 = 0.
    #    gs_eIp0 = 0.
    #    gs_eIp1 = 0.
    #    gs_eIp2 = 0.
    #    gs_eIp3 = 0.
    #    gs_iCo = 0.
    #    gs_iIp = 0.
    
    msoAxonSpks = SpikeMonitor(nrn)
    #msoSomaState = StateMonitor(nrn, ['v','gs_eCo','gs_eIp','gs_iCo','gs_iIp'], record=True)
    msoSomaState = StateMonitor(nrn, 'v', record=True)
    msoAxonState = StateMonitor(nrn, 'v', record=morpho.axon[200*um])
    msocDendState = StateMonitor(nrn, 'v', record=morpho.cDend[75*um])
    msoiDendState = StateMonitor(nrn, 'v', record=morpho.iDend[75*um])
    #msoSynapses = Syn_eCo, Syn_eIp, Syn_iCo, Syn_iIp
    
    run(800*ms, report='text')
        
    #plt.plot(msoSomaState.t / ms, msoSomaState[0].v / mV)
    #plt.xlabel('t (ms)')
    #plt.ylabel('v (mV)')
    #plt.show()
    plt.plot(msoSomaState.t / ms, msoAxonState.v[0] / mV)
    plt.xlabel('t (ms)')
    plt.ylabel('v (mV)')
    plt.show()
    #plt.plot(msoSomaState.t / ms, msocDendState.v[0] / mV)
    #plt.plot(msoSomaState.t / ms, msoiDendState.v[0] / mV)
    
    #sbCoSpkFile = 'sb3SpTMmsCF600HzCa616HzStPhsN090AMBB32Hz75dBsplMdSpSpec3.txt'
    #msoSpkFile = 'msoSpTMms' + anfSpkFile[10:len(anfSpkFile)]
    #msoSpkFile = 'mson' + sbCoSpkFile[3:6] + sbCoSpkFile[9:16] + 'StIPDn90C' + sbCoSpkFile[23:len(sbCoSpkFile)]
    #msoSpkFile = 'msonSpTs3' + sbCoSpkFile[9:16] + 'StIPDn90C' + sbCoSpkFile[23:len(sbCoSpkFile)]
    
    PhsStrCo = sbCoSpkFile[32:36]
    PhsStrIp = sbIpSpkFile[32:36]
    if (PhsStrCo[0] == 'N'):
        PhsIntCo = -1 * int(PhsStrCo[1:4])
    else:
        PhsIntCo = int(PhsStrCo[0:3])
    if (PhsStrIp[0] == 'N'):
        PhsIntIp = -1 * int(PhsStrIp[1:4])
    else:
        PhsIntIp = int(PhsStrIp[0:3])
    IPD = (PhsIntCo - PhsIntIp) % 360
    IPDstr = str(IPD)
#    while (len(IPDstr) < 3):
#        IPDstr = '0' + IPDstr
    msoSpkFile = 'msonSpT83s3CaCF' + sbCoSpkFile[14:19] + 'IPD' + IPDstr + 'C' + sbCoSpkFile[27:len(sbCoSpkFile)]
    file0 = open(msoSpkFile,'w')
    for index in range(len(msoAxonSpks.t)):
        #file0.write(str(msoAxonSpks.i[index]) + " " + str(msoAxonSpks.t[index] / ms) + '\n')
        file0.write(str(msoAxonSpks.t[index] / ms) + '\n')
    file0.close()
    
    msonTuple = (nrn, msoAxonSpks, msoSomaState, msoAxonState, msocDendState, msoiDendState)
    
    return msonTuple

## end mkmson