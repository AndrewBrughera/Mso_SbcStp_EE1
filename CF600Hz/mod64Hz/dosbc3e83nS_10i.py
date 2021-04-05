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

anfSpkFiles.append('ANSpkTmSecCF600HzCa568HzStPhs000AMBB64Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa568HzStPhsN045AMBB64Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa568HzStPhsN090AMBB64Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa568HzStPhsN135AMBB64Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa568HzStPhsN180AMBB64Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa568HzStPhsN225AMBB64Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa568HzStPhsN270AMBB64Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa568HzStPhsN315AMBB64Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa632HzStPhs000AMBB64Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa632HzStPhsN045AMBB64Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa632HzStPhsN090AMBB64Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa632HzStPhsN135AMBB64Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa632HzStPhsN180AMBB64Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa632HzStPhsN225AMBB64Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa632HzStPhsN270AMBB64Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa632HzStPhsN315AMBB64Hz75dBsplMdSpSpec3.txt')

bcTriTuples = []
for f in anfSpkFiles:
    bcTriTuple = mksbc3e83nS_10i(f)
    bcTriTuples.append(bcTriTuple)

