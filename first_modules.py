
def first_function(x):
    if type(x) is list:
        if len(x) == 2:
            if x[0] > x[1]:
                x =  x[::-1]
                print("Number sorted")
            elif x[0] < x[1]
            else:
                print("Numbers are equal")
        else:
            print("Length should be equal to 2")
    else:
        print("Please give me a list")
    return x


def second_function(x):
    if type(x) is list:
        if len(x) > 1:
            length = len(x)
            matrix = [[0 for x in range(length)] for x in range(length)]
            for i in range(length):
                for j in range(length):
                    matrix[i][j] = x[i] * x[j]
        else:
            print("Not a long list")
    else:
        print("Not even a list")
    
    return matrix