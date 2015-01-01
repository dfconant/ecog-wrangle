import h5py
import numpy as np

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

def loadhdf5mat(hdf5matfilename):
    # borrow "globals dictionary"
    q = globals()
    with h5py.File(hdf5matfilename,'r') as h5f:
        q.update(mat_struct_unpack(var) for var in h5f.values())

    del q

        
