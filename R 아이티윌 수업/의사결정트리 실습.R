
#■ 화장품 구매에 영향을 크게 미치는 변수(컬럼) 가 무엇인지 정보획득량을 구하시오 !

skin <- read.csv("skin.csv", header = T, stringsAsFactor = T )
summary(skin)  
View(skin)
nrow(skin)
ncol(skin)
colnames(skin)

#install.packages("FSelector")
library(FSelector)
wg <- information.gain(cupon_react~ ., skin, unit ='log2')
# 설명 : information.gain( 라벨 컬럼 ~ 모든 컬럼, 데이터 프레임명, unit 은 엔트로피 쓸때 쓰는 로그)

wg

#            attr_importance
# cust_no      0.00000000
# gender       0.06798089
# age          0.00000000
# job          0.03600662
# marry        0.18350551
# car          0.02487770
# 설명: 확인해보면 결혼유무가 가장 정보획득량이 높은것으로 확인이 됩니다.

# 문제198 지방간을 일으키는 원인중에  가장 큰 영향력을 보이는 요인은 무엇인지
# 정보획득량을 구해서 알아내시오 !

fat <- read.csv("fatliver2.csv", header = T, stringsAsFactors = T)
View(fat)
summary(fat)
nrow(fat)
library(FSelector)

wg <- information.gain(FATLIVER ~ . , fat, unit ='log2')
wg



# 1. 의사결정 패키지인 C50 패키지를 설치한다.

install.packages("C50")
library(C50)

#※ 의사결정 나무 알고리즘 4가지
#1. CART : 나무의 분리기준은 지니지수
#2. C4.5 와 C5.0 : 나무의 분리기준이 엔트로피 지수
#3. CHAID : 나무의 분리기준이 카이제곱 통계량과 F검정
#4. QUEST : 나무의 분리기준이 카이제곱 통계량과 F검정

# 2. 백화점 화장품 고객 데이터를 로드하고 shuffle 한다.

skin <- read.csv("skin.csv", header=T ,stringsAsFactors = TRUE)
nrow(skin)
summary(skin)

skin_real_test_cust <- skin[30,  ] # 테스용으로 따로 분리한다. 
skin2 <-  skin[ 1:29, ] # 29개의 데이터로 학습 시켜서 의사결정나무를 생성한다.
nrow(skin2)

skin_real_test_cust

# cust_no gender age job marry car cupon_react

# 30      30 female  40 YES   YES  NO         YES

skin2 <- skin2[ , -1] # 고객번호를 제외시킨다. 
skin2
set.seed(10)
skin2_shuffle <- skin2[sample(nrow(skin2)),    ]  # shuffle 시킴 

# 3. 화장품 고객 데이터를 7대 3로 train 과 test 로 나눈다.

table(skin2_shuffle$cupon_react)
table(skin2_test$cupon_react)

train_num <-  round(0.7 * nrow(skin2_shuffle), 0) 

skin2_train <- skin2_shuffle[1:train_num,  ]  
skin2_test  <- skin2_shuffle[(train_num+1) : nrow(skin2_shuffle), ] 
nrow(skin2_train)  # 20
nrow(skin2_test)   #  9 
skin2_train
#4. C50 패키지를 이용해서 분류 모델을 생성한다. 
  
library(C50)

skin_model <- C5.0(skin2_train[  , -6],  skin2_train$cupon_react )  
#                        ↑                        ↑
#             라벨을 뺀 train 전체 data    train 데이터의 라벨 
skin_model

#Classification Tree
#Number of samples: 20 
#Number of predictors: 5 

#5. 위에서 만든 skin_model 를 이용해서 테스테 데이터의 라벨을 예측하시오!

  skin2_result  <- predict( skin_model , skin2_test[  , -6])
#                                                 ↑
#                                     라벨을 뺀 테스트 데이터 전체 
skin2_result
#6. 이원 교차표로 결과를 확인하시오 !
  
  library(gmodels)

g3 <- CrossTable( skin2_test[  , 6],  skin2_result ) 
g3$prop.tbl



#문제199. 위의 의사결정트리의 성능을 높이시오 !

#naiveBayes 일때 하이퍼 파라미터는 ? laplace 값, seed 값
#knn 일때의 하이퍼 파라미터는 ? k 값, seed값
#decision tree 일때 하이퍼 파라미터는 ? trials 값 , seed값 

