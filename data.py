import pandas as pd
import os
import zipfile
import gdown

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

    print("Fill missing data")

    # get columns with missing data
    cols_w_missing_data = df.columns[df.isnull().any()]

    # fill missing data with the average of the other values in the column
    for column in cols_w_missing_data:
        mean = df[column].mean()
        df[column].fillna(mean,inplace=True)


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


# Class for generating one-hot codes from the labels
class LabelCoder:
  # Extracting the categories from the header of a csv file (sample_submissions.csv in this case). Filepath, and the index of the first column in the header with a valid label are required arguments
  def __init__(self, path_to_file, labels_start_in_header):
    self.encoding_list = pd.read_csv(path_to_file, header=None).loc[0, labels_start_in_header:].tolist()

  # Converting the labels to one-hot codes. This method considers the possibility for one file to have multiple labels
  def encode(self, labels):
    indices = []
    # Gathering the indices of the labels in the original list
    for label in labels:
      if label in self.encoding_list:
        indices.append(self.encoding_list.index(label))
    # Creating an array with the size of the number of categories with all zero values
    encoded_info = np.zeros(len(self.encoding_list))
    # Replacing zeros with ones at the indices of the present categories
    encoded_info[indices] = 1
    return encoded_info

  # Converting one-hot arrays to lists of categories
  def decode(self, array):
    # Gathering the indices of the ones in the
    indices = np.where(array != 0)[0]
    labels_list = []
    for index in indices:
        # Retrieving the appropriate label for the index from the original list of categories
        labels_list.append(self.encoding_list[index])
    return labels_list

