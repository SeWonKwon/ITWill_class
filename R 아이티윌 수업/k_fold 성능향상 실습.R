■  k-foldout 실습

실습1_설명: 

이 실습의 목적은 k-foldout 을 통해서 의사결정트리 C50 패키지의 최적의
하이퍼파라미터를 테스트 하기 전에 알아내겠다는게 목적입니다. 
이 실습에서는 독일 은행 데이터 1000개를 다 사용해서 k-holdout 테스트를
진행합니다.

# setwd("d:\\data")
# install.packages("caret")

library(caret)
credit <- read.csv("credit.csv") # 독일 은행의 채무 불이행자를 예측
nrow(credit)
str(credit$default)
str(credit)

# 10-fold CV 
folds <- createFolds(credit$default, k = 10)
str(folds) #설명: 전체 10폴드 교차검증을 수행하기 위해 샘플링 된 인덱스가 생성됨

credit01_test <- credit[folds$Fold01, ] 
credit01_train <- credit[-folds$Fold01, ]
nrow(credit01_test ) # 100
nrow(credit01_train) # 900

#전체 10폴드 교차검증을 수행하려면 이 단계는 10회 반복되어야한다.

## Automating 10-fold CV for a C5.0 Decision Tree using lapply() ---- l
# install.packages("irr")
library(caret)
library(C50)
library(irr)
credit <- read.csv("credit.csv", stringsAsFactors = TRUE)

set.seed(123)

folds <- createFolds(credit$default, k = 10)

cv_results <- sapply(folds, function(x) {
  credit_train <- credit[-x, ]
  credit_test <- credit[x, ]
  credit_model <- C5.0(default ~ ., data = credit_train)
  credit_pred <- predict(credit_model, credit_test)
  credit_actual <- credit_test$default
  kappa <- kappa2(data.frame(credit_actual, credit_pred))$value
  return(kappa) })

str(cv_results)
a<- as.numeric(cv_results)
mean(a)

a

문제1. 위의 결과가 카파지수가 아니라 정확도가 출력되게 하시오.



답:
  
library(caret)
library(C50)
library(irr)
credit <- read.csv("credit.csv", stringsAsFactors = TRUE)
str(credit)
set.seed(123)

folds <- createFolds(credit$default, k = 10)

cv_results <- lapply(folds, function(x) {
  credit_train <- credit[-x, ]
  credit_test <- credit[x, ]
  credit_model <- C5.0(default ~ ., data = credit_train)
  credit_pred <- predict(credit_model, credit_test)
  credit_actual <- credit_test$default
  
  x<-data.frame(credit_actual,credit_pred)
  a <-sum(x$credit_actual==x$credit_pred)/length(x$credit_actual)
  return(a)
  
  # library(gmodels)
  # g <- CrossTable( credit_actual, credit_pred )
  # a<-sum(g$prop.tbl *diag(2))   # 정확도 확인하는 코드
  # return(a)
    
    
})

str(cv_results)

library(gmodels)
g <- CrossTable( credit_actual, credit_pred )
a<-sum(g$prop.tbl *diag(2))   # 정확도 확인하는 코드
return(a)



문제2. 위의 정확도의 평균을 구하시오 ! 
  
  
  
  # 답:
  unlist(cv_results)
  
  mean(as.numeric(cv_results))
  
문제3. 위의 데이터를 훈련 데이터 75%, 테스트 데이터 25% 로 나누고 훈련 데이터 75%

에 대해서만 k-foldout 을 진행하고 훈련 데이터의 정확도의 평균을 확인하시오 !

  힌트코드:
  
library(caret)
in_train <- createDataPartition(credit$default, p = 0.75, list = FALSE)
credit_train <- credit[in_train, ] # 훈련 데이터 구성
credit_test <- credit[-in_train, ] # 테스트 데이터 구성

답: 

library(caret)
library(C50)
library(irr)
credit <- read.csv("credit.csv", stringsAsFactors = TRUE)

