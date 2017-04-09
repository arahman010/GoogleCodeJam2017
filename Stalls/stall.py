import sys

def main(argv):
    outPutFile = open(argv[2],'w')

    with open(argv[1], 'r') as my_file:
        t = int(my_file.readline())
        for i in range(1, t + 1):
            N, K = [int(s) for s in (my_file.readline()).split(" ")]
            path = getPath(K)
            result = Stalling(N,path)
            if ( result == 1 or result == 0):
                maxRslt = 0
                minRslt = 0
            elif (result % 2 == 1):    #odd
                maxRslt = (result-1)/2
                minRslt = (result-1)/2
            else:
                maxRslt = (result)/2
                minRslt = (result/2) - 1
                
            
            outPutFile.write("Case #{}: {} {}".format(i, maxRslt, minRslt))
            outPutFile.write("\n")
            #print("Case #{}: {} {}".format(i, maxRslt, minRslt))
        outPutFile.close()

def getPath(i):
    if ( i < 4):
        if ( i != 1):
            pathList = [i,1]
        else:
            pathList = [1]
    else:
        pathList = [i]
        while(i != 1):
            if(i % 2 == 1):     #Odd
                pathList.append((i-1)/2)
                i = (i-1)/2
            else:       #even
                pathList.append(i/2)
                i = i/2
    return list(reversed(pathList))
    


def Stalling(N,path):
    k = 1
    for i in path:
        if (i != 1):
            if(2*k+1 == i):
                N = StallingLeftRight(N,"right")
                k = 2*k + 1
            elif(2*k == i):
                N = StallingLeftRight(N,"left")
                k = 2*k
    return N

def StallingLeftRight(N,direction):
    if(direction == "left"):
        if(N % 2 == 1):
            return (N-1)/2
        else:
            return (N/2)

    elif(direction == "right"):
        if(N % 2 == 1):
            return (N-1)/2
        else:
            return (N/2) - 1
    
            
            

if __name__ == "__main__":
    main(sys.argv)
