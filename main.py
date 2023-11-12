from scrape import *

def main():
        # original recipe page url
        baseUrl = 'https://www.foodnetwork.com/recipes/recipes-a-z/'

        # strings of links to search
        letUrls = popUrls(baseUrl)      
        
        # search all letter urls
        for url in letUrls:
                # tuple containing url and title
                recTups = searchLet(url)
                for r in recTups:
                        print(searchRecipe(r[0]))


if __name__ == "__main__":
        main()