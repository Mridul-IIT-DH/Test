import numpy as np

def t1(L):
    """
    Inputs:
    - L: A list of M numpy arrays, each of shape (1, N)

    Returns:
    A numpy array of shape (M, N) giving all inputs stacked together

    Par: 1 line
    Instructor: 1 line

    Hint: vstack/hstack/dstack, no for loop
    """
    return np.vstack(L)

def t2(X):
    """
    Inputs:
    - X: A numpy array of shape (N, N)

    Returns:
    Numpy array of shape (N,) giving the eigenvector corresponding to the
    smallest eigenvalue of X

    Par: 5 lines
    Instructor: 3 lines

    Hints:
    1) np.linalg.eig
    2) np.argmin
    3) Watch rows and columns!
    """
    eigenvalues, eigenvectors = np.linalg.eig(X)
    min_index = np.argmin(eigenvalues)
    return eigenvectors[:, min_index]

def t3(X):
    """
    Inputs:
    - A: A numpy array of any shape

    Returns:
    A copy of X, but with all negative entires set to 0

    Par: 3 lines
    Instructor: 2 lines

    Hint:
    1) If S is a boolean array with the same shape as X, then X[S] gives an
       array containing all elements of X corresponding to true values of S
    2) X[S] = v assigns the value v to all entires of X corresponding to
       true values of S.
    """
    X_copy = np.copy(X)
    X_copy[X_copy < 0] = 0
    return X_copy

def t4(R, X):
    """
    Inputs:
    - R: A numpy array of shape (3, 3) giving a rotation matrix
    - X: A numpy array of shape (N, 3) giving a set of 3-dimensional vectors

    Returns:
    A numpy array Y of shape (N, 3) where Y[i] is X[i] rotated by R

    Par: 3 lines
    Instructor: 1 line

    Hint:
    1) If v is a vector, then the matrix-vector product Rv rotates the vector
       by the matrix R.
    2) .T gives the transpose of a matrix
    """
    return np.dot(X, R.T)

def t5(X):
    """
    Inputs:
    - X: A numpy array of shape (N, N)

    Returns:
    A numpy array of shape (4, 4) giving the upper left 4x4 submatrix of X
    minus the bottom right 4x4 submatrix of X.

    Par: 2 lines
    Instructor: 1 line

    Hint:
    1) X[y0:y1, x0:x1] gives the submatrix
       from rows y0 to (but not including!) y1
       from columns x0 (but not including!) x1
    """
    return X[:4, :4] - X[-4:, -4:]

def t6(N):
    """
    Inputs:
    - N: An integer

    Returns:
    A numpy array of shape (N, N) giving all 1s, except the first and last 5
    rows and columns are 0.

    Par: 6 lines
    Instructor: 3 lines
    """
    array = np.ones((N, N))
    array[:5, :] = 0
    array[-5:, :] = 0
    array[:, :5] = 0
    array[:, -5:] = 0
    return array

def t7(X):
    """
    Inputs:
    - X: A numpy array of shape (N, M)

    Returns:
    A numpy array Y of the same shape as X, where Y[i] is a vector that points
    the same direction as X[i] but has unit norm.

    Par: 3 lines
    Instructor: 1 line

    Hints:
    1) The vector v / ||v||| is the unit vector pointing in the same direction
       as v (as long as v != 0)
    2) Divide X by a vector of normalization factors, of shape (N, 1)
    3) Elementwise operations between an array of shape (N, M) and an array of
       shape (N, 1) work -- try it! This is called "broadcasting"
    4) Elementwise operations between an array of shape (N, M) and an array of
       shape (N,) won't work -- try reshaping
    """
    norms = np.linalg.norm(X, axis=1, keepdims=True)
    return X / norms

def t8(X):
    """
    Inputs:
    - X: A numpy array of shape (N, M)

    Returns:
    A numpy array Y of shape (N, M) where Y[i] contains the same data as X[i],
    but normalized to have mean 0 and standard deviation 1.

    Par: 3 lines
    Instructor: 1 line
    """
    means = np.mean(X, axis=1, keepdims=True)
    stds = np.std(X, axis=1, keepdims=True)
    return (X - means) / stds

def t9(q, k, v):
    """
    Inputs:
    - q: A numpy array of shape (1, K) (queries)
    - k: A numpy array of shape (N, K) (keys)
    - v: A numpy array of shape (N, 1) (values)

    Returns:
    sum_i exp(-||q-k_i||^2) * v[i]

    Par: 3 lines
    Instructor: 1 ugly line

    Hints:
    1) You can perform elementwise operations on arrays of shape (N, K) and
       (1, K) with broadcasting
    2) Recall that np.sum has useful "axis" and "keepdims" options
    3) np.exp and friends apply elementwise to arrays
    """
    diff = q - k
    squared_distances = np.sum(diff ** 2, axis=1, keepdims=True)
    weights = np.exp(-squared_distances)
    return np.sum(weights * v)

