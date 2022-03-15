#Alex Teboul
#Due: 3/5/19 by 11:59pm
#Honor Statement: “I have not given or received any unauthorized assistance on this assignment.”
#Problem 2: Web Word Counts Attempt 2

import requests
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation


#Getting the counts for the first page using beautiful soup over lecture strategy:
webpage = "https://www.cdm.depaul.edu"

def wordcounter(webpage):
    ''' Gets the top 25 word counts for a single webpage'''
    r = requests.get(webpage)

    soup = BeautifulSoup(r.content, "lxml")
    #print(soup)
    text = (''.join(s.findAll(text=True)) for s in soup.findAll('p'))
    #print(text)
    mytext = soup.get_text()
        
    c = Counter((x.rstrip(punctuation).lower() for y in text for x in y.split()))
    print(c)
    
    return (c.most_common(25)) 

print(wordcounter(webpage))

#Page 1 Results
#[('and', 16), ('the', 15), ('of', 12), ('on', 7), ('to', 6),
#('a', 5), ('design', 5), ('community', 3), ('cybersecurity', 3),
#('is', 3), ('one', 3), ('for', 3), ('her', 3), ('by', 2), ('latest', 2),
#('technology', 2), ('nationally', 2), ('programs', 2), ('with', 2),
#('drawing', 2), ('research', 2), ('film', 2), ('students', 2), ('sharevski', 2), ('has', 2)]
print()

#to get for all pages, add to master dictionary, keep track of links visited,
#crawl through and on every link run wordcounter. Repeat until the num of links visited is 500.

#Best i could get it for P2. Hope we can see how it was
#done using the method we used in class, couldn't get that running like the prof did.
#Used beautiful soup instead to get the data in.
#-----------------------------------------------------------------------------
from urllib.parse import urljoin
from html.parser import HTMLParser
from urllib.request import urlopen


#Code from lecture
class Collector(HTMLParser):
    'collects hyperlink URLs into a list'

    def __init__(self, url):
        'initializes parser, the url, and a list'
        HTMLParser.__init__(self)
        self.url = url
        self.links = []

    def handle_starttag(self, tag, attrs):
        'collects hyperlink URLs in their absolute format'
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    # construct absolute URL
                    absolute = urljoin(self.url, attr[1])
                    if absolute[:4] == 'http': # collect HTTP URLs
                        self.links.append(absolute)
                        
    def getLinks(self):
        'returns hyperlinks URLs in their absolute format'
        return self.links
    
    def getData(self):
        'returns the data obtained by parsing'
        return self.data

def analyze(url):
    
    print('\n\nVisiting', url)           # for testing

    # obtain links in the web page
    content = urlopen(url).read().decode()
    collector = Collector(url)
    collector.feed(content)
    urls = collector.getLinks()          # get list of links

    # compute word frequencies
    content = collector.getData()
    freq = frequency(content)

    # print the frequency of every text data word in web page
    print('\n{:45} {:10} {:5}'.format('URL', 'word', 'count'))
    for word in freq:
        print('{:45} {:10} {:5}'.format(url, word, freq[word]))

    # print the http links found in web page
    print('\n{:45} {:10}'.format('URL', 'link'))
    for link in urls:
        print('{:45} {:10}'.format(url, link))

    return urls

def crawl2(url):
    '''a recursive web crawler that calls analyze()
       on every visited web page'''

    # add url to set of visited pages
    global visited     # warns the programmer 
    visited.add(url)

    # analyze() returns a list of hyperlink URLs in web page url 
    links = analyze(url)

    # recursively continue crawl from every link in links
    for link in links:
        # follow link only if not visited
        if link not in visited:
            try:
                crawl2(link)
            except:
                pass

#-----------------------------------------------------------------------------
#Can I get the counts for multiple pages

#Estimated total counts 500 pages as sums of pages:
#1 [('and', 16812),
#2 ('the', 13678),
#3 ('of', 9578),
#4 ('in', 8443),
#5 ('a', 6671),
#6 ('to', 6664),
#7 ('cdm', 6292),
#8 ('admission', 6009),
#9 ('graduate', 5278),
#10 ('course', 4205),
#11 ('students', 4126),
#12 ('for', 3996),
#13 ('depaul', 3850),
#14 ('resources', 3677),
#15 ('or', 3595),
#16 ('courses', 3428),
#17 ('programs', 3320),
#18 ('concentration', 3283),
#19 ('student', 3165),
#20 ('academic', 3121),
#21 ('program', 3004),
#22 ('is', 3002),
#23 ('computing', 2582),
#24 ('undergraduate',1807)
#25 ('csc', 1794)]

    
