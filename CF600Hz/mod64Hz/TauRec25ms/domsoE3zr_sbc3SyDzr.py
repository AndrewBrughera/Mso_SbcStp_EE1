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

from msoEfn3zr_sbc3SyDzr import mkmsoEnzr

# StIPD = 0
sbCoSpkFiles = []
sbIpSpkFiles = []

sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhs000AMBB64Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN045AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN090AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN135AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN180AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN225AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN270AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN315AMBB64Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhs000AMBB64Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN045AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN090AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN135AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN180AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN225AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN270AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN315AMBB64Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
#    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i], gbCoSpkFiles[i], gbIpSpkFiles[i])
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEnzr(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop


# StIPD = 45
sbCoSpkFiles = []
sbIpSpkFiles = []

sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN315AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhs000AMBB64Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN045AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN090AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN135AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN180AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN225AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN270AMBB64Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhs000AMBB64Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN045AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN090AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN135AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN180AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN225AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN270AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN315AMBB64Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
#    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i], gbCoSpkFiles[i], gbIpSpkFiles[i])
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEnzr(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop


# StIPD = 90
sbCoSpkFiles = []
sbIpSpkFiles = []

sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN270AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN315AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhs000AMBB64Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN045AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN090AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN135AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN180AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN225AMBB64Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhs000AMBB64Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN045AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN090AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN135AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN180AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN225AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN270AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN315AMBB64Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
#    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i], gbCoSpkFiles[i], gbIpSpkFiles[i])
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEnzr(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop


# StIPD = 135
sbCoSpkFiles = []
sbIpSpkFiles = []

sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN225AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN270AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN315AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhs000AMBB64Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN045AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN090AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN135AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN180AMBB64Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhs000AMBB64Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN045AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN090AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN135AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN180AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN225AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN270AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN315AMBB64Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
#    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i], gbCoSpkFiles[i], gbIpSpkFiles[i])
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEnzr(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop


# StIPD = 180
sbCoSpkFiles = []
sbIpSpkFiles = []

sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN180AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN225AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN270AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN315AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhs000AMBB64Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN045AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN090AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN135AMBB64Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhs000AMBB64Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN045AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN090AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN135AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN180AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN225AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN270AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN315AMBB64Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
#    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i], gbCoSpkFiles[i], gbIpSpkFiles[i])
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEnzr(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop


# StIPD = 225
sbCoSpkFiles = []
sbIpSpkFiles = []

sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN135AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN180AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN225AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN270AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN315AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhs000AMBB64Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN045AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN090AMBB64Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhs000AMBB64Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN045AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN090AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN135AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN180AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN225AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN270AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN315AMBB64Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
#    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i], gbCoSpkFiles[i], gbIpSpkFiles[i])
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEnzr(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop


# StIPD = 270
sbCoSpkFiles = []
sbIpSpkFiles = []

sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN090AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN135AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN180AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN225AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN270AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN315AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhs000AMBB64Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN045AMBB64Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhs000AMBB64Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN045AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN090AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN135AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN180AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN225AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN270AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN315AMBB64Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
#    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i], gbCoSpkFiles[i], gbIpSpkFiles[i])
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEnzr(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop


# StIPD = 315
sbCoSpkFiles = []
sbIpSpkFiles = []

sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN045AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN090AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN135AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN180AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN225AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN270AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhsN315AMBB64Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa632HzStPhs000AMBB64Hz75dBsplMdSpSpec3.txt')  

sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhs000AMBB64Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN045AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN090AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN135AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN180AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN225AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN270AMBB64Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa568HzStPhsN315AMBB64Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
#    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i], gbCoSpkFiles[i], gbIpSpkFiles[i])
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEnzr(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop


