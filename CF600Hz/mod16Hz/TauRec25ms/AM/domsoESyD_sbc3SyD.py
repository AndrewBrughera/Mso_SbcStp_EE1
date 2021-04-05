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

from msoEfn3SyD_sbc3SyD import mkmsoEnSyD


sbCoSpkFiles = []
sbIpSpkFiles = []
#gbCoSpkFiles = []
#gbIpSpkFiles = []

'''For the AMBB, set sequences for starting-IPD ipsi-leading by 90 degrees.
This will give zero IPD at 90 degrees into the AMBB cycle,
and IPD 45 deg contra-leading at 135 deg into the AMBB cycle.
This is to match:
The MSO neurons in Dietz et al. 2014 have best-IPDs near 45 deg Contra-leading.
And for AM 32 Hz, they have maximum spike rate around 135 degrees into the 
AMBB cycle. 
'''

# Static IPD = 135 = 135 - 360 = -225 degrees
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN225AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN270AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN315AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhs000AM16Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN045AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN090AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN135AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN180AM16Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhs000AM16Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN045AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN090AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN135AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN180AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN225AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN270AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN315AM16Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
#    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i], gbCoSpkFiles[i], gbIpSpkFiles[i])
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEnSyD(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop


sbCoSpkFiles = []
sbIpSpkFiles = []
# Static IPD = 90 = 90 - 360 = -270 degrees
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN270AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN315AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhs000AM16Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN045AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN090AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN135AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN180AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN225AM16Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhs000AM16Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN045AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN090AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN135AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN180AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN225AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN270AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN315AM16Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
#    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i], gbCoSpkFiles[i], gbIpSpkFiles[i])
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEnSyD(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop


sbCoSpkFiles = []
sbIpSpkFiles = []
# Static IPD = 45 = 45 - 360 = -315 degrees
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN315AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhs000AM16Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN045AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN090AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN135AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN180AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN225AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN270AM16Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhs000AM16Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN045AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN090AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN135AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN180AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN225AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN270AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN315AM16Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
#    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i], gbCoSpkFiles[i], gbIpSpkFiles[i])
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEnSyD(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop


sbCoSpkFiles = []
sbIpSpkFiles = []
# Static IPD = 0 degrees
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhs000AM16Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN045AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN090AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN135AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN180AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN225AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN270AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN315AM16Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhs000AM16Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN045AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN090AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN135AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN180AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN225AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN270AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN315AM16Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
#    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i], gbCoSpkFiles[i], gbIpSpkFiles[i])
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEnSyD(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop


sbCoSpkFiles = []
sbIpSpkFiles = []
# Static IPD = -45 degrees
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN045AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN090AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN135AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN180AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN225AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN270AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN315AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhs000AM16Hz75dBsplMdSpSpec3.txt')  

sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhs000AM16Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN045AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN090AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN135AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN180AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN225AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN270AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN315AM16Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
#    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i], gbCoSpkFiles[i], gbIpSpkFiles[i])
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEnSyD(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop


sbCoSpkFiles = []
sbIpSpkFiles = []
# Static IPD = -90 degrees
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN090AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN135AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN180AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN225AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN270AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN315AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhs000AM16Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN045AM16Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhs000AM16Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN045AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN090AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN135AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN180AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN225AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN270AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN315AM16Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
#    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i], gbCoSpkFiles[i], gbIpSpkFiles[i])
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEnSyD(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop


sbCoSpkFiles = []
sbIpSpkFiles = []
# Static IPD = -135 degrees
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN135AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN180AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN225AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN270AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN315AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhs000AM16Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN045AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN090AM16Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhs000AM16Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN045AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN090AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN135AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN180AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN225AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN270AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN315AM16Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
#    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i], gbCoSpkFiles[i], gbIpSpkFiles[i])
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEnSyD(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop


sbCoSpkFiles = []
sbIpSpkFiles = []
# Static IPD = -180 degrees
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN180AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN225AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN270AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN315AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhs000AM16Hz75dBsplMdSpSpec3.txt')  
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN045AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN090AM16Hz75dBsplMdSpSpec3.txt') 
sbCoSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz2StPhsN135AM16Hz75dBsplMdSpSpec3.txt') 

sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhs000AM16Hz75dBsplMdSpSpec3.txt')  
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN045AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN090AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN135AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN180AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN225AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN270AM16Hz75dBsplMdSpSpec3.txt') 
sbIpSpkFiles.append('sb3SyDSpTMmsCF600HzCa600Hz1StPhsN315AM16Hz75dBsplMdSpSpec3.txt') 

msonOutputTuples = []
for i in range(len(sbCoSpkFiles)):
    # Note, in MSO model contra is 1st, Ipsi is 2nd
#    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i], gbCoSpkFiles[i], gbIpSpkFiles[i])
    inputSpkFileTuple = (sbCoSpkFiles[i], sbIpSpkFiles[i])
    msonOutputTuple = mkmsoEnSyD(inputSpkFileTuple)
    msonOutputTuples.append(msonOutputTuples)
    
# end of mson loop


