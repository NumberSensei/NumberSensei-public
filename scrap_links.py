import urllib2
import os
import re
from urllib2 import URLError
from HTMLParser import HTMLParser


RAW_PAGE_SEGMENT = '''
if(MSFPhover) { MSFPnav2n=MSFPpreload("_derived/basic_memorization.htm_cmp_sumipntg010_hbtn.gif"); MSFPnav2h=MSFPpreload("_derived/basic_memorization.htm_cmp_sumipntg010_hbtn_a.gif"); }
// --></script><a href="basic_memorization.htm" language="JavaScript" onmouseover="if(MSFPhover) document['MSFPnav2'].src=MSFPnav2h.src" onmouseout="if(MSFPhover) document['MSFPnav2'].src=MSFPnav2n.src"><img src="_derived/basic_memorization.htm_cmp_sumipntg010_hbtn.gif" width="140" height="40" border="0" alt="Basic Memorization" align="middle" name="MSFPnav2"></a> <script language="JavaScript"><!--
if(MSFPhover) { MSFPnav3n=MSFPpreload("_derived/fractions_decimals.htm_cmp_sumipntg010_hbtn.gif"); MSFPnav3h=MSFPpreload("_derived/fractions_decimals.htm_cmp_sumipntg010_hbtn_a.gif"); }
// --></script><a href="fractions_decimals.htm" language="JavaScript" onmouseover="if(MSFPhover) document['MSFPnav3'].src=MSFPnav3h.src" onmouseout="if(MSFPhover) document['MSFPnav3'].src=MSFPnav3n.src"><img src="_derived/fractions_decimals.htm_cmp_sumipntg010_hbtn.gif" width="140" height="40" border="0" alt="Fractions and Decimals" align="middle" name="MSFPnav3"></a> <script language="JavaScript"><!--
if(MSFPhover) { MSFPnav4n=MSFPpreload("_derived/multiply_numbers.htm_cmp_sumipntg010_hbtn.gif"); MSFPnav4h=MSFPpreload("_derived/multiply_numbers.htm_cmp_sumipntg010_hbtn_a.gif"); }
// --></script><a href="multiply_numbers.htm" language="JavaScript" onmouseover="if(MSFPhover) document['MSFPnav4'].src=MSFPnav4h.src" onmouseout="if(MSFPhover) document['MSFPnav4'].src=MSFPnav4n.src"><img src="_derived/multiply_numbers.htm_cmp_sumipntg010_hbtn.gif" width="140" height="40" border="0" alt="Multiplying Numbers" align="middle" name="MSFPnav4"></a> <script language="JavaScript"><!--
if(MSFPhover) { MSFPnav5n=MSFPpreload("_derived/multiply_srat.htm_cmp_sumipntg010_hbtn.gif"); MSFPnav5h=MSFPpreload("_derived/multiply_srat.htm_cmp_sumipntg010_hbtn_a.gif"); }
// --></script><a href="multiply_srat.htm" language="JavaScript" onmouseover="if(MSFPhover) document['MSFPnav5'].src=MSFPnav5h.src" onmouseout="if(MSFPhover) document['MSFPnav5'].src=MSFPnav5n.src"><img src="_derived/multiply_srat.htm_cmp_sumipntg010_hbtn.gif" width="140" height="40" border="0" alt="Multiplying Strategies" align="middle" name="MSFPnav5"></a> <script language="JavaScript"><!--
if(MSFPhover) { MSFPnav6n=MSFPpreload("_derived/base_manipulation.htm_cmp_sumipntg010_hbtn.gif"); MSFPnav6h=MSFPpreload("_derived/base_manipulation.htm_cmp_sumipntg010_hbtn_a.gif"); }
// --></script><a href="base_manipulation.htm" language="JavaScript" onmouseover="if(MSFPhover) document['MSFPnav6'].src=MSFPnav6h.src" onmouseout="if(MSFPhover) document['MSFPnav6'].src=MSFPnav6n.src"><img src="_derived/base_manipulation.htm_cmp_sumipntg010_hbtn.gif" width="140" height="40" border="0" alt="Base Manipulation" align="middle" name="MSFPnav6"></a> <script language="JavaScript"><!--
if(MSFPhover) { MSFPnav7n=MSFPpreload("_derived/sequences.htm_cmp_sumipntg010_hbtn.gif"); MSFPnav7h=MSFPpreload("_derived/sequences.htm_cmp_sumipntg010_hbtn_a.gif"); }
// --></script><a href="sequences.htm" language="JavaScript" onmouseover="if(MSFPhover) document['MSFPnav7'].src=MSFPnav7h.src" onmouseout="if(MSFPhover) document['MSFPnav7'].src=MSFPnav7n.src"><img src="_derived/sequences.htm_cmp_sumipntg010_hbtn.gif" width="140" height="40" border="0" alt="Sequences" align="middle" name="MSFPnav7"></a> <script language="JavaScript"><!--
if(MSFPhover) { MSFPnav8n=MSFPpreload("_derived/miscellaneous.htm_cmp_sumipntg010_hbtn.gif"); MSFPnav8h=MSFPpreload("_derived/miscellaneous.htm_cmp_sumipntg010_hbtn_a.gif"); }
// --></script><a href="miscellaneous.htm" language="JavaScript" onmouseover="if(MSFPhover) document['MSFPnav8'].src=MSFPnav8h.src" onmouseout="if(MSFPhover) document['MSFPnav8'].src=MSFPnav8n.src"><img src="_derived/miscellaneous.htm_cmp_sumipntg010_hbtn.gif" width="140" height="40" border="0" alt="Miscellaneous" align="middle" name="MSFPnav8"></a> <script language="JavaScript"><!--
if(MSFPhover) { MSFPnav9n=MSFPpreload("_derived/approximate.htm_cmp_sumipntg010_hbtn.gif"); MSFPnav9h=MSFPpreload("_derived/approximate.htm_cmp_sumipntg010_hbtn_a.gif"); }
// --></script><a href="approximate.htm" language="JavaScript" onmouseover="if(MSFPhover) document['MSFPnav9'].src=MSFPnav9h.src" onmouseout="if(MSFPhover) document['MSFPnav9'].src=MSFPnav9n.src"><img src="_derived/approximate.htm_cmp_sumipntg010_hbtn.gif" width="140" height="40" border="0" alt="Approximations" align="middle" name="MSFPnav9"></a> <script language="JavaScript"><!--
if(MSFPhover) { MSFPnav10n=MSFPpreload("_derived/probability.htm_cmp_sumipntg010_hbtn.gif"); MSFPnav10h=MSFPpreload("_derived/probability.htm_cmp_sumipntg010_hbtn_a.gif"); }
// --></script><a href="probability.htm" language="JavaScript" onmouseover="if(MSFPhover) document['MSFPnav10'].src=MSFPnav10h.src" onmouseout="if(MSFPhover) document['MSFPnav10'].src=MSFPnav10n.src"><img src="_derived/probability.htm_cmp_sumipntg010_hbtn.gif" width="140" height="40" border="0" alt="Odds &amp; Probability" align="middle" name="MSFPnav10"></a> <script language="JavaScript"><!--
if(MSFPhover) { MSFPnav11n=MSFPpreload("_derived/geometry.htm_cmp_sumipntg010_hbtn.gif"); MSFPnav11h=MSFPpreload("_derived/geometry.htm_cmp_sumipntg010_hbtn_a.gif"); }
// --></script><a href="geometry.htm" language="JavaScript" onmouseover="if(MSFPhover) document['MSFPnav11'].src=MSFPnav11h.src" onmouseout="if(MSFPhover) document['MSFPnav11'].src=MSFPnav11n.src"><img src="_derived/geometry.htm_cmp_sumipntg010_hbtn.gif" width="140" height="40" border="0" alt="Geometry" align="middle" name="MSFPnav11"></a> <script language="JavaScript"><!--
if(MSFPhover) { MSFPnav12n=MSFPpreload("_derived/algebra.htm_cmp_sumipntg010_hbtn.gif"); MSFPnav12h=MSFPpreload("_derived/algebra.htm_cmp_sumipntg010_hbtn_a.gif"); }
// --></script><a href="algebra.htm" language="JavaScript" onmouseover="if(MSFPhover) document['MSFPnav12'].src=MSFPnav12h.src" onmouseout="if(MSFPhover) document['MSFPnav12'].src=MSFPnav12n.src"><img src="_derived/algebra.htm_cmp_sumipntg010_hbtn.gif" width="140" height="40" border="0" alt="Advanced Algebra" align="middle" name="MSFPnav12"></a> <script language="JavaScript"><!--
if(MSFPhover) { MSFPnav13n=MSFPpreload("_derived/trig.htm_cmp_sumipntg010_hbtn.gif"); MSFPnav13h=MSFPpreload("_derived/trig.htm_cmp_sumipntg010_hbtn_a.gif"); }
// --></script><a href="trig.htm" language="JavaScript" onmouseover="if(MSFPhover) document['MSFPnav13'].src=MSFPnav13h.src" onmouseout="if(MSFPhover) document['MSFPnav13'].src=MSFPnav13n.src"><img src="_derived/trig.htm_cmp_sumipntg010_hbtn.gif" width="140" height="40" border="0" alt="Trigonometry" align="middle" name="MSFPnav13"></a> <script language="JavaScript"><!--
if(MSFPhover) { MSFPnav14n=MSFPpreload("_derived/calculus.htm_cmp_sumipntg010_hbtn.gif"); MSFPnav14h=MSFPpreload("_derived/calculus.htm_cmp_sumipntg010_hbtn_a.gif"); }
// --></script><a href="calculus.htm" language="JavaScript" onmouseover="if(MSFPhover) document['MSFPnav14'].src=MSFPnav14h.src" onmouseout="if(MSFPhover) document['MSFPnav14'].src=MSFPnav14n.src"><img src="_derived/calculus.htm_cmp_sumipntg010_hbtn.gif" width="140" height="40" border="0" alt="Calculus" align="middle" name="MSFPnav14"></a></p>
<p align="center">&nbsp;</p>
'''


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
  