def t10(Xs):
    """
    Inputs:
    - Xs: A list of length L, containing numpy arrays of shape (N, M)

    Returns:
    A numpy array R of shape (L, L) where R[i, j] is the Euclidean distance
    between C[i] and C[j], where C[i] is an M-dimensional vector giving the
    centroid of Xs[i]

    Par: 12 lines
    Instructor: 3 lines (after some work!)

    Hints:
    1) You can use a for loop over L
    2) Distances are symmetric
    3) Go one step at a time
    4) Our 3-line solution uses no loops, and uses the algebraic trick from the
       next problem.
    """
    centroids = [np.mean(X, axis=0) for X in Xs]
    centroids = np.array(centroids)
    D = np.linalg.norm(centroids[:, np.newaxis] - centroids[np.newaxis, :], axis=2)
    return D

def t11(X):
    """
    Inputs:
    - X: A numpy array of shape (N, M)

    Returns:
    A numpy array D of shape (N, N) where D[i, j] gives the Euclidean distance
    between X[i] and X[j], using the identity
    ||x - y||^2 = ||x||^2 + ||y||^2 - 2x^T y

    Par: 3 lines
    Instructor: 2 lines (you can do it in one but it's wasteful compute-wise)

    Hints:
    1) What happens when you add two arrays of shape (1, N) and (N, 1)?
    2) Think about the definition of matrix multiplication
    3) Transpose is your friend
    4) Note the square! Use a square root at the end
    5) On some machines, ||x||^2 + ||x||^2 - 2x^Tx may be slightly negative,
       causing the square root to crash. Just take max(0, value) before the
       square root. Seems to occur on Macs.
    """
    norm_squared = np.sum(X ** 2, axis=1, keepdims=True)
    D = norm_squared + norm_squared.T - 2 * np.dot(X, X.T)
    return np.sqrt(np.maximum(D, 0))

def t12(X, Y):
    """
    Inputs:
    - X: A numpy array of shape (N, F)
    - Y: A numpy array of shape (M, F)

    Returns:
    A numpy array D of shape (N, M) where D[i, j] is the Euclidean distance
    between X[i] and Y[j].

    Par: 3 lines
    Instructor: 2 lines (you can do it in one, but it's more than 80 characters
                with good code formatting)

    Hints: Similar to previous problem
    """
    X_norm_squared = np.sum(X ** 2, axis=1, keepdims=True)
    Y_norm_squared = np.sum(Y ** 2, axis=1, keepdims=True)
    D = X_norm_squared + Y_norm_squared.T - 2 * np.dot(X, Y.T)
    return np.sqrt(np.maximum(D, 0))

def t13(q, V):
    """
    Inputs:
    - q: A numpy array of shape (1, M) (query)
    - V: A numpy array of shape (N, M) (values)

    Return:
    The index i that maximizes the dot product q . V[i]

    Par: 1 line
    Instructor: 1 line

    Hint: np.argmax
    """
    return np.argmax(np.dot(V, q.T))

def t14(X, y):
    """
    Inputs:
    - X: A numpy array of shape (N, M)
    - y: A numpy array of shape (N, 1)

    Returns:
    A numpy array w of shape (M, 1) such that ||y - Xw||^2 is minimized

    Par: 2 lines
    Instructor: 1 line

    Hint: np.linalg.lstsq, or use the pseudoinverse (X^T X)^-1 X^T y
    """
    return np.linalg.lstsq(X, y, rcond=None)[0]

def t15(X, Y):
    """
    Inputs:
    - X: A numpy array of shape (N, 3)
    - Y: A numpy array of shape (N, 3)

    Returns:
    A numpy array C of shape (N, 3) such C[i] is the cross product between X[i]
    and Y[i]

    Par: 1 line
    Instructor: 1 line

    Hint: np.cross
    """
    return np.cross(X, Y)

def t16(X):
    """
    Inputs:
    - X: A numpy array of shape (N, M)

    Returns:
    A numpy array Y of shape (N, M - 1) such that
    Y[i, j] = X[i, j] / X[i, M - 1]
    for all 0 <= i < N and all 0 <= j < M - 1

    Par: 1 line
    Instructur: 1 line

    Hints:
    1) If it doesn't broadcast, reshape or np.expand_dims
    2) X[:, -1] gives the last column of X
    """
    return X[:, :-1] / X[:, -1, np.newaxis]

def t17(X):
    """
    Inputs:
    - X: A numpy array of shape (N, M)

    Returns:
    A numpy array Y of shape (N, M + 1) such that
        Y[i, :F] = X[i]
        Y[i, F] = 1

    Par: 1 line
    Instructor: 1 line

    Hint: np.hstack, np.ones
    """
    return np.hstack((X, np.ones((X.shape[0], 1))))

