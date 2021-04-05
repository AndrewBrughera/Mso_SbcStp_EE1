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

from msoEfnzr_sbc3SyDzr import mkmsoEnzr


sbCoSpkFiles = []
sbIpSpkFiles = []
#gbCoSpkFiles = []
#gbIpSpkFiles = []

# Static IPD = 135 = 135 - 360 = -225 degrees
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN225AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN270AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN315AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhs000AM8Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN045AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN090AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN135AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN180AM8Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhs000AM8Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN045AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN090AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN135AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN180AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN225AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN270AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN315AM8Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
#    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i], gbCoSpkFiles[i], gbIpSpkFiles[i])
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEnzr(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop


sbCoSpkFiles = []
sbIpSpkFiles = []
# Static IPD = 90 = 90 - 360 = -270 degrees
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN270AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN315AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhs000AM8Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN045AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN090AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN135AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN180AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN225AM8Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhs000AM8Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN045AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN090AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN135AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN180AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN225AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN270AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN315AM8Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
#    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i], gbCoSpkFiles[i], gbIpSpkFiles[i])
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEnzr(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop


sbCoSpkFiles = []
sbIpSpkFiles = []
# Static IPD = 45 = 45 - 360 = -315 degrees
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN315AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhs000AM8Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN045AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN090AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN135AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN180AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN225AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN270AM8Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhs000AM8Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN045AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN090AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN135AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN180AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN225AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN270AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN315AM8Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
#    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i], gbCoSpkFiles[i], gbIpSpkFiles[i])
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEnzr(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop


sbCoSpkFiles = []
sbIpSpkFiles = []
# Static IPD = 0 degrees
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhs000AM8Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN045AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN090AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN135AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN180AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN225AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN270AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN315AM8Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhs000AM8Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN045AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN090AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN135AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN180AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN225AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN270AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN315AM8Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
#    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i], gbCoSpkFiles[i], gbIpSpkFiles[i])
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEnzr(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop


sbCoSpkFiles = []
sbIpSpkFiles = []
# Static IPD = -45 degrees
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN045AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN090AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN135AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN180AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN225AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN270AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN315AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhs000AM8Hz75dBsplMdSpSpec3.txt')  

sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhs000AM8Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN045AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN090AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN135AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN180AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN225AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN270AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN315AM8Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
#    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i], gbCoSpkFiles[i], gbIpSpkFiles[i])
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEnzr(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop


sbCoSpkFiles = []
sbIpSpkFiles = []
# Static IPD = -90 degrees
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN090AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN135AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN180AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN225AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN270AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN315AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhs000AM8Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN045AM8Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhs000AM8Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN045AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN090AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN135AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN180AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN225AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN270AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN315AM8Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
#    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i], gbCoSpkFiles[i], gbIpSpkFiles[i])
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEnzr(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop


sbCoSpkFiles = []
sbIpSpkFiles = []
# Static IPD = -135 degrees
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN135AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN180AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN225AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN270AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN315AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhs000AM8Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN045AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN090AM8Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhs000AM8Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN045AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN090AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN135AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN180AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN225AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN270AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN315AM8Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
#    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i], gbCoSpkFiles[i], gbIpSpkFiles[i])
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEnzr(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop


sbCoSpkFiles = []
sbIpSpkFiles = []
# Static IPD = -180 degrees
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN180AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN225AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN270AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN315AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhs000AM8Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN045AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN090AM8Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz2StPhsN135AM8Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhs000AM8Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN045AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN090AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN135AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN180AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN225AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN270AM8Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDzrSpTMmsCF600HzCa600Hz1StPhsN315AM8Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
#    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i], gbCoSpkFiles[i], gbIpSpkFiles[i])
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEnzr(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop


