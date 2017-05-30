from bs4 import BeautifulSoup
from urllib.request import urlopen
from time import sleep
 
url = 'http://www.goal.com/en-india/match/concordia-chiajna-vs-boto%C5%9Fani/2424326?ICID=LS'
source = urlopen(url)
html = source.read()
soup = BeautifulSoup(html, "html.parser")
match_container = soup.find("div",{"class":"match-header"})
home = match_container.find("div",{"class":"home"}).a.h2.text
away = match_container.find("div",{"class":"away"}).a.h2.text
match_status = match_container.find("div",{"class":"score"})
home_score = match_status.div.text
time = match_status.find("div",{"class":"vs"}).text
away_score = match_status.find("div",{"class":"away-score"}).text

while(True):
    home_score = match_status.div.text
    away_score = match_status.find("div",{"class":"away-score"}).text
    time = match_status.find("div",{"class":"vs"}).text
    if(time == "v"):
        print("{} vs {}".format(home, away))
        print("Match didn't start yet")
        break
    print("{} {}-{} {}".format(home, home_score, away_score, away))
    if (time == "HT"):
        print("Half-time")
        sleep(960)
        continue
    elif (time == "FT"):
        print("Full-time")
        break
    print("Time = {}".format(time))
    sleep(30)
    source = urlopen(url)
    html = source.read()
    soup = BeautifulSoup(html, "html.parser")
    match_container = soup.find("div",{"class":"match-header"})
    match_status = match_container.find("div",{"class":"score"})
source.close()