def t18(N, r, x, y):
    """
    Inputs:
    - N: An integer
    - r: A floating-point number
    - x: A floating-point number
    - y: A floating-point number

    Returns:
    A numpy array I of floating point numbers and shape (N, N) such that:
    I[i, j] = 1 if ||(j, i) - (x, y)|| < r
    I[i, j] = 0 otherwise

    Par: 3 lines
    Instructor: 2 lines

    Hints:
    1) np.meshgrid and np.arange give you X, Y
    2) Arrays have an astype method
    """
    I = np.sqrt((np.arange(N)[:, np.newaxis] - x) ** 2 + (np.arange(N) - y) ** 2)
    return (I < r).astype(float)

def t19(N, s, x, y):
    """
    Inputs:
    - N: An integer
    - s: A floating-point number
    - x: A floating-point number
    - y: A floating-point number

    Returns:
    A numpy array I of shape (N, N) such that
    I[i, j] = exp(-||(j, i) - (x, y)||^2 / s^2)

    Par: 3 lines
    Instructor: 2 lines

    Hint: Be careful with types -- float and int aren't the same!
    """
    I = np.sqrt((np.arange(N)[:, np.newaxis] - x) ** 2 + (np.arange(N) - y) ** 2)
    return np.exp(-I ** 2 / s ** 2)

def t20(N, v):
    """
    Inputs:
    - N: An integer
    - v: A numpy array of shape (3,) giving coefficients v = [a, b, c]

    Returns:
    A numpy array of shape (N, N) such that M[i, j] is the distance between the
    point (j, i) and the line a*j + b*i + c = 0

    Par: 4 lines
    Instructor: 2 lines

    Hints:
    1) The distance between the point (x, y) and the line ax+by+c=0 is given by
       abs(ax + by + c) / sqrt(a^2 + b^2)
       (The sign of the numerator tells which side the point is on)
    2) np.abs
    """
    a, b, c = v
    x_coords, y_coords = np.arange(N), np.arange(N)
    X, Y = np.meshgrid(x_coords, y_coords)
    return np.abs(a * X + b * Y + c) / np.sqrt(a ** 2 + b ** 2)


# Sample inputs for testing

L = [np.array([[1]]), np.array([[2]]), np.array([[3]])]

X_t2 = np.array([[4.0, 2.0], [2.0, 3.0]])

X_t3 = np.array([[1.0, -2.0], [-3.0, 4.0]])

R_t4 = np.array([[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]])
X_t4 = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]])

X_t5 = np.random.rand(8, 8)

N_t6 = 10

X_t7 = np.array([[3., -6., 9.], [12., -15., 18.]])

X_t8 = np.random.rand(5, 5)

q_t9 = np.array([[1., 2.]])
k_t9 = np.array([[3., 4.], [5., 6.]])
v_t9 = np.array([[7.], [8.]])

Xs_t10 = [np.random.rand(10, 3), np.random.rand(10, 3)]

X_t11 = np.random.rand(5, 3)

X_t12 = np.random.rand(5, 3)
Y_t12 = np.random.rand(7, 3)

q_t13 = np.array([[1., 2., 3.]])
V_t13 = np.random.rand(10, 3)

X_t14 = np.random.rand(10, 3)
y_t14 = np.random.rand(10, 1)

X_t15 = np.random.rand(5, 3)
Y_t15 = np.random.rand(5, 3)

X_t16 = np.random.rand(5, 4)

X_t17 = np.random.rand(5, 3)

N_t18, r_t18, x_t18, y_t18 = 10, 0.5, 0.25, 0.25

N_t19, s_t19, x_t19, y_t19 = 10, 0.25, 0.25, 0.25

N_t20, v_t20 = 10, [1., -2., -3.]

# Calling functions and printing outputs

print("t1 result:\n", t1(L))
print("t2 result:\n", t2(X_t2))
print("t3 result:\n", t3(X_t3))
print("t4 result:\n", t4(R_t4, X_t4))
print("t5 result:\n", t5(X_t5))
print("t6 result:\n", t6(N_t6))
print("t7 result:\n", t7(X_t7))
print("t8 result:\n", t8(X_t8))
print("t9 result:\n", t9(q_t9, k_t9, v_t9))
print("t10 result:\n", t10(Xs_t10))
print("t11 result:\n", t11(X_t11))
print("t12 result:\n", t12(X_t12, Y_t12))
print("t13 result:\n", t13(q_t13, V_t13))
print("t14 result:\n", t14(X_t14, y_t14))
print("t15 result:\n", t15(X_t15, Y_t15))
print("t16 result:\n", t16(X_t16))
print("t17 result:\n", t17(X_t17))
print("t18 result:\n", t18(N_t18, r_t18, x_t18, y_t18))
print("t19 result:\n", t19(N_t19, s_t19, x_t19, y_t19))
print("t20 result:\n", t20(N_t20, v_t20))
