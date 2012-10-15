##### 
# WARNING: MATCHING OF FILE NAMES SOMETIMES INACCURATE
#####

import urllib2
import os
import re
from urllib2 import URLError
from HTMLParser import HTMLParser


def request(link):
  """
  Request a page at link at return the HTTP response
  """
  the_page = ""
  try:
    print "## Requesting page at " + link 
    req = urllib2.Request(link)
    response = urllib2.urlopen(req)
    the_page = response.read()
  except URLError, e:
    print e.reason
    
  return the_page


def save(data, path):
  """
  Saves a file, unless it already exists
  """
  if (os.path.isfile(path)):
    print('Already exists! ' + path)
  else:
    f = open(path, 'wb')
    f.write(data)
    print('Saved ' + path)


class SylvanParser(HTMLParser):
  def __init__(self):
    HTMLParser.__init__(self)
    htmlLinks = []
    pdfLinks = []
  
  def getResults(self):
    link = self.imageLink
    self.imageLink = ''
    return link
  
  def handle_starttag(self, tag, attrs):
    if tag == 'a':
      #TODO request the .htm
      #TODO request the .pdf
      pass
    if tag == 'img':
      attributeDictionary = dict(attrs)
      if 'id' in attributeDictionary and attributeDictionary[ 'id' ] == 'mainImg':
        self.imageLink = attributeDictionary[ 'src' ]

"""Singleton instance of our HTML parser"""
PARSER = SylvanParser()


def makeHttpLink(link):
  return "http://math-magic.com/" + link

def main():
  """
  Scrap all tricks and save them locally.
  """
  
  with open('trick_lists.txt', 'r') as f:
    for line in f:
      trickCategoryLink = line.strip()
      
      # Save the page containing the list
      content = request(trickCategoryLink)
      save(content, os.path.split(trickCategoryLink)[-1])
      
      # Now save each page linked to by the list
      scrapTrickList(trickCategoryLink) 
      print '#########################################################'


def scrapTrickList(pageLink):
  content = request(pageLink)
  contentCopy = content #Note: apparently something happens after the first finditer( , content)
  
#  # PDF versions of the trick guides (.pdf)
#  patternForPdf = r'a href="(.*pdf)"'
#  for m in re.finditer(patternForPdf, content):
#    pdfLink = m.group(1)
#    print pdfLink
#    
#    pdfLinkSplinters = os.path.split(pdfLink)
#    folderName = pdfLinkSplinters[0]
#    fileName = pdfLinkSplinters[1]
#    
#    try:
#      os.makedirs(folderName)
#    except:
#      pass
#    
#    content = request(makeHttpLink(pdfLink))
#    save(content, pdfLink)
  
  # HTML versions of the trick guides (.htm)
  patternForHtm = r'<a href="(.*htm)">'
  for m in re.finditer(patternForHtm, contentCopy):
    link = m.group(1)
    print link
    scrapGuidePage(makeHttpLink(link))
  


def scrapGuidePage(pageLink):
  """
  Scrap a page containing one trick guide
  """
  response = request(pageLink)
  if response:
    patternForGuideBody = r'(.*)((?:<h4.*)+)(Back\s+to\s+top.*)'
    matchObject = re.match(patternForGuideBody, response, re.DOTALL)
    
    if not matchObject:
      matchObject = re.match(patternForGuideBody.replace('h4', 'h3'), response, re.DOTALL)
    
    if matchObject:
      content = matchObject.group(2)
      
      linkSplinters = os.path.split(pageLink)
      fileName = linkSplinters[-1]
      folderName = os.path.split(linkSplinters[0])[-1]
      try:
        os.makedirs(folderName)
      except:
        pass
      
      save(content, os.path.join(folderName, fileName))

    else:
      print 'ERROR: no matches found for guide ' + pageLink 


if __name__ == "__main__":
  main()