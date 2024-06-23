import numpy as np
import math

'''
def WHT(x):
    x = np.array(x)
    if (len(x.shape) < 2): # make sure x is 1D array
        if (len(x) > 3): # accept x of min length of 4 elements (M=2)
            # check length of signal, adjust to 2**m
            n = len(x)
            M = math.trunc(math.log(n, 2))
            x = x[0:2 ** M]
            h2 = np.array([[1, 1], [1,-1]])
            for i in range(M- 1):
                if (i == 0):
                    H = np.kron(h2, h2)
                else:
                    H = np.kron(H, h2)
                return (np.dot(H, x) / 2. ** M, x, M)
'''

def recursive_kronecker(H, h2, depth, max_depth):
    if depth == max_depth:
        return H
    elif depth == 0:
        return recursive_kronecker(h2, h2, depth + 1, max_depth)
    else:
        return recursive_kronecker(np.kron(H, h2), h2, depth + 1, max_depth)

def WHT(x):
    x = np.array(x)
    if (len(x.shape) < 2): # make sure x is 1D array
        if (len(x) > 3): # accept x of min length of 4 elements (M=2)
            # check length of signal, adjust to 2**m
            n = len(x)
            M = math.trunc(math.log(n, 2))
            x = x[0:2 ** M]
            h2 = np.array([[1, 1], [1,-1]])
            H = recursive_kronecker(None, h2, 0, M)
            return (np.dot(H, x) / 2. ** M, x, M)
                         

x = np.array([1, 2, 3, 4])
WHT_x, x_original, M = WHT(x)
print(WHT_x)
print(x_original)
print(M)