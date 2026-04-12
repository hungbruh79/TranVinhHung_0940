input_str = input(" nhập X, Y : ")
Dimensions=[int(x) for x in input_str.split(',')]
rowNum= Dimensions[0]
colNum= Dimensions[1]
multilist = [[0 for col in range(colNum)]for row in range(rowNum)]
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col
print (multilist)
