# BME-DeepLearning-BirdCLEF_2023

**Team name:** Deep Dream Team

**Members:**
- Rimai Dániel (BR2BUJ)
- Skribanek Csanád Mihály (G0OTOY)
- Pethő Dominik (HEBAPU)

## Project Description

The project is a Kaggle competition named [BirdCLEF 2023](https://www.kaggle.com/competitions/birdclef-2023). The primary goal is to train a model capable of predicting whether each of the 264 species of birds provided in the training data can be heard in a given sound sample.

## Repository Contents

There are currently three files in the repository:

- [Deep_Dream_Team_Milestone1.ipynb](Deep_Dream_Team_Milestone1.ipynb): This Jupyter Notebook contains the preprocessing steps for the project. This is outdated, the current preprocessing steps can be found in:
- [preprocess_final.ipynb](preprocess_final.ipynb): This contains all the neccesar code to preprocess the whole dataset. Running it creates a parent folder with the name 'final samples' and child folders named after the bird labels. Every folder contains the respective chirps to the bird.
The two notebooks below were run using a 13100 files long dataset that we created by randomly picking 50 samples from all the birds.
- [Experimenting_with_tensorflow_data_pipeline.ipynb](Experimenting_with_tensorflow_data_pipeline.ipynb): This contains the experimenting steps for creating a data pipeline for efficiently loading the spectrograms and a training on a simple network to see if it actually works.
- [Milestone2_Bird_Unet_with_data_loader.ipynb](Milestone2_Bird_Unet_with_data_loader.ipynb): This Jupyter Notebook contains one training with the Unet model. This file has to be run for training.
- [pretrained_model_transfer_learning.ipynb](pretrained_model_transfer_learning.ipynb): This Jupyter Notebook contains experimenting with google's pretrained model and using transfer learning to build our model



## Info about projects current state
We have done the preprocessing steps, and are currently working on training the model
