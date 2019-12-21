import fileinput
import sys
from random import seed
from random import randint

def assignCards(wholeList,makeDeckFor1):
	# assign 13 cards randomly from deck
	# removes from deck after adding
	# if its remvoed and gets called, a new one gets assigned
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

	numList = list()
	alphaList = list()
	soZiList = list()
	tongZiList = list()
	manZiList = list()
	restList = list()
	
	
	# adds and sorts depending on what type
	# puts back into one single list
	for i in range(13):
		card = str(deck.get(i))
		if(card[0].isalpha()):
			#print(card,"isalpha")
			restList.append(card)
		else:
			if(card[1]=='s'):
				soZiList.append(card)
			
			elif(card[1]=='t'):
				tongZiList.append(card)
			
			else:
				manZiList.append(card)
			
	tongZiList.sort(reverse = False)
	manZiList.sort(reverse = False)
	soZiList.sort(reverse = False)
	restList.sort(reverse = False)
	
	sortedDeck = tongZiList+soZiList+manZiList+restList
	return sortedDeck
	
def diceRoll():	
	return randint(1,6)+randint(1,6)

def makePlayer(player):
	# did they win
	# at index 0
	
	player["Win"] = "False"
	player["Fong"] = ""
	#player["Position"] = ""


def changeFong(counter):
	if counter == 1:
		return "dong"
	elif counter == 2:
		return "nam"
	elif counter == 3:
		return "xi"
	else:
		return "bei"

		# assume there is something for them to know who is starting


def startGame(player1,player2,player3,player4):
	player1["Fong"] = "dong"
	player2["Fong"] = "dong"
	player3["Fong"] = "dong"
	player4["Fong"] = "dong"

	player1["Position"] = "dong"
	player2["Position"] = "nam"
	player3["Position"] = "xi"
	player4["Position"] = "bei"

def changePosition(player,symTable):
	listFong = ["dong","nam","xi","bei"]
	currPosition = ""

	#print(currFong,"currFon")
	if (player["Position"] == "bei"):
		player["Position"] = listFong[0:1]
		currFong = symTable["currFong"]+1
		
		symTable["currFong"] = currFong
		return currFong
	elif (player["Position"] in listFong):
		
		currPosition = listFong.index((player["Position"]))
		player["Position"] = listFong[currPosition+1:currPosition+2]

def main():

    inputFile = open(sys.argv[1])
    lineList = list()
    copyList = list()
    lineCounter = 0
    counter = 0
    emptyDeck = {}
    deck1 = deck2 = deck3 = deck4 = {}
    diceNumber = 1 
    symTable = {}
    symTable["currFong"] = 1
    sortedDeck1 = list()
    sortedDeck2 = list()
    sortedDeck3 = list()
    sortedDeck4 = list()
    player1 = {}
    player2 = {}
    player3 = {}
    player4 = {}
    
    playerList = list()
    playerList.append(player1)
    playerList.append(player2)
    playerList.append(player3)
    playerList.append(player4)
    
	
    for line in inputFile: # adding to a list
   
    	symTable[counter] = line.strip()
        counter = counter+1
    
    assignCards(symTable,deck1)
    assignCards(symTable,deck2)
    assignCards(symTable,deck3)
    assignCards(symTable,deck4)

    # having sorted decks by tong,so,wan,rest
    sortedDeck1 = sortCards(deck1,sortedDeck1)
    sortedDeck2 = sortCards(deck2,sortedDeck2)
    sortedDeck3 = sortCards(deck3,sortedDeck3)
    sortedDeck4 = sortCards(deck4,sortedDeck4)
    makePlayer(player1)
    makePlayer(player2)
    makePlayer(player3)
    makePlayer(player4)
    fong = ""

    dice = diceRoll()

    # change counter later
    currFong = 1
  

    startGame(player1,player2,player3,player4)
    
    # something to be called later o 
    changePosition(player1,symTable)
    changePosition(player2,symTable)
    changePosition(player3,symTable)
    changePosition(player4,symTable)
    
    
    print(symTable["currFong"])

if __name__ == "__main__":
    main()        