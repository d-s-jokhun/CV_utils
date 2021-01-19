


#%%

import numpy as np


#%%

def extract_crops (img, target_shape):
        
    row_start = int(np.floor((img.shape[0] % target_shape[0])/2))
    col_start = int(np.floor((img.shape[1] % target_shape[1])/2))

    num_of_row_segs = img.shape[0] // target_shape[0]
    num_of_col_segs = img.shape[1] // target_shape[1]

    segs = []
    for row_seg in range(num_of_row_segs):
        for col_seg in range(num_of_col_segs):
            segs.append(img[\
                row_start+(row_seg*target_shape[0]):row_start+(row_seg*target_shape[0])+target_shape[0],\
                    col_start+(col_seg*target_shape[1]):col_start+(col_seg*target_shape[1])+target_shape[1]\
                        ])

    return segs


#%%





#%%





#%%



