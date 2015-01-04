# createDatStruct.py
import scipy as sp
import scipy.io
import parseTranscripts as pT
import HTK
import glob
import ecogUtil
import numpy as np

def createDat(subj,blocks,datatype):
    for b in blocks:
        bdir = subj+'_B'+str(b)
        badTimes = sp.io.loadmat(bdir+'/Artifacts/badTimeSegments')
        badTimes = badTimes['badTimeSegments']
        with open(bdir+'/Artifacts/badChannels.txt') as bC:
            badChannels = bC.readlines()
            
        #Metadata
        meta = {'block': b}
        
        
        #Get events from transcription

        tname = bdir+'/'+bdir+'_transcription_final.TextGrid'
        events = pT.parseTextGrid(tname,badTimes)
        
        #Load datatypes specified
        if 1 in datatype:
            neural = readAA(bdir+'/HilbAA_70to150_8band')
            meta = {'AAfs',neural['AAfs']}
            AA = neural['AA']


        DatStruct = {'meta':meta,
                    'events':events,
                    'AA':AA}
        
        return DatStruct

        
        
def readAA(dir):
    elects = glob.glob(dir+'/*.htk')
    tmp = HTK.readHTK(elects[0])
    AA = np.zeros(shape = [256,np.shape(tmp['data'])[1]])
    AAfs  = tmp['sampling_rate']
    tmp = None
    for e in elects:
        chan = ecogUtil.wav2chan(int(e[len(dir)+4:-4])) - 1
        d = HTK.readHTK(e)
        AA[chan,:] = sp.nanmean(d['data'])
    return {'AA':AA, 'AAfs':AAfs}
