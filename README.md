# LU & PLU algorithm

## Description
This is a problem of Scientific Computing HW1.
The data type for real number is float32 (single-precision floating-point number).

Here is the problem:

1. write out the code of LU decomposition, 
1. use this code and PLU method (a function found in Numpy) to solve the Vandermonde matrix system Au=b, where

	![](https://latex.codecogs.com/gif.latex?A%3D%5Cbegin%7Bpmatrix%7D%201%20%26%20%5Cfrac%7B1%7D%7B20%7D%20%26%20%28%5Cfrac%7B1%7D%7B20%7D%29%5E%7B2%7D%20%26%20%5Ccdots%20%26%20%28%5Cfrac%7B1%7D%7B20%7D%29%5E%7B19%7D%20%5C%5C%201%20%26%20%5Cfrac%7B2%7D%7B20%7D%20%26%20%28%5Cfrac%7B2%7D%7B20%7D%29%5E%7B2%7D%20%26%20%5Ccdots%20%26%20%28%5Cfrac%7B2%7D%7B20%7D%29%5E%7B19%7D%20%5C%5C%20%5Cvdots%26%20%5Cvdots%20%26%20%5Cvdots%20%26%20%5Ccdots%20%26%20%5Cvdots%20%5C%5C%201%20%26%5Cfrac%7B19%7D%7B20%7D%20%26%20%28%5Cfrac%7B19%7D%7B20%7D%29%5E%7B2%7D%26%20%5Ccdots%20%26%20%28%5Cfrac%7B19%7D%7B20%7D%29%5E%7B19%7D%20%5C%5C%201%20%26%201%20%26%201%5E%7B2%7D%20%26%20%5Ccdots%20%26%201%5E%7B19%7D%20%5C%5C%20%5Cend%7Bpmatrix%7D%2C%5Ctext%7B%20and%20%7D%20b%3D%5Cbegin%7Bpmatrix%7D%20%5Cfrac%7B1%7D%7B20%7D%20%5C%5C%20%5Cfrac%7B2%7D%7B20%7D%20%5C%5C%20%5Cvdots%20%5C%5C%20%5Cfrac%7B19%7D%7B20%7D%20%5C%5C%201%5C%5C%20%5Cend%7Bpmatrix%7D)


1. compare the difference between these two solutions.
2. add a small perturbation to vector b, which is given by 
	![](https://latex.codecogs.com/gif.latex?%5Cdelta%20b%3D10%5E%7B-16%7D%5Ccdot%20rand%2820%2C1%29)