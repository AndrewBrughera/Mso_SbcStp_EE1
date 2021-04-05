# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 12:19:29 2018

@author: Andrew Brughera
"""
#from brian2 import mV, amp, pA, pF, siemens, nS, ms, second
#from brian2 import SpikeGeneratorGroup, NeuronGroup, Synapses
from brian2 import cm, um, mV, amp, uF, ohm, siemens, nS, ms, second
from brian2 import SpatialNeuron, Soma, Cylinder, Synapses
from brian2 import SpikeMonitor, StateMonitor, Network, run
from brian2 import defaultclock
from math import exp
import numpy as np
import matplotlib.pyplot as plt

from msoEfn3SyD_sbc3_83nS import mkmsoEnSyD

# StIPD = 0
sbCoSpkFiles = []
sbIpSpkFiles = []

sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhs000AMBB8Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN045AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN090AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN135AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN180AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN225AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN270AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN315AMBB8Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhs000AMBB8Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN045AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN090AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN135AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN180AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN225AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN270AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN315AMBB8Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEnSyD(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop

# StIPD = 45
sbCoSpkFiles = []
sbIpSpkFiles = []

sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN315AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhs000AMBB8Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN045AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN090AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN135AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN180AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN225AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN270AMBB8Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhs000AMBB8Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN045AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN090AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN135AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN180AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN225AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN270AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN315AMBB8Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
#    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i], gbCoSpkFiles[i], gbIpSpkFiles[i])
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEnSyD(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop


# StIPD = 90
sbCoSpkFiles = []
sbIpSpkFiles = []

sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN270AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN315AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhs000AMBB8Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN045AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN090AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN135AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN180AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN225AMBB8Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhs000AMBB8Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN045AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN090AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN135AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN180AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN225AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN270AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN315AMBB8Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
#    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i], gbCoSpkFiles[i], gbIpSpkFiles[i])
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEnSyD(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop


# StIPD = 135
sbCoSpkFiles = []
sbIpSpkFiles = []

sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN225AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN270AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN315AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhs000AMBB8Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN045AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN090AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN135AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN180AMBB8Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhs000AMBB8Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN045AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN090AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN135AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN180AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN225AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN270AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN315AMBB8Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
#    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i], gbCoSpkFiles[i], gbIpSpkFiles[i])
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEnSyD(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop


# StIPD = 180
sbCoSpkFiles = []
sbIpSpkFiles = []

sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN180AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN225AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN270AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN315AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhs000AMBB8Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN045AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN090AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN135AMBB8Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhs000AMBB8Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN045AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN090AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN135AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN180AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN225AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN270AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN315AMBB8Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
#    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i], gbCoSpkFiles[i], gbIpSpkFiles[i])
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEnSyD(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop


# StIPD = 225
sbCoSpkFiles = []
sbIpSpkFiles = []

sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN135AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN180AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN225AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN270AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN315AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhs000AMBB8Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN045AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN090AMBB8Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhs000AMBB8Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN045AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN090AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN135AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN180AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN225AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN270AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN315AMBB8Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
#    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i], gbCoSpkFiles[i], gbIpSpkFiles[i])
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEnSyD(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop


# StIPD = 270
sbCoSpkFiles = []
sbIpSpkFiles = []

sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN090AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN135AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN180AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN225AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN270AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN315AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhs000AMBB8Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN045AMBB8Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhs000AMBB8Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN045AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN090AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN135AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN180AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN225AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN270AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN315AMBB8Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
#    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i], gbCoSpkFiles[i], gbIpSpkFiles[i])
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEnSyD(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop


# StIPD = 315
sbCoSpkFiles = []
sbIpSpkFiles = []

sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN045AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN090AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN135AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN180AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN225AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN270AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhsN315AMBB8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa604HzStPhs000AMBB8Hz75dBsplMdSpSpec3.txt')  

sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhs000AMBB8Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN045AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN090AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN135AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN180AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN225AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN270AMBB8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa596HzStPhsN315AMBB8Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
#    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i], gbCoSpkFiles[i], gbIpSpkFiles[i])
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEnSyD(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop


