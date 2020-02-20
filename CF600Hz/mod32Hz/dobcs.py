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

from bcfn import mkbcs


anfSpkFiles = []

# in bcfn.py w_egbc = 6e-9
#anfSpkFiles.append('ANSpkTmSecCF200HzCa184HzStPhs000AMBB32Hz75dBsplMdSpSpec3.txt')
#anfSpkFiles.append('ANSpkTmSecCF200HzCa184HzStPhsN045AMBB32Hz75dBsplMdSpSpec3.txt')
#anfSpkFiles.append('ANSpkTmSecCF200HzCa184HzStPhsN090AMBB32Hz75dBsplMdSpSpec3.txt')
#anfSpkFiles.append('ANSpkTmSecCF200HzCa184HzStPhsN135AMBB32Hz75dBsplMdSpSpec3.txt')
#anfSpkFiles.append('ANSpkTmSecCF200HzCa184HzStPhsN180AMBB32Hz75dBsplMdSpSpec3.txt')
#anfSpkFiles.append('ANSpkTmSecCF200HzCa184HzStPhsN225AMBB32Hz75dBsplMdSpSpec3.txt')
#anfSpkFiles.append('ANSpkTmSecCF200HzCa184HzStPhsN270AMBB32Hz75dBsplMdSpSpec3.txt')
#anfSpkFiles.append('ANSpkTmSecCF200HzCa184HzStPhsN315AMBB32Hz75dBsplMdSpSpec3.txt')
#anfSpkFiles.append('ANSpkTmSecCF200HzCa216HzStPhs000AMBB32Hz75dBsplMdSpSpec3.txt')
#anfSpkFiles.append('ANSpkTmSecCF200HzCa216HzStPhsN045AMBB32Hz75dBsplMdSpSpec3.txt')
#anfSpkFiles.append('ANSpkTmSecCF200HzCa216HzStPhsN090AMBB32Hz75dBsplMdSpSpec3.txt')
#anfSpkFiles.append('ANSpkTmSecCF200HzCa216HzStPhsN135AMBB32Hz75dBsplMdSpSpec3.txt')
#anfSpkFiles.append('ANSpkTmSecCF200HzCa216HzStPhsN180AMBB32Hz75dBsplMdSpSpec3.txt')
#anfSpkFiles.append('ANSpkTmSecCF200HzCa216HzStPhsN225AMBB32Hz75dBsplMdSpSpec3.txt')
#anfSpkFiles.append('ANSpkTmSecCF200HzCa216HzStPhsN270AMBB32Hz75dBsplMdSpSpec3.txt')
#anfSpkFiles.append('ANSpkTmSecCF200HzCa216HzStPhsN315AMBB32Hz75dBsplMdSpSpec3.txt')

# in bcfn.py w_egbc = 12e-9
anfSpkFiles.append('ANSpkTmSecCF600HzCa584HzStPhs000AMBB32Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa584HzStPhsN045AMBB32Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa584HzStPhsN090AMBB32Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa584HzStPhsN135AMBB32Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa584HzStPhsN180AMBB32Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa584HzStPhsN225AMBB32Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa584HzStPhsN270AMBB32Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa584HzStPhsN315AMBB32Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa616HzStPhs000AMBB32Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa616HzStPhsN045AMBB32Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa616HzStPhsN090AMBB32Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa616HzStPhsN135AMBB32Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa616HzStPhsN180AMBB32Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa616HzStPhsN225AMBB32Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa616HzStPhsN270AMBB32Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa616HzStPhsN315AMBB32Hz75dBsplMdSpSpec3.txt')

bcTriTuples = []
for f in anfSpkFiles:
    bcTriTuple = mkbcs(f)
    bcTriTuples.append(bcTriTuple)




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





