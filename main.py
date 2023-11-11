import requests as req
from bs4 import BeautifulSoup as bs
from string import ascii_lowercase

# original recipe page url
baseUrl = 'https://www.foodnetwork.com/recipes/recipes-a-z/'
# strings of links to search
letUrls = []            

page = req.get(baseUrl + 'a')
# print(page.content)
soup = bs(page.content, "html.parser")
results = soup.find_all("li", class_ = "m-PromoList__a-ListItem")

# loop through each link on the letter's page
for r in results:
        # get the link and title section
        str1 = str(r.find_all('a'))
        str1 += ','
        # separate the link and title
        url = str1.split('\"')[1]
        title = str1.split(">")[1][:-3]

        # recipe page
        recPage = req.get('https:' + url)
        # content from recipe page
        rPcont = bs(recPage.content, "html.parser")
        # get all of the ingredients (in checkboxes [html section])
        temp = rPcont.find("div", class_ = "o-Ingredients__m-Body")
        if(temp is None):
                continue
        recipeSearch = str(temp.find_all("span", class_="o-Ingredients__a-Ingredient--CheckboxLabel"))
        # filtering out html formatting, keep title
        splitRec = recipeSearch.split('<span class="o-Ingredients__a-Ingredient--CheckboxLabel">')
        splitRec[-1] += ","
        temp2 = list(map(lambda e: 
                         e[:-9] if ("\xa0" not in e) else e[:-13]
                         , splitRec))[2:]
        print(temp2)



        



# use this for final version
# results = soup.find_all("li", class_ = "m-PromoList__a-ListItem")
"""
string1 = str(results.find("a"))

url = string1.split('\"')[1]
title = string1.split(">")[1][:-4]


page2 = req.get('https:' + url)

soup2 = bs(page2.content, "html.parser")
res2 = str(soup2.find("div", class_ = "o-Ingredients__m-Body").find_all("span", class_="o-Ingredients__a-Ingredient--CheckboxLabel"))
split2 = res2.split('<span class="o-Ingredients__a-Ingredient--CheckboxLabel">')
split2[-1] += ","
temp2 = list(map(lambda e: e[:-9], split2))[2:]
"""

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
letUrls += page
c1 = 0
for url in letUrls:
        # page of all links to recipe starting with letter
        letPage = req.get(url)
        
        # beautifulsoup object, parses html content from page
        lpCont = bs(letPage.content, "html.parser")

        # finds all recipe headers, a list
        results = lpCont.find_all("li", {"class" : "m-PromoList__a-ListItem"})
        # get the a section in header
        aStr = str(results.find("a"))

        # separate the url and title from section
        url = aStr.split('\"')[1]
        title = aStr.split(">")[1][:-4]
        # access the individual recipe 
        page2 = req.get('https:' + url)
        soup2 = bs(page2.content, "html.parser")

        res2 = str(soup2.find("div", class_ = "o-Ingredients__m-Body").find_all("span", class_="o-Ingredients__a-Ingredient--CheckboxLabel"))
        split2 = res2.split('<span class="o-Ingredients__a-Ingredient--CheckboxLabel">')
        split2[-1] += ","
        temp2 = list(map(lambda e: e[:-9], split2))[2:]
        print(temp2)
        """