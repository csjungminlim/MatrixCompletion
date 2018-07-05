# -*- coding: utf-8 -*-
import openpyxl
import requests
import json


def read_data():                         # .txt 파일에서 데이터 파싱을 진행; Movie ID 와 User ID 별로 분류

    fh = open('combined_data_1.txt')     # 파일 오픈
    movie_dict = {}                      # 영화를 사요자별로 구분한 dict
    movieID = []                         # 각 텍스트 줄의 정보를 dict 에 임시적으로 저장 (다음 루프때 갱신)
    counter = 0                          # 영화 한개당 사용자의 수; 영화 갱신시 초기화
    movie_data_list = []
    number_of_entries = 0
    average_dict = {}
    for line in fh:     # 라인별로 루프
        if not line.strip():             # 빈줄 제거
            continue
        if ":" in line:
            movie_list = []
            total_sum = 0
            number_of_entries = 0
            counter = 0             # 카운터 초기화
            length = line.__len__() -2
            movieID = line[:length].rstrip()            # 영화 번호만 슬라이싱
            print movieID                # 디버깅용 프린트

        else:
            counter += 1
            number_of_entries += 1
            userid = line.partition(",")        # 자료 나누기 (인덱싱을 하기위하여)
            date = userid[2].partition(",")
            movie_data_dict = {"UserID" : userid[0], "Rating" : date[0], "Date" : date[2]}
            total_sum = eval(movie_data_dict['Rating']) + total_sum
            average = float(total_sum) / number_of_entries
            average_dict[movieID] = average
            movie_list.append(movie_data_dict)
            movie_dict[movieID] = movie_list     # 영화에 해당하는 자료를 그 영화 키에 맞춰서 생성
            print movieID
    print average_dict
    print 'complete'
    # 영화별 분류 종료; 유저별 분류 시작

#    id_dict = {}  # movie_dict 의 유저 버전. 아이디 번호가 key, 영화가 value 이다
#    mult_id_list = []
#    sing_id_list = []
#    y = 1
#    x = 1
#    print movie_dict["MovieID" + str(x) + " - " + str(y)]['UserID']

#    print movie_data_list.count(movie_data_list[1])
#    print movie_data_list

#    for x in movie_data_list:
#        if movie_data_list.count(x) > 1:
#            if x not in mult_id_list:
#                mult_id_list.append(x)
#        if movie_data_list.count(x) == 1:
#            if x not in sing_id_list:
#                sing_id_list.append(x)

#    print "The multiple id list is " + str(mult_id_list)
#    print "The short id list is" + str(sing_id_list)
#    i = 1

#    for key, value in movie_dict.iteritems():
#        for item in sing_id_list:
#            if value["UserID"] == item:
#                id_dict[item] = ({"MovieID" : key, "Rating" : value['Rating'], "Date" : value['Date']})

#    for item in mult_id_list:
#        for key, value in movie_dict.iteritems():
#            if value["UserID"] == item:
#                id_dict[item + "-" + str(i)] = ({"MovieID": key, "Rating": value['Rating'], "Date": value['Date']})
#                i += 1
#        i = 1
#    print id_dict
    #                                                           중요한 데이터는 id_dict, movie_dict 에 저장

    userID = raw_input("Please enter the userID to look up: \n")
    index = 0
    user_dict = {}
    user_list = []
    for key, value in movie_dict.iteritems():
        index += 1
        for x in value:
            if userID == x["UserID"]:
                print 'yes'
                user_list.append(key)
                user_dict[userID] = user_list
                print user_dict


#def get_movie_api(movie_dict):
#    excel_file = openpyxl.load_workbook("sampleData.xlsx")
#    movie_list = []
#    sheet = excel_file['Sheet1']
#    cell_range = sheet['C1':'C17700']
#    date_range = sheet['B1':'B17700']
#    excel_dict = {}
#    for x in range(1,17700):
#        excel_dict[sheet['A'+ str(x)]] = sheet['C' + str(x)]   # Excel_dict 의 key 는 영화 아이디, value 는 영화 제목
    counter = 0
    movie_info = {}
    excel_file = openpyxl.load_workbook("sampleData.xlsx")          #6485
    sheet = excel_file['Sheet1']
    for x in user_dict[userID]:
        if eval(x) > 6485:
            x -= 1

        plusincluded = sheet['C' + str(x)].value
        if " " in plusincluded:
            plusincluded = plusincluded.replace(' ', '+')
        print str(plusincluded)
        movie_info[x] = {}
        url = 'https://api.themoviedb.org/3/search/movie?api_key=5f2f74c5dad2ce53ec50300cf1633a34&query=' + str(plusincluded)
        r = requests.get(url)

        genre_dict = {'28': 'Action', '12': 'Adventure', '16': 'Animation', '35': 'Comedy', '80': 'Crime',
                      '99': 'Documentary', '18': 'Drama', '10751': 'Family', '14': 'Fantasy', '36': 'History',
                      '27': 'Horror', '10402': 'Music', '9648': 'Mystery', '10749': 'Romance', '878': 'ScienceFiction',
                      '10770': 'TV Movie', '53': 'Thriller', '10752': 'War', '37': 'Western'}

            # genre_dict 는 api 에서 지칭한 장르별 ID 를 각 장르의 실제 이름으로 변환한 Dictionary 다.

        try:
            genre = r.json()['results'][0]["genre_ids"]
            genre = str(genre[0])
            genre = genre_dict[genre]
            movie_info[x]['genre'] = str(genre)
        except:
            movie_info[x]['genre'] = 'N/A'
            pass

        try:
            id = r.json()['results'][0]['id']
        except:
            pass
        urlb = 'https://api.themoviedb.org/3/movie/' + str(id) + '/credits?api_key=5f2f74c5dad2ce53ec50300cf1633a34'
        r = requests.get(urlb)

        try:
            movie_info[x]['Actor1'] = str(r.json()['cast'][0]['name'])
        except:
            movie_info[x]['Actor1'] = 'N/A'
            pass

        try:
            movie_info[x]['Actor2'] = str(r.json()['cast'][1]['name'])
        except:
            movie_info[x]['Actor2'] = 'N/A'
            pass

        try:
            movie_info[x]['Director'] = str(r.json()['crew'][0]['name'])
        except:
            movie_info[x]['Director'] = 'N/A'
            pass

        print "-------------------New-Movie------------------------"
        print movie_info
        i = 0
        print 'done'

        print movie_info

    actorList = []
    directorList = []
    genreList = []
    for keys, values in movie_info.iteritems():
        actorList.append(values['Actor1'])
        actorList.append(values['Actor2'])
        directorList.append(values['Director'])
        genreList.append(values['genre'])

    for actor in actorList:
        if actorList.count(actor) > 1:
            x = actorList.count(actor)
            print "The actor " + str(actor) + "appears " + str(x) + " times \n"
            for keys, values in movie_info.iteritems():
                if values["Actor1"] == actor:
                    print "The actor " + actor + "appears in the movie " + keys
                if values["Actor2"] == actor:
                    print "The actor " + actor + "appears in the movie " + keys
    print actorList
    print directorList
    print genreList

    
if __name__ == '__main__':

    read_data()
