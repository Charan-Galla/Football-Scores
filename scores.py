from bs4 import BeautifulSoup
from urllib.request import urlopen
from time import sleep

url = input('Enter the Goal.com live match url here:  ')
try:
    def Retrieve_Data(url):
        global source, html, match_container, match_status, home, away, home_score, away_score, time
        source = urlopen(url)
        html = source.read()
        soup = BeautifulSoup(html, "html.parser")
        match_container = soup.find("div",{"class":"match-header"})
        match_status = match_container.find("div",{"class":"score"})
        home = match_container.find("div",{"class":"home"}).a.h2.text
        away = match_container.find("div",{"class":"away"}).a.h2.text
        home_score = match_status.div.text
        time = match_status.find("div",{"class":"vs"}).text
        away_score = match_status.find("div",{"class":"away-score"}).text

    while(True):
        Retrieve_Data(url)
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
        print("Time : {}".format(time))
        sleep(30)
    source.close()

except ValueError:
    print("**** Invalid url. Try again. Make sure the url has http:// ****")
