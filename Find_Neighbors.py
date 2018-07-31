# -*- coding: utf-8 -*-
import numpy as np
from sklearn.neighbors import NearestNeighbors

# 유사한 성향을 가지고 있는 유저를 찾는 알고리즘


#   1. get_rating: 유저, 영화, 레이팅 데이터를 SparseMatrix.py 에서 가지고 오기

class Find_Neighbors():

    def __init__(self, _rating_matrix):

        self.data = _rating_matrix
        self.movie, self.user = _rating_matrix.shape
#   2. compare 의 기준 정의: 성향이 비슷한 유저를 어떻게 찾을까??
#      두 유저가 공통으로 본 영화를 비교한다. 비교1: 유저들이 본영화 중에 겹치는 영화의 퍼센트
    def compare(self):
        movie_counter = 0
        user_index = 0
        userA_list = []
        for movie in range(self.movie):
            if self.data[movie, user_index] is not 0:
                movie_counter += 1
                userA_list.append(self.data[movie, user_index])

            else:
                continue







