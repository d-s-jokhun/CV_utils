#%% Written by Doorgesh S Jokhun on 15/02/2022

#%%
import cv2 as cv
import numpy as np


#%% im_bestfitResize
# Resizes the image while maintaining its aspect ratio till it fits within the frame defined by img_dim

def im_bestfitResize (img, img_dim=None, interpolation=cv.INTER_CUBIC):
    if type(img_dim)==type(None):
        return img
    elif type(img_dim)==int:
        img_dim = [img_dim,img_dim]
    elif (type(img_dim)==tuple or type(img_dim)==list) and len(img_dim)==1:
        img_dim=[img_dim[0],img_dim[0]]

    scale_factor = np.amin([img.shape[0]/img_dim[0], img.shape[1]/img_dim[1]])
    final_dim = [int(np.floor(img.shape[0]/scale_factor)),int(np.floor(img.shape[1]/scale_factor))]
    
    return cv.resize(img, final_dim, interpolation=interpolation)


#%% im_pad
# Symmetrically pads an image (on the x and y axes) to a size defined by finalSize
def im_pad (im,finalSize,mode='constant',constant_values=0):
    assert (len(im.shape)==2 or len(im.shape)==3), 'Image can only be 2D or 3D!'
    padWidth_0 = finalSize[0] - im.shape[0]
    if padWidth_0 > 0:
        pad_0 = (int(np.floor(padWidth_0/2)),int(np.ceil(padWidth_0/2)))
    else : pad_0 = (0,0)
    padWidth_1 = finalSize[1] - im.shape[1]
    if padWidth_1 > 0:
        pad_1 = (int(np.floor(padWidth_1/2)),int(np.ceil(padWidth_1/2)))
    else : pad_1 = (0,0)
    pad_2 = (0,0)
    if len(im.shape)==2:
        return np.pad(im,((pad_0,pad_1)),mode=mode,constant_values=constant_values)
    elif len(im.shape)==3:
        return np.pad(im,((pad_0,pad_1,pad_2)),mode=mode,constant_values=constant_values)



#%%





#%%




