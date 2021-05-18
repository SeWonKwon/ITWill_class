# ■ ( 의사결정트리 실습3) 은행 대출 채무를 불이행 할 것 같은 고객이 누구인지 ?

#1단계: 데이터 수집

credit <- read.csv("credit.csv", header = T, stringsAsFactors = T)
str(credit)


#  데이터 설명 : 독일의 한 신용기관에서 얻은 대출 정보가 들어 있습니다.
#                신용 데이터셋은 1000개의 대출 예시와 대출금액과 대출 신청자의 
#                특성을 나타내는 일련의 수치특징과 명목특징을 포함하고 있습니다.

# 라벨(정답)컬럼: default --> yes : 대출금 상환 안함
#                             no  : 대출금 상환

prop.table( table(credit$default))
# no yes 
#0.7 0.3  대출금을 상환한 고객이 70% 이고 상환 안한 고객이 30% 를 이루고 있습니다.
summary(credit)

# checking_balance 컬럼: 예금 계좌
# saving_balance 컬럼 : 적금 계좌
# amount 컬럼 : 대출금액 ( 250 마르크 ~ 18424 마르크) 100마르크=7만원

unique(credit$checking_balance)

# checking_balance 컬럼을 소개 : unique(credit$checking_balance)


# 예제1. amount 컬럼의 데이터를 히스토그램 그래프로 그리시오 !
#r() #파일선택 4 , 5

# 예제2. amount 컬럼에 대한 통계정보를 확인하시오 !

summary( credit$amount)
# Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
# 250    1366    2320    3271    3972   18424 

# 설명 : 최소 250마르크(철칠백 오십만원) 최대 18424 마르크까지 구성되어 있으며 평균이 3271입니다.

# 은행의 목표 : 과거의 데이터를 분석해 보니 대출금 상환 불이행자가 30% 나 되어서 앞으로는 
# 30% 이내로 떨어뜨리겠금 하는게 은행의 목표라서 거기에 맞는 머신러닝 모델을 생성해야합니다.

# * 데이터가 명목형 데이터인지 수치형 데이터인지 확인

str(credit)
View(credit)

# 설명 : 전부 수치형으로만 되어 있다면 KNN 을 사용하면 되고 전부 명목형 데이터로만 구성되어 있다면
#        naivebayes 를 쓰면 되는데, 섞여 있는 데이터 이므로 decesion tree 를 써서 기계학습을 시키겠습니다.

# * 데이터를 shuffle 시킵니다.

set.seed(659)
credit_shuffle <- credit[sample(nrow(credit)),]
nrow(credit_shuffle)

# * 데이터를 9대 1로 나눕니다. ( 훈련 데이터 : 9, 테스트 데이터 : 1 )

train_num <- 0.9*(nrow(credit_shuffle))
credit_train <- credit_shuffle[1:train_num, ]
credit_test <- credit_shuffle[(train_num+1) : nrow(credit_shuffle),]
nrow(credit)
nrow(credit_train)
nrow(credit_test)

# 3단계 : 

library(C50)
str(credit_train)
ncol(credit_train) # default 값 ( 라벨값) 의 위치를 찾기위해서
# 문법 : credit_model <- C5.0(라벨을 뺀 나머지 데이터, 라벨 컬럼 데이터)
credit_model <- C5.0(credit_train[,-17], credit_train[,17])

#설명: 900개의 데이터로 학습한 모델을 생성했습니다.

# 4단계: 모델 평가
# * 위에서 만든 모델을 이용하여 테스트 데이터 100개를 예측해봅니다.

credit_result <- predict( credit_model, credit_test[,-17])

table(credit_result)
# 설명: 머신러닝이 예측한 결과는 75명이 채무이행을 했고 25명이 채무 불이행 했다고 나옵니다.
#       그렇다면 정답은 어떻게 되었는지 보겠습니다.

table(credit_test[,17])
#no yes 
#65  35

# 설명 : 실제 정답과 예측이 10명의 차이를 보이고 있습니다.
# 설명: table(실제값, 예측값)
table(credit_test[,17],credit_result)

# credit_result no yes
#           no  55  10
#           yes 20  15

# 설명 : 총 100명의 고객들중에서
#       채무 예측: 이행  실제:이행 55--> O 
#       채무 예측: 이행  실제:불이행 20--> x
#       채무 예측: 불이행  실제:이행 10--> x
#       채무 예측: 불이행  실제:불이행 15--> O 
# 채무 이행할거라 예측했는데 채무를 불이행한 고객이 10명이나 되므로 우리는 이 부분을 0 으로 만들수 있도록
# 모델의 성능을 개선을 해야합니다.
library(gmodels)
x <- CrossTable(x= credit_test[,17], y=credit_result)
# 설명: CrossTable(x= 실제, y= 예측측)
print(sum(x$prop.tbl*diag(2)))

