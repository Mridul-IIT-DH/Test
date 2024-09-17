import numpy as np

def w1(X):
    """
    Input:
    - X: A numpy array

    Returns:
    - A matrix Y such that Y[i, j] = X[i, j] * 10 + 100
    """
    return X * 10 + 100


def w2(X, Y):
    """
    Inputs:
    - X: A numpy array of shape (N, N)
    - Y: A numpy array of shape (N, N)

    Returns:
    A numpy array Z such that Z[i, j] = X[i, j] + 10 * Y[i, j]
    """
    return X + 10 * Y


def w3(X, Y):
    """
    Inputs:
    - X: A numpy array of shape (N, N)
    - Y: A numpy array of shape (N, N)

    Returns:
    A numpy array Z such that Z[i, j] = X[i, j] * Y[i, j] - 10
    """
    return X * Y - 10


def w4(X, Y):
    """
    Inputs:
    - X: A numpy array of shape (N, N)
    - Y: A numpy array of shape (N, N)

    Returns:
    A numpy array giving the matrix product X times Y
    """
    return np.dot(X, Y)


def w5(X):
    """
    Inputs:
    - X: A numpy array of shape (N, N) of floating point numbers

    Returns:
    A numpy array with the same data as X, but cast to 32-bit integers
    """
    return X.astype(np.int32)


def w6(X, Y):
    """
    Inputs:
    - X: A numpy array of shape (N,) of integers
    - Y: A numpy array of shape (N,) of integers

    Returns:
    A numpy array Z such that Z[i] = float(X[i]) / float(Y[i])
    """
    return X.astype(float) / Y.astype(float)


def w7(X):
    """
    Inputs:
    - X: A numpy array of shape (N, M)

    Returns:
    A numpy array Y of shape (N * M, 1) containing the entries of X in row order.
    """
    return np.reshape(X, (-1, 1))


def w8(N):
    """
    Inputs:
    - N: An integer

    Returns:
    A numpy array of shape (N, 2N) initialized with zeros
    """
    return np.zeros((N, 2 * N))


def w9(X):
    """
    Inputs:
    - X: A numpy array of shape (N, M) where each entry is between 0 and 1

    Returns:
    A numpy array Y where Y[i, j] = True if X[i, j] > 0.5, else False
    """
    return X > 0.5


def w10(N):
    """
    Inputs:
    - N: An integer

    Returns:
    A numpy array X of shape (N,) such that X[i] = i
    """
    return np.arange(N)


def w11(A, v):
    """
    Inputs:
    - A: A numpy array of shape (N, F)
    - v: A numpy array of shape (F, 1)

    Returns:
    A numpy array of shape (N, 1) giving the matrix-vector product Av
    """
    return np.dot(A, v)


def w12(A, v):
    """
    Inputs:
    - A: A numpy array of shape (N, N), of full rank
    - v: A numpy array of shape (N, 1)

    Returns:
    A numpy array of shape (N, 1) giving the matrix-vector product of the inverse
    of A and v: A^-1 v
    """
    return np.dot(np.linalg.inv(A), v)


def w13(u, v):
    """
    Inputs:
    - u: A numpy array of shape (N, 1)
    - v: A numpy array of shape (N, 1)

    Returns:
    The inner product u^T v
    """
    return np.dot(u.T, v)[0, 0]


def w14(v):
    """
    Inputs:
    - v: A numpy array of shape (N, 1)

    Returns:
    The L2 norm of v: norm = (sum_i^N v[i]^2)^(1/2)
    You MAY NOT use np.linalg.norm
    """
    return np.sqrt(np.sum(v ** 2))


def w15(X, i):
    """
    Inputs:
    - X: A numpy array of shape (N, M)
    - i: An integer in the range 0 <= i < N

    Returns:
    Numpy array of shape (M,) giving the ith row of X
    """
    return X[i]


def w16(X):
    """
    Inputs:
    - X: A numpy array of shape (N, M)

    Returns:
    The sum of all entries in X
    """
    return np.sum(X)


def w17(X):
    """
    Inputs:
    - X: A numpy array of shape (N, M)

    Returns:
    A numpy array S of shape (N,) where S[i] is the sum of row i
    """
    return np.sum(X, axis=1)


def w18(X):
    """
    Inputs:
    - X: A numpy array of shape (N, M)

    Returns:
    A numpy array S of shape (M,) where S[j] is the sum of column j
    """
    return np.sum(X, axis=0)


def w19(X):
    """
    Inputs:
    - X: A numpy array of shape (N, M)

    Returns:
    A numpy array S of shape (N, 1) where S[i, 0] is the sum of row i
    """
    return np.sum(X, axis=1).reshape(-1, 1)


def w20(X):
    """
    Inputs:
    - X: A numpy array of shape (N, M)

    Returns:
    A numpy array S of shape (N, 1) where S[i, 0] is the L2 norm 
    for row i.
    """
    return np.sqrt(np.sum(X ** 2, axis=1)).reshape(-1, 1)


# Define a sample input for testing all functions
X = np.array([[0.1, 0.5, 0.9],
              [0.2, 0.6, 0.4],
              [0.3, 0.8, 0.7]])

Y = np.array([[1., 2., 3.],
              [4., 5., 6.],
              [7., 8., 9.]])

v = np.array([[1],
              [2],
              [3]])

A = np.array([[1., 2., 3.],
              [0., 1., 4.],
              [5., 6., 0.]])

u = np.array([[1],
              [2],
              [3]])

# Now you can call the functions with these arrays.
print("w1 result:\n", w1(X))
print("w2 result:\n", w2(X, Y))
print("w3 result:\n", w3(X, Y))
print("w4 result:\n", w4(X, Y))
print("w5 result:\n", w5(X))
print("w6 result:\n", w6(np.array([1, 2, 3]), np.array([4, 5, 6])))
print("w7 result:\n", w7(X))
print("w8 result:\n", w8(4))
print("w9 result:\n", w9(X))
print("w10 result:\n", w10(5))
print("w11 result:\n", w11(A, v))
print("w12 result:\n", w12(A, v))
print("w13 result:\n", w13(u, v))
print("w14 result:\n", w14(v))
print("w15 result:\n", w15(X, 1)) # Get the second row
print("w16 result:\n", w16(X))
print("w17 result:\n", w17(X))
print("w18 result:\n", w18(X))
print("w19 result:\n", w19(X))
print("w20 result:\n", w20(X))
