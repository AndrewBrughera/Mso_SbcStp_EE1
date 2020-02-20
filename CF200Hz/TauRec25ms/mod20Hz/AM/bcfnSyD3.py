# -*- coding: utf-8 -*-
"""
Downloaded from Brian2 website on Sat Jan 13 10:02:04 2018

Cochlear neuron model of Rothman & Manis
----------------------------------------
Rothman JS, Manis PB (2003) The roles potassium currents play in
regulating the electrical activity of ventral cochlear nucleus neurons.
J Neurophysiol 89:3097-113.

All model types differ only by the maximal conductances.

Adapted from their Neuron implementation by Romain Brette

Adapted for mso input model by Andrew Brughera
"""
#from brian2.units import *
#from brian2.stdunits import *
from brian2 import mV, amp, pA, pF, siemens, nS, ms, second
from brian2 import SpikeGeneratorGroup, NeuronGroup, Synapses
from brian2 import SpikeMonitor, StateMonitor, Network, run
from brian2 import defaultclock
from math import exp
import numpy as np
import matplotlib.pyplot as plt

# To apply in ipython or script:  from bcfn import mkbcs

def mksbc3SyD(anfSpkFile, temp_degC=37):

    defaultclock.dt = 0.02*ms # for better precision
    
    #temp_degC=37.
    neuron_type='type2'
    
    nSbcs = 4
    nAnfsPerSbc = 3
    #nGbcs = 4
    #nAnfsPerGbc=30
    
    anfIdxSpktimeArray = np.loadtxt(anfSpkFile)
    anfIndices = anfIdxSpktimeArray[:, 0].astype(int)
    nANF = 132
    #anfSpkTimes = [i * second for i in anfIdxSpktimeArray[:, 1]]
    anfSpkTimes = anfIdxSpktimeArray[:, 1] * 1000*ms
    anfSpkGeneratorGrp = SpikeGeneratorGroup(nANF, anfIndices, anfSpkTimes)
    
    # Membrane and Ion-Channel parameters
    C = 12*pF
    EH = -43*mV
    EK = -70*mV  # -77*mV in mod file
    EL = -65*mV
    ENa = 55*mV # 55*mV in RM2003; 50*mv by Brette
    nf = 0.85  # proportion of n vs p kinetics
    zss = 0.5  # steady state inactivation of glt
    # default temp_degC = 37., human body temperature in degree celcius
    # q10 for ion-channel time-constants (RM2003, p.3106):
    q10 = 3. ** ((temp_degC - 22.) / 10.)
    # q10 for ion-channel gbar parameters (RM2003, p.3106):
    q10gbar = 2. ** ((temp_degC - 22.) / 10.)
    # hcno current (octopus cell)
    frac = 0.0
    qt = 4.5 ** ((temp_degC - 33.) / 10.)
    # Synaptic parameters:
    Es_e = 0.*mV
    tausE = 0.2*ms
    '''Synaptic weights are unitless according to Brian2.
    The effective unit is siemens, so they can work in amp, volt, siemens eqns.
    We multiply synaptic weight w_e by unit siemens when adding it to g_e.
    We use a local variable w_e for synaptic weight rather than the standard w:'''
    '''Here's why we use a local variable:
    The synapses sbc3SynE.w synaptic weight references the Same State Variable as 
    as the neuron group sbc3Grp.w (klt activation w).
    Update sbc3Grp.w, and you set sbc3SynE.w to same value, and vice versa.
    This way klt activation and synaptic weight are identical and quite ridiculous.
    So use a local variable other than w for the synaptic weight!'''
    # Undepleted synaptic weights
#    w0_esbc = 70e-9
#    w0_esbc3 = w0_esbc
    w0_esbc3 = 83e-9
    w0_egbc = 6e-9
    # Synaptic Depression from Rudnicki and Hemmert 2017
    # synaptic weights (will vary during simulation)
    # (can be depleted, but are intitialized as not depleted)