# 5단계: 모델 성능 개선

# 의사결정트리의 하이퍼 파라미터를 조정하겠습니다.
#credit_model <- C5.0(credit_train[,-17], credit_train[,17])하이퍼 파라미터가 2개가 있는데

# 1. trials : trials 는 의사결정 나무의 갯수를 결정하는 파라미터
#             최대 0 ~ 100개
# 
# 2. seed 값 : shuffle 할때 섞는 규칙을 결정하는 파라미터 정수형 범위안에 다 줄수 있다.

credit_model2 <- C5.0(credit_train[,-17], credit_train[,17], trials = 100)
credit_result2 <- predict( credit_model2, credit_test[,-17])
x2 <- CrossTable(x= credit_test[,17], y=credit_result2)
# 설명: CrossTable(x= 실제, y= 예측측)
print(sum(x2$prop.tbl*diag(2)))

# 정확도를 90% 이상 올려야 하므로 의사결정트리 말고 다른 알고리즘을 적용해야 합니다. 
# 다른 분류 알고리즘을 사용해야 합니다.

# knn naivebasyes, decesion tree, 신경망, 서포트 벡터 머신, 랜덤 포레스트


#문제212. 은행 채무 불이행자를 예측하는 머신 러닝 모델을 의사결정트리 알고리즘으로 구현했는데
#         엔트로피 지수로 순수도를 계산하고 정보획득량을 계산하는 C50 패키지로 모델을 생성했었습니다.
#         그런데 이번에는 party 패키지 ctree 함수를 이용해서 의사결정 분류 모델을 만들어보는 
#         실험을 하세요 !!


library(party)
credit <- read.csv("credit.csv", header = T, stringsAsFactors = T)

set.seed(590)
credit_shuffle <- credit[sample(nrow(credit)),]
set.seed(590)
ind <- sample(2,nrow(credit),replace=T,prob=c(0.9,0.1)) 

traindata <- credit_shuffle[ind==1,]
testdata <- credit_shuffle[ind==2,]
nrow(traindata)
nrow(testdata)
summary(ind==1)
table(traindata$default)
table(testdata$default)


myformula <- default ~ .
credit_ctree <- ctree(myformula,data=traindata)

table(predict(credit_ctree),traindata$default)

print(credit_ctree)    


plot(credit_ctree)
plot(credit_ctree,type="simple")

testpred <- predict(credit_ctree, newdata=testdata)

table(testpred,testdata$default)

g3<-CrossTable( testdata$default,  testpred ) 


print(g3$prop.tbl)
print(sum(g3$prop.tbl*diag(2)))


# ■ party 패키지 를 이용하여 채무불이행자 예측 알고리즘 구현

# 1. party 패키지를 불러옴
library(party) 
library(gmodels) 

# 2. 데이터를 불러옴
credit <-read.csv("c:\\data\\credit.csv", stringsAsFactors=TRUE)
str(credit)


# 3. 데이터에 대한 정보를 확인
nrow(credit) #1000
ncol(credit) #17
summary(credit)

# ※ 중요 : 데이터의 결측치가 있는지 반드시 확인하세요 ! 
colSums(is.na(credit))
# 결측치가 있따면 결측치를 다른 데이터 로 치환하거나 삭제를 해야 합니다.

# 4. 은행 데이터의 종속변수 컬럼의 종류와 건수를 확인
table(credit$default)


#5. 데이터를 shuffle 시킵니다.

set.seed(659)
credit_shuffle <-  credit[ sample(1000),  ]
nrow(credit_shuffle)

#6. 데이터를 9대 1로 나눕니다. (훈련 데이터: 9, 테스트 데이터 : 1 )

train_num <-   0.9 * 1000
credit_train <- credit_shuffle[ 1:train_num,   ] #1번부터 900번째행까지
credit_test  <- credit_shuffle[ (train_num+1) : nrow(credit_shuffle),   ]
#  901번부터 1000번까지는 테스트 데이터로 구성 

nrow(credit_train)  #900
nrow(credit_test)   #100

# 7. 의사결정트리 모델을 생성
myformula <- default ~ .
credit_ctree <- ctree(myformula, data=credit_train)


# 8. 모델이 예측한 결과를 확인
predict(credit_ctree)

# 9. 예측 결과와 실제 훈련 데이터의 정답과 비교
table(predict(credit_ctree), credit_train$default)

#설명:훈련데이터(70%) 를 가지고 잘 맞췄는지 확인,123개중에 10개 틀렸습니다. 

