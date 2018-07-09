# This program will determine the price of the product stated on amazon. Just copy the url of the product on clipboard and run the script. 

import bs4,requests,pyperclip

def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()
    
    try:
        soup  = bs4.BeautifulSoup(res.text, 'html.parser')
        elems = soup.select('#priceblock_ourprice')
        if elems:
            return elems[0].text.strip()
        elems = soup.select('#priceblock_dealprice')
        if elems:
            return elems[0].text.strip()
    except:
        return 'The requested price was not found'
       

productLink = pyperclip.paste()
price       = getAmazonPrice(productLink)
print('The price is:' + price)
