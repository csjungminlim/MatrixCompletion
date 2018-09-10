# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import surprise
import time

from surprise.model_selection import train_test_split
from surprise import SVD
from surprise import accuracy

def readFile(path):

    data_file = open(path)
    return data_file

def makeCustomDataFile(data_file):

    # combined_data_1.txt에는 4499개의 movieID가 저장되어있음.
    custom_data_file = open("/Users/limjungmin/Netflix_Recommender/u.data", 'w')

    #cnt = 0 : 디버깅용 Count 계수
    for line in data_file:

        if ":" in line:
            movieID = line.split(":")[0]
            #print(movieID)
            #cnt+=1
        else :

            info = line.split(",")

            userID = info[0]
            rating = info[1]
            date = info[2].split('\n')[0]

            str = userID + ";" + movieID + ";" + rating + "\r\n"
            custom_data_file.write(str)

            #if cnt > 50 : break

    print("make Custom Data File Done")

    reader = surprise.Reader(line_format='user item rating', sep=';')
    data = surprise.Dataset.load_from_file('/Users/limjungmin/Netflix_Recommender/u.data', reader=reader)
    df = pd.DataFrame(data.raw_ratings, columns=["user", "item", "rate", "id"])
    del df["id"]

    print(df.head(10))

    return data

def train_custom_data_file(data, algo):

    trainset, testset = train_test_split(data, test_size=.25)

    algo.fit(trainset)

    predictions = algo.test(testset)

    return predictions

def get_accuracy(predictions):

    return accuracy.rmse(predictions)

if __name__ == '__main__':

    # 1. 데이터 파일 읽어오기
    start_time = time.time()
    data_file = readFile("/Users/limjungmin/Netflix_Recommender/netflix-prize-data/combined_data_1.txt")
    run_time = time.time() - start_time
    print ( " Run time for readFile : %.4f (sec)" % (run_time) )


    # 2. Surprise  패키지에 활용할 수 있도록 데이터 전처리
    start_time = time.time()
    custom_data_file = makeCustomDataFile(data_file)
    run_time = time.time() - start_time
    print ( " Run time for makeCustomDataFile : %.4f (sec)" % (run_time) )


    # 3. 사용할 알고리즘(SVD)를 통한 학습 진행
    start_time = time.time()
    predictions = train_custom_data_file(custom_data_file, algo = SVD())
    run_time = time.time() - start_time
    print ( " Run time for train_custom_data_file : %.4f (sec)" % (run_time) )

    # 4. 예측 결과를 가지고 RMSE 측정값 구하기
    get_accuracy(predictions)
