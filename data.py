import pandas as pd
import os
import zipfile
import gdown
import numpy as np

def download_data():
    
    # download the database zip file from drive
    url = 'https://drive.google.com/uc?id=1DFmudcCxYPOoaeBBSRh1yAsLLz03M4KV'
    zipfile = 'database.zip'

    gdown.download(url,zipfile)

    # unzip database
    zip_file = 'database.zip'

    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall()



def cleandata():
    
    
    df = pd.read_csv('train_metadata.csv')

 
    print("Cleaning data...")

    # get the names of the files with a rating of 0.0 or 0.5 - these are the files we want to get rid of
    # we also need to delete the rows with these ratings as we won't be able to use them
    rows_to_delete = df.loc[df['rating'].isin([0.0, 0.5])].index
    df.drop(rows_to_delete, inplace=True)
    poorRatingFilenames = df.loc[df['rating'].isin([0.0, 0.5])]['filename'].values.tolist()
          
    # the folder which contains the audio files
    trainpath='train_audio'

    # creating an array of the files to delete with the full path
    filesToDelete = [os.path.join(subdir, file) for subdir, dirs, files in os.walk(trainpath) for file in files if os.path.basename(subdir)+'/'+file in poorRatingFilenames]
    
    ## if there aren't any files to delete, then we dont need to do anything - assuming the data path is right
    if len(filesToDelete) == 0:
        print("Data has already been cleaned")
    else:
        count = sum(1 for file in filesToDelete if os.remove(file) is None)
        print(f"Deleted {count} files")


    print("Preprocessing...")

    # this far the only columns with missing data are longitude and latitude
    cols_w_missing_data = ['latitude', 'longitude']
    df[cols_w_missing_data] = df.groupby('primary_label')[cols_w_missing_data].transform(lambda x: x.fillna(round(x.mean(),4)))

    
    # one-hot encoding 
    # primary label, secondary label, and type is important to us
    df = pd.get_dummies(df, columns=['primary_label', 'secondary_labels', 'type'])
    for col in df.columns:
        if col.startswith('type') or col.startswith('secondary_labels') or col.startswith('primary_label' ):
            df[col] = df[col].astype('int8')

    # some columns are not important to us -> dropping them
    df = df.drop(['scientific_name', 'common_name', 'author', 'license', 'url', 'filename'], axis=1)

    print('Preprocessing done.')





