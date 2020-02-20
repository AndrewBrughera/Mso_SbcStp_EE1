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

# in bcfn.py w_egbc = 6e-9
#anfSpkFiles.append('ANSpkTmSecCF200HzCa198HzStPhs000AMBB4Hz75dBsplMdSpSpec3.txt')
#anfSpkFiles.append('ANSpkTmSecCF200HzCa198HzStPhsN045AMBB4Hz75dBsplMdSpSpec3.txt')
#anfSpkFiles.append('ANSpkTmSecCF200HzCa198HzStPhsN090AMBB4Hz75dBsplMdSpSpec3.txt')
#anfSpkFiles.append('ANSpkTmSecCF200HzCa198HzStPhsN135AMBB4Hz75dBsplMdSpSpec3.txt')
#anfSpkFiles.append('ANSpkTmSecCF200HzCa198HzStPhsN180AMBB4Hz75dBsplMdSpSpec3.txt')
#anfSpkFiles.append('ANSpkTmSecCF200HzCa198HzStPhsN225AMBB4Hz75dBsplMdSpSpec3.txt')
#anfSpkFiles.append('ANSpkTmSecCF200HzCa198HzStPhsN270AMBB4Hz75dBsplMdSpSpec3.txt')
#anfSpkFiles.append('ANSpkTmSecCF200HzCa198HzStPhsN315AMBB4Hz75dBsplMdSpSpec3.txt')
#anfSpkFiles.append('ANSpkTmSecCF200HzCa202HzStPhs000AMBB4Hz75dBsplMdSpSpec3.txt')
#anfSpkFiles.append('ANSpkTmSecCF200HzCa202HzStPhsN045AMBB4Hz75dBsplMdSpSpec3.txt')
#anfSpkFiles.append('ANSpkTmSecCF200HzCa202HzStPhsN090AMBB4Hz75dBsplMdSpSpec3.txt')
#anfSpkFiles.append('ANSpkTmSecCF200HzCa202HzStPhsN135AMBB4Hz75dBsplMdSpSpec3.txt')
#anfSpkFiles.append('ANSpkTmSecCF200HzCa202HzStPhsN180AMBB4Hz75dBsplMdSpSpec3.txt')
#anfSpkFiles.append('ANSpkTmSecCF200HzCa202HzStPhsN225AMBB4Hz75dBsplMdSpSpec3.txt')
#anfSpkFiles.append('ANSpkTmSecCF200HzCa202HzStPhsN270AMBB4Hz75dBsplMdSpSpec3.txt')
#anfSpkFiles.append('ANSpkTmSecCF200HzCa202HzStPhsN315AMBB4Hz75dBsplMdSpSpec3.txt')

# in bcfn.py w_egbc = 12e-9
anfSpkFiles.append('ANSpkTmSecCF600HzCa600Hz1StPhs000AM64Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa600Hz1StPhsN045AM64Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa600Hz1StPhsN090AM64Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa600Hz1StPhsN135AM64Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa600Hz1StPhsN180AM64Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa600Hz1StPhsN225AM64Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa600Hz1StPhsN270AM64Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa600Hz1StPhsN315AM64Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa600Hz2StPhs000AM64Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa600Hz2StPhsN045AM64Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa600Hz2StPhsN090AM64Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa600Hz2StPhsN135AM64Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa600Hz2StPhsN180AM64Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa600Hz2StPhsN225AM64Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa600Hz2StPhsN270AM64Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa600Hz2StPhsN315AM64Hz75dBsplMdSpSpec3.txt')

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





