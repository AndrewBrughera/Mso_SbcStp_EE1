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

sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhs000AM16Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN045AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN090AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN135AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN180AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN225AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN270AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN315AM16Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhs000AM16Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN045AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN090AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN135AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN180AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN225AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN270AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN315AM16Hz75dBsplMdSpSpec3.txt') 

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

sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN315AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhs000AM16Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN045AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN090AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN135AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN180AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN225AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN270AM16Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhs000AM16Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN045AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN090AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN135AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN180AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN225AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN270AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN315AM16Hz75dBsplMdSpSpec3.txt') 

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

sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN270AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN315AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhs000AM16Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN045AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN090AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN135AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN180AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN225AM16Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhs000AM16Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN045AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN090AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN135AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN180AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN225AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN270AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN315AM16Hz75dBsplMdSpSpec3.txt') 

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

sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN225AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN270AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN315AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhs000AM16Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN045AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN090AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN135AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN180AM16Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhs000AM16Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN045AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN090AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN135AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN180AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN225AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN270AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN315AM16Hz75dBsplMdSpSpec3.txt') 

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

sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN180AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN225AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN270AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN315AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhs000AM16Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN045AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN090AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN135AM16Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhs000AM16Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN045AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN090AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN135AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN180AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN225AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN270AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN315AM16Hz75dBsplMdSpSpec3.txt') 

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

sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN135AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN180AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN225AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN270AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN315AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhs000AM16Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN045AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN090AM16Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhs000AM16Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN045AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN090AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN135AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN180AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN225AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN270AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN315AM16Hz75dBsplMdSpSpec3.txt') 

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

sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN090AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN135AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN180AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN225AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN270AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN315AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhs000AM16Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN045AM16Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhs000AM16Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN045AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN090AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN135AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN180AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN225AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN270AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN315AM16Hz75dBsplMdSpSpec3.txt') 

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

sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN045AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN090AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN135AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN180AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN225AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN270AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhsN315AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz2StPhs000AM16Hz75dBsplMdSpSpec3.txt')  

sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhs000AM16Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN045AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN090AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN135AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN180AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN225AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN270AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3_83nS_SpTCF600HzCa600Hz1StPhsN315AM16Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
#    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i], gbCoSpkFiles[i], gbIpSpkFiles[i])
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEnSyD(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop


