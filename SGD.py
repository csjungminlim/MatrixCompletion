# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
class MF():

# 기본 INIT 과정
    def __init__(self, R, K, alpha, beta, iterations):

        self.R = R
        self.num_items, self.num_users = R.shape
        self.K = K
        self.alpha = alpha
        self.beta = beta
        self.iterations = iterations
        self.graph_list = []
        self.graph_y = []
        self.counter_y = 0

# 학습시키는 Iteration Loop

    def train(self):

        self.P = np.random.normal(scale = 1./self.K, size = (self.num_items, self.K))
        self.Q = np.random.normal(scale = 1./self.K, size = (self.num_users, self.K))

        self.b_i = np.zeros(self.num_items)
        self.b_u = np.zeros(self.num_users)
        self.b = np.mean(self.R[np.where(self.R != 0)])

        self.samples = [
            (i, j, self.R[i,j])
            for i in range(self.num_items)
            for j in range(self.num_users)
            if self.R[i,j] > 0
        ]

        training_process = []

        for i in range(self.iterations):
            np.random.shuffle(self.samples)
            self.sgd()
            mse = self.mse()
            training_process.append((i, mse))

            if (i+1) % 1 == 0:
                print("Iteration: %d ; error = %.4f" % (i+1, mse))
            self.graph_list.append(mse)
            self.graph_y.append(self.counter_y)
            self.counter_y += 1

# 에러의 변화를 그래프로 표시

        z = np.polyfit(self.graph_y, self.graph_list,3)
        f = np.poly1d(z)
        print f

        y_new = np.linspace(self.graph_list[0], self.graph_list[-1], 50)
        x_new = f(y_new)
        plt.plot( self.graph_y,self.graph_list,'o', y_new, x_new)
        ax = plt.gca()
        fig = plt.gcf()
        plt.show()

        return training_process

# 에러 계산

    def mse(self):

        xs, ys = self.R.nonzero()
        predicted = self.full_matrix()
        error = 0
        for x,y in zip(xs, ys):
            error += pow(self.R[x,y] - predicted[x,y], 2)
            return np.sqrt(error)

# SGD 작업 진행

    def sgd(self):

        for i, j, r in self.samples:

            prediction = self.get_rating(i,j)
            e = (r-prediction)

            self.b_i[i] += self.alpha * (e - self.beta * self.b_i[i])
            self.b_u[j] += self.alpha * (e - self.beta * self.b_u[j])

            self.P[i, :] += self.alpha * (e * self.Q[j, :] - self.beta * self.P[i, :])
            self.Q[j, :] += self.alpha * (e * self.P[i, :] - self.beta * self.Q[j, :])

    def get_rating(self, i, j):

        prediction = self.b + self.b_i[i] + self.b_u[j] + self.P[i,:].dot(self.Q[j,:].T)
        return prediction

    def full_matrix(self):

        return self.b + self.b_i[:, np.newaxis] + self.b_u[np.newaxis:,] + self.P.dot(self.Q.T)

    def get_movie_SVD(self):

        return self.P

    def get_item_SVD(self):

        return self.Q

    def get_average(self):

        return self.b