#trials 파라미터로 나무의 갯수를 정한다. 여러개의 나무를 만들어서
#그 나무들중에서 가장 분류를 잘하는 나무를 투표를 통해서 선택을 합니다. 

skin <- read.csv("skin.csv", header=T ,stringsAsFactors = TRUE)

skin_real_test_cust <- skin[30,  ]  # 테스트용으로 따로 분리한다. 
skin2 <-  skin[ 1:30, ]  # 29개의 데이터로 학습 시켜서 의사결정나무를 생성한다. 
skin2 <- skin2[ , -1] # 고객번호를 제외시킨다. 

for ( i in 101:101 ) {
set.seed(i)
skin2_shuffle <- skin2[sample(nrow(skin2)),    ]  # shuffle 시킴 
train_num <-  round(0.8 * nrow(skin2_shuffle), 0) 
skin2_train <- skin2_shuffle[1:train_num,  ]  
skin2_test  <- skin2_shuffle[(train_num+1) : nrow(skin2_shuffle), ] 

nrow(skin2_train)  # 20  훈련데이터는 20개이고 
nrow(skin2_test)   #  9   테스트 데이터는 9개이다. 

library(C50)
skin_model2 <- C5.0(skin2_train[  , -6],  skin2_train$cupon_react , trials=10)  

skin_result2  <- predict( skin_model2 , skin2_test[  , -6])

library(gmodels)
g3<-CrossTable( skin2_test[  , 6],  skin_result2 ) 
  
print(i)  
print(g3$prop.tbl)
print( g3$prop.tb[1] + g3$prop.tb[4] )
}



skin <- read.csv("skin.csv", header=T ,stringsAsFactors = TRUE)

skin_real_test_cust <- skin[30,  ]  # 테스트용으로 따로 분리한다. 
skin2 <-  skin[ 1:29, ]  # 29개의 데이터로 학습 시켜서 의사결정나무를 생성한다. 
skin2 <- skin2[ , -1] # 고객번호를 제외시킨다. 

set.seed(101)
skin2_shuffle <- skin2[sample(nrow(skin2)),    ]  # shuffle 시킴 
train_num <-  round(0.7 * nrow(skin2_shuffle), 0) 
skin2_train <- skin2_shuffle[1:train_num,  ]  
skin2_test  <- skin2_shuffle[(train_num+1) : nrow(skin2_shuffle), ] 

nrow(skin2_train)  # 20  훈련데이터는 20개이고 
nrow(skin2_test)   #  9   테스트 데이터는 9개이다. 

library(C50)
skin_model2 <- C5.0(skin2_train[  , -6],  skin2_train$cupon_react , trials=10)  

skin_result2  <- predict( skin_model2 , skin2_test[  , -6])

library(gmodels)
CrossTable( skin2_test[  , 6],  skin_result2 ) 

#■ 아이리스 데이터를 가지고 의사결정트리 실습

#C50 패키지 말고 ctree 함수를 사용할 수 있는 party 패키지를 설치하고
#의사결정트리 테스트를 해보겠습니다.
# 이실습은 빅데이터 기사 시험책의 3-44 페이지의 내용을 좀더 보강한 
# 내용입니다.

#1. party 패키지를 설치합니다.
#install.packages("party")
library(party)
data(iris) # 데이터 불러오기
# iris 데이타 파악하기
summary(iris)
nrow(iris)
colnames(iris)
table(iris$Species)

#6. sample 사용해서 shuffle 도 하면서 데이터를 7대 3으로 나눕니다.
#   replace=T 를 사용해서 복원 추출합니다.
set.seed(11)
ind <- sample(2,nrow(iris),replace=T,prob=c(0.7,0.3)) 
# ※ 설명: 숫자 2 는 2개로 데이터를 나누겠다.
#          nrow(iris) 로 전체 행수를 적어줍니다.
#            replace= T 로 복원 추출
#          prob=c(0.7,0.3) 으로 7대 3으로 나누겠다고 지정합니다.

traindata <- iris[ind==1,]
testdata <- iris[ind==2,]
nrow(traindata)
nrow(testdata)
summary(ind==1)
table(traindata$Species)
table(testdata$Species)
#8. 의사결정트리 모델(나무)을 생성합니다.

myformula <- Species ~ Sepal.Length + Sepal.Width + Petal.Length + Petal.Width
또는 
#myformula <- Species ~ . 
iris_ctree <- ctree(myformula,data=traindata)
#설명: party 패키지의 ctree 함수를 이용해서 의사결정 모델을 생성합니다.
table(predict(iris_ctree),traindata$Species)

