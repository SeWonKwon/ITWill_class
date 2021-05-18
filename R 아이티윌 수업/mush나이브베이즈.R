# 1. 버섯 데이터를 R 로 로드한다. 

mushroom <- read.csv("mushrooms.csv", header=T, stringsAsFactors=TRUE)
View(mushroom)
summary(mushroom)
str(mushroom) # Factor 인지 확인
# 맨 앞에 있는 Type 이 라벨입니다.
unique(mushroom$type)


# 설명 : stringsAsFactors=TRUE 로 설정해서 문자형 데이터를 전부 factor로 변환 
        # 데이터를 살펴보니 전부 문자형 데이터여서 knn 알고리즘으로 분류를 할수 없고 
        # 나이브 베이즈 알고리즘으로 분류를 해야합니다.

# 독버섯과 정상버섯의 비율이 어떻게 되는지 확인하시오!
table(mushroom$type)

# r()

prop.table(table(mushroom$type))
# edible poisonous 
# 0.5179714 0.4820286

# 두개가 딱 절반이어서 독버섯도 잘 학습할 수있고 정상 버섯도 잘 할습할수 있게
# 되어있습니다. 위의 라벨 컬럼의 비율을 확인하는게 중요한게 비율이 위와같이 
# 균등해야 오버피팅이 발생할 가능성이 많이 줄어듭니다.

# 2. 8124 독버섯 데이터만 따로 빼서 mush_test.csv 로 저장한다. 

mush_test <- mushroom[8123, ]
mush_test 
write.csv( mush_test, "mush_test.csv",row.names=FALSE )

#설명: write.csv 로 mush_test 데이터를 mush_test.csv 로 저장합니다.


#3. 8123 독버섯 데이터를 훈련 데이터에서 제외 시키시오 !
nrow(mushroom)
mushrooms <- mushroom[ -8123,  ] 
nrow(mushrooms)

# 이 데이터를 따로 뺀 이유는 나중에 학습을 다 시키고 
# 만든 모델이 이 데이터가 독버섯인지 정상버섯인지 잘 맞추는지
# 확인하려고 한건만 따로 분리했습니다.

#4. mushrooms 데이터를 훈련 데이터와 테스트 데이터로 나눈다 

#( 훈련 데이터는 75%,  테스트 데이터는 25% )
set.seed(6)

dim(mushrooms) # 몇 차원인지 알려줌
# 8123 열과 23개의 행
dim(mushrooms)[1]
dim(mushrooms)[2]
train_cnt <- round( 0.75*dim(mushrooms)[1] )
train_cnt 
train_index <- sample( 1:dim(mushrooms)[1], train_cnt, replace=F)
# replace=F 비복원 추출, 1: dim 사이의 숫자 중에서 train_cnt 만큼 추출

train_index
mushrooms_train <- mushrooms[ train_index,  ]
mushrooms_test <- mushrooms[- train_index,  ] 

nrow(mushrooms_train)  #  6092
nrow(mushrooms_test)    #  2031 
str(mushrooms_train)

#5. 나이브 베이즈 알고리즘으로 독버섯과 일반 버섯을 분류하는 모델을 생성한다.
#install.packages("e1071")
library(e1071)         #모든 컬럼들

                          #↓

model1 <- naiveBayes(type~ . ,  data=mushrooms_train)

                      #↑

                 #라벨 컬럼명 

# type~ 를 빼고 모든 컬럼들을 이용한 모델을 만들어라.
# 설명: naiveBayes(정답컬럼~모든컬럼들, data=훈련 데이터 프레임명)
model1 # 버섯데이터로 빈도표를 만들고 그 빈도표로 우도표를 생성한것임


#6. 위에서 만든 모델과 테스트 데이터를 가지고 독버섯과 일반버섯을 잘 분류하는지 예측해 본다.

result1 <- predict( model1, mushrooms_test[  , -1] )
result1 
#결과를 뺀 모델 mushrooms_test[  , -1] 1번째 컬럼은 제외 하고 !( 왜냐? 정답 컬럼이니까)

length(result1)
#7. 이원 교차표를 그려서 최종 분류 결과를 확인한다. 
library(gmodels)



g2 <- CrossTable( mushrooms_test[  ,1], result1) 
                        #↑                ↑
#                     실제              예측 
g2$prop.tbl
print( g2$prop.tb[1] + g2$prop.tb[4] )  # 정확도

#8. 위의 모델의 성능을 올리시오 ! 라플라스로 성능올리기기

model2 <- naiveBayes(type~ . ,  data=mushrooms_train, laplace=0.000001)
result2 <- predict( model2, mushrooms_test[ , -1] )
g3 <- CrossTable( mushrooms_test[ ,1], result2) 
mushrooms_test[ ,1]
g3$prop.tbl
print( g3$prop.tb[1] + g3$prop.tb[4] )  # 정확도

#|
  
#  위의 모델에  별도로 구분해 놓은 테스트 데이터 한개(독버섯) 8123 번 데이터를 넣어서 독버섯인지 정상인지 확인하시오 ! 
  
  
mush_test2 <- read.csv("mush_test.csv", stringsAsFactors = TRUE)
result3 <- predict( model2, mush_test2[ ,-1] )
mush_test2[ ,1]==result3

