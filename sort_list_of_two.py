
def sort_values(x):
    if type(x) is list:
        if len(x) == 2:
            if x[0] > x[1]:
                x =  x[::-1]
                print("Number sorted")
            elif x[0] < x[1]:
                print("Numbers already in order")
            else:
                print("Numbers are equal")
        else:
            print("Length not 2")
    else:
        print("Not a list")
    print(x)
    return x

def product_array(x):
    if type(x) is list:
        if len(x) > 1:
            length = len(x)
            matrix = [[0 for x in range(length)] for x in range(length)]
            for i in range(length):
                for j in range(length):
                    matrix[i][j] = x[i] * x[j]
        else:
            print("List not long enough")
    else:
        print("Not a list")
        
    #print(matrix)
    return matrix