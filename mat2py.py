#mat2py.py
#Module containing functions to import matlab files into python

import os
import sys
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy as sp
import scipy.io
import tables
import h5py

def loadMat(mat):
    d = sp.io.loadmat(mat)
    return d
        
    

def loadMatH5(mat):
    # borrow "globals dictionary"
    q = dict()
    with h5py.File(mat,'r') as h5f:
        q.update(mat_struct_unpack(var) for var in h5f.values())

    return q
    
def mat_struct_unpack(obj):
    if type(obj)==h5py._hl.dataset.Dataset:
        objvals = np.zeros(obj.shape,obj.dtype)
        obj.read_direct(objvals)
        objname = obj.name.split('/')[-1]
        return (objname,objvals)
    else:
        objname = obj.name.split('/')[-1]
        objvals = dict(mat_struct_unpack(aa) for aa in obj.values())
        return (objname,objvals)


def evnt2d(subj,blocks,datatype):
    subj = 'EC41';
    blocks = [20];
    datatype = [1,2,3];
    dtnames = np.array(['AA','ProdAud','StimAud','Kin','Timeseries','ANIN4']);
    datatype = [x-1 for x in datatype];  #fix for 0 indexing
    for b in blocks
        dataFile = subj+'_B'+str(b)+'_'+'_'.join(list(dtnames[datatype]))+'.mat'
        try 
            d = sp.io.loadmat(dataFile)
        except:
            print('Loading HDF5 mat')
        f = tables.openFile(dataFile)
            
            f = h5py.File(dataFile)
            dat = (f['Dat']['AA'])
            dat.read_direct('AA')
            with tables.openFile(dataFile) as tf:
                dat = tables.openFile(dataFile)
                dat = tf.root.(evnt)
                for evnt in dat[Dat]
            
            dtlib[dt](Dat)
            AA(dat)


def AA(times)
    

            
    