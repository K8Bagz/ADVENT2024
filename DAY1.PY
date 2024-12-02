import fileinput

file = open('input.txt','r')

leftList = []
rightList = []
distance = 0

for row in file.readlines():
    splitList = row.split('   ')
    leftList.append(splitList[0].strip())
    rightList.append(splitList[1].strip())
    
leftList.sort()
rightList.sort()


for i in range(len(leftList)):
    distance+= abs(int(leftList[i]) - int(rightList[i]))
    print(distance)
   
