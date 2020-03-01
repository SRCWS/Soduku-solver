import random



def check_zero(source):
    for i in range(len(source)):
        for j in range(len(source[0])):
            if source[i][j] == 0:
                return (i, j)
    return None


def valid(source, number, position):
    # row
    for i in range(len(source[0])):
        if source[position[0]][i] == number and i != position[1]:
            return False
    # columns
    for i in range(len(source[0])):
        if source[i][position[1]] == number and i != position[0]:
            return False
    # box
    box_x = int((position[0] - position[0] % 3) / 3)
    box_y = int((position[1] - position[1] % 3) / 3)
    for i in range(box_x * 3, box_x * 3 + 3):
        for j in range(box_y * 3, box_y * 3 + 3):
            if source[i][j] == number and (i, j) != position:
                return False
    return True

def Full(source):


    #print(source)

    number_list = [1,2,3,4,5,6,7,8,9]
    random.shuffle(number_list)
    find = check_zero(source)
    # print(find)
    if not find:
        return True
    else:
        row, columns = find
        for i in number_list:

            if valid(source, i, (row, columns)):
                source[row][columns] = i
                if Full(source):
                    return True
                source[row][columns] = 0
    return False


def print_sudoko(source):
    for i in range(len(source)):
        if i % 3 == 0 and i != 0:
            print("+ + + + + + + + + + +")
        # print("")
        for j in range(len(source[0])):
            if j % 3 == 0 and j != 0:
                print("+", end=' ')
            if source[i][j] == 0:
                print("#", end=' ')
            else:
                print(source[i][j], end=' ')
        print("")




# random.shuffle(number_list)
def random_xy():
    x = random.randint(0, 8)
    y = random.randint(0, 8)
    return x, y

def remove( source, count = 40):
    #global source
    #print(count)
    while count >0:
        x,y = random_xy()
        if source[x][y]!=0:
            source[x][y] = 0
            source[8-x][8-y] = 0
            count -=2

#print(source)
def NewGame():
    source = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    #number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(number_list)
    Full(source)

    remove(source)
    return source
#print(NewGame())
"""
for i in range(10):
    #print(NewGame())
    number_list = [1,2,3,4,5,6,7,8,9]
    random.shuffle(number_list)
    #print(number_list)
    #print(NewGame())
"""