% ANSR100kHzAMBB1Species3.m
% Applying the Zilany et al. 2014 model with amplitude modulated
% binaural beats stimuli (AMBB) as in Dietz et al. 2013 PNAS, 2014 JNrPhys
% (also consider 2 control stimuli:
% binaural beats with no AM, AM tones with a fixed, static IPD)
% Andrew Brughera 8 June, 2017
%
% Fs_Hz to 100 kHz, compatible with Zilany et al. 2014 model
% Checking the effects of CF on response to 32-Hz pure tone at 60 dBSPL rms
% CFs_Hz = [64 56 48 40];
% low-, medium-, and high-spontaneous-rate AN fibers simulated
% only 2 fibers per CF for quick preliminary results
%
% model fiber parameters
%clear all;
% (CF varied) CF in Hz;
cohc  = 1.0;   % normal ohc function
cihc  = 1.0;   % normal ihc function
%fiberType = 3; % spontaneous rate (in spikes/s) of the fiber BEFORE refractory effects; "1" = Low, 0 spk/s; "2" = Medium, 5 spk/s; "3" = High, 100 spk/s
implnt = 1;    % "0" for approximate or "1" for actual implementation of the power-law functions in the Synapse

% stimulus parameters
Fs_Hz = 100e3;  % sampling rate of 100,000 Hz;
Fs_kHzStr = num2str(round(Fs_Hz/1000));
Ts_s = 1/Fs_Hz;
% Zilany et al. 2009, 2014, adaptation coefficients designed for
% sample rate of 100 kHz, "must be 100 kHz".

% PSTH parameters -> make these SpikeTime parameters instead
% We can make a psth later, but
nrep = 1;              % number of stimulus repetitions (e.g., 50);
%psthbinwidth_s = 1/(80 * F0_Hz) % 0.5e-3; % binwidth in seconds;
psthbinwidth_s = Ts_s; % binwidth in seconds at full temporal resolution;

fiberTypeStrings = {'Low Spont'; 'Medium Spont'; 'High Spont'};
fiberTypeStringsShort = {'LoSp'; 'MdSp'; 'HiSp'};
nFiberTypes = length(fiberTypeStringsShort);

CarrierFreqs_Hz = [200];
% CarrierFreqs_Hz = [600];
% BBeatFreqs_Hz = [8 20];
BBeatFreqs_Hz = [8];
% BBeatFreqs_Hz = [4 8 16 32 64];
% BBeatFreqs_Hz = [16 32 64];
% (Generate stimuli and model AN spike responses in Matlab.)
% (Generate bushy cell spike responses in EarLab)
% (Apply the beat direction at the model MSO inputs in NEURON)
% BBeatDirections = [1 -1];
% Dietz et al.:
% "The polarity of the IPD was defined with respect to the AMBB beat direction:
% positive IPD means leading on the side with the higher carrier
% frequency."


StartPhases_deg = [0 -45 -90 -135 -180 -225 -270 -315]; % phase lags
% Also present AM stimuli with same modulation freqs and static IPD
minimumZilanyCF_Hz = 56;
CFs_Hz = max(CarrierFreqs_Hz,minimumZilanyCF_Hz);
% CFs_Hz = [56];
% Minimum CF allowed by Zilany et al. model is 91.2 Hz
% In c code by Zilany et al. 2009, 2014:
% /** Calculate the location on basilar membrane from CF */
% bmplace = 11.9 * log10(0.80 + cf / 456.0);

% Stimulus duration 750 ms, T_s = 0.75
Tdur_s = 0.75;
% rise/fall time in seconds
rTdur_s = 0.15; % Dietz et al. 2013:  Stimuli with modulation frequencies > 8 Hz
% were gated on with a squared sine ramp of 150-ms duration to minimize the
% influence of the stimulus onset.
t_s = 0:Ts_s:Tdur_s-Ts_s;
mxpts = length(t_s);
irpts = rTdur_s*Fs_Hz;
n = 2; % raised sine power
rt_s = t_s(1:(irpts));
onRamp = sin(2*pi*(1/(4*rTdur_s)) * rt_s).^n;
offRamp = cos(2*pi*(1/(4*rTdur_s)) * rt_s).^n;

stimI_dBSPLrms = 75; % rms stimulus intensity in dB SPL