#    w_esbc = w0_esbc
#    w_esbc3 = w0_esbc3
#    w_egbc = w0_egbc
    # time constants at which synaptic depression decays
    # 90*ms from Xu-Friedman and Yang, 2008 2009
    tauSyD_esbc = 25*ms
    #tauSyD_egbc = tauSyD_esbc
    '''
    X%-depressing synapses from Tsodyks and Markram, 1997
    The depression level X% is defined as a relative decrease of steady-state 
    synaptic strength sf between the spontaneous rate (SR) (f = 50Hz) and the 
    driven rate (f = 300Hz).
    X% = (1 - (s300Hz/s50Hz))*100
    u = portion synaptics strength depleted with each presynapitc spike
    u = 0.01 # 10% depleting
    u = 0.02 # 30% depleting
    u = 0.05 # 50% depleting
    u = 0.18 # 70% depleting
    '''
    u = 0.5
    
    # Maximal conductances of different cell types in nS
    maximal_conductances = dict(
    type1c=(1000, 150, 0, 0, 0.5, 0, 2),
    type1t=(1000, 80, 0, 65, 0.5, 0, 2),
    type12=(1000, 150, 20, 0, 2, 0, 2),
    type21=(1000, 150, 35, 0, 3.5, 0, 2),
    type2=(1000, 150, 200, 0, 20, 0, 2),
    type2o=(1000, 150, 600, 0, 0, 40, 2) # octopus cell
    )
    gnabar, gkhtbar, gkltbar, gkabar, ghbar, gbarno, gl = [x * nS for x in maximal_conductances[neuron_type]]
    
    # Classical Na channel
    eqs_na = """
    ina = gnabar*m**3*h*(ENa-v) : amp
    dm/dt=q10*(minf-m)/mtau : 1
    dh/dt=q10*(hinf-h)/htau : 1
    minf = 1./(1+exp(-(vu + 38.) / 7.)) : 1
    hinf = 1./(1+exp((vu + 65.) / 6.)) : 1
    mtau =  ((10. / (5*exp((vu+60.) / 18.) + 36.*exp(-(vu+60.) / 25.))) + 0.04)*ms : second
    htau =  ((100. / (7*exp((vu+60.) / 11.) + 10.*exp(-(vu+60.) / 25.))) + 0.6)*ms : second
    """
    
    # KHT channel (delayed-rectifier K+)
    eqs_kht = """
    ikht = gkhtbar*(nf*n**2 + (1-nf)*p)*(EK-v) : amp
    dn/dt=q10*(ninf-n)/ntau : 1
    dp/dt=q10*(pinf-p)/ptau : 1
    ninf = (1 + exp(-(vu + 15) / 5.))**-0.5 : 1
    pinf =  1. / (1 + exp(-(vu + 23) / 6.)) : 1
    ntau = ((100. / (11*exp((vu+60) / 24.) + 21*exp(-(vu+60) / 23.))) + 0.7)*ms : second
    ptau = ((100. / (4*exp((vu+60) / 32.) + 5*exp(-(vu+60) / 22.))) + 5)*ms : second
    """
    
    # Ih channel (subthreshold adaptive, non-inactivating)
    eqs_ih = """
    ih = ghbar*r*(EH-v) : amp
    dr/dt=q10*(rinf-r)/rtau : 1
    rinf = 1. / (1+exp((vu + 76.) / 7.)) : 1
    rtau = ((100000. / (237.*exp((vu+60.) / 12.) + 17.*exp(-(vu+60.) / 14.))) + 25.)*ms : second
    """
    
    # KLT channel (low threshold K+)
    eqs_klt = """
    iklt = gkltbar*w**4*z*(EK-v) : amp
    dw/dt=q10*(winf-w)/wtau : 1
    dz/dt=q10*(zinf-z)/ztau : 1
    winf = (1. / (1 + exp(-(vu + 48.) / 6.)))**0.25 : 1
    zinf = zss + ((1.-zss) / (1 + exp((vu + 71.) / 10.))) : 1
    wtau = ((100. / (6.*exp((vu+60.) / 6.) + 16.*exp(-(vu+60.) / 45.))) + 1.5)*ms : second
    ztau = ((1000. / (exp((vu+60.) / 20.) + exp(-(vu+60.) / 8.))) + 50)*ms : second
    """
    
    # Ka channel (transient K+)
    eqs_ka = """
    ika = gkabar*a**4*b*c*(EK-v): amp
    da/dt=q10*(ainf-a)/atau : 1
    db/dt=q10*(binf-b)/btau : 1
    dc/dt=q10*(cinf-c)/ctau : 1
    ainf = (1. / (1 + exp(-(vu + 31) / 6.)))**0.25 : 1
    binf = 1. / (1 + exp((vu + 66) / 7.))**0.5 : 1
    cinf = 1. / (1 + exp((vu + 66) / 7.))**0.5 : 1
    atau =  ((100. / (7*exp((vu+60) / 14.) + 29*exp(-(vu+60) / 24.))) + 0.1)*ms : second
    btau =  ((1000. / (14*exp((vu+60) / 27.) + 29*exp(-(vu+60) / 24.))) + 1)*ms : second
    ctau = ((90. / (1 + exp((-66-vu) / 17.))) + 10)*ms : second
    """
    
    # Leak
    eqs_leak = """
    ileak = gl*(EL-v) : amp
    """
    
    # h current for octopus cells
    eqs_hcno = """
    ihcno = gbarno*(h1*frac + h2*(1-frac))*(EH-v) : amp
    dh1/dt=(hinfno-h1)/tau1 : 1
    dh2/dt=(hinfno-h2)/tau2 : 1
    hinfno = 1./(1+exp((vu+66.)/7.)) : 1
    tau1 = bet1/(qt*0.008*(1+alp1))*ms : second
    tau2 = bet2/(qt*0.0029*(1+alp2))*ms : second
    alp1 = exp(1e-3*3*(vu+50)*9.648e4/(8.315*(273.16+temp_degC))) : 1
    bet1 = exp(1e-3*3*0.3*(vu+50)*9.648e4/(8.315*(273.16+temp_degC))) : 1 
    alp2 = exp(1e-3*3*(vu+84)*9.648e4/(8.315*(273.16+temp_degC))) : 1
    bet2 = exp(1e-3*3*0.6*(vu+84)*9.648e4/(8.315*(273.16+temp_degC))) : 1
    """
    
