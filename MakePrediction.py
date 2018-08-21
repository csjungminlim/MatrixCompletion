# -*- coding: utf-8 -*-
import numpy as np
# 기계학습으로 찾은 aspect vector 을 통해서 새로운 값들에대한 예상값을 구한다.
# parameter: 영화의 aspect vector, 유저의 aspect vector
# 두 백터의 dot product 를 구하면 결과값이 나온다

from SGD import MF

def make_prediction(movie_matrix, user_matrix, user_index_dict, mf):

    file1 = open("qualifying.txt")
    for line in file1:
        if not line:
            continue
        if ":" in line:
            length = line.__len__() - 2
            movieID = line[:length].rstrip()
            print movieID
            movieindex = eval(movieID) - 1

        else:
            userID = line.rstrip()
            if userID not in user_index_dict:
                continue
            else:
                id_index = user_index_dict[userID]

                prediction = MF.get_rating(mf, movieindex, id_index)
                print "The rating prediction for user " + userID + " for movie ID " + movieID + " is " + str(prediction)


