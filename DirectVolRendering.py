import numpy as np
import time

# Ray casting 
# Dakai Zhou

def TransferFunc1(vol, l1, l2, l3, l4, alpha1, alpha2, alpha3, alpha4, alpha5):
    dim = np.shape(vol)
    fres = np.zeros([dim[0], 4, dim[1], dim[2]])
    res1 = np.zeros([dim[1], dim[2]])
    res2 = np.zeros([dim[1], dim[2]])
    res3 = np.zeros([dim[1], dim[2]])
    res4 = np.zeros([dim[1], dim[2]])
    idxall = np.ones([dim[1], dim[2]])
    for i in range(dim[0]):
        idx = vol[i, :, :] < l1
        res1[idx] = 0
        res2[idx] = 0
        res3[idx] = 0
        res4[idx] = alpha1
        pidx = idx
        
        idx = vol[i, :, :] < l2
        res1[np.logical_xor(idx, pidx)] = 0
        res2[np.logical_xor(idx, pidx)] = 0
        res3[np.logical_xor(idx, pidx)] = 255
        res4[np.logical_xor(idx, pidx)] = alpha2
        pidx = idx
        
        idx = vol[i, :, :] < l3
        res1[np.logical_xor(idx, pidx)] = 0
        res2[np.logical_xor(idx, pidx)] = 255
        res3[np.logical_xor(idx, pidx)] = 0
        res4[np.logical_xor(idx, pidx)] = alpha3
        pidx = idx

        idx = vol[i, :, :] < l4
        res1[np.logical_xor(idx, pidx)] = 255
        res2[np.logical_xor(idx, pidx)] = 0
        res3[np.logical_xor(idx, pidx)] = 0
        res4[np.logical_xor(idx, pidx)] = alpha4
        pidx = idx

        res1[np.logical_xor(idxall, pidx)] = 127
        res2[np.logical_xor(idxall, pidx)] = 0
        res3[np.logical_xor(idxall, pidx)] = 127
        res4[np.logical_xor(idxall, pidx)] = alpha5

        fres[i, 0, :, :] = res1
        fres[i, 1, :, :] = res2
        fres[i, 2, :, :] = res3
        fres[i, 3, :, :] = res4

    return fres


def Compositing1(trans_vol):
    dim = np.shape(trans_vol)
    res = np.zeros([dim[2], dim[3], dim[1]])
    tmp_res = np.zeros([4, dim[2], dim[3]])
    ps = np.zeros([dim[1], dim[2], dim[3]])
    # stop condition
    #stc = np.ones([1, dim[2], dim[3]]) * 0.95
    for i in range(dim[0]):
        s = trans_vol[i, :, :, :]
        tmp_res[0:3, :, :] = ps[0:3, :, :] + (np.ones([dim[2], dim[3]]) - ps[3, :, :]) * s[3, :, :] * s[0:3, :, :]
        tmp_res[3, :, :] = ps[3, :, :] + (np.ones([dim[2], dim[3]]) - ps[3, :, :]) * s[3, :, :]
        ps = tmp_res
        # acceleration
        #stid = tmp_res[4, :, :] >= stc
        
        #conid = tmp_res[4, :, :] < stc

    for i in range(dim[1]):
        res[:, :, i] = tmp_res[i, :, :]
    return res


def DirectVolRendering1(vol, l1, l2, l3, l4, alpha1, alpha2, alpha3, alpha4, alpha5):
    tic = time.clock()
    trans_vol = TransferFunc1(vol, l1, l2, l3, l4, alpha1, alpha2, alpha3, alpha4, alpha5)
    res = Compositing1(trans_vol)
    dim = np.shape(res)
    res[:, :, 3] = np.ones([dim[0], dim[1]]) - res[:, :, 3]
    toc = time.clock()
    print 'Time elspsed ', toc - tic
    return res
