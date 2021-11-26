"""

#
# File      :Q_2_WebScraping.py
# Created   : 24/11/2021 23:05
# Author    : Zoltan Takacs
# Version   : v1.0.0
# Licensing : (C) 2021 Zoltan Takacs, LYIT
#             Available under GNU Public License (GPL)
# Description: Web Scraping of the Apache2 landing page from the OOPR VM.
#
"""
if __name__ == '__main__':
    '''
  Main method of application:

  Parameters: None

  Returns: Scrapings of the Apache2 landing page.

    '''
import requests
from bs4 import BeautifulSoup

url = "http://192.168.136.128/"

result = requests.get(url)
doc = BeautifulSoup(result.text, "lxml")
print(doc.prettify())

with open("results.text", "w") as f:
    f.write(result.text)
    f.close()

################################
print(50 * "=")
print(20*(" ")+"Questions" )
print(50 * "=")

print("Q.2.1:")

################################
file = open("results.text" , "r")
data = file.read()
Apache2 = data.count("Apache2")
print("Q.2.2: The word Apache2 appears {} times in the Apache2 landing page.".format(Apache2))

################################
print("Q.2.3:")

