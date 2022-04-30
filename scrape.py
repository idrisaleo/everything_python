import requests
from bs4 import BeautifulSoup ## allows us to grab and use diff html data
import pprint


url = requests.get('https://news.ycombinator.com/') 
url_soup = BeautifulSoup(url.text, 'html.parser') ## converting site from string to an html file
links = url_soup.select('.titlelink') # select class titlelink
subtext = url_soup.select('.subtext') #
url2 = requests.get('https://news.ycombinator.com/news?p=2')
url_soup2 = BeautifulSoup(url2.text, 'html.parser') ## converting site from string to an html file
links2 = url_soup2.select('.titlelink')
subtext2=url_soup2.select('.subtext')





def merge_custom(links2, subtext2):
	    return custom_link(links+links2, subtext+subtext2)


def rank(hnrank):
	return sorted(hnrank, key = lambda k:k['points'], reverse = True)


def custom_link(links, subtext):
	hn = []
	for idx, item in enumerate(links):
		title = links[idx].getText()
		href = links[idx].get('href', None) ## get the link, and none in place of a blank href
		vote = subtext[idx].select('.score') ## to prevent imbalance between links and points, could have copied class score 4rm d start
		print(vote)
		if len(vote):
			points = int(vote[0].getText().replace(' points', '')) ##since it is an array, its got to be indexed. trying to get only values
			if points > 99:
				hn.append({'title': title, 'link': href, 'points': points})
	return rank(hn)			

pprint.pprint(merge_custom(links2, subtext2))







#<span class="score" id="score_31205072">40 points</span>




