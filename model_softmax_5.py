#!/usr/bin/env python
# coding: utf-8

# In[2]:


from keras import models
from keras import layers


# In[11]:


def make_model() :
    model = models.Sequential()
    model.add(layers.Dense(16, activation = 'relu', input_shape=(1000,)))
    model.add(layers.Dense(16, activation = 'relu'))
    model.add(layers.Dense(5, activation = 'softmax'))

    model.compile(optimizer = 'rmsprop',
                  loss = 'categorical_crossentropy',
                  metrics = ['accuracy'])

    return model

