x = int(input("Enter the width "))
def diamond(rows):
    for row in range(rows):
        print(' '*(rows-row-1)+'# '*(row+1))
    for col in range(rows-1,0,-1):
        print(' '*(rows-col)+'# '*(col))

diamond(x)