# 10. 어떠한 질문을 기준으로 나뉘는지 확인 (스므고개 질문들 확인)
print(credit_ctree)
print(credit_ctree, type='simple')

# 11. 테스트 데이터를 예측하고 잘 맞췄는지 확인

test_pred <- predict(credit_ctree, newdata=credit_test)

table(test_pred, credit_test$default)

#설명: 테스트 데이터도 55개중에 9개나 틀렸습니다. 

# 12. 교차검정표와 정확도 계산

g2 <- CrossTable(credit_test$default, test_pred)

#설명:  CrossTable( 테스트 데이터의 진짜 정답, 테스트 데이터를 기계가 예측한 결과)

sum(g2$prop.tbl*diag(2))  

#13. 시각화를 합니다. 

plot(credit_ctree)
plot(credit_ctree, type='simple')

# 설명 : 의사결정 트리 패키지 2가지

# 1. C50 : 엔트로피 지수로 정보획득량을 구해서 의사결정 나무를 구성
#       성능 개선 하이퍼 파리미터: trials 와 seed 값ㅌ
# 2. party : 카이제곱검정으로 정보획득량을 구해서 의사결정나무를 구성
#       성능 개선 하이퍼 파라미터 : seed 값 , ?

#■ 최적의 seed 값을 루프문으로 돌려서 알아내는 방법

library(party)

#2.wine을 데이터를 불러온다.
wine<-read.csv('wine.csv',stringsAsFactors = T)

#3.와인 데이터 라벨 컬럼 종류와 건수를 확인합니다.
#summary(wine$Type)

#4.repeat문 돌려서 seed값찾기

i<-1
repeat { 
  set.seed(i)
  i<-i+1
  ind <- sample(2,nrow(wine),replace=T,prob=c(0.7,0.3)) 
  
  
  #5.ind==1과 ind==2를 이용해서 훈련데이터와 테스트 데이터를 만든다.
  traindata <- wine[ind==1,] #70%의 데이터로 훈련데이터
  testdata <- wine[ind==2,] #30%의 데이터로 테스트데이터
  
  #6.의사결정트리 모델(나무)를 생성한다.
  myformula <- Type ~ .
  
  
  #7. party패키지의 ctree함수를 이용해서 의사결정모델을 생성한다.
  wine_ctree <- ctree(myformula,data=traindata)
  
  #8.예측결과를 확인한다.
  #predict(wine_ctree)
  
  #9.예측결과와 실제 테스트 데이터의 정답과 비교한다.
  #table(predict(wine_ctree),traindata$Type)
  
  
  #12.test데이터를 예측하고 확인한다.
  testpred <- predict(wine_ctree, newdata=testdata)
  library(gmodels)
  g3<-CrossTable(testdata$Type, testpred)
  x<- (g3$prop.tb[1] + g3$prop.tb[5]+g3$prop.tb[9]) 
  
  if(x==1) break 
  print(i) 
  print(x)}
print(i)

# 문제213. (오늘의 마지막 문제) party 패키지를 이용하여 채무불이행자 예측 알고리즘 구현한 코드의 
# seed 값이 무엇인지 출력되게 하시오 !


library(party)
library(gmodels) 
data <- read.csv("credit.csv", header = T, stringsAsFactors = T) # 데이터 불러오기

temp<- c()
temp2 <-c()
i<-0
repeat { 
  i<- i+1
  set.seed(i)
  ind <- sample(2,nrow(dataw),replace=T,prob=c(0.9,0.1)) 
  set.seed(i)
  dataw <- data[sample(nrow(data)),]
  traindata <- dataw[ind==1,]
  testdata <- dataw[ind==2,]
  myformula <- default ~ . 
  dataw_ctree <- ctree(myformula,data=traindata)
  testpred <- predict(dataw_ctree, newdata=testdata)
  g3<-CrossTable( testdata$default,  testpred ) 
  j <- sum(g3$prop.tbl*diag(2)) 
  if(is.na(g3$prop.tb[4])==T) next
  temp <- append( temp,  j)
  temp2 <- append (temp2, i)
  print(c(i,j))
  if(j>=0.88) # 목표 정확도 설정
  {print(c(i,j)) 
    break }
  else if( i==1200) # 목표 정확도에 도달하지 못했다면 최고값
  {result <- data.frame( 'seed'= temp2, '정확도'= temp)
  print(result[result$정확도==max(result$정확도),])
  break}
}



seed    정확도 # set.seed 1번째만 했을때
850  850 0.8529412

seed    정확도 # set. seed 2번째만 했을때
185  185 0.8627451

seed    정확도 # set. seed 를 2개 다 했을 때