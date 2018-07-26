# Implementation of Stochastic Gradient Descent on SparseMatrix
# Parameters: Array X of size [n_samples, x_features] , Array Y of size [n_samples] (holds target values)

import numpy as np
from sklearn import linear_model
from scipy import sparse
from sklearn.linear_model import SGDClassifier


class vector:
    user_vector = [0.1] * 400000
    movie_vector = [0.1] * 17700

def sgd(a, b, c):

    lrate = 0.0001
    init_feature = 0.01

    matrix_data = sparse.coo_matrix((c, (a, b)))
    matrix_data = sparse.csr_matrix(matrix_data)

    maxA = max(a)
    maxB = max(b)
    globalAverage = global_average(matrix_data, maxA, maxB)
    print globalAverage
    for i in range((max(a))):
        for j in range((max(b))):
            avgRow = getAvg(matrix_data[i,:])
            avgCol = getAvg(matrix_data[:,j])
            offset = predictRating(i, j, matrix_data, globalAverage)
            print matrix_data[i,j]
            err = lrate * (matrix_data[i,j] - offset)
            uv = vector.user_vector[j]
            vector.user_vector[j] += lrate * (err * vector.movie_vector[i] - 0.02 * uv)
            vector.movie_vector[i] += lrate * (err * uv - 0.02 * vector.movie_vector[i])
            print "Feature 1 of userVector of user " + str(j) + " is " + str(vector.user_vector[j])
            print "Feature 1 of movieVector of movie " + str(i) + ' is ' + str(vector.movie_vector[i])


def global_average(matrix, a, b):
    average = 0
    count = 0
    for i in range(a):
        for j in range(b):
            if matrix[i,j] != 0:
                average += matrix[i,j]
                count += 1
            else:
                continue

    return float(average) / count

def predictRating(movie, user, matrix_data, globalAverage):
    row_num = -1
    average = 0
    count = 0
    print matrix_data[:,user].data
    for x in matrix_data[:,user].data:
        row_num += 1
        if x is not 0:
            movie_avg = getbetterAvg(matrix_data[row_num,:], globalAverage)
            average += (movie_avg - x)
            count += 1
        else:
            continue

    return float(average) / count

# Returns the value of the dot product for a given row and column

def dotproduct(row_array, col_array, num_features):
    total_dot_product = 0
    for x in range(num_features):
         total_dot_product += row_array[x] + col_array[x]

    return total_dot_product

# given a vector, find the average rating in that particular vector (can be either movie vector or user vector)

def getAvg(vector):
    total = 0
    count = 0

    for x in vector.data:
        if x is not 0:
            total += x
            count += 1

        else:
            continue

    average = float(total) / count
    return average

def getbetterAvg(vector, glo_average):

    total = 0
    count = 0

    for x in vector.data:
        if x is not 0:
            total += x
            count += 1

        else:
            continue

    k = 25

    betterAverage = (glo_average * k + total) / (k + count)
    return betterAverage