#    eqs = """
#    dv/dt = (ileak + ina + ikht + iklt + ika + ih + ihcno + I + Is_e)/C : volt
#    Is_e = gs_e * (Es_e - v) : amp
#    gs_e : siemens
#    vu = v/mV : 1  # unitless v
#    I : amp
#    """
#    eqs += eqs_leak + eqs_ka + eqs_na + eqs_ih + eqs_klt + eqs_kht + eqs_hcno

    eqs_sbc3 = """
    dv/dt = (ileak + ina + ikht + iklt + ika + ih + ihcno + I + Is_e0 + Is_e1 + Is_e2)/C : volt
    Is_e0 = gs_e0 * (Es_e - v) : amp
    gs_e0 : siemens
    Is_e1 = gs_e1 * (Es_e - v) : amp
    gs_e1 : siemens
    Is_e2 = gs_e2 * (Es_e - v) : amp
    gs_e2 : siemens
    vu = v/mV : 1  # unitless v
    I : amp
    """
    
    eqs_sbc3 += eqs_leak + eqs_ka + eqs_na + eqs_ih + eqs_klt + eqs_kht + eqs_hcno
    
    
#    gbcGrp = NeuronGroup(nGbcs, eqs, method='exponential_euler', 
#                        threshold='v > -20*mV', refractory='v > -35*mV')
#    #gbcGrp.I = 2500.0*pA
#    gbcGrp.I = 0.0*pA
#    # Initialize model near v_rest with no inputs
#    gbcGrp.v = -63.6*mV
#    vu = EL/mV # unitless v
#    gbcGrp.m = 1./(1+exp(-(vu + 38.) / 7.))
#    gbcGrp.h = 1./(1+exp((vu + 65.) / 6.))
#    gbcGrp.n = (1 + exp(-(vu + 15) / 5.))**-0.5
#    gbcGrp.p = 1. / (1 + exp(-(vu + 23) / 6.))
#    gbcGrp.r = 1. / (1+exp((vu + 76.) / 7.))
#    gbcGrp.w = (1. / (1 + exp(-(vu + 48.) / 6.)))**0.25
#    gbcGrp.z = zss + ((1.-zss) / (1 + exp((vu + 71.) / 10.)))
#    gbcGrp.a = (1. / (1 + exp(-(vu + 31) / 6.)))**0.25
#    gbcGrp.b = 1. / (1 + exp((vu + 66) / 7.))**0.5
#    gbcGrp.c = 1. / (1 + exp((vu + 66) / 7.))**0.5
#    gbcGrp.h1 = 1./(1+exp((vu+66.)/7.))
#    gbcGrp.h2 = 1./(1+exp((vu+66.)/7.))
#    #gbcGrp.gs_e = 0.0*siemens
    
