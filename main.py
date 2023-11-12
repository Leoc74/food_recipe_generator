from scrape import *
import threading

def main():
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
        ingrList = [None] * len(recList)*len(recList[0])
        for subr in recList: #recList is 2d array
                for recUrl, recTitle in subr:
                    x = threading.Thread(target=threadSearchRecipe, args=(recUrl, ingrList, tcount2))
                    tarr2.append(x)
                    tarr2[tcount2].start()
                    tcount2 += 1
        for t in tarr2: #Reaping threads
                t.join()
        for r in ingrList:
                print(r)


if __name__ == "__main__":
        main()