print("hello world")
temp = [
    [0,3,2,1,5,0,0,0,0],
    [0,0,5,0,0,0,2,0,8],
    [1,9,0,2,0,4,7,0,3],
    [2,5,7,0,3,0,6,4,0],
    [9,8,0,0,7,2,0,0,1],
    [6,0,0,0,0,9,8,2,7],
    [3,7,8,0,0,0,9,0,0],
    [4,0,0,0,6,0,0,8,0],
    [0,0,1,0,0,0,3,0,0]
]

def print_sudoko(source):

    for i in range(len(source)):
        if i % 3 == 0 and i != 0:
            print("+ + + + + + + + + + +")
        #print("")
        for j in range(len(source[0])):
            if j %3 == 0 and j != 0:
                print("+", end = ' ')
            if source[i][j] == 0:
                print("#",end= ' ')
            else:
                print(source[i][j], end = ' ')
        print("")

#print(print_sudoko(source))

def find_empty(source):
    for i in range(len(source)):
        for j in range(len(source[0])):
            if source[i][j] == 0:
                return (i,j)
    return None


def valid(source, number,position):
    #row
    for i in range(len(source[0])):
        if source[position[0]][i] == number and i != position[1]:
            return False
    #columns
    for i in range(len(source[0])):
        if source[i][position[1]] == number and i != position[0]:
            return False
    #box
    box_x = int((position[0] - position[0]%3)/3)
    box_y = int((position[1] - position[1]%3)/3)
    for i in range(box_x*3,box_x*3+3):
        for j in range(box_y*3,box_y*3+3):
            if source[i][j]==number and (i,j) != position:
                return False

    return True
def solver(source):
    #print(print_sudoko(source))
    find = find_empty(source)
    if not find:
        return True
    else:
        row, columns = find
        for i in range(1,len(source)+1):
            if valid(source, i ,(row,columns)):
                source[row][columns] = i
                if solver(source):
                    return True
                source[row][columns] = 0
    return False

def input_sudoko():
    start = 0
    while start ==0:
        temp = []
        for i in range(9):
            temp.append(input("inter the {} row '0' for empty(example 97012036): ".format(i+1)))
        source = []
        for i in temp:
            source.append([int(x) for x in list(i)])
        print("Is that your Soduku")
        print_sudoko(source)
        start = int(input("yes input 1 no input 0"))
        print("Finish input")
        print("checking the soduku")
        print("Finish checking")
    print("Start solver")
    solver(source)
    print("The solver have finish")
    print("the result is ")
    print_sudoko(source)
if __name__ =="__main__":
    input_sudoko()
#print_sudoko(source)
#solver(temp)
#print_sudoko(temp)
