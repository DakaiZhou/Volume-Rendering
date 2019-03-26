#################################################
# Read 2D slices of DICOM file into a volume
# Input:
# fp              file path
# Return:
# vol             volume
#
# ---Dakai Zhou
#################################################

import glob
import pydicom
import numpy as np

def DicomSlice2Vol(fp):
    flist = glob.glob(fp)
    tmp = pydicom.dcmread(flist[0])
    vol = np.zeros((len(flist), tmp.Rows, tmp.Columns))
    for fname in flist:
        slice = pydicom.dcmread(fname)
        vol[slice.InstanceNumber-1, :, :] = slice.pixel_array
    return vol
