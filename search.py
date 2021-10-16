
import re
from bs4 import BeautifulSoup
import urllib.parse
from pytube import YouTube
import os
from pathlib import Path
from selenium import webdriver

youtubeSearchUrl = "https://www.youtube.com/results?search_query="
webdriverPath = "C:\chromedriver_win32\chromedriver.exe"
youtubeUrl = "https://www.youtube.com"
searchText = str(input("Search "))
searchTextEncoded = urllib.parse.quote(searchText)
searchResultsUrl = youtubeSearchUrl + searchTextEncoded
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(webdriverPath, options=options)
driver.get(searchResultsUrl)
html = driver.page_source
driver.quit()
soup = BeautifulSoup(html, 'html.parser')
link = soup.find(href=re.compile(re.escape("/watch?v=")), id="thumbnail")
youtubeVideoUrl = youtubeUrl + link['href']
try:
    yt = YouTube(youtubeVideoUrl)
    stream = yt.streams.get_by_itag(18)
    downloadPath = os.path.join(Path.home(), "Downloads")
    fileName = yt.title+'.mp4'
    stream.download(output_path=downloadPath, filename=fileName)
    os.startfile(os.path.join(downloadPath, fileName))
except:
    print("Error")
