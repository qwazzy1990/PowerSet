





def generatePowerSet(n, powerSet):
    
    if n == 1:
        powerSet.append([])
        powerSet.append([1])
        return
   
    generatePowerSet(n-1, powerSet)
    length = len(powerSet)
    for i in range(1, length):
        temp = []
        for j in range(0, len(powerSet[i])):
            temp.append(powerSet[i][j])
        temp.append(n)
        powerSet.append(temp)

    powerSet.append([n])


if __name__ == "__main__":
    pSet = []
    print('We generate the power set for a collection of size \'n\'')
    m = input("Enter the \'n\' value for the size of the collection\n")
    n = int(m)
    generatePowerSet(n, pSet)
    for i in range(0, len(pSet)):
        print(pSet[i])

