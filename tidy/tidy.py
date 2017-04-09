import sys

def main(argv):
    #t = int(input())

    inputList = []
    outPutFile = open(argv[2],'w')

    with open(argv[1], 'r') as my_file:
        t = int(my_file.readline())
        for i in range(1, t + 1):
            #n, m = [int(s) for s in input().split(" ")]
            inputNum = int(my_file.readline())
            #print("Case #{}: {} {}".format(i, n + m, n * m))
        
            #inputList.append(int(line))
            digitList = []
            for c in str(inputNum):
                digitList.append(int(c))
     
            for digitIndex in range(len(digitList)):
                if(digitIndex != (len(digitList)-1)):
                    if(digitList[digitIndex] > digitList[digitIndex+1]):
                       break;
                    
            first = digitList[:digitIndex+1]
            second = digitList[digitIndex+1:]
            if (not second):
                result = (toInt(first))
            else:
                result = tidyTest(first,second)
            outPutFile.write("Case #{}: {}".format(i, result))
            #print("Case #{}: {}".format(i, result))
            outPutFile.write("\n")
            #print("Case #{}: {}".format(i, result))
        outPutFile.close()


def tidyTest(first,second):
    index = len(first) - 1
    counter = 0
    if(len(first) > 1):
        while(first[index] == first[index-1]):
            index = index - 1
            counter = counter + 1
            if (index == 0):
                break;

    #print(first)
    zeros = [0] * (len(second) + counter)
    mulList = [1] + zeros
    multiplier = toInt(mulList)

    firstInt = toInt(first[:(len(first)-counter)])
    if(multiplier != 1):
        return ((firstInt*multiplier)-1)
    else:
        return ((firstInt*multiplier))
    

def toInt(numList):
    s = ''.join(map(str, numList))
    return int(s)


if __name__ == "__main__":
    main(sys.argv)
