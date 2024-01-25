# -*- coding: utf-8 -*-
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
import zipfile
import shutil 
import os

def extract_zip(zip_file, target_dir):

  with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    # Create the target directory if it doesn't exist
    os.makedirs(target_dir, exist_ok=True)

    # Extract all files to the target directory
    zip_ref.extractall(target_dir)

if __name__ == '__main__':
    curr_dir = Path.cwd()

    raw_dir = curr_dir.as_posix() + '/data/raw'
    proceesed_dir = curr_dir.as_posix() + '/data/processed'

    raw_dataset = "brand_recognition.zip"
    raw_file_loc = Path(raw_dir, raw_dataset)

    extract_zip(zip_file=raw_file_loc, target_dir=proceesed_dir)

    parent_dir = Path(proceesed_dir)
    dataset_dir = Path(parent_dir, 'dataset')

    train_val_path_list = [d for d in dataset_dir.glob('*') if d.is_dir()]
    
    try:
        for sub_dir in train_val_path_list:
            shutil.move(sub_dir, parent_dir)
    except Exception as e:
       print(e)

    try:
        if not any(dataset_dir.iterdir()):
            shutil.rmtree(dataset_dir) 
    except Exception as e:
       print(e)
    
