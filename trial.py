def Domino_Solitaire(domino):
    if len(domino)==1:
        print (abs(domino[0][0]-domino[0][1]))
        return (abs(domino[0][0]-domino[0][1]))

    elif len(domino) > 1:
        if (abs(domino[0][0] - domino[0][1])) + Domino_Solitaire(domino=domino[1:]) > (abs(domino[0]))
            print(abs(domino[0][0]-domino[0][1]))
            return (abs(domino[0][0]-domino[0][1])) + Domino_Solitaire(domino=domino[1:])
        #horizontal allignment
        else:
            print(abs(domino[0][0]-domino[1][0]))
            print(abs(domino[0][1]-domino[1][1]))
            return (abs(domino[0][0]-domino[1][0])) + (abs(domino[0][1]-domino[1][1])) + Domino_Solitaire(domino=domino[2:])

domino =[]
coloumns = int(input())
list1=list(map(int, input().split()))
list2=list(map(int,input().split()))

for i in range(coloumns):
    domino.append([list1[i],list2[i]])
a=Domino_Solitaire(domino)
print(a)



