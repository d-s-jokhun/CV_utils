

#%%

import os
import pathlib
import multiprocessing as mp
import zipfile
import io
from extract_crops import extract_crops
import tifffile
from tqdm import tqdm


#%%

def extract_crop_save (archive_path,img_name,target_dir,target_shape):
    with zipfile.ZipFile(archive_path) as archive:
        img = tifffile.imread(io.BytesIO(archive.read(img_name)))  
    segs = extract_crops(img, target_shape)
    seg_num = -1
    for seg in segs:
        seg_num+=1
        save_path = os.path.join(str(target_dir),img_name[:-4]+f'_{seg_num}.tif')
        tifffile.imsave(save_path,seg)
    return

def img_process (archive_path,target_dir,target_shape):
    target_dir = pathlib.Path(os.path.join(target_dir,os.path.basename(archive_path)[:-4]))
    target_dir.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive_path) as archive:
        namelist = [filename for filename in archive.namelist() if '.tif' in filename]
    with mp.Pool() as pool:
        pool.starmap(extract_crop_save,zip ([archive_path for img in namelist],namelist,[target_dir for img in namelist],[target_shape for img in namelist]))
            
    return

#%%

if __name__=='__main__':

    root_dir = pathlib.Path("/gpfs0/home/jokhun/Pro 1/U2OS small mol screening")
    source_dir = root_dir.joinpath('FullFields_3Ch')
    target_dir = root_dir.joinpath('BigFields_3Ch')
    target_shape = (232,232)

    archive_names = sorted([zipped.name for zipped in source_dir.glob('*.zip')])

    for archive_name in tqdm(archive_names):
        img_process (os.path.join(str(source_dir),archive_name) ,target_dir,target_shape)


# %%
