#!/usr/bin/env python
# coding: utf-8

# In[13]:


def preprocessing():
    baseball_news = open("C:/Users/bong/팀플/미니프로젝트 뉴스분류/sports/baseball/baseball_news.txt","r",-1,'utf-8')
    basketball_news = open("C:/Users/bong/팀플/미니프로젝트 뉴스분류/sports/basketball/basketball_news.txt","r",-1,'utf-8')
    football_news = open("C:/Users/bong/팀플/미니프로젝트 뉴스분류/sports/football/football_news.txt","r",-1,'utf-8')
    volleyball_news = open("C:/Users/bong/팀플/미니프로젝트 뉴스분류/sports/volleyball/volleyball_news.txt","r",-1,'utf-8')
    golf_news = open("C:/Users/bong/팀플/미니프로젝트 뉴스분류/sports/golf/golf_news.txt","r",-1,'utf-8')
    
    baseball_news_list = baseball_news.read()
    basketball_news_list = basketball_news.read()
    football_news_list = football_news.read()
    volleyball_news_list = volleyball_news.read()
    golf_news_list = golf_news.read()
    
    baseball_news_list = baseball_news_list.split('\n')
    basketball_news_list = basketball_news_list.split('\n')
    football_news_list = football_news_list.split('\n')
    volleyball_news_list = volleyball_news_list.split('\n')
    golf_news_list = golf_news_list.split('\n')
    
    baseball_news_list= baseball_news_list[:len(baseball_news_list)-1]
    basketball_news_list = basketball_news_list[:len(basketball_news_list)-1]
    football_news_list = football_news_list[:len(football_news_list)-1]
    volleyball_news_list = volleyball_news_list[:len(volleyball_news_list)-1]
    golf_news_list = golf_news_list[:len(golf_news_list)-1]

    
    lists = [baseball_news_list, basketball_news_list, football_news_list, volleyball_news_list, golf_news_list]
    
    list_all_news = []
    for list_article in lists :
        for article in list_article :
            list_all_news.append(article)
            
    word_group = ''
    for list_article in lists :
        for article in list_article :
             word_group = word_group+article
    import os
    from konlpy.tag import Hannanum
    hannanum = Hannanum()
    
    file = 'C:/Users/bong/팀플/미니프로젝트 뉴스분류/nouns.txt' 
    if os.path.isfile(file):
        nouns = open("C:/Users/bong/팀플/미니프로젝트 뉴스분류/nouns.txt","r",-1,'utf-8')
        nouns = nouns.read()
        nouns = nouns.split('\n')
    else:
        nouns = hannanum.nouns(word_group)
        t = open("C:/Users/bong/팀플/미니프로젝트 뉴스분류/nouns.txt","w",-1,'utf-8')
        for noun in nouns:
            t.write(noun)
            t.write('\n')
    
    from collections import Counter            
    count = Counter(nouns)          
    words = dict(count.most_common())
    from keras.preprocessing.text import Tokenizer

    tokenizer = Tokenizer(num_words = 1000)
    tokenizer.fit_on_texts(nouns)
    word_index = tokenizer.word_index

    # 문자열을 정수 인덱스의 리스트로 변환
    sequences = tokenizer.texts_to_sequences(list_all_news)

    # 원-핫 이진 벡터 표현
    one_hot_results = tokenizer.texts_to_matrix(list_all_news,mode='binary')
    X_train = one_hot_results
    
    # 라벨생성
    list_label = []
    for list_article in lists :
        for i in range(len(list_article)) :
            if list_article == baseball_news_list:
                list_label.append('baseball_news')
            elif list_article == basketball_news_list:
                list_label.append('basketball_news')
            elif list_article == football_news_list:
                list_label.append('football_news')
            elif list_article == volleyball_news_list:
                list_label.append('volleyball_news')
            elif list_article == golf_news_list:
                list_label.append('golf_news')
    from sklearn.preprocessing import LabelEncoder
    from sklearn import preprocessing
    
    le = preprocessing.LabelEncoder()
    le = le.fit(list_label)
    list_label_=le.transform(list_label)
    from tensorflow.keras.utils import to_categorical
    one_hot = to_categorical(list_label_)
    y_train = one_hot
    
    return y_train, X_train

