#!/usr/bin/env python
# coding: utf-8

# In[7]:


def train_model():
    from sklearn.model_selection import train_test_split
    from model_softmax_5 import make_model
    from preprocessing_1000_3 import preprocessing
    from crawling_1 import crawling
    
    crawling()
    model = make_model()
    preprocessing = preprocessing()
    
    y_train, X_train = preprocessing
    X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.2, random_state=1234)
    
    history = model.fit(X_train,
                        y_train,
                        epochs = 20,
                        batch_size = 512,
                        )
    return model,X_test,y_test