# 훈련 데이터와 테스트 데이터를 구분
in_train <- createDataPartition(credit$default, p = 0.75, list = FALSE)
credit_train <- credit[in_train, ] # 훈련 데이터 구성
credit_test <- credit[-in_train, ] # 테스트 데이터 구성

set.seed(123)
folds <- createFolds(credit_train$default, k = 10)

cv_results <- lapply(folds, function(x) {
  credit_train2 <- credit_train[-x, ]
  credit_test2 <- credit_train[x, ]
  credit_model <- C5.0(default ~ ., data = credit_train2)
  credit_pred <- predict(credit_model, credit_test2)
  credit_actual <- credit_test2$default
  
  x<-data.frame(credit_actual,credit_pred)
  a <-sum(x$credit_actual==x$credit_pred)/length(x$credit_actual)
  return(a)
  
  # library(gmodels)
  # g <- CrossTable( credit_actual, credit_pred )
  # a<-sum(g$prop.tbl *diag(2))   # 정확도 확인하는 코드
  # return(a)
})    

mean(as.numeric(cv_results))
  
# 설명: 위와 같이 훈련 데이터를 일부 분리해서 validation 데이터로 사용하는것은 
# 훈련 데이터를 가지고 최적의 하이퍼 파라미터를 찾아내기 위해서이다. 


문제4. 하이퍼 파라미터인 seed 값은 659로 하고 trials는 100으로 해서 다시 훈련 데이터의 정확도 평균을 확인하시오



답:
  
library(caret)
library(C50)
library(irr)

credit <- read.csv("credit.csv", stringsAsFactors = TRUE)
str(credit)

library(caret)

set.seed(659)
in_train <- createDataPartition(credit$default, p = 0.75, list = FALSE)
credit_train <- credit[in_train, ] # 훈련 데이터 구성
credit_test <- credit[-in_train, ] # 테스트 데이터 구성

set.seed(123)
folds <- createFolds(credit_train$default, k = 10)


cv_results <- lapply(folds, function(x) {
  credit_train2 <- credit_train[-x, ]
  credit_test2 <- credit_train[x, ]
  credit_model <- C5.0(default ~ ., data = credit_train2, trials=100)
  credit_pred <- predict(credit_model, credit_test2)
  credit_actual <- credit_test2$default
  x <- data.frame(credit_actual, credit_pred)
  a <- sum(x$credit_actual==x$credit_pred) / length(x$credit_actual)
  return(a)
})


str(cv_results)

mean(unlist(cv_results))
# 0.75

문제5. 위에서 알아낸 seed값과 trials 를 가지고 만든 모델로 테스트 데이터의 정확도를 확인하시오 ~ 
  
  
  
  답:
  
  
library(caret)
library(C50)
library(irr)

credit <- read.csv("credit.csv", stringsAsFactors = TRUE)
  
set.seed(659)
in_train <- createDataPartition(credit$default, p = 0.75, list = FALSE)
credit_train <- credit[in_train, ] # 훈련 데이터 구성
credit_test <- credit[-in_train, ]  
set.seed(123) 
  
credit_model <- C5.0(default ~ ., data = credit_train, trials=100)  
  
credit_pred <- predict(credit_model, credit_test)
credit_actual <- credit_test$default  
  
x <- data.frame(credit_actual, credit_pred)
a <- sum(x$credit_actual==x$credit_pred) / length(x$credit_actual)
print(a)

# 0.74

설명: 훈련 데이터의 정확도가 0.75이고 테스트 데이터의 정확도가 0.74이면
아주 작게 오버피팅이 일어난것 이므로 나쁘지 않습니다. 


문제6. [빅데이터 기사 시험]  다음중 k-fold cross validation 에 대한 설명으로 가장 부적절한것은 ?  
  수제비 p4-39

1. 데이터 집합을 무작위로 K개의 부분집합으로 나누어 검증하는 방법이다.
2. 전체 데이터를 K개의 동일 크리로 나눈다.
3. 모든 데이터를 학습과 평가에 사용할 수 있다.
4. K값이 증가하면 수행시간과 계산량이 감소한다. 





