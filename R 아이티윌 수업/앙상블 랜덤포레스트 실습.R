random forest 는  decesion tree 와 bagging 을 결합한 알고리즘이다.


실습 :  kyphosis(후만증)은 척추의 비정상적으로 과도한 볼록 곡률입니다. 
후만증 데이터 프레임에는 81 개의 행과 4 개의 열이 있습니다. 
척추 교정 수술을받은 어린이에 대한 데이터를 나타냅니다. 데이터 세트는 3 개의 입력과 1 개의 출력을 포함합니다.
데이터로서 독립변수가 나이(개월수)와 관련된 척추의 수 그리고 수술 된 첫 번째 (최상위) 척추의 수이다.
데이터가 81개 밖에 안되므로 데이터를 전부 의사 결정트리에 넣어서 예측과 실제 라벨을 비교해서 정확도를 봅니다.

# 0. 필요한 패키지를 다운로드 합니다. 

# install.packages("rpart")
# install.packages("rattle")
# install.packages("randomForest")

# 1. 데이터를 로드한다.

kyphosis <- read.csv("kyphosis.csv", stringsAsFactors = TRUE)
View(kyphosis)
# 2. rpart 를 이용해서 의사 결정트리 모델을 생성한다.

library(rpart)

fit <- rpart(kyphosis ~ age + number + start,method="class", data=kyphosis)

# 3. 모델을 시각화 한다.

library(rattle)
library(rpart.plot)

x11()
fancyRpartPlot(fit)

dev.off()

# 4. 정확도를 확인한다.
result <- predict(fit , newdata = kyphosis)
sum(kyphosis$kyphosis == ifelse(result[,1]>0.5 , "absent" , "present"))/NROW(kyphosis)

# [1] 0.8395062
# 그럼 83% 로 나온다.
# 이 수치를 높이기 위해서  random forest 를 사용한다.

# 1. 랜덤 포레스트 모델을 만든다.
library(randomForest)

# 랜덤포레스트 패키지 설명 : https://www.rdocumentation.org/packages/randomForest/versions/4.6-14/topics/randomForest

fit <- randomForest(kyphosis ~ age + number + start,   data=kyphosis)

res2 <- predict(fit , newdata = kyphosis)

sum(res2 == kyphosis$kyphosis)/NROW(kyphosis)

# [1] 0.9876543  <--- 98% 로 정확도가 올라간다.


# 위에서 500개의 트리가 나오는데 이 트리들은 다 똑같은 트리는 아니고 우리는 모르게 미세하게 조금씩 파라미터가 다르다.

# 그 값들도 자동으로 함수에서 알아서 조정해준다.

summary(fit)

# 문제1. 척추 데이터의 랜덤 포레스트 모델을 다시 생성하는데 ntree 의 갯수와 
#       mtry의 갯수를 늘려서 테스트 하시오 !
#   

  
fit2 <- randomForest(kyphosis ~ age + number + start,   data=kyphosis, mtry=2, ntree=21)

res22 <- predict(fit2 , newdata = kyphosis)

sum(res22 == kyphosis$kyphosis)/NROW(kyphosis)

summary(fit2)

fit2$mtry
fit2$ntree


■ 11장. 랜덤포레스트 실습2 (iris데이터)

#0.필요한 패키지 다운로드

#install.packages('randomForest')
library(randomForest)
library(caret)

#0. shuffle 을 먼저 합니다. 
set.seed(123)
iris_shuffle <- sample(1:150, 150)
iris2 <- iris[iris_shuffle,]

# 1. 훈련 데이터와 테스트 데이터 분리 


set.seed(123)
in_train <- createDataPartition(iris2$Species, p = 0.75, list = FALSE)
iris_train <- iris2[in_train, ] # 훈련 데이터 구성
iris_test <- iris2[-in_train, ] # 테스트 데이터 구성
nrow(iris_train)
nrow(iris_test)
prop.table(table(iris_train$Species))
prop.table(table(iris_test$Species))

