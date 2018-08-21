# -*- coding: utf-8 -*-
import numpy as np
from sklearn.neighbors import NearestNeighbors
from scipy.stats import pearsonr
# 유사한 성향을 가지고 있는 유저를 찾는 알고리즘


#   1. get_rating: 유저, 영화, 레이팅 데이터를 SparseMatrix.py 에서 가지고 오기

class Find_Neighbors():

    def __init__(self, _rating_matrix):

        self.data = _rating_matrix
        self.movie, self.user = _rating_matrix.shape

#   2. compare 의 기준 정의: 성향이 비슷한 유저를 어떻게 찾을까??
#      두 유저가 공통으로 본 영화를 비교한다. 비교1: 유저들이 본영화 중에 겹치는 영화의 퍼센트

    def _compare_user_(self):

        _userA_ = 0
        _userB_ = self.user

        for x in range(_userB_):
            similarity = pearsonr(self.data[,:_userA_], self.data[,:_userB_])
            print str(similarity)











