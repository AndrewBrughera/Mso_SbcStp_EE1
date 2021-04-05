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

from bcfnSyD3zrest import mksbc3SyDzrest


anfSpkFiles = []

# in bcfn.py w_egbc = 12e-9
anfSpkFiles.append('ANSpkTmSecCF600HzCa592HzStPhs000AMBB16Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa592HzStPhsN045AMBB16Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa592HzStPhsN090AMBB16Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa592HzStPhsN135AMBB16Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa592HzStPhsN180AMBB16Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa592HzStPhsN225AMBB16Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa592HzStPhsN270AMBB16Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa592HzStPhsN315AMBB16Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa608HzStPhs000AMBB16Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa608HzStPhsN045AMBB16Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa608HzStPhsN090AMBB16Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa608HzStPhsN135AMBB16Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa608HzStPhsN180AMBB16Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa608HzStPhsN225AMBB16Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa608HzStPhsN270AMBB16Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa608HzStPhsN315AMBB16Hz75dBsplMdSpSpec3.txt')

sbc3Tuples = []
for f in anfSpkFiles:
    sbc3Tuple = mksbc3SyDzrest(f)
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





