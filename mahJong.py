import fileinput
import sys
from random import seed
from random import randint

def assignCards(wholeList,makeDeckFor1):
		useKey = ""
		keyHolder = ""
		counter = 0
	
		for i in range(13):
			val = randint(0,135)
			use = wholeList.get(val)
			if( use is None):
				while(use is None):
					val = (randint(1,33))
					use = wholeList.get(val)
		
			makeDeckFor1[counter] = wholeList[val]
			wholeList.pop(val)
			counter = counter + 1

def sortCards(deck,sortedDeck):
	for i in range(13):
		print(deck.get(i))

def main():

    inputFile = open(sys.argv[1])
    lineList = list()
    copyList = list()
    lineCounter = 0
    counter = 0
    emptyDeck = {}
    deck1 = {}
    deck2 = {}
    deck3 = {}
    deck4 = {}
    symTable = {}
    sortedDeck1 = {}



    for line in inputFile: # adding to a list
    	#lineList.append(line.strip())
    	symTable[counter] = line.strip()
        counter = counter+1
    # lets make a copy of it first
  

    #print(symTable)	


    assignCards(symTable,deck1)
    assignCards(symTable,deck2)
    assignCards(symTable,deck3)
    assignCards(symTable,deck4)
   # print(deck1)
    sortCards(deck1,sortedDeck1)
    
    
    
    
if __name__ == "__main__":
    main()        