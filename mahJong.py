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
					#val = (randint(1,33))
					val = (randint(0,135))
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
	player["HasDice"] = "False"
	player["PrevWin"] = "False"


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

	player1["PrevDice"] = "False"
	player2["PrevDice"] = "False"
	player3["PrevDice"] = "False"
	player4["PrevDice"] = "False"

	player1["Starter"] = "True"
	player2["Starter"] = "False"
	player3["Starter"] = "False"
	player4["Starter"] = "False"

def changePosition(player,symTable):
	listFong = ["dong","nam","xi","bei"]
	listWithDiceFong = ["dong","bei","xi","nam"]
	currPosition = ""
	s = " "

	# is starter  then go in diff list
	if(player["Starter"] == "True" ):
		if(player["Win"] == "False"):
			a = listWithDiceFong.index(player["Position"])
			player["Position"] = s.join(listWithDiceFong[a+1:a+2])
	else:
	# if they didnt start
	# if they won then dont change
	# if they didnn't win ,
		if(player["HasDice"]):
			player["Position"] = "dong"
		else:
			a = listFong.index(player["Position"])
			player["Position"] = s.join(listFong[a+1:a+2])
		
def addCard(deck,symTable):
	#print(deck)
	val = randint(0,135)
	
	if (symTable.get(val) is None):
		while (symTable.get(val) is None):
			val = randint(0,135)
	deck.append(symTable[val])
	return deck

def removeCard(deck,symTable):
	print(deck)
	a = input()
	deck.remove(a)
	print(deck)
	
	#print(symTable)
def genWin(deck):
	listS = list()
	listT = list()
	listW = list()
	listE = list()
	pong = 0;
	for a in (deck):
		if(a[1] == 's'):
			listS.append(a)
		elif(a[1] == 't'):
			listT.append(a)
		elif(a[1] == 'w'):
			listW.append(a)
		else:
			listE.append(a)
	# check all pairs
	listPong = list()

	dic = {}
	dicT = {}
	dicW = {}
	dicE = {}
	counter = 1
	eyes = 0
	#print(SO_ZI)
	for so_Zi in listS:
		if( not (so_Zi in dic)): # add to dic
			dic[so_Zi] = 1
		else:
			dic[so_Zi] = dic[so_Zi]+1
	for key,val in dic.items():
		if (val ==3): # if it occurs 3 times
			pong = pong+1
			print(key)
			print(dic)
		if (val ==2):
			eyes = eyes+1
	#print(TONG_ZI)
	for tong_Zi in listT:
		if(not (tong_Zi in dicT)):
			dicT[tong_Zi] = 1
		else:
			dicT[tong_Zi] = dicT[tong_Zi]+1
	for key2,val2 in dicT.items():
		if(val2 ==3):
			print(key2)
			print(dicT)
			pong = pong+1
		if (val2 ==2):
			eyes = eyes+1
	#print(WAN_ZI)
	for wan_Zi in listW:
		if(not (wan_Zi in dicW)):
			dicW[wan_Zi] = 1
		else:
			dicW[wan_Zi] = dicW[wan_Zi]+1
	for key3,val3 in dicW.items():
		if(val3 ==3):
			print(key3)
			print(dicW)
			pong = pong+1
		if (val3 ==2):
			eyes = eyes+1
	#print(else)
	for others in listE:
		if(not (others in dicE)):
			dicE[others] = 1
		else:
			dicE[others] = dicE[others]+1
	for key4,val4 in dicE.items():
		if(val4 ==3):
			print(key4)
			print(dicE)
			pong = pong+1
		if (val4 ==2):
			eyes = eyes+1

	
	if(pong == 4 and eyes ==2): 
		return True

	return False



def checkConsecutive(deck):
	listS = list()
	listT = list()
	listW = list()
	listE = list()
	pong = 0;
	for a in (deck):
		if(a[1] == 's'):
			listS.append(a)
		elif(a[1] == 't'):
			listT.append(a)
		elif(a[1] == 'w'):
			listW.append(a)
		else:
			listE.append(a)

	listS.sort()
	b = 0
	dicA = list()
	alreadyAdded = list()
	while b < len(listS):
		if (listS[b] in dicA):
			alreadyAdded.append(listS[b])
		else:
			dicA.append(listS[b])

		b = b + 1
	print(listS)
	print(alreadyAdded)
	print(dicA)

	check = 0
	listOfThree = list()
	print(listOfThree)
	while check < len(dicA):
		if(check == len(dicA)-1):
			print("last")
			return
		if(check == len(dicA)-2):
			print("2ndToLast")
			return
		pieceA = (dicA[check])
		checkA = int(pieceA[0])
		pieceB = (dicA[check+1])
		checkB = int(pieceB[0])
		pieceC = dicA[check+2]
		checkC = int(pieceC[0])
		if(((checkA + 1) == checkB) and ((checkA+2) ==checkC)):
			listOfThree.append(pieceA)
			listOfThree.append(pieceB)
			listOfThree.append(pieceC)
		print(listOfThree, "i")
		check+=1

	"""
	dicA = {}
	dicA = listS
	valHolder = 0
	a_pointer = 0
	b_pointer = 0
	valHolder2 = 0
	print(listS)
	"""
	"""

	if(len(listS) > 2):
		while(not( b_pointer == len(listS)-3) ):

			# first case
			# given 5 check if it has 6 7
			use = listS[b_pointer]
			valHolder = int(use[0])

			use2 = listS[b_pointer+1]
			valHolder2 = int(use2[0])

			use3 = listS[b_pointer+2]
			valHolder3 = int(use3[0])
			print(valHolder,valHolder2,valHolder3)
			b_pointer+=1
			if((valHolder + 1 ) == (valHolder2) and ((valHolder + 2) == valHolder3 ) ):
				print("in here")
				print(valHolder,valHolder2,valHolder3)
	"""	
	#print(listS)




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
    makePlayer(player1) # dong dong
    makePlayer(player2) # dong nam
    makePlayer(player3)
    makePlayer(player4)
    fong = ""

    dice = diceRoll()

    # change counter later
    currFong = 1
 
    #startGame(player1,player2,player3,player4)
    #changePosition(player2,symTable)
    #print(sortedDeck1)
    #addCard(sortedDeck1,symTable)
    #print(sortedDeck1)
    #removeCard(sortedDeck1,symTable)
    checkConsecutive(sortedDeck1)

    
   # print(addedCardToDeck1)

if __name__ == "__main__":
    main()        