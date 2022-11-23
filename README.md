# MultiModalClassifier
This is a project repo for multi-modal deep learning classifier with popular models from Tensorflow and Pytorch. The goal of these baseline models is to provide a template to build on and can be a starting point for any new ideas, applications. If you want to learn basics of ML and DL, please refer this repo: https://github.com/lkk688/DeepDataMiningLearning.

# Package setup
Install this project in development mode
```bash
(venv38) MyRepo/MultiModalClassifier$ python setup.py develop
```
After the installation, the package "MultimodalClassifier==0.0.1" is installed in your virtual environment. You can check the import
```bash
>>> import TFClassifier
>>> import TFClassifier.Datasetutil
>>> import TFClassifier.Datasetutil.Visutil
```

If you went to uninstall the package, perform the following step
```bash
(venv38) lkk@cmpeengr276-All-Series:~/Developer/MyRepo/MultiModalClassifier$ python setup.py develop --uninstall
```

Used the PASCAL VOC dataset for training and testing the model.
Made modifications to myTFDistributedCustomTrainer.py
Genereated dataset from PASCAL VOC dataset for training and testing.
Build VGG16 model to train the dataset.


