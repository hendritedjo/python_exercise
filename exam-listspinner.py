#Soal 2
list1 = [[1, 2, 3, 4], 
         [5, 6, 7, 8], 
         [9, 10, 11, 12], 
         [13, 14, 15, 16]]

def counterClockwise(num):
    num1 = [[a for a in range(num[0][3], num[3][3]+1, 4)],
            [a for a in range(num[0][2], num[3][2]+1, 4)],
            [a for a in range(num[0][1], num[3][1]+1, 4)],
            [a for a in range(num[0][0], num[3][0]+1, 4)]]
    return num1

print(counterClockwise(list1))