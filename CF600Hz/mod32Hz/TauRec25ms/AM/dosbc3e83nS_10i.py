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

anfSpkFiles.append('ANSpkTmSecCF600HzCa600Hz1StPhs000AM32Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa600Hz1StPhsN045AM32Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa600Hz1StPhsN090AM32Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa600Hz1StPhsN135AM32Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa600Hz1StPhsN180AM32Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa600Hz1StPhsN225AM32Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa600Hz1StPhsN270AM32Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa600Hz1StPhsN315AM32Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa600Hz2StPhs000AM32Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa600Hz2StPhsN045AM32Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa600Hz2StPhsN090AM32Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa600Hz2StPhsN135AM32Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa600Hz2StPhsN180AM32Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa600Hz2StPhsN225AM32Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa600Hz2StPhsN270AM32Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpkTmSecCF600HzCa600Hz2StPhsN315AM32Hz75dBsplMdSpSpec3.txt')

bcTriTuples = []
for f in anfSpkFiles:
    bcTriTuple = mksbc3e83nS_10i(f)
    bcTriTuples.append(bcTriTuple)

