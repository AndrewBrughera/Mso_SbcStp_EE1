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

anfSpkFiles.append('ANSpkTmSecCF600HzCa596HzStPhs000AMBB8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa596HzStPhsN045AMBB8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa596HzStPhsN090AMBB8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa596HzStPhsN135AMBB8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa596HzStPhsN180AMBB8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa596HzStPhsN225AMBB8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa596HzStPhsN270AMBB8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa596HzStPhsN315AMBB8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa604HzStPhs000AMBB8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa604HzStPhsN045AMBB8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa604HzStPhsN090AMBB8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa604HzStPhsN135AMBB8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa604HzStPhsN180AMBB8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa604HzStPhsN225AMBB8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa604HzStPhsN270AMBB8Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa604HzStPhsN315AMBB8Hz75dBsplMdSpSpec3.txt')

bcTriTuples = []
for f in anfSpkFiles:
    bcTriTuple = mksbc3e83nS_10i(f)
    bcTriTuples.append(bcTriTuple)

