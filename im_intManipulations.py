#%% Written by Doorgesh S Jokhun on 15/02/2022

#%%
import numpy as np


#%% im_021
# scales intensity values to 0-1
def im_021 (img):
    img = img + abs(np.min(img)) # in case the image is not a uint type and has negative values, this offset will make everything positive
    img = np.array(img).astype(np.float32)
    img = img - np.min(img[np.nonzero(img)])
    img = (img * (img>0).astype(np.float32))
    img = img/np.max(img)
    return img
    