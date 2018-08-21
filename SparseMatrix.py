# -*- coding: utf-8 -*-

from scipy import sparse
from scipy.sparse import csr_matrix
from scipy.stats import uniform
import numpy as np
import SVD
from SGD import MF
from Find_Neighbors import Find_Neighbors

def construct_sparse_matrix():

    data_file = open("combined_data_1.txt")
    movie_row = []
    movie_column = []
    data = []
    already_used = []
    user_index = {}
    col_index = 0
    printcounter = 0
    check_example = 0

    for line in data_file:
        if check_example == 1:
            break
        if not line.strip():
            continue
        if ":" in line:
            printcounter += 1
            print printcounter
            length = line.__len__() - 2
            movieID = line[:length].rstrip()
            movie_index = eval(movieID) - 1
            if eval(movieID) == 30:
                check_example = 1

        else:
            userID = line.partition(",")
            rating = userID[2].partition(",")[0]
            if userID[0] not in user_index.keys():
                user_index[userID[0]] = col_index
                movie_row.append(movie_index)
                movie_column.append(col_index)
                data.append(eval(rating))
                col_index += 1

            else:
                x = user_index[userID[0]]
                movie_row.append(movie_index)
                movie_column.append(x)
                data.append(eval(rating))

    a = np.asarray(movie_row)
    b = np.asarray(movie_column)
    c = np.asarray(data)
    c = c.astype('float')

#    SVD.sgd(a, b, c)
    matrix_data = sparse.coo_matrix((c, (a, b)))
    matrix_data = sparse.csr_matrix(matrix_data)
    R = matrix_data.toarray()
    mf = MF(R, K=2, alpha=0.02, beta=0.001, iterations=120)
    mf.train()
    print mf.full_matrix()
    neighbor_module = Find_Neighbors(matrix_data)
    Find_Neighbors._compare_user_(neighbor_module)
    movie_aspect_vector = mf.get_movie_SVD()
    item_aspect_vector = mf.get_item_SVD()

    matrix_data = sparse.coo_matrix((c, (a, b)))
    matrix_data = sparse.csr_matrix(matrix_data)
    R = matrix_data
    print "done"

if __name__ == '__main__':
    sparse_matrix = construct_sparse_matrix()