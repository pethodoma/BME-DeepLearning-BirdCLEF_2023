# BME-DeepLearning-BirdCLEF_2023

**Team name:** Deep Dream Team

**Members:**
- Rimai Dániel (BR2BUJ)
- Skribanek Csanád Mihály (G0OTOY)
- Pethő Dominik (HEBAPU)

## Project Description

The project is a Kaggle competition named [BirdCLEF 2023](https://www.kaggle.com/competitions/birdclef-2023). The primary goal is to train a model capable of classifyng sound samples of bird calls based on which bird they belong
 to.
## Repository Contents

### The files in the testruns folder
- [CNN_curriculum_learning.ipynb](testruns/CNN_curriculum_learning.ipynb): This notebook contains a testrun where we tried curriculum learning for the classes with above 100 samples.
- [Custom_datagenerator_augmentation.ipynb](testruns/Custom_datagenerator_augmentation.ipynb): This notebook contains a testrun for the classes with above 500 samples using a costum datagenerator for augmentation.
- [Custom_datagenerator_augmentation_Resnet50.ipynb](testruns/Custom_datagenerator_augmentation_Resnet50.ipynb): This notebook contains our try with Resnet 50, for the classes with above 500 samples.
- [Milestone2_Bird_Unet_with_data_loader.ipynb](testruns/Milestone2_Bird_Unet_with_data_loader.ipynb): This notebook contains one training with the Unet model. This file has to be run for training.
- [pretrained_model_transfer_learning.ipynb](testruns/pretrained_model_transfer_learning.ipynb): This  notebook contains experimenting with google's pretrained model and using transfer learning to build our model.
- [Best_performance_30_classes.ipynb](testruns/Best_performance_30_classes.ipynb): This notebook contains a convnetwork model we trained with only the classes with above 500 samples. With this model we could reach more than 0.72 validation accuracy.


### Base folder
- [preprocess_final.ipynb](preprocess_final.ipynb): This notebook contains the code for the preprocess.
- [final_model_training.ipynb](final_model_training.ipynb): This notebook contains the training process we used to train the final model.


## Preprocessing data, training, evaluating model
*Preprocessing data:* The notebook [preprocess_final.ipynb](preprocess_final.ipynb) needs to be run. This contains code for downloading all the files needed (given by kaggle) and create the folders with the final, usable samples\
*Training the model:* This can be done by running the [final_model_training.ipynb](final_model_training.ipynb) notebook. The notebook contains code for downloading the png files we used for training, finding the optimal hyperparameters and training the model accordingly.\
*Model evaluation:* The notebook [model_eval.ipynb](model_eval.ipynb) must be run. In this notebook, we can see that the accuracy is as expected according to the training process, and there are predictions given for the test sample used by Kaggle.\
The elaborate documantetaion can be seen in [Documentation](Documentation)