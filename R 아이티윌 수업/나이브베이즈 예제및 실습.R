# 영화 선호 장르
movie <- read.csv("movie.csv", header = T, stringsAsFactors = TRUE)
# 설명 : stringsAsFactor= TRUE 를 써서 문자형 데이터를 팩터로 변환해야 
# 머신러닝이 학습을 할 수 있는 데이터가 됩니다.
nrow(movie)
 

 #2. 한글명인 컬럼을 영어로 변환합니다.
 
colnames(movie) <- c("age","gender","job","marry","freind", "m_type")
View(movie)

# 3. 39개의 행 밖에 안되므로 38개의 데이터로 학습을 시키고 39번째 하나로 테스트합니다.
train_data <- movie[1:38, ]
test_data <- movie[39,]
View(test_data)

#4. 훈련 데이터를 가지고 나이브 베이즈 모델을 생성합니다.

library(e1071)
View( train_data[ ,1:5])
# 훈련 데이터의 첫번째 컬럼부터 5번째 컬럼까지의 데이터만 학습시킵니다.
# 6번째 컬럼이 정답인데 정답은 따로 제공합니다.

model2 <- naiveBayes( train_data[ , 1:5], train_data$m_type, laplace=0)
# 설명: naiveBayes( 정답 없는 훈련 데이터, 정답, 라플라스 값)

model2 

#5. 테스트 데이터 test_data 를 가지고 예측을 해봅니다.
result2 <- predict(model2, test_data[,1:5])
result2==test_data[,6]

test_data2 <- data.frame(age='20대', gender='여', job='IT' , marry='NO' , freind='NO')
test_data2

result3 <- predict(model2, test_data2)
result3

#■ 나이브 베이즈 실습 3번째 (독감 환자인지 아닌지 분류)

#1. flu.csv 를 R로 로드하시오 !

flu <- read.csv("flu.csv", header = T, stringsAsFactors = TRUE)
View(flu)

# 데이터 설명: patient_id : 환자 번호
#              chills : 오한
#              runny_nose : 콧물
#              headache : 두통
#              fever : 열
#              flue : 독감환자 여부 ( 정답 라벨 컬럼)


train_data <- flu[1:7,]
test_data <- flu[8,]
View(train_data)

library(e1071)
View( train_data[ ,2:5])

model2 <- naiveBayes( train_data[ , 2:5], train_data$flue, laplace=0)

model2 
result3 <- predict(model2, test_data[,2:5])
result3
test_data[,6]==result3


1test_data2 <- data.frame(patient_id='',chills='', runny_nose='', headache='', fever='' )
test_data2

result3 <- predict(model2, test_data2)
result3


naive_func <- function() {  library(e1071)
  flu <- read.csv("flu.csv", header = T, stringsAsFactors = TRUE)
  train_data <- flu[1:8,]
  v_chills <- readline('오한이 있나요? (Y/N)')
  v_runny <- readline('콧물이 있나요? (Y/N)')
  v_headache <- readline('두통이 있나요? (STRONG/MILD/NO)')
  v_fever <- readline('열이 있나요? (Y/N)')
  
  test_data <- data.frame(chills=v_chills, runny_nose=v_runny, 
                          headache=v_headache, fever=v_fever )
  
  model2 <- naiveBayes( train_data[ , 2:5], train_data$flue, laplace=0)
  result3 <- predict(model2, test_data[,1:4])
  if (result3=='Y') {print('독감 환자 입니다.')}
  else              {print('독감환자가 아닙니다.')}
                          }
naive_func()

#문제197. (점심시간 문제) 영화 장르를 예측하는 나이브 베이즈 모델을 이용해서 아래와 같이 질문을 하고 결과를 출력하는 movie_fun 함수를 생성하시오 !


movie_fun <- function() { 
  library(e1071)
  movie <- read.csv("movie.csv", header = T, stringsAsFactors = TRUE)
  colnames(movie) <- c("age","gender","job","marry","freind", "m_type")
  movie$age <- factor(trimws(movie$age),
                      levels =c("10대","20대","30대","40대"),
                      labels = c("10대","20대","30대","40대") )
  v_age <- readline('성별을 입력하세요 (여/남) :')
  v_gender  <- readline('나이대를 입력하세요 (20대/30대/40대) :')
  v_job <- readline('직업을 입력하세요 (IT/디자이너/무직/언론/영업/자영업/학생/홍보마케팅) :')
  v_marry  <- readline('결혼 여부를 입력하세요 (YES/NO) : ')
  v_freind  <- readline('이성친구 여부를 입력하세요 (YES/NO) :' )
  
  train_data <- movie[1:39, ]
  test_data <- data.frame(age=v_age, gender=v_gender, job=v_job, marry=v_marry, freind=v_freind)
  
  model2 <- naiveBayes( train_data[ , 1:5], train_data$m_type, laplace=0)
  result2 <- predict(model2, test_data[,1:5])
  print( result2)
}

movie_fun()

movie <- read.csv("movie.csv", header = T, stringsAsFactors = TRUE)

summary(movie)
movie$age
unique(movie$age)
movie$job
unique(movie$job)
movie <- read.csv("movie.csv", header = T, stringsAsFactors = TRUE)
colnames(movie) <- c("age","gender","job","marry","freind", "m_type")
movie$age <- trimws(movie$age)
summary(movie)
movie$age <- trimws(movie$age)
movie$age <- factor(trimws(movie$age),
                    levels =c("10대","20대","30대","40대"),
                    labels = c("10대","20대","30대","40대") )
str(movie$age)

