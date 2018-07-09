#This script is aimed at opening several Google search results all at once. 
#The method to run this script is simple. 
    # Download the script
    # Open terminal and run python feelinglucky.py 'search term' (excluding the quotes)

import webbrowser,sys,requests,bs4

print('Googling....')
search = requests.get('https://www.google.co.in/search?q=' + ' '.join(sys.argv[1:]))
search.raise_for_status()

SoupElem = bs4.BeautifulSoup(search.text)
linkElems = SoupElem.select('.r a')
NumLinks = min(5,len(linkElems))

for i in range(NumLinks):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))