#    sbcGrp = NeuronGroup(nSbcs, eqs, method='exponential_euler', 
#                        threshold='v > -20*mV', refractory='v > -35*mV')
#    #sbcGrp.I = 2500.0*pA
#    sbcGrp.I = 0.0*pA
#    # Initialize model near v_rest with no inputs
#    sbcGrp.v = -63.6*mV
#    sbcGrp.m = gbcGrp.m
#    sbcGrp.h = gbcGrp.h
#    sbcGrp.n = gbcGrp.n
#    sbcGrp.p = gbcGrp.p
#    sbcGrp.r = gbcGrp.r
#    sbcGrp.w = gbcGrp.w
#    sbcGrp.z = gbcGrp.z
#    sbcGrp.a = gbcGrp.a
#    sbcGrp.b = gbcGrp.b
#    sbcGrp.c = gbcGrp.c
#    sbcGrp.h1 = gbcGrp.h1
#    sbcGrp.h2 = gbcGrp.h2
#    #sbcGrp.gs_e = 0.0*siemens
    
    sbc3Grp = NeuronGroup(nSbcs, eqs_sbc3, method='exponential_euler', 
                    threshold='v > -20*mV', refractory='v > -35*mV')
    #sbc3Grp.I = 2500.0*pA
    sbc3Grp.I = 0.0*pA
    # Initialize model near v_rest with no inputs
    sbc3Grp.v = -63.6*mV
    vu = EL/mV # unitless v
    sbc3Grp.m = 1./(1+exp(-(vu + 38.) / 7.))
    sbc3Grp.h = 1./(1+exp((vu + 65.) / 6.))
    sbc3Grp.n = (1 + exp(-(vu + 15) / 5.))**-0.5
    sbc3Grp.p = 1. / (1 + exp(-(vu + 23) / 6.))
    sbc3Grp.r = 1. / (1+exp((vu + 76.) / 7.))
    sbc3Grp.w = (1. / (1 + exp(-(vu + 48.) / 6.)))**0.25
    sbc3Grp.z = zss + ((1.-zss) / (1 + exp((vu + 71.) / 10.)))
    sbc3Grp.a = (1. / (1 + exp(-(vu + 31) / 6.)))**0.25
    sbc3Grp.b = 1. / (1 + exp((vu + 66) / 7.))**0.5
    sbc3Grp.c = 1. / (1 + exp((vu + 66) / 7.))**0.5
    sbc3Grp.h1 = 1./(1+exp((vu+66.)/7.))
    sbc3Grp.h2 = 1./(1+exp((vu+66.)/7.))
    #sbc3Grp.gs_e = 0.0*siemens
#    sbc3Grp.v = -63.6*mV
#    sbc3Grp.m = gbcGrp.m
#    sbc3Grp.h = gbcGrp.h
#    sbc3Grp.n = gbcGrp.n
#    sbc3Grp.p = gbcGrp.p
#    sbc3Grp.r = gbcGrp.r
#    sbc3Grp.w = gbcGrp.w
#    sbc3Grp.z = gbcGrp.z
#    sbc3Grp.a = gbcGrp.a
#    sbc3Grp.b = gbcGrp.b
#    sbc3Grp.c = gbcGrp.c
#    sbc3Grp.h1 = gbcGrp.h1
#    sbc3Grp.h2 = gbcGrp.h2
#    #sbc3Grp.gs_e = 0.0*siemens
    
    #netGbcEq = Network(gbcGrp, report='text')
    #netGbcEq.run(50*ms, report='text')
    
