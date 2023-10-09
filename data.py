import pandas as pd
import os


def cleandata():
    
    df = pd.read_csv('train_metadata.csv'))

    print("Cleaning data...")

    # get the names of the files with a rating of 0.0 or 0.5 - these are the files we want to get rid of
    zeroratingArr = df.loc[df['rating'].isin([0.0, 0.5])]['filename'].values.tolist()
          
    # the folder which contains the audio files
    trainpath='train_audio'

    # creating an array of the files to delete with the full path
    FilesToDelete = [os.path.join(subdir, file) for subdir, dirs, files in os.walk(trainpath) for file in files if os.path.basename(subdir)+'/'+file in zeroratingArr]
    
    ## if there aren't any files to delete, then we dont need to do anything - assuming the data path is right
    if len(FilesToDelete) == 0:
        print("Data has already been cleaned\n")
        return
    
    # deleting the files
    count = sum(1 for file in FilesToDelete if os.remove(file) is None)
    print(f"Deleted {count} files\n")




