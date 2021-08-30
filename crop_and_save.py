

#%%

from extract_crops import extract_crops
import numpy as np
from os import listdir
from os.path import join
from os.path import basename
import tifffile
import string
import multiprocessing as mp

#%%

source_dir = "/MBELab/jokhun/Pro 1 - Cellular Biosensor/Cellular biosensor/6. Data/Projected_Fea1"
des_dir = "/MBELab/jokhun/Pro 2 - DeepReal/Data"

filenames = [f for f in listdir(source_dir) if '.TIF' in f]
source_paths = [join(source_dir,f) for f in filenames]

#%%

def load_split_save (source_path,des_dir,target_shape):
    RawImg = tifffile.imread(source_path)
    Crops = extract_crops(RawImg,target_shape)
    suffix = list(string.ascii_lowercase)
    for count,Crop in enumerate(Crops):
        des_path = join(des_dir,basename(source_path).replace('.TIF',f'{suffix[count]}.TIF'))
        tifffile.imsave(des_path,Crop)
    return

#%%

if __name__ == '__main__':
    with mp.Pool() as p:
        p.starmap (load_split_save,zip(source_paths,[des_dir for _ in source_paths],[[706,706] for _ in source_paths]))


#%%



#%%




