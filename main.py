import requests
import re
from bs4 import BeautifulSoup
def song_dload(url,filename):
    data=requests.get(url)
    output=open(filename,'wb')
    output.write(data.content)
song_url=[]
filename=[]
inp=raw_input("Enter movie name \n")
url="https://www.google.co.in/search?q=naasongs.com+"+inp
r=requests.get(url)
soup=BeautifulSoup(r.content,'html.parser')
bang=str(soup.find('h3'))
url_new=bang.split('q=')
url_new=str(url_new[1])
url_new=url_new.split('&')
url_new=url_new[0]
r=requests.get(url_new)
soup=BeautifulSoup(r.content,'html.parser')
print url_new
s_list=soup.find_all(class_=re.compile("entry-content"))
s_list=str(s_list)
s_list=s_list.split("<a href=")
for i in range(1,7):

    temp=s_list[i]
    temp=temp.split('>')[0]
    temp=temp.replace('"','')
    song_url.append(temp)
    #print temp.split('>')
for _ in song_url:
    #tempo=requests.get(_)
    _=str(_)
    _=_.replace('%20',' ')
    _=_.split(' -')
    _=_[-1]
    _=_.split('"')
    _=_[0]
    filename.append(_)
i=0
for i in range(len(song_url)):
    try:
        song_dload(song_url[i],filename[i])
        print "Downloaded",filename[i],"Sucessfully"
    except:
        pass
print "Check your pwd :)"

