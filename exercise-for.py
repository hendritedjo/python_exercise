'''
#Tugas 1
for a in range (5):
    print((str(a+1)+' ')*(a+1))
print('')

#Tugas 2
s = ''
for a in range (5):
    for b in range (a+1):
        s = s + str(b+1) + ' '    
    s += '\n'
print(s)

#Tugas 3
s = ''
for a in range (5):
    for b in range (a+1):
        s = s + str(5-b) + ' '    
    s += '\n'
print(s)

#Tugas 4
for a in range (5):
    print((str(a+1)+' ')*(5-a))
print('')

#Tugas 5
s = ''
for a in range (5):
    for b in range (5-a):
        s = s + str(b+1) + ' '    
    s += '\n'
print(s)

#Tugas 6
s = ''
for a in range (5):
    for b in range (5-a):
        s = s + str(5-b) + ' '    
    s += '\n'
print(s)
'''
#Tugas 7
for a in range (0,7,2):
    print(' '*(6-a)+'* '*(a+1)+' '*(6-a))
for a in range (6,-1,-2):
    print(' '*(6-a)+'* '*(a+1)+' '*(6-a))