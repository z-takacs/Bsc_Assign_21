"""

#
# File      :Q_2_WebScraping.py
# Created   : 24/11/2021 23:05
# Author    : Zoltan Takacs
# Version   : v1.0.0
# Licensing : (C) 2021 Zoltan Takacs, LYIT
#             Available under GNU Public License (GPL)
# Description: Web Scraping the Apache webpage from the OOPR VM.
#
"""
if __name__ == '__main__':

    '''
  Main method of application:

  Parameters: None

  Returns: None

    '''
from bs4 import BeautifulSoup
import requests

url = "http://192.168.136.128/"

result = requests.get(url)
doc= BeautifulSoup (result.text, "html.parser")
print (doc.prettify())

