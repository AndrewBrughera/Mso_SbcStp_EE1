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

from sbc3e83nS_10i import mksbc3e83nS_10i

anfSpkFiles = []

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
    bcTriTuple = mksbc3e83nS_10i(f)
    bcTriTuples.append(bcTriTuple)