#    gbcSynE = Synapses(anfSpkGeneratorGrp, gbcGrp, 
#                     model='''dg_e/dt = -g_e/tausE : siemens (clock-driven)
#                              gs_e_post = g_e : siemens (summed)
#                              dw_egbc/dt = (w0_egbc - w_egbc)/tauSyD_egbc : 1 (event-driven)''',
#                     on_pre='''g_e += w_egbc*siemens
#                               w_egbc = w_egbc*(1 - u)''')
#    gbcSynE.connect(i=np.arange(nAnfsPerGbc), j=0)
#    gbcSynE.connect(i=np.arange(nAnfsPerGbc, 2*nAnfsPerGbc), j=1)
#    gbcSynE.connect(i=np.arange(2*nAnfsPerGbc, 3*nAnfsPerGbc), j=2)
#    gbcSynE.connect(i=np.arange(3*nAnfsPerGbc, 4*nAnfsPerGbc), j=3)
#    gbcSynE.w_egbc = w0_egbc
#    
#    gbcSpks = SpikeMonitor(gbcGrp)
#    #gbcSpks = SpikeMonitor(gbcGrp, variables='v', record=True, name='spkMonGbc')
#    
#    gbcState = StateMonitor(gbcGrp, ['v','gs_e'], record=True)
#    #gSynEState = StateMonitor(gbcSynE, ['g_e','gs_e_post'], record=True)
#    #netGbc = Network(gbcGrp, gbcSpks, report='text')
#    #netGbc.run(100*ms, report='text')


