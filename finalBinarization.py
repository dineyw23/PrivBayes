import math

class binarization:
    domain = [16,32,16] #Last column of domain file
    numRows,numCols = 3,3
    qData = [[0 for x in range(numRows)] for y in range(numCols)]
    qData[0][0] = 5
    qData[0][1] = 3
    qData[0][2] = 2
    qData[1][0] = 7
    qData[1][1] = 8
    qData[1][2] = 1
    qData[2][0] = 7
    qData[2][1] = 8
    qData[2][2] = 9



    def binarization(self,x):
        temp1,temp2,temp3 = 0,0,0
        a = int(math.log(self.domain[0],2)) 
        b = a + int(math.log(self.domain[1],2)) 
        for y in range(self.numCols):
            if y == 0:    
                temp1 = self.qData[x][y]
            elif y == 1:
                temp2 = self.qData[x][y] << a
            elif y == 2:
                temp3 = self.qData[x][y] << b
        temp3 = temp1 | temp2 | temp3  
        return temp3 


    def main(self):
        entries = []
        for x in range(self.numRows):
           entries.append(self.binarization(x))

        print "The entries is:"
        for p in entries:
            print "As String", bin(p)
            print p

Object = binarization()
Object.main()