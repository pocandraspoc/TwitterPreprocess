import numpy

from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils

def file_opener(fiename = "test.txt"):
	raw_text = open(fiename).read()
	raw_text = raw_text.lower()
	return raw_text

raw_text = file_opener()
raw_text = raw_text[0:100100]

chars = sorted(list(set(raw_text)))
char_to_int = dict(
	(c, i) for i, c in enumerate(chars)
	)

n_chars = len(raw_text)
n_vocab = len(chars)
seq_length = 100

dataX = []
dataY = []

for i in range(0, n_chars - seq_length, 1):
	seq_in = raw_text[i:i + seq_length]
	seq_out = raw_text[i + seq_length]
	dataX.append([char_to_int[char] for char in seq_in])
	dataY.append(char_to_int[seq_out])
n_patterns = len(dataX)


# reshape X to be [samples, time steps, features]
X = numpy.reshape(dataX, (n_patterns, seq_length, 1))
# normalize
#X = X / float(n_vocab)
# one hot encode the output variable


y = (dataY)
y= y[0:100000]
X=X[0:100000]

model_2 = load_model('my_model_weights.h5')

model_2.fit(X,
            y,
            epochs=1000,
            batch_size=2000) #18 hours to run on GPU
model_2.save('my_model_weights_02.h5')