import requests as req
from bs4 import BeautifulSoup as bs
from string import ascii_lowercase

"""
methods used for getting recipe information from food network website
SPECIFIC FOR FOOD NETWORK WEBSITE (https://www.foodnetwork.com/recipes/recipes-a-z/)
"""

def popUrls(base):
        """ 
        take a base url, add a letter for each webpage for recipes that start with that letter
        
        parameters:
                base (str): base url to find branch links for
        returns:
                listUrls (list): list of urls with same base link
        """
        listUrls = []
        # populate list of urls to search
        for let in ascii_lowercase:
                if let == 'x':
                        let = 'xyz'
                if let == 'y' or let == 'z':
                        break
                listUrls.append(base + let)
        return listUrls


def searchLet(url):    
        """
        take a url, search for all link sections
        
        parameters:
                url (str): url to search for links on
        returns:
                sections (list): list of tuples that contain url and title of recipe
        """    
        lim = 20
        # get request for url 
        page = req.get(url)
        # get the content, parse using bs
        pageCont = bs(page.content, "html.parser")
        # list of all sections that are recipes, limits to lim links found
        sections = pageCont.find_all("li", class_ = "m-PromoList__a-ListItem", limit = lim)
        
        # list of tuples containing the url and title
        urlTitleList = []
        for r in sections:
                # get the link and title section
                tempSect = str(r.find_all('a'))
                tempSect += ','
                # separate the link and title
                url = tempSect.split('\"')[1]
                title = tempSect.split(">")[1][:-3]
                # add a tuple containing link and title to list
                urlTitleList.append((url, title))
        return urlTitleList


def searchRecipe(url):
        """
        take a section, get the link and url, get list of ingredients
        
        parameters:
                url (str): url of recipe
        returns:
                ingrList (list): list of ingredients for recipe
        """
        # recipe page
        recPage = req.get('https:' + url)
        # content from recipe page
        rPcont = bs(recPage.content, "html.parser")
        # get all of the ingredients (in checkboxes [html section])
        temp = rPcont.find("div", class_ = "o-Ingredients__m-Body")
        if(temp is None):
                return
        recipeSearch = str(temp.find_all("span", class_="o-Ingredients__a-Ingredient--CheckboxLabel"))
        # filtering out html formatting, keep title
        splitRec = recipeSearch.split('<span class="o-Ingredients__a-Ingredient--CheckboxLabel">')
        splitRec[-1] += ","
        # list of ingredients
        ingrList = list(map(lambda e: 
                        e[:-9] if ("\xa0" not in e) else e[:-13]
                        , splitRec))[2:]
        return ingrList

def threadSearchLet(var, ret, i):
        """
        take a url, array, and index, uses the searchLet function to find all link sections and stores it in ret[i]
        parameters:
                var (str): url to search for links on
                ret (list/iterable): list to store the output
                i (num/str): index in ret to store the output
        returns:
                void
        """
        ret[i] = searchLet(var)
        return 


def threadSearchRecipe(var, ret, i):
        """
        take a section, array, and index, get the link and url, get list of ingredients
        parameters:
                var (str): url of recipe
                ret (list/iterable): list to store the output
                i (num/str): index in ret to store the output
        returns:
                void
        """
        temp = searchRecipe(var)
        if(temp is not None):
                ret[i] = temp
        return 