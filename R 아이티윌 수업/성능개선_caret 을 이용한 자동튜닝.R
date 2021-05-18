■ 실습1. caret  패키지 사용 실습 
library(caret)
library(C50)
library(irr)

credit <- read.csv("credit.csv", stringsAsFactors=TRUE)
set.seed(300)

# C5.0 의 하이퍼파라미터인 trials, winnow, model 의 27개의 조합에 대한 # 각각의 정확도를 구하는 작업

m <- train( default~ . , data=credit, method="C5.0")
m # 튜닝한 결과를 확인할 수 있다.

p <- predict( m , credit )
table(p, credit$default)

# 문제 점심시간

library(caret)
library(C50)
library(irr)
credit <- read.csv("credit.csv", stringsAsFactors = TRUE)
str(credit)
library(caret)

set.seed(123)

in_train <- createDataPartition(credit$default, p = 0.75, list = FALSE)
credit_train <- credit[in_train, ] # 훈련 데이터 구성
credit_test <- credit[-in_train, ] # 테스트 데이터 구성

m<-train(default~., data=credit_train, method="C5.0")
m

p<-predict(m,credit_test)
table(p, credit_test$default)

library(gmodels)
y <- CrossTable(credit_test$default,p)
sum(y$prop.tbl*diag(2))


■ winnow 가 무엇인지 ?
  
  
■ 이론설명. 튜닝절차 커스터 마이징 하기 

튜닝절차를 customizing 해서 더 성능을 높이도록 설정할 수 있다.

# 예를들면 방금 수행한 튜닝은 앞에서 배웠던 k-폴드교차검증의 k 값을 25개를
# 사용하는 방법이었습니다. 
# 옵션을 주어서 튜닝할 때 사용할 수 있게 설정을 할 수 있다. 

# 1. 기존 방법:  
  
  m <- train( default~ . , data=credit, method="C5.0")

# 2. 커스터마이징 방법 :
  
  ctrl <-  trainControl( method="cv", number=30, 
                         selectionFunction="oneSE" )

# ※  
# method="cv"  --> k 폴드 교차검증 하겠다.
# number=30    --> 폴드수 
# oneSE           --> 다양한 후보중에서 최적의 모델을 선택하는 방법중 하나인데 이 방법이 3가지가 있다.
# best, oneSE, tolerance  세가지가 있다. 
# 
# best -->  후보중에 단순히 성능척도값중에 최고값을 갖는 후보를 선택(default)
# oneSE --> 최고성능의 1표준오차내의 가장 단순한 후보를 선택한다.
# tolerance--> 사용자 지정 비율내에 가장 단순한 후보를 선택한다. 
# 

  # ※  trials 의 갯수도 아래와 같이 8개로 제한할 수 있다. 

grid <-  expand.grid( .model="tree",
                      .trials= c(1, 5, 10, 15, 20, 25, 30, 35),
                      .winnow="FALSE" )

m <- train( default~ . , data=credit, method="C5.0",
            metric="Kappa",
            trControl= ctrl
            tuneGrid=grid)

p <- predict( m, credit )

table( p, credit$default )  

# p      no yes
# no  656 117
# yes  44 183


문제1. 이번에는 폴드수를 10이 아닌 20으로 늘려서 테스트하시오 !
  
  
  
  답:
  
ctrl <-  trainControl( method="cv", number=20, selectionFunction="oneSE" )       

grid <-  expand.grid( .model="tree",  .trials= c(1, 5, 10, 15, 20, 25, 30, 35),    .winnow="FALSE" )   

m <- train( default~ . , data=credit,
            method="C5.0",                    
            metric="Kappa",                   
            trControl= ctrl,                   
            truneGrid= grid )

p <- predict( m, credit ) 
table( p, credit$default )

#문제5_2


library(caret)
library(C50)
library(irr)
credit <- read.csv("credit.csv", stringsAsFactors = TRUE)
str(credit)
library(caret)

set.seed(123)

in_train <- createDataPartition(credit$default, p = 0.75, list = FALSE)
credit_train <- credit[in_train, ] # 훈련 데이터 구성
credit_test <- credit[-in_train, ] # 테스트 데이터 구성

