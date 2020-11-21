class linkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        newNode = Node(data)
        previousNode = None
        if self.head == None:
            self.head = newNode
        else:
            currentNode = self.head
            while currentNode.nextNode != None:
                previousNode = currentNode
                currentNode = currentNode.nextNode
            if(previousNode == None):
                previousNode = currentNode
            currentNode.nextNode = newNode
            newNode.prevNode = previousNode


llist = linkedList()


class Car:
    def __init__(self, identification, name, brand, price, active):
        self.identification = int(identification)
        self.name = str(name)
        self.brand = str(brand)
        self.price = int(price)
        self.active = bool(active)


class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None
        self.prevNode = None


def sortCars(allCars):
    internalList = allCars
    fixedLen = len(internalList)
    sortedList = []
    while len(sortedList) < fixedLen:
        minPrice = None
        for i in range(0, len(internalList)):
            if(minPrice == None):
                minPrice = internalList[i].price
                currentIndex = i
            elif(internalList[i].price < minPrice):
                minPrice = internalList[i].price
                currentIndex = i
        sortedList.append(internalList[currentIndex])
        internalList.pop(currentIndex)
    return sortedList


def init(cars):
    sortedList = sortCars(cars)
    for car in sortedList:
        llist.push(car)


def getDatabase():
    #printval = llist.head
    # if(printval == None):
    #    return
    # while printval is not None:
    #    print(printval.data.name)
    #    printval = printval.nextNode
    return llist


def getDatabaseHead():
    # print("The head Node is:", llist.head.data.name)¨
    return llist.head


def clean():
    llist.head.nextNode = None
    llist.head = None


def add(car):
    newNode = Node(car)
    placeFounded = False
    currentNode = llist.head
    previousNode = None
    if(currentNode == None):
        llist.head = newNode
        placeFounded = True
    while not placeFounded:
        if(currentNode == llist.head):
            if(currentNode.data.price > newNode.data.price):
                llist.head = newNode
                previousNode = currentNode.prevNode
                if(previousNode is not None):
                    previousNode.nextNode = newNode
                currentNode.prevNode = newNode
                newNode.prevNode = previousNode
                newNode.nextNode = currentNode
                placeFounded = True
            else:
                previousNode = currentNode
                if(currentNode.nextNode == None):
                    previousNode.nextNode = newNode
                    newNode.prevNode = previousNode
                    placeFounded = True
                currentNode = currentNode.nextNode
        else:
            if(currentNode.data.price > newNode.data.price):
                previousNode = currentNode.prevNode
                if(previousNode is not None):
                    previousNode.nextNode = newNode
                currentNode.prevNode = newNode
                newNode.prevNode = previousNode
                newNode.nextNode = currentNode
                placeFounded = True
            else:
                previousNode = currentNode
                if(currentNode.nextNode == None):
                    previousNode.nextNode = newNode
                    newNode.prevNode = previousNode
                    placeFounded = True
                currentNode = currentNode.nextNode


def updateName(identification, name):
    searchedNode = int(identification)
    currentNode = llist.head
    if(currentNode == None):
        return None
    foundedNode = False
    while not foundedNode:
        if(currentNode.data.identification == searchedNode):
            currentNode.data.name = str(name)
            foundedNode = True
        else:
            if(currentNode.nextNode == None):
                foundedNode = True
                return None
            currentNode = currentNode.nextNode


def updateBrand(identification, brand):
    searchedNode = int(identification)
    currentNode = llist.head
    if(currentNode == None):
        return None
    foundedNode = False
    while not foundedNode:
        if(currentNode.data.identification == searchedNode):
            currentNode.data.brand = str(brand)
            foundedNode = True
        else:
            if(currentNode.nextNode == None):
                foundedNode = True
                return None
            currentNode = currentNode.nextNode


def activateCar(identification):
    searchedNode = identification
    currentNode = llist.head
    if(currentNode == None):
        return None
    foundedNode = False
    while not foundedNode:
        if(currentNode.data.identification == searchedNode):
            currentNode.data.active = True
            foundedNode = True
        else:
            if(currentNode.nextNode == None):
                foundedNode = True
                return None
            currentNode = currentNode.nextNode


def deactivateCar(identification):
    searchedNode = identification
    currentNode = llist.head
    if(currentNode == None):
        return None
    foundedNode = False
    while not foundedNode:
        if(currentNode.data.identification == searchedNode):
            currentNode.data.active = False
            foundedNode = True
        else:
            if(currentNode.nextNode == None):
                foundedNode = True
                return None
            currentNode = currentNode.nextNode


def calculateCarPrice():
    totalPrice = 0
    currentNode = llist.head
    while currentNode is not None:
        if(currentNode.data.active == True):
            totalPrice += currentNode.data.price
        currentNode = currentNode.nextNode
    return totalPrice