#2. 모델 훈련
forest_m <- randomForest(Species ~ ., data=iris_train)
forest_m   

# Type of random forest: classification     : 분류
# Number of trees: 500                      : ntree
# No. of variables tried at each split: 2   : mtry
# OOB estimate of  error rate: 5.26%        : 오분류율




forest_m$predicted            # 학습된 모델을 통한 train data 의 예측값 확인
length(forest_m$predicted)
forest_m$importance        # 각 feature importance(각 불순도 기반 설명변수 중요도) 

#               MeanDecreaseGini
# Sepal.Length         6.792552
# Sepal.Width          2.137378
# Petal.Length        31.762519
# Petal.Width         34.492492 # 가장 중요함.


forest_m$mtry      # 모델의 mtry 값 확인
forest_m$ntree     # 모델의 ntree 값 확인

# 3. 모델을 통한 예측 
new_data <- iris_train[10,-5] + 0.2
new_data

predict(forest_m, newdata = new_data, type = 'class') # 500개 트리의 다중투표 결과 

iris_train[10,'Species']

# 4. 모델 평가 
# 4-1) test data에 대한 score 확인
prd_v <- predict(forest_m, newdata = iris_test, type = 'class')
sum(prd_v == iris_test$Species) / nrow(iris_test) * 100

# 4-2) train data에 대한 score 확인 
prd_v2 <- predict(forest_m, newdata = iris_train, type = 'class')
sum(prd_v2 == iris_train$Species) / nrow(iris_train) * 100

# 5. 모델 시각화
layout(matrix(c(1,2),nrow=1),width=c(4,1)) 
par(mar=c(5,4,4,0)) # 오른쪽 마진 제거 
# x11()
plot(forest_m)
par(mar=c(5,0,4,2)) # 왼쪽 마진 제거 
plot(c(0,1),type="n", axes=F, xlab="", ylab="")
legend("top", colnames(forest_m$err.rate),col=1:4,cex=0.8,fill=1:4)


# 문제 랜덤포레스트의 최적의 파라미터를 자동으로 찾는 loop문을 구현하시오!

ntree <- c(400, 500, 600)
mtry <- c(2:4)

t<-0
for (i in ntree) {
    for(j in mtry) {
    cat('\n') 
    cat('ntree=', i,'  ',' mtry=',j,'\n')
    model_iris <- randomForest(Species ~ ., data=iris_train, ntree=i, mtry=j,
                               na.action=na.omit)
    print(model_iris)
    print(model_iris$ntree)
    print(t)
    t<-t+1
  }
}
# model_iris$err.rate

■ 11장. 앙상블과 자동 튜닝을 결합하여 최적의 모델찾기 실험



library(caret)
library(randomForest)
library(irr)
data(iris)
head(iris)

#0.shuffle 을 먼저 합니다. 
set.seed(123)
iris_shuffle <- sample(1:150, 150)
iris_shuffle
iris2 <- iris[iris_shuffle,]
iris2

#1. 훈련 데이터 75%, 테스트 데이터 25%로 분리합니다. 
set.seed(123)
in_train <- createDataPartition(iris2$Species, p = 0.75, list = FALSE)
iris_train <- iris2[in_train, ] # 훈련 데이터 구성
iris_test <- iris2[-in_train, ] # 테스트 데이터 구성

#2. 랜덤 포레스트를 이용해서 훈련을 시키는데 자동파라미터 튜닝도 같이 진행합니다. 
m <- train( Species~ . , data=iris_train, method="rf" )
m
m$bestTune

# 랜덤포레스트: 의사결정트리 + 앙상블 기법 
m # 튜닝한 결과를 확인할 수 있다.

p <- predict( m , iris_test )
table(p, iris_test$Species)


library(gmodels)
y <- CrossTable(iris_test$Species ,p)
sum(y$prop.tbl * diag(3))