ctrl <-  trainControl( method="cv", number=30, selectionFunction="oneSE" )
m<-train(default~., data=credit_train, method="C5.0", trControl=ctrl)


p<-predict(m,credit_test)
table(p, credit_test$default)

library(gmodels)
y <- CrossTable(credit_test$default,p)
sum(y$prop.tbl*diag(2))

#0.732

문제5_2. k 값을 40으로 하면 정확도가 더 올라가는지 확인하시오 !
  
library(caret)
library(C50)
library(irr)
credit <- read.csv("credit.csv", stringsAsFactors = TRUE)
str(credit)
library(caret)

set.seed(123)

in_train <- createDataPartition(credit$default, p = 0.75, list = FALSE)
credit_train <- credit[in_train, ] # 훈련 데이터 구성
credit_test <- credit[-in_train, ] # 테스트 데이터 구성

ctrl <-  trainControl( method="cv", number=40, selectionFunction="oneSE" )
m<-train(default~., data=credit_train, method="C5.0", trControl=ctrl)
m

p<-predict(m,credit_test)
table(p, credit_test$default)

library(gmodels)
y <- CrossTable(credit_test$default,p)
sum(y$prop.tbl*diag(2))

# 문제 7. 이번에는 데이터를 iris 데이터로 구현하시오 !  



library(caret)
library(C50)
library(irr)
data(iris)
head(iris)

set.seed(123)
in_train <- createDataPartition(iris$Species, p = 0.75, list = FALSE)
iris_train <- iris[in_train, ] # 훈련 데이터 구성
iris_test <- iris[-in_train, ] # 테스트 데이터 구성


m <- train( Species~ . , data=iris_train, method="C5.0")
m
m # 튜닝한 결과를 확인할 수 있다.

p <- predict( m , iris_test ) 
table(p, iris_test$Species)

library(gmodels)
y <- CrossTable(iris_test$Species ,p)
sum(y$prop.tbl * diag(3))

문제8. 위에서는 의사결정트리의 C5.0 패키지를 이용해서 의사결정트리로 분류하라고 했는데
이번에는 앙상블 기법의 랜덤포레스트를 써서 분류하라고 하시오 . 

랜덤포레스트 + 최적의 파라미터를 자동으로 찾게 하는 방법
# 랜덤 포레스트 : 의가결정트리 + 앙상블 기법

library(caret)
library(C50)
library(irr)
data(iris)
head(iris)

set.seed(123)
in_train <- createDataPartition(iris$Species, p = 0.75, list = FALSE)
iris_train <- iris[in_train, ] # 훈련 데이터 구성
iris_test <- iris[-in_train, ] # 테스트 데이터 구성


m <- train( Species~ . , data=iris_train, method="rf")

m # 튜닝한 결과를 확인할 수 있다.

p <- predict( m , iris_test ) 
table(p, iris_test$Species)

library(gmodels)
y <- CrossTable(iris_test$Species ,p)
sum(y$prop.tbl * diag(3))




■ knn의 k 값을 자동으로 알아내는 방법



colnames(iris)
levels(iris$Species)

set.seed(1)
train <- sample(1:150, 100) #무작위로 100개 추출 (학습데이터)
train_Set <- iris[train, ] #학습데이터 list형
test_Set <- iris[-train, ] #테스트 데이터 list형

## Do 5 repeats of 10-Fold CV for the iris data. We will fit
## a KNN model that eval‎uates 12 values of k and set the seed ## at each iteration. 

set.seed(123)
seeds <- vector(mode = "list", length = 51)
seeds

for(i in 1:50) seeds[[i]] <- sample.int(1000, 22)
seeds

## For the last model:

seeds[[51]] <- sample.int(1000, 1)
seeds

ctrl <- trainControl(method = "repeatedcv", repeats = 5, seeds = seeds)

set.seed(1)
mod <- train(Species ~ ., data = train_Set, method = "knn", tuneLength = 12, trControl = ctrl)
mod


test.pred <- predict(mod, newdata = test_Set)
test.pred

table(test.pred,test_Set$Species)

# 정확도 확인 

library(gmodels)
g <- CrossTable( test_Set$Species, test.pred )
x <- sum(g$prop.tbl *diag(3)) # 정확도 확인하는 코드
x




