import requests as req
from bs4 import BeautifulSoup as bs
from string import ascii_lowercase

# original recipe page url
baseUrl = 'https://www.foodnetwork.com/recipes/recipes-a-z/'
# strings of links to search
letUrls = []            

print(req.get(baseUrl+'a'))
"""
# populate array of urls to search
for let in ascii_lowercase:
        if let == 'x':
                let = 'xyz'
        if let == 'y' or let == 'z':
                break
        letUrls.append(baseUrl + let)
"""

"""
for url in letUrls:
        page = req.get(url)
        

        # beautifulsoup object, parses html content from page
        soup = bs(page.content, "html.parser")

        # finds all links 
        results = soup.find("a", {"class" : "m-PromoList__a-ListItem"})


"""