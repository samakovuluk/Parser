# -*- encoding: utf-8 -*-
from grab import Grab
import codecs
g = Grab(log_file='out.html')
from newspaper import Article
from bs4 import BeautifulSoup
import re
import csv
import io
import gzip
import unicodedata as ucd
import sys
sr="banana"
pop='MOscva'
url='https://news.yandex.kz/yandsearch?text='+sr+'+'+pop+'&rpt=nnews2&grhow=clutop'+'&p='
a=list()
for i  in range(0,2):
    try:
        g.go(url+str(i))
        print(url)
        #g.doc.set_input("q","grab")
        #g.doc.submit(submit_name = 'btnK')
        #print g.doc.select('//head/title').text()

        for el in g.doc.select('//li[@class="search-item"]'):
            soup=BeautifulSoup(el.html())
            for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
                a.append(link.get('href'))
    except:
        break

d=dict()
c=0
r=list()
with codecs.open("withnewspaper.csv", "w", "utf-8") as file:
    file.write('publishedAt,title,author,url,urlToImage,description'+'\r\n')
    for i in a:
        url = i
        article = Article(url)
        article.download()
        article.parse()
                         
        title=article.title
        authors=article.authors
        publish_date=article.publish_date
        text=article.text
        top_image=article.top_image
        '''print(type(title.encode('UTF-8')))
        print(type(authors))
        print(type(str(publish_date)))
        print(type(text))
        print(type(top_image))'''
        print(i)
        file.write(str(publish_date)+',')
        file.write(title+',')
        file.write(' '.join([str(x) for x in authors])+ ',')
        file.write(i+',')
        file.write(top_image+',')
        file.write(text)
        file.write('\r\n')


        
       
        





    '''print title
    print authors
    print publish_date
    print text
    print top_image'''
    
    '''if title!=None:
        r.append({'title':title})
    else:
        r.append({'title':''})
        
    if publish_date!=None:
        r.append({'publishedAt':publish_date})
    else:
        r.append({'publishedAt':''})
        
    if authors!=None:
        r.append({'author':authors})
    else:
        r.append({'author':''})
        
    if top_image!=None:
        r.append({'urlToImage':top_image})
    else:
        r.append({'urlToImage':''})
        
    if text!=None:
        r.append({'description':(text)})
    else:
        r.append({'description':''})
    r.append({'url':i})'''
    '''try:
        if(publish_date!=None):
            file.write(publish_date)
        file.write(',')
        if(len(title)>0):
            file.write(title)
        file.write(',')
        if(authors!=None):
            file.write(authors)
        file.write(',')
        file.write(str(i))
        file.write(',')
        if(top_image!=None):
            file.write(top_image)
        file.write(',')
        if(text!=None):
            file.write(text)
        file.write('\n')
    except:
        file.write('\n')'''
    
    
    
    

        
    #print "----------------"

        #writer.writerow(({'publishedAt': str(article.publish_date), 'title': str(article.title), 'author': str(article.authors), 'url': i, 'urlToImage': str(article.top_image), 'description': str(article.text) }))
        #writer.write( article.publish_date,  article.title, article.authors,  i,  article.top_image,  article.text,"\n" )
    
    
