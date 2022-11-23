Used the PASCAL VOC dataset for training and testing the model.
Made modifications to myTFDistributedCustomTrainer.py
Genereated dataset from PASCAL VOC dataset for training and testing.
Build VGG16 model to train the dataset.

ML-MODEL FLASK DEPLOYMENT:

In this project we have used Tensor flows library keras and used resnet model  to comparision i.e times taken to run original(i.e on Normal cloab run) vs the inffered one (which is done using FLask)

It is a flask webapp deployed with resnet50 model

We need to install all the required packages(flask,keras) on the local machine before executing out model.

Run app.py, this will load the deployed model in the localhost 5000 port.

Then we drew the comparision on both the approaches and obsered the following: the time taken to predict using inference is 30 milliseconds while the time taken in cloab is 86 milliseconds, there’s a significant difference i.e the inference is 2.8 times faster than the one on colab.

