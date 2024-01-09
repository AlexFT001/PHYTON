import time, requests
from bs4 import BeautifulSoup

def findYT(search):
    words = search.split()

    link = "http://www.youtube.com/results?search_query="

    for i in words:
        link += i + "+"

    search_result = requests.get(link)

    if search_result.status_code == 200:
        soup = BeautifulSoup(search_result.text, 'html.parser')

        videos = soup.select('a',attrs={'class':'yt-uix-tile-link'})

        videolist=[]
        for v in videos:
            tmp = 'https://www.youtube.com' + v['href']
            videolist.append(tmp)
            print(videolist)
    else:
        print(f"Failed to retrieve page. Status code: {search_result.status_code}")



findYT("quim barreiros")