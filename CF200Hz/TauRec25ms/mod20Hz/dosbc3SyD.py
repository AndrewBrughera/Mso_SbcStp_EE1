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
anfSpkFiles.append('ANSpTsCF200HzCa190HzStPhs000AMBB20Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpTsCF200HzCa190HzStPhsN045AMBB20Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpTsCF200HzCa190HzStPhsN090AMBB20Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpTsCF200HzCa190HzStPhsN135AMBB20Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpTsCF200HzCa190HzStPhsN180AMBB20Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpTsCF200HzCa190HzStPhsN225AMBB20Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpTsCF200HzCa190HzStPhsN270AMBB20Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpTsCF200HzCa190HzStPhsN315AMBB20Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpTsCF200HzCa210HzStPhs000AMBB20Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpTsCF200HzCa210HzStPhsN045AMBB20Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpTsCF200HzCa210HzStPhsN090AMBB20Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpTsCF200HzCa210HzStPhsN135AMBB20Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpTsCF200HzCa210HzStPhsN180AMBB20Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpTsCF200HzCa210HzStPhsN225AMBB20Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpTsCF200HzCa210HzStPhsN270AMBB20Hz75dBsplMdSpSpec3.txt')
anfSpkFiles.append('ANSpTsCF200HzCa210HzStPhsN315AMBB20Hz75dBsplMdSpSpec3.txt')


sbc3Tuples = []
for f in anfSpkFiles:
    sbc3Tuple = mksbc3SyD(f)
    sbc3Tuples.append(sbc3Tuple)






