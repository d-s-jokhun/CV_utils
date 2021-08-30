
#%%

import numpy as np
from os import listdir
from os.path import join
import tifffile
import multiprocessing as mp
import cv2


#%%

def z_projection (id_str, replacement_str):

    source_dir = "/MBELab/jokhun/Pro 2 - IntelZoom/Data/60xSR"
    des_dir = "/MBELab/jokhun/Pro 2 - IntelZoom/Projected Data/"

    # id_str = '_sam1__SR_w2CSU Cy5_'
    # replacement_str = '_Lysosome_Fea1Cy5_Sam1_'
    # id_str = '_sam1__SR_w3CSU RFP_'
    # replacement_str = '_ER_Fea1RFP_Sam1_'
    # id_str = '_sam1__SR_w4CSU GFP_'
    # replacement_str = '_MT_Fea1GFP_Sam1_'
    # id_str = '_sam1__SR_w5CSU DAPI_'
    # replacement_str = '_Nuc_Fea1DAPI_Sam1_'

    # filenames = [f for f in listdir(source_dir) if id_str in f]
    # source_path = [join(source_dir,f) for f in filenames]
    # des_path = [join(des_dir,f.replace(id_str,replacement_str)) for f in filenames]

    filenames = [f for f in listdir(source_dir) if ('.TIF' in f and 'DIC' not in f and '_SR_SR_' in f)]
    source_path = [join(source_dir,f) for f in filenames]
    des_path = [join(des_dir,'60x_SR_'+f[19:]) for f in filenames]  # '100x_'+f[17:], '60x_'+f[16:], '40x_'+f[14:]

    print('No. of files detected =',len(filenames))

    return source_path, des_path


#%%

def img_project (img_path, z_dim=0, projection='max'):

    if projection == 'max':
        projectred_img = np.amax(tifffile.imread(img_path).astype(np.float64), axis = z_dim)
    elif projection == 'sum':
        projectred_img = np.sum(tifffile.imread(img_path).astype(np.float64), axis = z_dim)
    elif projection == 'None':
        projectred_img = tifffile.imread(img_path).astype(np.float64)

    return projectred_img

def project_resize_save (source_path, destination_path, z_dim=0, projection='max', dst_size=(512,512)):
    img = img_project (source_path, z_dim=z_dim, projection=projection)
    # img = cv2.resize(img, dsize=dst_size, interpolation=cv2.INTER_AREA)
    img = np.subtract(img,img.min())
    img = (np.multiply(np.divide(img,img.max()),255)).astype(np.uint8)
    tifffile.imsave(destination_path,img)


#%%

# identity = ['_Fea2_Sam1_SR_w1CSU DIC_', '_Fea2_Sam1_SR_w2CSU Cy5_', '_Fea2_Sam1_SR_w3CSU RFP_', '_Fea2_Sam1_SR_w4CSU GFP_', '_Fea2_Sam1_SR_w5CSU DAPI_']
# new_identity = ['_DIC_Fea2DIC_Sam1_', '_Actin_Fea2Cy5_Sam1_', '_ER_Fea2RFP_Sam1_', '_Golgi_Fea2GFP_Sam1_', '_Nuc_Fea2DAPI_Sam1_']

# for sample in range (5):
#     z_dim = 0
#     if sample == 0:
#         projection = 'None'
#     else: projection = 'max'

#     source_path, des_path = z_projection(identity[sample],new_identity[sample])

#     if __name__ == '__main__':
#         with mp.Pool() as p:
#             p.starmap (project_resize_save,zip(source_path,des_path,[z_dim for path in source_path],[projection for path in source_path]))


# %%

source_path, des_path = z_projection(0,0)
z_dim = 0
projection = 'max'

if __name__ == '__main__':
    with mp.Pool() as p:
        p.starmap (project_resize_save,zip(source_path,des_path,[z_dim for _ in source_path],[projection for _ in source_path]))


#%%



#%%


