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

from msoEfn3_sbc3SyD import mkmsoEn

# StIPD = 0
sbCoSpkFiles = []
sbIpSpkFiles = []

sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhs000AMBB32Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN045AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN090AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN135AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN180AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN225AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN270AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN315AMBB32Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhs000AMBB32Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN045AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN090AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN135AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN180AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN225AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN270AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN315AMBB32Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
#    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i], gbCoSpkFiles[i], gbIpSpkFiles[i])
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEn(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop


# StIPD = 45
sbCoSpkFiles = []
sbIpSpkFiles = []

sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN315AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhs000AMBB32Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN045AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN090AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN135AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN180AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN225AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN270AMBB32Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhs000AMBB32Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN045AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN090AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN135AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN180AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN225AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN270AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN315AMBB32Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
#    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i], gbCoSpkFiles[i], gbIpSpkFiles[i])
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEn(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop


# StIPD = 90
sbCoSpkFiles = []
sbIpSpkFiles = []

sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN270AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN315AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhs000AMBB32Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN045AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN090AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN135AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN180AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN225AMBB32Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhs000AMBB32Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN045AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN090AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN135AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN180AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN225AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN270AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN315AMBB32Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
#    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i], gbCoSpkFiles[i], gbIpSpkFiles[i])
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEn(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop


# StIPD = 135
sbCoSpkFiles = []
sbIpSpkFiles = []

sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN225AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN270AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN315AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhs000AMBB32Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN045AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN090AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN135AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN180AMBB32Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhs000AMBB32Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN045AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN090AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN135AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN180AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN225AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN270AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN315AMBB32Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
#    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i], gbCoSpkFiles[i], gbIpSpkFiles[i])
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEn(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop


# StIPD = 180
sbCoSpkFiles = []
sbIpSpkFiles = []

sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN180AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN225AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN270AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN315AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhs000AMBB32Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN045AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN090AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN135AMBB32Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhs000AMBB32Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN045AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN090AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN135AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN180AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN225AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN270AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN315AMBB32Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
#    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i], gbCoSpkFiles[i], gbIpSpkFiles[i])
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEn(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop


# StIPD = 225
sbCoSpkFiles = []
sbIpSpkFiles = []

sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN135AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN180AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN225AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN270AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN315AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhs000AMBB32Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN045AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN090AMBB32Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhs000AMBB32Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN045AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN090AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN135AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN180AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN225AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN270AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN315AMBB32Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
#    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i], gbCoSpkFiles[i], gbIpSpkFiles[i])
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEn(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop


# StIPD = 270
sbCoSpkFiles = []
sbIpSpkFiles = []

sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN090AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN135AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN180AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN225AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN270AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN315AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhs000AMBB32Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN045AMBB32Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhs000AMBB32Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN045AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN090AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN135AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN180AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN225AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN270AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN315AMBB32Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
#    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i], gbCoSpkFiles[i], gbIpSpkFiles[i])
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEn(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop


# StIPD = 315
sbCoSpkFiles = []
sbIpSpkFiles = []

sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN045AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN090AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN135AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN180AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN225AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN270AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhsN315AMBB32Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa616HzStPhs000AMBB32Hz75dBsplMdSpSpec3.txt')  

sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhs000AMBB32Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN045AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN090AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN135AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN180AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN225AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN270AMBB32Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa584HzStPhsN315AMBB32Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
#    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i], gbCoSpkFiles[i], gbIpSpkFiles[i])
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEn(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop


