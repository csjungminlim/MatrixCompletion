# -*- Coding: UTF-8 -*-

import re

def ReadData():
    fh = open("Example.txt")
    movie_list = []
    x = 1
    for line in fh:
        if line[1] == ":":
            my_dict = {"MovieID" : line[0]}
            movie_list.append(my_dict)
                                                # my_dict = {MovieID : Value, {PersonID1 : Value, Rating: Value, Date, Value} , {...}}
        else:
            ID_line = line.partition(",")
            Date_line = ID_line[2].partition(",")
            ID_dict = {"PersonID" : ID_line[0], "Rating" : Date_line[0], "Date" : Date_line[2]}
            movie_list.append(ID_dict)





if __name__ == '__main__':
    ReadData()