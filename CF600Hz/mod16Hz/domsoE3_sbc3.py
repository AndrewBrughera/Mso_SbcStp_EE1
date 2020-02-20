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

from msoEfn3_sbc3 import mkmsoEn

# StIPD = 0
sbCoSpkFiles = []
sbIpSpkFiles = []

sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhs000AMBB16Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN045AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN090AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN135AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN180AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN225AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN270AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN315AMBB16Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhs000AMBB16Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN045AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN090AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN135AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN180AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN225AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN270AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN315AMBB16Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEn(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop

# StIPD = 45
sbCoSpkFiles = []
sbIpSpkFiles = []

sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN315AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhs000AMBB16Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN045AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN090AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN135AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN180AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN225AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN270AMBB16Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhs000AMBB16Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN045AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN090AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN135AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN180AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN225AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN270AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN315AMBB16Hz75dBsplMdSpSpec3.txt') 

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

sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN270AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN315AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhs000AMBB16Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN045AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN090AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN135AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN180AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN225AMBB16Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhs000AMBB16Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN045AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN090AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN135AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN180AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN225AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN270AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN315AMBB16Hz75dBsplMdSpSpec3.txt') 

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

sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN225AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN270AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN315AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhs000AMBB16Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN045AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN090AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN135AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN180AMBB16Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhs000AMBB16Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN045AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN090AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN135AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN180AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN225AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN270AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN315AMBB16Hz75dBsplMdSpSpec3.txt') 

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

sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN180AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN225AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN270AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN315AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhs000AMBB16Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN045AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN090AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN135AMBB16Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhs000AMBB16Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN045AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN090AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN135AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN180AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN225AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN270AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN315AMBB16Hz75dBsplMdSpSpec3.txt') 

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

sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN135AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN180AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN225AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN270AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN315AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhs000AMBB16Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN045AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN090AMBB16Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhs000AMBB16Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN045AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN090AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN135AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN180AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN225AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN270AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN315AMBB16Hz75dBsplMdSpSpec3.txt') 

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

sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN090AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN135AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN180AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN225AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN270AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN315AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhs000AMBB16Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN045AMBB16Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhs000AMBB16Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN045AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN090AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN135AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN180AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN225AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN270AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN315AMBB16Hz75dBsplMdSpSpec3.txt') 

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

sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN045AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN090AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN135AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN180AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN225AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN270AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhsN315AMBB16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SpTMmsCF600HzCa608HzStPhs000AMBB16Hz75dBsplMdSpSpec3.txt')  

sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhs000AMBB16Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN045AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN090AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN135AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN180AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN225AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN270AMBB16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SpTMmsCF600HzCa592HzStPhsN315AMBB16Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
#    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i], gbCoSpkFiles[i], gbIpSpkFiles[i])
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEn(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop


