from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

from fake_useragent import UserAgent

ua = UserAgent()
print(ua.chrome)

headers = {
    "User-Agent": ua.chrome,
    "Referer": "https://www.google.com",
}
response = requests.get("https://www.capterra.in/directory", headers=headers)
print(response.text)









# html=urlopen("https://www.capterra.in/directory")
# bsObj=BeautifulSoup(html,features="html.parser")

# print(bsObj)

#for chiild in bsObj.find("table",{"id":"giftList"}).children:
 #   print(chiild)

#for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
#      print(sibling)



#print(bsObj.find("table",{"id":"giftList"}).tr) the row which is skipped while finding next sibling

# print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text()) #here code goes throgh img tag -->then <td> tag which conatain img(parent) -->after that previous sibling (td tag) --> then we select text within 




#print(bsObj.find("h1").get_text())