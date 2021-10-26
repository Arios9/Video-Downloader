
import re
from bs4 import BeautifulSoup
import urllib.parse
from pytube import YouTube
import os
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import subprocess

youtubeSearchUrl = "https://www.youtube.com/results?search_query="
youtubeUrl = "https://www.youtube.com"
searchText = str(input("Search "))
searchTextEncoded = urllib.parse.quote(searchText)
searchResultsUrl = youtubeSearchUrl + searchTextEncoded
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get(searchResultsUrl)
html = driver.page_source
driver.quit()
soup = BeautifulSoup(html, 'html.parser')
link = soup.find(href=re.compile(re.escape("/watch?v=")), id="thumbnail")
youtubeVideoUrl = youtubeUrl + link['href']
print(youtubeVideoUrl)