% setup for  maximum number of MSO inputs, Bushy Cells (BCs), AN fibers
% maxMSOInputsContraI = 4;
% maxMSOInputsIpsiI = maxMSOInputsContraI;
% maxMSOInputsContraE = 4;
% maxMSOInputsIpsiE = maxMSOInputsContraE;
% nBCs = maxMSOInputsContraI + maxMSOInputsIpsiI + maxMSOInputsContraE + maxMSOInputsIpsiE;
% nANFsPerSBC = 3;
% nANFsPerGBC = 30;
% On each side (left and right)
nANFsPerFiberType = 132; % The EarLab BushyCell modules select M fibers at random from nANFsPerFiberType
% ITD varies continuously so don't need
% % independent spikes for each ITD tested
% ITDsPerCarrierPeriod = 20;
% nITDs = 2*ITDsPerCarrierPeriod + 1;

spikeTimes_s = cell([length(CFs_Hz) length(BBeatFreqs_Hz) length(StartPhases_deg) length(fiberTypeStrings) nANFsPerFiberType]);
% Synchrony Index (help synccalc)
syncIdx   = -1 * ones([length(CFs_Hz) length(BBeatFreqs_Hz) length(StartPhases_deg) length(fiberTypeStrings) nANFsPerFiberType]);
% Rayleigh Criterion for significance: 2*number_of_spikes*(syncIdx^2) > 13.8
two_n_Rsq  = -1 * ones([length(CFs_Hz) length(BBeatFreqs_Hz) length(StartPhases_deg) length(fiberTypeStrings) nANFsPerFiberType]);

% (ear can be used to set the lead and lag frequencies)
ears = cell(1,2);
ears{1} = 'LeadEar'; % left, right, ispi, contra, (often contra or left)
ears{2} = 'LagEar'; % left, right, ispi, contra, (often ipsi or right)

% +1 for contra, -1 for ipsi
LeadLag = [1 -1];

% %better to use a structure?
% earStruct = struct('side',{'Contra','Ipsi'},'LeadLag',{1,-1});

% species
% 1: Cat
% 2: Human (Q10 from Shera et al. 2002)
% 3: Human (Q10 from Glasberg & Brown 1990)
species = 3;

% noiseType
% 0: fixed fGn: (noise will be same in every simulation)
% 1: variable fGn:
noiseType = 1;


