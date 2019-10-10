"""
Use LU decomposition, created by my own, and LU decomp with pivoting(i.e. PLU), built-in function in numpy/scipy package,
to solve a system of equations with Vandermonde matrix as coefficient matrix.
"""

import numpy as np
import numpy.random as rand
import scipy.linalg as sciLA 
import numpy.linalg as npLA

def LU_decom(A):
    U = A.copy()
    row = U.shape[0]
    L = np.identity(row)

    for i in range(0,row-1):
        """
        E : elementary row operation that multiplies row i by lamb[k] 
            and adds the result to row k, k=i+1,...,row
        """
        E = np.identity(row)
        lamb = U[i+1:,i]/U[i,i]
        E[i+1:,i] = -lamb
        L[i+1:,i] = lamb
        U = E @ U 
    return L,U

def solveEq_GE(A,b,pivot=False):

    if pivot:
        P,L,U = sciLA.lu(A)
        # turn PLUx=b proble into LUx=(P^t)b problem and cast its variable type to float
        x = P.transpose()@ (b.astype(np.float32))
    else:
        L,U = LU_decom(A)
        x = b.astype(np.float32)

    n = A.shape[0]
    #forward substitution -- solve Ly=b
    for i in range(0,n):
        x[i] = ( x[i] - np.dot(L[i,:i],x[:i])[0] ) / L[i,i] 
    #backward substitution -- solve Ux=y
    for i in range(n-1,-1,-1):
        x[i] = ( x[i] - np.dot(U[i,i+1:],x[i+1:])[0] ) / U[i,i]
    return x

# create Vandermonde matrix
a = np.arange(1,21,dtype=np.float32).reshape((20,1))/20
A = np.ones((20,1),dtype=np.float32)
for i in range(1,20):
    A=np.hstack((A,a**i))
# Remember tp cast the variable type of A and a to float32!



# solution of Ax=a using different method
x_lu = solveEq_GE(A,a,False)
y_lu = A @ x_lu

x_plu = solveEq_GE(A,a,True)
y_plu = A @ x_plu

x_np = npLA.solve(A,a)
y_np = A @ x_np

# compute condition number
back_err = npLA.norm(y_lu - y_plu)/npLA.norm(y_plu)
for_err = npLA.norm(x_lu - x_plu)/npLA.norm(x_plu)
cond_est = for_err/back_err

print("用LU的solution x1=\n{}\n用PLU的solution x2=\n{}".format(x_lu.reshape((1,20)),x_plu.reshape((1,20))))
print("relative backward error (|y1-y2|/|y2|)={}".format(back_err))
print("relative forward error (|x1-x2|/|x2|)={}".format(for_err))

# add perturbation to a

"""
所有的rel_delta都小於float32的machine epsilon ~5.96e-08，
即使是double，他的machine epsilon也只有1.11e-16
所以會產生a == a+delta
"""
noise = rand.ranf((20,1)).astype(np.float32) * 10**(-16)
a_noise = a+noise
ratio = noise/a

x_lu_n = solveEq_GE(A,a,False)
y_lu_n = A @ x_lu_n

x_plu_n = solveEq_GE(A,a,True)
y_plu_n = A @ x_plu_n

x_np_n = npLA.solve(A,a)
y_np_n = A @ x_np_n 

print("(擾動後)用LU的solution x1=\n{}\n(擾動後)用PLU的solution x_2=\n{}".format(x_lu_n.reshape((1,20)),x_plu_n.reshape((1,20))))
print("擾動前後的solution x1相差={}".format(npLA.norm(x_lu-x_lu_n)))
print("擾動前後的solution x2相差={}".format(npLA.norm(x_plu-x_plu_n)))