#설명: 훈련데이터 120개를 가지고 예측한 결과를 보니 120개중 6개 틀리고
#다 맞췄습니다. 우리가 knn 과 나이브 베이즈 실습 할때는 모델 생성한 후에 
#그 모델로 테스트 데이터를 잘 맞추는지 확인을 했었는데 지금 이실습은
#훈련 데이터 부터 먼저 확인을 하고 있습니다. 지금 만든 의사결정트리 모델이
#훈련 데이터를 잘 분류하는 모델인지를 먼저 확인하고 있습니다.

print(iris_ctree)    

#12. 아리스 데이터의 의사결정 트리 모델을 시각화 합니다.
plot(iris_ctree)
plot(iris_ctree,type="simple")

testpred <- predict(iris_ctree, newdata=testdata)

table(testpred,testdata$Species)

g3<-CrossTable( testdata$Species,  testpred ) 


print(g3$prop.tbl)
print( g3$prop.tb[1] + g3$prop.tb[5] + g3$prop.tb[9] )

#문제200. (오늘의 마지막 문제) 어제 사용했던 와인 데이터를 분류하는 의사결정트리
#모델을 생성하는 실험을 하시오. 

# 데이터 : wine.csv
# 의사결정트리 패키지 : party 패키지의 ctree 함수를 이용하세요 ~
#코드를 올리고 이원 교차표를 올리세요 ~

library(party)
dataw <- read.csv("wine.csv", header = T, stringsAsFactors = T) # 데이터 불러오기
#데이타 파악하기
summary(dataw)
nrow(dataw)
colnames(dataw)
table(dataw$Type)

set.seed(828)
ind <- sample(2,nrow(dataw),replace=T,prob=c(0.7,0.3)) 

traindata <- dataw[ind==1,]
testdata <- dataw[ind==2,]
nrow(traindata)
nrow(testdata)
summary(ind==1)
table(traindata$Type)
table(testdata$Type)
#8. 의사결정트리 모델(나무)을 생성합니다.

#myformula <- Species ~ Sepal.Length + Sepal.Width + Petal.Length + Petal.Width
또는 
myformula <- Type ~ . 
dataw_ctree <- ctree(myformula,data=traindata)
#설명: party 패키지의 ctree 함수를 이용해서 의사결정 모델을 생성합니다.
table(predict(dataw_ctree),traindata$Type)

#설명: 훈련데이터 120개를 가지고 예측한 결과를 보니 120개중 6개 틀리고
#다 맞췄습니다. 우리가 knn 과 나이브 베이즈 실습 할때는 모델 생성한 후에 
#그 모델로 테스트 데이터를 잘 맞추는지 확인을 했었는데 지금 이실습은
#훈련 데이터 부터 먼저 확인을 하고 있습니다. 지금 만든 의사결정트리 모델이
#훈련 데이터를 잘 분류하는 모델인지를 먼저 확인하고 있습니다.

print(dataw_ctree)    

#12. 아리스 데이터의 의사결정 트리 모델을 시각화 합니다.
plot(dataw_ctree)
plot(dataw_ctree,type="simple")

testpred <- predict(dataw_ctree, newdata=testdata)

table(testpred,testdata$Type)

g3<-CrossTable( testdata$Type,  testpred ) 


print(g3$prop.tbl)
print( g3$prop.tb[1] + g3$prop.tb[5] + g3$prop.tb[9] )


#%% 성능 높이기 포문으로 seed 값 찾기

library(party)
dataw <- read.csv("wine.csv", header = T, stringsAsFactors = T) # 데이터 불러오기

temp <- c()
temp2 <-c()

for ( i in 1:1000 ) { 
  set.seed(i)
  ind <- sample(2,nrow(dataw),replace=T,prob=c(0.7,0.3)) 
  
  traindata <- dataw[ind==1,]
  testdata <- dataw[ind==2,]
  myformula <- Type ~ . 
  dataw_ctree <- ctree(myformula,data=traindata)
  testpred <- predict(dataw_ctree, newdata=testdata)
  g3<-CrossTable( testdata$Type,  testpred ) 
  j <- g3$prop.tb[1] + g3$prop.tb[5] + g3$prop.tb[9] 
  temp <- append( temp,  j)
  temp2 <- append (temp2, i)
}

result <- data.frame( 'seed'= temp2, '정확도'= temp)
result[result$정확도==max(result$정확도),]








