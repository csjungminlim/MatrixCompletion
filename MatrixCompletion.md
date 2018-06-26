# Matrix Completion for the Netflix Data Set

### 프로젝트 목표:

​	Netflix db 를 자료로 해서 영화 평점 Predictor Algorithm 을 구현하면서 Matrix Completion Algorithm

​	에 대해서 이해하고 코딩하기.



### 바탕:

​	2009 년에 Netflix 라는 미국 소재의 드라마 및 영화 스트리밍 기업은 방대한 양의 데이터를 제공하면서 

​	본인들의 Predictor Algorithm 보다 10% 향상된 성능의 알고리즘을 개발하는 팀에게 100만 달러를 상금

​	으로 약속하였다. 이 Predictor Algorithm 의 목표는 특정 유저가 몇몇의 영화에대한 평점을 분석하여 그 유저

​	들이다른 영화에 매긴 평점을 예측하는 것이다. 



### Matrix Completion 의 기본:

​	Matrix Completion 은 Big Data Optimization 의 한 종류이다. 기본적으로 각 항목 (Netflix 의 경우 소비자 

​	항목, 영화 항목) 을 각각 행과 열로 분류한후, 그 행과 열에 해당하는 자리에 데이터값을 넣는다. 

​	예) "지민" 이 "Inception" 이라는 영화에 대해서 4점 이라는 평점을 매기면 "지민" 에 해당되는 행에서 

​	"Inception" 이라는 열을 찾아서 그 자리에 "4" 를 넣는다. 

​	

​	주어진 모든 데이터를 이와 같이 채운후에 Data Optimization 이 진행된다. 



## 프로그램 구성

### .txt 파일에서 parsing 으로 데이터 수집

​	Netflix 에서 제공된 데이타는 .txt 파일로 정리되어있다.  형태는 

​		MOVIEID1:

​		CUSTOMERID1, RATING, DATE-OF-RATING 

​		CUSTOMERIDX, RATING, DATE-OF-RATING

​		...

​		MOVIEID2:

​		CUSTOMERID1, RATING, DATE-OF-RATING

​		CUSTOMERIDX, RATING, DATE-OF-RATING

​		... 

​	식 으로 되어있다.



​	1) 모든 데이터를 영화별로 분류. 

​		예) 영화 한개당 한개의 리스트를 생성. 영화 ID 는 순차적으로 나열되있으므로 마지막 CUSTOMERID 

​		      에서 새로운 리스트 생성.



​	2) 모든 데이터를 사람별로 분류.

​		예) CUSTOMER ID 당 한개의 리스트를 생성. 순차적으로 나열되있지 않으므로 이미 ID 에 해당하는 

​		      리스트가 있는지 확인해야함. 있다면 그 리스트에 append, 없으면 새로운 리스트 생성.

​	

