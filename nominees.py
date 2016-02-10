from html.parser import HTMLParser  
from urllib.request import urlopen  
from urllib import parse

########################################
#Define before running:
base_sites = ['http://www.slashfilm.com/', 'http://www.collider.com/', 'http://www.joblo.com/', 'http://www.geektyrant.com/', 'http://www.screencrush.com/', 'http://www.ign.com/movies', 'http://www.cinemablend.com/', 'http://www.denofgeek.us/#switched', 'http://www.guardian.co.uk/film', 'http://movies.yahoo.com/', 'http://www.screenjunkies.com/', 'http://www.filmschoolrejects.com/', 'http://www.screenrant.com/', 'http://www.darkhorizons.com/']
########################################

class LinkParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (key, value) in attrs:
                if key == 'href':
                    newUrl = parse.urljoin(self.baseUrl, value)
                    self.links = self.links + [newUrl]

    def getLinks(self, url):
        self.links = []
        self.baseUrl = url
        response = urlopen(url)
        if response.getheader('Content-Type')=='text/html':
            htmlBytes = response.read()
            htmlString = htmlBytes.decode("utf-8")
            self.feed(htmlString)
            return htmlString, self.links
        else:
            return "",[]

def spiderword(url, word):  
    pagesToVisit = [url]
    try:
        parser = LinkParser()
        data, links = parser.getLinks(url)
        if data.find(word)>-1:
            return True
    except:
        return False

def spider(url, words, maxPages):
    count = 0
    pagesToVisit = [url]
    numberVisited = 0
    foundWords = False
    while numberVisited < maxPages and pagesToVisit != []:
        numberVisited = numberVisited +1
        url = pagesToVisit[0]
        pagesToVisit = pagesToVisit[1:]
        try:
        	foundWord = True
		for word in words:
			if not spiderword(url, word):
				foundWord = False
                if foundWord:	
			pagesToVisit = pagesToVisit + links
                	count ++
    return count 

BEST_PICTURE = ['The Big Short', 'Bridge of Spies', 'Brooklyn', 'Mad Max Fury Road', 'The Martian', 'The Revenant', 'Room', 'Spotlight']
results = [None] * len(BEST_PICTURE)
for site in base_sites:	
	for i, c in enumerate(BEST_PICTURE):
		results[i] = spider(site, c.split(), 20)
print BEST_PICTURE
print results