문제2.  이번에는 method="adaptive_cv"  로 해서 수행하고 정확도를 확인하시오 !
  
  
  
  답:
  
colnames(iris)
levels(iris$Species)

set.seed(1)
train <- sample(1:150, 100) #무작위로 100개 추출 (학습데이터)
train_Set <- iris[train, ] #학습데이터 list형
test_Set <- iris[-train, ] #테스트 데이터 list형

## Do 5 repeats of 10-Fold CV for the iris data. We will fit
## a KNN model that eval‎uates 12 values of k and set the seed ## at each iteration. 

set.seed(123)
seeds <- vector(mode = "list", length = 51)
seeds

for(i in 1:50) seeds[[i]] <- sample.int(1000, 22)
seeds

## For the last model:

seeds[[51]] <- sample.int(1000, 1)
seeds

ctrl <-                        ?  
  
  set.seed(1)
mod <- train(Species ~ ., data = train_Set, method = "knn", tuneLength = 12, trControl = ctrl)
mod


test.pred <- predict(mod, newdata = test_Set)
test.pred

table(test.pred,test_Set$Species)

# 정확도 확인 

library(gmodels)
g <- CrossTable( test_Set$Species, test.pred )
x <- sum(g$prop.tbl *diag(3)) # 정확도 확인하는 코드
x

문제3. 위의 스크립트에서 튜닝되는 과정을 출력하시오 !
  
  
  
  답:
  
  colnames(iris)
levels(iris$Species)

set.seed(1)
train <- sample(1:150, 100) #무작위로 100개 추출 (학습데이터)
train_Set <- iris[train, ] #학습데이터 list형
test_Set <- iris[-train, ] #테스트 데이터 list형

## Do 5 repeats of 10-Fold CV for the iris data. We will fit
## a KNN model that eval‎uates 12 values of k and set the seed ## at each iteration. 

set.seed(123)
seeds <- vector(mode = "list", length = 51)
seeds

for(i in 1:50) seeds[[i]] <- sample.int(1000, 22)
seeds

## For the last model:

seeds[[51]] <- sample.int(1000, 1)
seeds

ctrl <- trainControl(method = "adaptive_cv",
                     repeats = 5,
                     ?   ,
                     seeds = seeds)

set.seed(1)
mod <- train(Species ~ ., data = train_Set, method = "knn", tuneLength = 12, trControl = ctrl)
mod
args(train)

test.pred <- predict(mod, newdata = test_Set)
test.pred

table(test.pred,test_Set$Species)

# 정확도 확인 

library(gmodels)
g <- CrossTable( test_Set$Species, test.pred )
x <- sum(g$prop.tbl *diag(3)) # 정확도 확인하는 코드
x


#%%
colnames(iris)
levels(iris$Species)
nrow(iris)
set.seed(1)
train <- sample(1:150, 100) #무작위로 100개 추출 (학습데이터)
train_Set <- iris[train, ] #학습데이터 list형
test_Set <- iris[-train, ] #테스트 데이터 list형

## Do 5 repeats of 10-Fold CV for the iris data. We will fit
## a KNN model that eval uates 12 values of k and set the seed ## at each iteration. 

set.seed(123)
seeds <- vector(mode = "list", length = 51)
seeds

for(i in 1:50) seeds[[i]] <- sample.int(1000, 22)
seeds

## For the last model:

seeds[[51]] <- sample.int(1000, 1)
seeds

ctrl <- trainControl(method = "adaptive_cv",
                     repeats = 5,
                     verboseIter = TRUE,
                     seeds = seeds)

set.seed(2)
mod <- train(Species ~ ., data = train_Set, method = "knn", tuneLength = 12, trControl = ctrl)
str(mod)
mod$bestTune


test.pred <- predict(mod, newdata = test_Set)
test.pred

table(test.pred,test_Set$Species)

# 정확도 확인 

library(gmodels)
g <- CrossTable( test_Set$Species, test.pred )
x <- sum(g$prop.tbl *diag(3)) # 정확도 확인하는 코드
x

seeds <- vector(mode = "list", length = 51)
seeds

for(i in 1:50) seeds[[i]] <- sample.int(1000, 22)
seeds
seeds[[51]] <- sample.int(1000, 1)
seeds
