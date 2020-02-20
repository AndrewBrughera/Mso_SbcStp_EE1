# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 12:19:29 2018

@author: Andrew Brughera
"""
from brian2 import mV, amp, pA, pF, siemens, nS, ms, second
from brian2 import SpikeGeneratorGroup, NeuronGroup, Synapses
from brian2 import SpikeMonitor, StateMonitor, Network, run
from brian2 import defaultclock
from math import exp
import numpy as np
import matplotlib.pyplot as plt

from bcfnSyD3 import mksbc3SyD


anfSpkFiles = []

anfSpkFiles.append('ANSpkTmSecCF200HzCa200Hz1StPhs000AM8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF200HzCa200Hz1StPhsN045AM8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF200HzCa200Hz1StPhsN090AM8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF200HzCa200Hz1StPhsN135AM8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF200HzCa200Hz1StPhsN180AM8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF200HzCa200Hz1StPhsN225AM8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF200HzCa200Hz1StPhsN270AM8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF200HzCa200Hz1StPhsN315AM8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF200HzCa200Hz2StPhs000AM8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF200HzCa200Hz2StPhsN045AM8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF200HzCa200Hz2StPhsN090AM8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF200HzCa200Hz2StPhsN135AM8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF200HzCa200Hz2StPhsN180AM8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF200HzCa200Hz2StPhsN225AM8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF200HzCa200Hz2StPhsN270AM8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF200HzCa200Hz2StPhsN315AM8Hz75dBsplMdSpSpec3.txt')

sbc3Tuples = []
for f in anfSpkFiles:
    sbc3Tuple = mksbc3SyD(f)
    sbc3Tuples.append(sbc3Tuple)




#bc3Tuples0 = mkbcs(anfSpkFile)
#
#gbcGrp0 = bc3Tuples0[0][0]
#sbcGrp0 = bc3Tuples0[0][1]
#sbc3Grp0 = bc3Tuples0[0][2]
#
#gbcSpks0 = bc3Tuples0[1][0]
#sbcSpks0 = bc3Tuples0[1][1]
#sbc3Spks0 = bc3Tuples0[1][2]
#
#gbcState0 = bc3Tuples0[2][0]
#sbcState0 = bc3Tuples0[2][1]
#sbc3State0 = bc3Tuples0[2][2]





