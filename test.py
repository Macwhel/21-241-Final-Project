import numpy as np
from numpy import linalg as LA

a = np.matrix(
    [[0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0]]
    )

at = a.getT()

authValMat = at @ a
hubValMat = a @ at

'''print(authValMat)
print()
print(hubValMat)
print()'''

authValEigens = LA.eig(authValMat) 
hubValEigens = LA.eig(hubValMat)

print(authValEigens[0])
maxEigenIndex = list(authValEigens[0]).index(max(authValEigens[0]))
#print(maxEigenIndex)
maxAuthValEVec = authValEigens[1][:, maxEigenIndex]
#print(maxAuthValEVec)
AVList = [val.tolist()[0][0] for val in maxAuthValEVec]
print(AVList)
print(np.argsort(AVList)[::-1])

'''print(authValEigens)
print(np.argsort(authValEigens))
'''
a = [0.08824683,
 0.28365354,
 0.25619926,
 0.28365354,
 0.08824683]
print(a)
print(np.argsort(a)[::-1])
'''
print()
print(np.argsort(hubValEigens))
a = [0.45160596,
 0.14049815,
 0.20394795,
 0.        ,
 0.20394795]
 
print(np.argsort(a))'''

'''
[0.1793383954483855, 0.5764509452353924, 0.5206573684395938, 0.5764509452353921, 0.17933839544838517]
[1 3 2 0 4]
[0.08824683, 0.28365354, 0.25619926, 0.28365354, 0.08824683]
[3 1 2 4 0]
'''