for ear = 1:length(ears)
    
    for idxCF = 1:length(CFs_Hz)
        
        % T_s = T_s_vector(idxCF);
        CF_Hz = CFs_Hz(idxCF); % Characteristic Frequency in Hz;
        
        for idxBBeatF = 1:length(BBeatFreqs_Hz)
            
            BBFreqHz = BBeatFreqs_Hz(idxBBeatF);
            F0_Hz = CarrierFreqs_Hz(idxCF) + (LeadLag(ear)*(BBFreqHz/2)); % carrier frequency in Hz
            
            for idxStartPhase = 1:length(StartPhases_deg)
                
                StartPhase_deg = StartPhases_deg(idxStartPhase);
                StartPhase_rad = (2*pi/360)*StartPhase_deg;
                
                % Apply the amplitude modulation at the BBFreq_Hz
                AM = (1 - cos(2*pi*BBFreqHz*t_s))/2;
                % pressureInput_Pa = sqrt(2)*20e-6*10^(stimI_dBSPLrms/20)*AM.*sin(2*pi*F0_Hz*t_s + StartPhase_rad); % unramped stimulus
                pressureInput_Pa = (1/0.433)*20e-6*10^(stimI_dBSPLrms/20)*AM.*sin(2*pi*F0_Hz*t_s + StartPhase_rad); % unramped stimulus
                
                % Apply on/off ramps (sin^2) for stimuli with modulation frequencies > 8 Hz
                if (BBFreqHz > 8)
                    pressureInput_Pa(1:(irpts))=pressureInput_Pa(1:irpts).*onRamp;
                    pressureInput_Pa((mxpts-irpts+1):mxpts)=pressureInput_Pa((mxpts-irpts+1):mxpts).*offRamp;
                end
                %             % Linear ramp
                %             if (rTdur_s > 0)
                %                 pressureInput_Pa(1:irpts)=pressureInput_Pa(1:irpts).*(0:(irpts-1))/irpts;
                %                 pressureInput_Pa((mxpts-irpts):mxpts)=pressureInput_Pa((mxpts-irpts):mxpts).*(irpts:-1:0)/irpts;
                %             end
                
                for fiberType = 1:nFiberTypes
                    
                    spikeCountThisFiberType = 0;
                    
                    for ANFiber = 1:nANFsPerFiberType
                        %for ANFiber = 1:2   % short test
                        
                        vihc = model2014_IHC_30Hz(pressureInput_Pa,CF_Hz,nrep,Ts_s,Tdur_s*2,cohc,cihc,species);
                        [meanrate,varrate,psth] = model2014_Synapse_30Hz(vihc,CF_Hz,nrep,Ts_s,fiberType,noiseType,implnt);
                        
                        timeout_s = (1:length(psth))*Ts_s;
                        %     psth_samples_per_bin = round(psthbinwidth_s*Fs_Hz);  % number of psth bins per psth bin
                        %     psthtime_s = timeout_s(1:psth_samples_per_bin:end); % time vector for psth
                        %     pr = sum(reshape(psth,psth_samples_per_bin,length(psth)/psth_samples_per_bin))/nrep; % pr of spike in each bin
                        %     Psth = pr/psthbinwidth_s; % psth in units of spikes/s
                        
                        spikeTimes_s{idxCF,fiberType,ANFiber} = timeout_s(psth==1);
                        spikeCountThisFiberType = spikeCountThisFiberType + length(spikeTimes_s{idxCF,fiberType,ANFiber});
                        [syncIdx(idxCF,fiberType,ANFiber),two_n_Rsq(idxCF,fiberType,ANFiber)] = synccalc(spikeTimes_s{idxCF,fiberType,ANFiber},1/CF_Hz);
                        
                    end  % ANFiber
                    
                    % (for computation efficiency in Matlab
                    % do not repeatedly concatenate spike times)
                    % Now that all ANFs are completed for this CF,
                    % loop again on ANFs.
                    % Sort fiber number & spike times for this CF by time,
                    % and write result to text file.
                    
                    % filename ANspikeTimes_s_FreqFiberTypeANF#
                    % DON'T USE RIGHT/LEFT, THE F0 AND AM FREQUENCY (SAME AS
                    % BEAT FREQUENCY: 'AMBB' num2str(BBeatFreq_Hz) 'Hz')
                    filename = ['ANSpTs' 'CF' num2str(CF_Hz) 'Hz' 'Ca' num2str(F0_Hz) 'Hz' 'StPhs' num2str(StartPhase_deg) 'AMBB' num2str(BBFreqHz) 'Hz' num2str(stimI_dBSPLrms) 'dBspl' fiberTypeStringsShort{fiberType} 'Spec' num2str(species)];
                    minusIndx = find(filename == '-');
                    for m = 1:length(minusIndx)
                        filename(minusIndx(m)) = 'N';
                    end
                    pointIndx = find(filename == '.');
                    for m = 1:length(pointIndx)
                        filename(pointIndx(m)) = 'p';
                    end
                    filename = [filename '.txt'];
                    fid0 = fopen(filename,'w');
                    
                    ANFNumber_SpikeTimes = -1*ones(spikeCountThisFiberType,2);
                    spikeIdx = 0;
                    
                    for ANFiber = 1:nANFsPerFiberType
                        newSpikeTimes_s = (spikeTimes_s{idxCF,fiberType,ANFiber});
                        newSpikeCount = length(newSpikeTimes_s);
                        % EarLab, 1st column: fiber number, 2nd column: spiketimes
                        ANFNumber_SpikeTimes((spikeIdx + 1):(spikeIdx + newSpikeCount),1) = (ANFiber - 1);
                        ANFNumber_SpikeTimes((spikeIdx + 1):(spikeIdx + newSpikeCount),2) = newSpikeTimes_s;
                        % prepare spikeIdx for next AN fiber
                        spikeIdx = spikeIdx + newSpikeCount;
                    end
                    
                    % Sort by times, saving the indexes
                    [sortedSpikeTimes,sortTimesIdxs] = sort(ANFNumber_SpikeTimes(:,2));
                    ANFNumber_SpikeTimes_sortedByTime = [ANFNumber_SpikeTimes(sortTimesIdxs,1) sortedSpikeTimes];
                    
                    for m = 1:size(ANFNumber_SpikeTimes_sortedByTime,1)
                        count_fpr = fprintf(fid0,'%2d %11.9f\n', ANFNumber_SpikeTimes_sortedByTime(m,:));
                    end
                    status_fcl = fclose(fid0);
                    
                end  % fiberType
                
            end % idxStartPhase
            
        end % idxBBeatF
        
    end  % idxCF
    
end % ear

% List CFs, Fiber Types, synchrony indexes, Rayleigh criterion value
% CFs_Hz
% fiberTypeStrings
% syncIdx
% two_n_Rsq
