import math;
a = [1, 2, 3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20];
b=[2,4,6,8,10]

def intersection(a,b):
    c = [value for value in a if value in b]
    return c
print("a intersection b : ", intersection(a,b))

def powret(set,size):
    sizep = (int) (math.pow(2, size));
    counter = 0;
    i = 0;
    for counter in range(0, sizep):
        for i in range(0, size):
            if((counter & (1 << i)) > 0):
                print(b[i], end = ", ");
        print("");
powret(b, len(b));
