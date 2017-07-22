import math

def quickSort(list):
    if len(list) >= 1:
        listLeft = []
        listRight = []
        chosenValue = list.pop(0)
        for item in list:
            if item >= chosenValue:
                listRight.append(item)
            else:
                listLeft.append(item)

        return quickSort(listLeft) + [chosenValue] + quickSort(listRight)
    return []


def mergeSort(list):
    leftList = []
    if len(list) > 1:
        for n in range(0, int(math.floor(len(list)/2))):
            leftList.append(list.pop())
        leftList = mergeSort(leftList)
        list = mergeSort(list)
    for item in leftList:
        added = False
        for i in range(0, len(list)):
            if item < list[i]:
                list.insert(i, item)
                added = True
                break
        if not added:
            list.append(item)
    return list


def bubbleSort(list):
    if len(list) <= 1:
        return list
    sorted = False
    countEnd = 1
    while not sorted:
        sorted = True
        for i in range(0, len(list)-countEnd):
            if list[i] > list[i+1]:
                sorted = False
                holder = list[i]
                list[i] = list[i+1]
                list[i+1] = holder
        countEnd += 1
        if sorted:
            return list
    return list


def mostFrequent(list):
    mostFrequentNumber = [-1, 0]
    if len(list) > 0:
        mostFrequentNumber = [list[0], 0]
    count = 1
    for i in range(0,  len(list)):
        if list[i] == mostFrequentNumber[0]:
            mostFrequentNumber[1] += 1
        else:
            if list[i-1] == list[i]:
                count += 1
            else:
                if count > mostFrequentNumber[1]:
                    mostFrequentNumber = [list[i-1], count]
                    count = 1
    return mostFrequentNumber[0]


def mostFrequentUnsorted(list):
    assert len(list) >= 1
    prevItems = []
    prevItems.insert(0, list[0])
    list.remove(list[0])
    while len(list) > 1:
        for item in list:
            if item in prevItems:
                continue
            else:
                list.remove(item)
                prevItems.insert(0, item)
        prevItems = []
    return list[0]


def main():
    myList = [12, 2, 1, 4, 5, 6, 4, 44, 3, 33, 3, 3, 7, 8, 9]
    print quickSort(myList)
    myList = [12, 2, 1, 4, 5, 6, 4, 44, 3, 33, 3, 3, 7, 8, 9]
    print bubbleSort(myList)
    myList = [12, 2, 1, 4, 5, 6, 4, 44, 3, 33, 3, 3, 7, 8, 9]
    print mergeSort(myList)
    myList = [12, 2, 1, 4, 5, 6, 4, 44, 3, 33, 3, 3, 7, 8, 9]
    print mostFrequent(quickSort(myList))
    myList = [12, 2, 1, 4, 5, 6, 4, 44, 3, 33, 3, 3, 7, 8, 9]
    print mostFrequentUnsorted(myList)

if __name__ == "__main__":
    main()
