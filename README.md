# Next_Word_Predictor
A Deep Learning Model to predict next word in a sequence using LSTM.

The Application is created using Tensorflow and Python.


## Getting Started
- Clone the repo and cd into the directory
```sh
$ git clone https://github.com/raj713335/Next_Word_Predictor.git
$ cd CORONA_HACKBOOK
```

## The training data is present in the corpus.txt file.


## The WordCloud of the traing Data

![](wordCloud.png)




## Install tensorflow and all the other required libraries 

```sh
$ pip install tensorflow, keras 

import numpy as np
from nltk.tokenize import RegexpTokenizer
from keras.models import Sequential, load_model
from keras.layers import LSTM
from keras.layers.core import Dense, Activation
from keras.optimizers import RMSprop
import matplotlib.pyplot as plt
import pickle
import heapq
import tensorflow as tf
from wordcloud import WordCloud, STOPWORDS
import numpy as npy
from PIL import Image
```

# Now To train the Model Enter to the NLP_DEEP_LEARNING FOLDER and then again to the sub directory CODE and run the Model Creator.py file

```sh
$ cd NLP_DEEP_LEARNING
$ cd CODE
$ python Model Creator.py
```


## The Summary of the model created

Model: "sequential_1"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
lstm_1 (LSTM)                (None, 128)               749056    
_________________________________________________________________
dense_1 (Dense)              (None, 1334)              172086    
_________________________________________________________________
activation_1 (Activation)    (None, 1334)              0         
=================================================================
Total params: 921,142
Trainable params: 921,142
Non-trainable params: 0
_________________________________________________________________

![](model.png)


# Now To run the Model keras_next_word_model.h5 run the Output.py file

```sh
$ python Output.py
```


# A X-Ray Report Example .

![](gr1_lrg-a.jpg)



## Run the coronovirus.py file to train a model and save it as coronovirus.py

```sh
$ python coronavirus.py
```

## Download The Trained Model From the Following link in case you don't have the computational power to train your model

$ url : https://drive.google.com/u/0/uc?id=1112evrjqWlEPw1hkPA44LoVfm_USuys8&export=download


## To load and run the model and test it against unknown data\images place you test images in the OUTPUT Folder with 1.jpg/1.jpeg name with it.


```sh
$ python coronovirus_validate.py
```
