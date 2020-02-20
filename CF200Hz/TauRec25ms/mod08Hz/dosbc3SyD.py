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
anfSpkFiles.append('ANSpkTmSecCF200HzCa196HzStPhs000AMBB8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF200HzCa196HzStPhsN045AMBB8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF200HzCa196HzStPhsN090AMBB8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF200HzCa196HzStPhsN135AMBB8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF200HzCa196HzStPhsN180AMBB8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF200HzCa196HzStPhsN225AMBB8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF200HzCa196HzStPhsN270AMBB8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF200HzCa196HzStPhsN315AMBB8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF200HzCa204HzStPhs000AMBB8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF200HzCa204HzStPhsN045AMBB8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF200HzCa204HzStPhsN090AMBB8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF200HzCa204HzStPhsN135AMBB8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF200HzCa204HzStPhsN180AMBB8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF200HzCa204HzStPhsN225AMBB8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF200HzCa204HzStPhsN270AMBB8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF200HzCa204HzStPhsN315AMBB8Hz75dBsplMdSpSpec3.txt')

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





