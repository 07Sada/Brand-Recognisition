import gdown
import os
from pathlib import Path
import shutil
from dotenv import load_dotenv, find_dotenv

# load the env variables
load_dotenv()

DATASET_URL = os.getenv('DATASET_URL')

def main(url,output_filepath)->None:
    # checking if raw dataset is available
    try:
        if not raw_file_loc.exists():
            # initate the downloading the dataset
            gdown.download(url, fuzzy=True, output=str(output_filepath))
    
    except Exception as e:
        print(e)

if __name__ == '__main__':
    curr_dir = Path.cwd()

    raw_dir = curr_dir.as_posix() + '/data/raw'
    proceesed_dir = curr_dir.as_posix() + '/data/processed'

    raw_dataset = "brand_recognition.zip"
    raw_file_loc = Path(raw_dir, raw_dataset)

    main(url=DATASET_URL, output_filepath=raw_file_loc)

