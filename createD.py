#createD.py
import os
import sys
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy as sp
import scipy.io
import scipy.stats.mstats
import tables
import h5py
import parseTranscripts as pT
import math



def matDat2D(matDat,datatype,align):
    dtnames = np.array(['AA','ProdAud','StimAud','Kin','Timeseries','ANIN4']);
    Dat = sp.io.loadmat(matDat)
    transcript = glob.glob('*Transcription_Final.TextGrid')
    events = pT.parseTranscripts(transcript)
    data = Dat[dtnames(datatype)]
    if datatype == 1:
    	data = sp.stats.mstats.zscore(data)
    Dat = None



    onsets = list()
    labels = list()
    D = np.array()
    for e in range(events):
    	if events[e][-1] is '2':
    		labels.append(events[e]['Phrase'])
    		onsetS=events[e]['Words']['Phones'][align][StartTime]
    		onset = onsetS*[dtnames[datatype]+'fs'] 

    return D,labels,onsets
    
    
def Dat2D(Dat,datatype,align,timing,dstring,zscore):    
    
    #Get events of interest
    words = np.where(np.char.find(Dat['events']['label'], dstring) >-1)  #search for matching labels
    phones = Dat['events']['contains'][words]                     #Access contained phones
    alignPhones = [w[align-1] for w in phones]                   #Use specified phone from align
    
    #Get info of events from Dat
    label = Dat['events']['label'][alignPhones]
    start = Dat['events']['start'][alignPhones]
    fs = Dat['meta'][datatype + 'fs']

    
    #z-score if desired
    if zscore:
        data = sp.stats.mstats.zscore(Dat[datatype],axis = 1)
    else:
        data = Dat[datatype]
    blockMean = np.nanmean(Dat[datatype],axis = 1)
    blockSTD = np.nanstd(Dat[datatype],axis = 1)
    
    #Initialize tensor
    nFeats = data.shape[0]
    nTime = math.floor((timing[1] +timing[0]) *fs)
    nTrials = start.size
    D = np.empty([nFeats,nTime,nTrials]) *np.nan
    
    #Use start times and timing to extract data    
    for t in range(nTrials):
        drange = range(int(math.floor((start[t]-timing[0])*fs)),int(math.floor((start[t]+timing[1])*fs)))
        D[:,:,t] = data[:,drange]
    
    meta = {'label':label,
            'fs':fs,
            'datatype':datatype,
            'dstring':dstring,
            'align':align,
            'timing':timing,
            'blockMean':blockMean,
            'blockSTD':blockSTD}
            
    return D,meta