#    sbcSynE = Synapses(anfSpkGeneratorGrp, sbcGrp, 
#                     model='''dg_e/dt = -g_e/tausE : siemens (clock-driven)
#                              gs_e_post = g_e : siemens (summed)
#                              dw_esbc/dt = (w0_esbc - w_esbc)/tauSyD_esbc : 1 (event-driven)''',
#                     on_pre='''g_e += w_esbc*siemens
#                               w_esbc = w_esbc*(1 - u)''')
#    sbcSynE.connect(i=120, j=0)
#    sbcSynE.connect(i=121, j=1)
#    sbcSynE.connect(i=122, j=2)
#    sbcSynE.connect(i=123, j=3)
#    sbcSynE.w_esbc = w0_esbc
#    
#    sbcSpks = SpikeMonitor(sbcGrp)
#    #sbcSpks = SpikeMonitor(sbcGrp, variables='v', record=True, name='spkMonSbc')
#    
#    sbcState = StateMonitor(sbcGrp, ['v','gs_e'], record=True)
#    #sSynEState = StateMonitor(sbcSynE, ['g_e','gs_e_post'], record=True)

    
    sbc3SynE0 = Synapses(anfSpkGeneratorGrp, sbc3Grp, 
                     model='''dg_e/dt = -g_e/tausE : siemens (clock-driven)
                              gs_e0_post = g_e : siemens (summed)
                              dw_esbc0/dt = (w0_esbc3 - w_esbc0)/tauSyD_esbc : 1 (event-driven)''',
                     on_pre='''g_e += w_esbc0*siemens
                               w_esbc0 = w_esbc0*(1 - u)''')
    sbc3SynE0.connect(i=120, j=0)
    sbc3SynE0.connect(i=120+nAnfsPerSbc, j=1)
    sbc3SynE0.connect(i=120+2*nAnfsPerSbc, j=2)
    sbc3SynE0.connect(i=120+3*nAnfsPerSbc, j=3)
    sbc3SynE0.w_esbc0 = w0_esbc3
    
    sbc3SynE1 = Synapses(anfSpkGeneratorGrp, sbc3Grp, 
                     model='''dg_e/dt = -g_e/tausE : siemens (clock-driven)
                              gs_e1_post = g_e : siemens (summed)
                              dw_esbc1/dt = (w0_esbc3 - w_esbc1)/tauSyD_esbc : 1 (event-driven)''',
                     on_pre='''g_e += w_esbc1*siemens
                               w_esbc1 = w_esbc1*(1 - u)''')
    sbc3SynE1.connect(i=121, j=0)
    sbc3SynE1.connect(i=121+nAnfsPerSbc, j=1)
    sbc3SynE1.connect(i=121+2*nAnfsPerSbc, j=2)
    sbc3SynE1.connect(i=121+3*nAnfsPerSbc, j=3)
    sbc3SynE1.w_esbc1 = w0_esbc3

    sbc3SynE2 = Synapses(anfSpkGeneratorGrp, sbc3Grp, 
                     model='''dg_e/dt = -g_e/tausE : siemens (clock-driven)
                              gs_e2_post = g_e : siemens (summed)
                              dw_esbc2/dt = (w0_esbc3 - w_esbc2)/tauSyD_esbc : 1 (event-driven)''',
                     on_pre='''g_e += w_esbc2*siemens
                               w_esbc2 = w_esbc2*(1 - u)''')
    sbc3SynE2.connect(i=122, j=0)
    sbc3SynE2.connect(i=122+nAnfsPerSbc, j=1)
    sbc3SynE2.connect(i=122+2*nAnfsPerSbc, j=2)
    sbc3SynE2.connect(i=122+3*nAnfsPerSbc, j=3)
    sbc3SynE2.w_esbc2 = w0_esbc3

    sbc3Spks = SpikeMonitor(sbc3Grp)
    #sbc3Spks = SpikeMonitor(sbc3Grp, variables='v', record=True, name='spkMonSbc')
    
    #sbc3State = StateMonitor(sbc3Grp, ['v','gs_e'], record=True)
    sbc3State = StateMonitor(sbc3Grp, 'v', record=True)
    #s3SynEState = StateMonitor(sbc3SynE, ['g_e','gs_e_post'], record=True)


    run(800*ms, report='text')
    
    #plt.plot(gbcState.t / ms, gbcState[0].v / mV)
    #plt.plot(gbcState.t / ms, gbcState[0].gs_e)
    #plt.plot(gSynEState.t / ms, gSynEState[0].gs_e_post)
    #plt.plot(gSynEState.t / ms, gSynEState[0].g_e)
    plt.plot(sbc3State.t / ms, sbc3State[0].v / mV)
    #plt.plot(sbcState.t / ms, sbcState[0].v / mV)
    
    plt.xlabel('t (ms)')
    plt.ylabel('v (mV)')
    plt.show()

#    gbcSpkFile = 'gbSyDSpTMms' + anfSpkFile[10:len(anfSpkFile)]
#    file0 = open(gbcSpkFile,'w')
#    for index in range(len(gbcSpks.t)):
#        file0.write(str(gbcSpks.i[index]) + " " + str(gbcSpks.t[index] / ms) + '\n')
#    file0.close()
#    
#    sbcSpkFile = 'sbSyDSpTMms' + anfSpkFile[10:len(anfSpkFile)]
#    file1 = open(sbcSpkFile,'w')
#    for index in range(len(sbcSpks.t)):
#        file1.write(str(sbcSpks.i[index]) + " " + str(sbcSpks.t[index] / ms) + '\n')
#    file1.close()
    
    sbc3SpkFile = 'sb3SyDSpTMms' + anfSpkFile[6:len(anfSpkFile)]
    file2 = open(sbc3SpkFile,'w')
    for index in range(len(sbc3Spks.t)):
        file2.write(str(sbc3Spks.i[index]) + " " + str(sbc3Spks.t[index] / ms) + '\n')
    file2.close()
    
    #bcGrps = gbcGrp, sbcGrp, sbc3Grp
    #bcSynEs = gbcSynE, sbcSynE, sbc3SynE
    #bcSpks = gbcSpks, sbcSpks, sbc3Spks
    #bcState = gbcState, sbcState, sbc3State
    
    return (sbc3Grp, sbc3Spks, sbc3State)
# end of mksbc3SyD    

#    return (bcGrps, bcSpks, bcState)

# end of mkgbcs