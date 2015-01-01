#createD.py
import os
import sys
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy as sp
import scipy.io
import tables
import h5py
import parseTranscripts as pT

matDat = 'EC41_B20_AA_ProdAud_StimAud.mat'

def matDat2D(matDat,datatype,align,):
    dtnames = np.array(['AA','ProdAud','StimAud','Kin','Timeseries','ANIN4']);
    Dat = sp.io.loadmat(matDat)
    transcript = glob.glob('*Transcription_Final.TextGrid')
    events = pT.parseTranscripts(transcript)
    data = Dat[dtnames(datatype)]
    if datatype == 1
    	data = sp.stats.mstats.zscore(data)
    Dat = None


l
    onsets = list()
    labels = list()
    D = np.array()
    for e = range(events)
    	if events[e][-1] is '2'
    		labels.append(events[e]['Phrase'])
    		onsetS=events[e]['Words']['Phones'][align][StartTime]
    		onset = onsetS*[dtnames[datatype]+'fs' 
    		drange = range(onset-())
    		D.append(data[onsets[-1]*[dtnames[datatype]+'fs'])
    return D,labels,onsets