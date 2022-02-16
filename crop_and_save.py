

#%%

from extract_crops import extract_crops
from os.path import join
from os.path import basename
import tifffile
import string


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




#%%



#%%




