myList = range(2, 120)
myFinalList = [2]


def deleteEvery():

    n = myFinalList.index(len(myFinalList))
    del myList[::n]
    myFinalList.insert(len(myFinalList), myList.pop(0))


def main():
    x = 7
    x >>= 2
    print x

if __name__ == "__main__":
    main()
