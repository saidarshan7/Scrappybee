#Traversing a Single Domain

#this part dont provide desired articles we get unexpected articles here

# from urllib.request import urlopen
# from bs4 import BeautifulSoup


# html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")

# bsObj = BeautifulSoup(html)

# for link in bsObj.findAll("a"):
#    if 'href' in link.attrs:
    # print(link.attrs['href'])





    #so, to get only relatbale articles we can modiefy this bit :

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import re
# html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
# bsObj = BeautifulSoup(html)
# for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$")):
#   if 'href' in link.attrs:
#     print(link.attrs['href'])



# Of course, having a script that finds all article links in one, hardcoded Wikipedia arti‐
# cle, while interesting, is fairly useless in practice. We need to be able to take this code
# and transform it into something more like the following:    


from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

# random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html)
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))



links = getLinks("/wiki/Kevin_Bacon")

while len(links) > 0:
  newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
  print(newArticle)
  links = getLinks(newArticle)


