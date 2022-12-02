import numpy as np
from sys import getsizeof

temp = [
    [
        [-1.5, -1.2, 0.0, 2.1, 24.2],
        [-1.5, -1.2, 0.0, 2.1, 24.2],
        [-1.5, -1.2, 0.0, 2.1, 24.2]
        
    ],
    [
        [-1.5, -1.2, 0.0, 2.1, 24.2],
        [-1.5, -1.2, 0.0, 2.1, 24.2],
        [-1.5, -1.2, 0.0, 2.1, 24.2]
    ]
        
]

npTemp = np.array(temp)

#print(npTemp/3)

dt = np.dtype((np.int32, (2,3)))
arr = np.zeros((5,5), dtype=dt)


#Dieses Arry braucht nur 1 Byte Warnung: Overflow möglich! maxZhal=(2^8 -1)
npArry8bit= np.array([42,127], np.int8)

#print(getsizeof(temp))
#print(getsizeof(npTemp))
#print(npTemp.shape)
print(arr.shape)
