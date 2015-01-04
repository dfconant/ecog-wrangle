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
    
    
    
def Dat2D(Dat,datatype,align,timing,dstring,datatype):
    
    words = np.where(np.char.find(Dat['events']['label'], dstring) >-1)  #search for matching labels
    phones = Dat['events']['contains'][words]                     #Access contained phones
    alignPhones = [w[1] for w in phones]
    label = Dat['events']['label'][alignPhones]
    starts = Dat['events']['starts'][alignPhones]
    
    nFeats = Dat[datatype].size[0]
    nTime = timing[1] -timing[0] *fs
    nTrials = starts.size
    D = np.empty([nFeats,nTime,nTrials]) *np.nan
    
    for t in range(starts)
        D
        D = Dat['AA']
    