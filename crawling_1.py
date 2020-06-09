#!/usr/bin/env python
# coding: utf-8

# In[100]:


from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import re
import time


# In[101]:


def baseball_crawling(page = 2):
    link_list = []
    for i in range(page):
        url_part1 = """https://sports.news.naver.com/kbaseball/news/index.nhn?isphoto=N&page="""
        url_part2 = str(i)

        url = url_part1+url_part2
    
        res = requests.get(url)
        soup=bs(res.text, 'html.parser')

        for link in soup.findAll("a"):
            if 'href' in link.attrs: 
                if link.attrs['href'][0:20] == '/kbaseball/news/read':
                    link_final = ('http://sports.news.naver.com'+link.attrs['href'])
                    link_list.append(link_final)
                    
    list_baseball_news = []
    for link in link_list :
        res = requests.get(link)
        soup=bs(res.text, 'html.parser')
        news = soup.find(id='newsEndContents').text
        news= news.replace("\n"," ")
        list_baseball_news.append(news)
        
    t = open("C:/Users/bong/팀플/미니프로젝트 뉴스분류/sports/baseball/baseball_news.txt","w",-1,'utf-8')
    for baseball_news in list_baseball_news:
        t.write(baseball_news)
        t.write('\n')


# In[102]:


def basketball_crawling(page = 2):
    link_list = []
    for i in range(page):
        url_part1 = """https://sports.news.naver.com/basketball/news/index.nhn?isphoto=N&page="""
        url_part2 = str(i)

        url = url_part1+url_part2
    
        res = requests.get(url)
        soup=bs(res.text, 'html.parser')

        for link in soup.findAll("a"):
            if 'href' in link.attrs: 
                if link.attrs['href'][0:21] == '/basketball/news/read':
                    link_final = ('http://sports.news.naver.com'+link.attrs['href'])
                    link_list.append(link_final)
                    
    list_basketball_news = []
    for link in link_list :
        res = requests.get(link)
        soup=bs(res.text, 'html.parser')
        news = soup.find(id='newsEndContents').text
        news= news.replace("\n"," ")
        list_basketball_news.append(news)
        
    t = open("C:/Users/bong/팀플/미니프로젝트 뉴스분류/sports/basketball/basketball_news.txt","w",-1,'utf-8')
    for basketball_news in list_basketball_news:
        t.write(basketball_news)
        t.write('\n')


# In[103]:


def football_crawling(page = 2):
    link_list = []
    for i in range(page):
        url_part1 = """https://sports.news.naver.com/kfootball/news/index.nhn?isphoto=N&page="""
        url_part2 = str(i)

        url = url_part1+url_part2
    
        res = requests.get(url)
        soup=bs(res.text, 'html.parser')

        for link in soup.findAll("a"):
            if 'href' in link.attrs: 
                if link.attrs['href'][0:20] == '/kfootball/news/read':
                    link_final = ('http://sports.news.naver.com'+link.attrs['href'])
                    link_list.append(link_final)
                    
    list_football_news = []
    for link in link_list :
        res = requests.get(link)
        soup=bs(res.text, 'html.parser')
        news = soup.find(id='newsEndContents').text
        news= news.replace("\n"," ")
        list_football_news.append(news)
        
    t = open("C:/Users/bong/팀플/미니프로젝트 뉴스분류/sports/football/football_news.txt","w",-1,'utf-8')
    for football_news in list_football_news:
        t.write(football_news)
        t.write('\n')


# In[104]:


def volleyball_crawling(page = 2):
    link_list = []
    for i in range(page):
        url_part1 = """https://sports.news.naver.com/volleyball/news/index.nhn?isphoto=N&page="""
        url_part2 = str(i)

        url = url_part1+url_part2
    
        res = requests.get(url)
        soup=bs(res.text, 'html.parser')

        for link in soup.findAll("a"):
            if 'href' in link.attrs: 
                if link.attrs['href'][0:21] == '/volleyball/news/read':
                    link_final = ('http://sports.news.naver.com'+link.attrs['href'])
                    link_list.append(link_final)
                    
    list_volleyball_news = []
    for link in link_list :
        res = requests.get(link)
        soup=bs(res.text, 'html.parser')
        news = soup.find(id='newsEndContents').text
        news= news.replace("\n"," ")
        list_volleyball_news.append(news)
        
    t = open("C:/Users/bong/팀플/미니프로젝트 뉴스분류/sports/volleyball/volleyball_news.txt","w",-1,'utf-8')
    for volleyball_news in list_volleyball_news:
        t.write(volleyball_news)
        t.write('\n')


# In[105]:


def golf_crawling(page = 2):
    link_list = []
    for i in range(page):
        url_part1 = """https://sports.news.naver.com/golf/news/index.nhn?isphoto=N&page="""
        url_part2 = str(i)

        url = url_part1+url_part2
    
        res = requests.get(url)
        soup=bs(res.text, 'html.parser')

        for link in soup.findAll("a"):
            if 'href' in link.attrs: 
                if link.attrs['href'][0:15] == '/golf/news/read':
                    link_final = ('http://sports.news.naver.com'+link.attrs['href'])
                    link_list.append(link_final)
                    
    list_golf_news = []
    for link in link_list :
        res = requests.get(link)
        soup=bs(res.text, 'html.parser')
        news = soup.find(id='newsEndContents').text
        news= news.replace("\n"," ")
        list_golf_news.append(news)
        
    t = open("C:/Users/bong/팀플/미니프로젝트 뉴스분류/sports/golf/golf_news.txt","w",-1,'utf-8')
    for golf_news in list_golf_news:
        t.write(golf_news)
        t.write('\n')


# In[106]:


def crawling():
    golf_crawling()
    volleyball_crawling()
    football_crawling()
    baseball_crawling()
    basketball_crawling()

