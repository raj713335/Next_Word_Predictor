#Import the required libraries

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


# We are Tryinng to Create a word Cloud that would enable us to view the moaximun used word in the file.corpus.txt.

dataset = open("corpus.txt", "r").read()

def create_word_cloud(string):
   cloud = WordCloud(background_color = "white", max_words = 1000,  stopwords = set(STOPWORDS))
   cloud.generate(string)
   cloud.to_file("wordCloud.png")


# Loading the dataset
path = 'corpus.txt'
text = open(path).read().lower()

print('corpus length:', len(text))


#Now, we want to split the entire dataset into each word in order without the presence of special characters.

tokenizer = RegexpTokenizer(r'\w+')
words = tokenizer.tokenize(text)

for each in words:
    print(each)



#Next, for the feature engineering part, we need to have the unique sorted words list. We also need a dictionary(<key: value>)
#with each word form the unique_words list as key and its corresponding position as value.

unique_words = np.unique(words)
unique_word_index = dict((c, i) for i, c in enumerate(unique_words))


WORD_LENGTH = 5
prev_words = []
next_words = []
for i in range(len(words) - WORD_LENGTH):
    prev_words.append(words[i:i + WORD_LENGTH])
    next_words.append(words[i + WORD_LENGTH])

print(prev_words[0])
print(next_words[0])



X = np.zeros((len(prev_words), WORD_LENGTH, len(unique_words)), dtype=bool)
Y = np.zeros((len(next_words), len(unique_words)), dtype=bool)
for i, each_words in enumerate(prev_words):
    for j, each_word in enumerate(each_words):
        X[i, j, unique_word_index[each_word]] = 1
    Y[i, unique_word_index[next_words[i]]] = 1


print(X[0][0])


# Building the model
#We use a single-layer LSTM model with 128 neurons, a fully connected layer, and a softmax function for activation.

model = Sequential()
model.add(LSTM(128, input_shape=(WORD_LENGTH, len(unique_words))))
model.add(Dense(len(unique_words)))
model.add(Activation('relu'))

# To view the modell summary and draw the graph of the model that we have creaeted

model.summary()

tf.keras.utils.plot_model(
    model, to_file='model.png', show_shapes=False, show_layer_names=True,
    rankdir='TB', expand_nested=False
)

# The model will be trained with 20 epochs with an RMSprop optimizer.


optimizer = RMSprop(lr=0.01)
model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])
history = model.fit(X, Y, validation_split=0.05, batch_size=128, epochs=2, shuffle=True).history

#After successful training, we will save the trained model and just load it back as needed.

model.save('keras_next_word_model.h5')
pickle.dump(history, open("history.p", "wb"))
model = load_model('keras_next_word_model.h5')
history = pickle.load(open("history.p", "rb"))

#The model outputs the training evaluation result after successful training, also we can access these evaluations from the history variable.



#Now, we need to predict new words using this model. To do that we input the sample as a feature vector. we convert the
# input string to a single feature vector.

def prepare_input(text):
    x = np.zeros((1, WORD_LENGTH, len(unique_words)))
    for t, word in enumerate(text.split()):
        print(word)
        try:
            x[0, t, unique_word_index[word]] = 1
        except:
            pass


    return x

prepare_input("The surgeon is".lower())






#To choose the best possible n words after the prediction from the model is done by sample function.

def sample(preds, top_n=3):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds)
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)

    return heapq.nlargest(top_n, range(len(preds)), preds.take)

#finally, for prediction, we use the function predict_completions which use the model to predict and return the list of n predicted words.

def predict_completions(text, n=3):
    if text == "":
        return("0")
    x = prepare_input(text)
    preds = model.predict(x, verbose=0)[0]
    next_indices = sample(preds, n)
    return [unique_words[idx] for idx in next_indices]

#Now let’s see how it predicts, we use tokenizer.tokenize fo removing the punctuations and also we choose 5 first words because our predicts base on 5 previous words.





boolx="N"

while boolx!="Y":
    try:
        seq=input("Enter Someting: ")
        seq = " ".join(tokenizer.tokenize(seq.lower())[0:5])
    except:
        seq="It is not a lack of love, but a lack of"

    print(predict_completions(seq, 5))

    boolx=input("To Exit Press  (Y) ELSE PRESS (N) AND ENTER: ")








