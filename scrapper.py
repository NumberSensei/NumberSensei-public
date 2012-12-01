### This is a random file to tweak the scrapping, DO NOT COMMIT

import re, os
import scrap_links
from scrap_links import makeHttpLink, scrapGuidePage, scrapTrickList

fullLink = 'http://math-magic.com/fractions_decimals.htm'
#scrapGuidePage(fullLink)

scrapTrickList(fullLink)