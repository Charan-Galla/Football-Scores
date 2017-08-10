from bs4 import BeautifulSoup
from urllib.error import URLError
from urllib.request import urlopen
from sys import exit
from time import sleep
from subprocess import Popen

def sendmessage(message):
    Popen(['notify-send', message])
    print(message)

def Retrieve_Data(url):
    try:
        global source, html, match_container, match_status, home, away, home_score, away_score, time, print_score, print_time
        source = urlopen(url)
        html = source.read()
        source.close()
        soup = BeautifulSoup(html, "html.parser")
        match_container = soup.find("div",{"class":"match-header"})
        match_status = match_container.find("div",{"class":"score"})
        home = match_container.find("div",{"class":"home"}).a.h2.text
        away = match_container.find("div",{"class":"away"}).a.h2.text
        home_score = match_status.div.text
        time = match_status.find("div",{"class":"vs"}).text
        away_score = match_status.find("div",{"class":"away-score"}).text
        print_score = "{} {}-{} {}".format(home, home_score, away_score, away)
        print_time = "Time : {}".format(time)
    except ValueError:
        print("**** Invalid url. Try again. Make sure the url has http:// ****")
        exit()
    except URLError:
        print("Check your internet connection")
        exit()

url = input('Enter the Goal.com live match url here:  ')
Retrieve_Data(url)
if(time == "v"):
    print("{} vs {}\nMatch didn't start yet".format(home, away))
    exit()
elif(time == "FT"):
    print("FT: {}\nMatch already finished".format(print_score))
    exit()
elif(time != "HT"):
    print("{}\n{}".format(print_score, print_time))

while(True):
    home_score_prev = home_score
    away_score_prev = away_score
    Retrieve_Data(url)
    if (home_score != home_score_prev or away_score != away_score_prev):
        sendmessage("Goal update! {}\n{}".format(print_time, print_score))
    if(time == "HT"):
        sendmessage("Half-Time\n{}".format(print_score))
        sleep(30)
        while(True):
            Retrieve_Data(url)
            if (time != "HT"):
                sendmessage("2nd half-kickoff\n{}".format(print_score))
                break
            else:
                sleep(30)
    if(time == "FT"):
        sendmessage("Full-Time\n{}".format(print_score))
        break
    sleep(30)
