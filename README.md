# Mso_SbcStp_EE1
(Anaconda Python 3.7, Brian 2 Neural Simulator)HodgkinHuxleyType models: EE MSO neurons & adapting SBCs (AMBB)

Medial Superior Olive (MSO) neurons 
with excitatory inputs from  
SphericalBushyCells (SBCs) adapting/non-adapting
(Rothman & Manis 2003; Rudnicki & Hemmert 2017)

Model SBCs receive excitatory inputs from Model  
Auditory Nerve Fibers (ANFs) (Zilany et al. 2014)
of medium spontaneous rate
Complete ANF Matlab code downloaded from
https://www.urmc.rochester.edu/labs/carney/publications-code/auditory-models.aspx

Amplitude modulated binaural beats (AMBBs) are the default stimulus.  modxHz folders hold code for AMBB-responses without synaptic adaptation; in the AM subfolders, stimuli are AM (no beats) with static interaural phase difference (IPD). TauRec25ms subfolders hold code for the synaptic adaptation conditions with AMBB stimuli, and have their own AM subfolders.

(Outside Github: data folders on figshare and network drives have additional conditions, and slightly different organization. There the data for AM-noBeats-staticIPD stimuli with and without synaptic adaptation, identified by filename, are in the TauRec25ms\AM folders.)