#  categoryNameList = re.findall(r'href="(.+)" language', RAW_PAGE_SEGMENT)
#  for trickCategoryPageName in categoryNameList:
#    trickCategoryLink = makeHttpLink(trickCategoryPageName)
#    scrapTrickList(trickCategoryLink)    
#    print '#########################################################'

  scrapTrickList('http://math-magic.com/trig.htm')
  
#  scrapGuidePage(link)


def scrapTrickList(pageLink):
  content = request(pageLink)
  contentCopy = content #Note: apparently something happens after the first finditer( , content)
  
  # PDF versions of the trick guides (.pdf)
  patternForPdf = r'a href="(.*pdf)"'
  for m in re.finditer(patternForPdf, content):
    pdfLink = m.group(1)
    print pdfLink
    
    pdfLinkSplinters = os.path.split(pdfLink)
    folderName = pdfLinkSplinters[0]
    fileName = pdfLinkSplinters[1]
    
    try:
      os.makedirs(folderName)
    except:
      pass
    
    content = request(makeHttpLink(pdfLink))
    save(content, pdfLink)
  
  # HTML versions of the trick guides (.htm)
  patternForHtm = r'a href="(.*htm)">'
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
    patternForGuideBody = r'(.*)(<h4.*)(<a href="#top".*)'
    matchObject = re.match(patternForGuideBody, response, re.DOTALL)
    
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