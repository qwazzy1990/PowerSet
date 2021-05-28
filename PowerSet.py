





def generatePowerSet(n, powerSet):
    
    ##if generating the power set of a collection of size 1
    ##then the only two subset are the empty set and [1]
    if n == 1:
        powerSet.append([])
        powerSet.append([1])
        return
   
    ##else do a recursive call
    generatePowerSet(n-1, powerSet)

    ##get the length of the power set of a collection of size n-1
    length = len(powerSet)

    ##for each subset in the current power set
    for i in range(1, length):
        ##copy the current subset
        temp = powerSet[i][:]
        ##append the 'n' value to the current subset
        temp.append(n)
        ##append the new subset to the power set
        powerSet.append(temp)

    ##append to set containing 'n' by itself
    powerSet.append([n])


if __name__ == "__main__":
    #power set
    pSet = []
    #get user input
    print('We generate the power set for a collection of size \'n\'')
    m = input("Enter the \'n\' value for the size of the collection\n")
    n = int(m)

    #generate the power set of a collection of size 'n' from {1,2,...,n-1,n}
    generatePowerSet(n, pSet)
    #print the power set
    for i in range(0, len(pSet)):
        print(pSet[i])

