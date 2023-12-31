from scrape import *
import threading
import time

def main():
        st = time.time()
        # original recipe page url
        baseUrl = 'https://www.foodnetwork.com/recipes/recipes-a-z/'

        # strings of links to search with threads
        letUrls = popUrls(baseUrl)      
        
        # search all letter urls
        tarr = []
        recList = [None] * len(letUrls) #2d array
        tcount = 0
        for url in letUrls:
                # tuple containing url and title
                tarr.append(threading.Thread(target=threadSearchLet, args=(url,recList, tcount)))
                tarr[tcount].start()
                tcount += 1
        for t in tarr: #Reaping threads
                t.join()
        #array of threads for individual recipes
        tarr2 = [] 
        tcount2 = 0
        ingrMap = {}
        for subr in recList: #recList is 2d array
                for recUrl, recTitle in subr:
                    x = threading.Thread(target=threadSearchRecipe, args=(recUrl, ingrMap, recTitle))
                    tarr2.append(x)
                    tarr2[tcount2].start()
                    tcount2 += 1
        for t in tarr2: #Reaping threads
                t.join()
        for r in ingrMap:
                print(r)
        end = time.time()
        print(end-st)


if __name__ == "__main__":
        main()