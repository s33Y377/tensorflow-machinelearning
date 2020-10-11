import numpy as np
from random import shuffle
try:
    l = np.arange((1000000))
    shuffle(l)
    q = 999999
    for x, y in enumerate(l):
        if x == q:
            message = "Found"
            index = y
            break
        else:
            message = "Not Found"
            index = "None"
except BaseException as e:
    message = "Not Found"
    index = "None"
print("Result is ", message, "and index is", index)
