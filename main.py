# -*- coding: utf-8 -*-
import numpy as np

def quadratic(A, x):
    A_inv = np.linalg.inv(A)
    return np.sqrt(np.dot(x.T, np.dot(A_inv, x)))

def second_eig(A):
    eigenvalues =np.linalg.engvalsh(A)
    return np.sort(eigenvalues)

def power_iter(A, x, k):
    Akx = np.linalg.matrix_power(A, k).dot(x)
    v1 = Akx / np.linalg.norm(Akx)
    lambda_1 = np.dot(v1.T, np.dot(A, v1))
    return lambda_1
