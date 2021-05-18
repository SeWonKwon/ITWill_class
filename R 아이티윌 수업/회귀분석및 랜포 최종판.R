# 타이타닉 생존자 분류 

# 1. 데이터 로드 
# 파이썬의 seaborn 에서 가져온 데이터임.

tat <- read.csv("tatanic.csv", stringsAsFactors = TRUE)
View(tat)
head(tat)

#survived : 생존=1, 죽음=0
#pclass : 승객 등급. 1등급=1, 2등급=2, 3등급=3
#sibsp : 함께 탑승한 형제 또는 배우자 수
#parch : 함께 탑승한 부모 또는 자녀 수
#ticket : 티켓 번호
#cabin : 선실 번호
#embarked : 탑승장소 S=Southhampton, C=Cherbourg, Q=Queenstown

#2.결측치 확인 


colSums( is.na(tat) ) 
?mean

tat$age[is.na(tat$age)] <- mean(tat$age,na.rm=TRUE)

#3.이상치 확인 

library(outliers)

grubbs.flag <- function(x) {
  outliers <- NULL
  test <- x
  grubbs.result <- grubbs.test(test)
  pv <- grubbs.result$p.value
  while(pv < 0.05) {
    outliers <- c(outliers,as.numeric(strsplit(grubbs.result$alternative," ")[[1]][3]))
    test <- x[!x %in% outliers]
    grubbs.result <- grubbs.test(test)
    pv <- grubbs.result$p.value
  }
  return(data.frame(X=x,Outlier=(x %in% outliers)))
}

wisc <- read.csv("tatanic.csv")

for (i in c(2,3,5,6,8)){
  
  a = grubbs.flag(wisc[,colnames(wisc)[i]])
  b = a[a$Outlier==TRUE,"Outlier"]
  print ( paste( colnames(wisc)[i] , '--> ',  length(b) )  )
  
}


#4. 랜덤포레스트로 분류합니다.

library(caret)
library(C50)
library(irr)

nrow(tat)


#0.shuffle 을 먼저 합니다. 
set.seed(123)
tat_shuffle <- sample(1:891, 891)
tat_shuffle
tat2 <- tat[tat_shuffle,]
tat2

set.seed(1244)
in_train <- createDataPartition(tat2$survived, p = 0.75, list = FALSE)
tat_train <- tat2[in_train, ] # 훈련 데이터 구성
tat_test <- tat2[-in_train, ] # 테스트 데이터 구성

m <- train( survived~ . , data=tat_train, method="rf" )

# 랜덤포레스트: 의사결정트리 + 앙상블 기법 
m # 튜닝한 결과를 확인할 수 있다.

p <- predict( m , tat_test )
p
round(p)

table(round(p), tat_test$survived)

library(gmodels)
y <- CrossTable(tat_test$survived ,round(p) )
sum(y$prop.tbl * diag(2))

[캐글도전] 랜덤 포레스트로 타이타닉 생존자 분류 실험

# 문제1. 이번에는 나이의 결측치를 나이의 평균값으로 하지말고 승객나이중에
# 승객나이중에 최대값으로 결측치를 채우고 다시 

tat <- read.csv("tatanic.csv", stringsAsFactors = TRUE)
View(tat)

colSums( is.na(tat) ) 


tat$age[is.na(tat$age)] <- max(tat$age,na.rm=TRUE)

max(tat$age)
table(tat$age)


## 보스톤 하우스 

boston<- read.csv("boston.csv")
View(boston)
colSums(is.na(boston))



#################### 1. 데이터 불러오기 ####################

getwd()
library(data.table)

boston <- read.csv("c:\\data\\boston.csv" )

nrow(boston)
length(boston)
#0.shuffle 을 먼저 합니다. 
set.seed(123)
boston_shuffle <- sample(1:nrow(boston), nrow(boston))
boston_shuffle
boston2 <- boston[boston_shuffle,]
nrow(boston2)
str(boston2)
colnames(boston2)<-tolower(colnames(boston))


set.seed(123)
set.seed(1234)
ind <- sample(2, nrow(boston2), replace = T, prob = c(0.8, 0.2))
boston_train <- boston2[ind==1,]
boston_test <- boston2[ind==2,]

nrow(boston_train)

#상관관계 분석, vif 확인등의 절차를 거친 후 추가되는 데이터 

# 1) 

boston_train$lstat_rm <- ifelse( ( boston_train$lstat >5  &  boston_train$rm <= 5) , 1, 0 ) 
boston_test$lstat_rm <- ifelse( ( boston_test$lstat >5  &  boston_test$rm <= 5) , 1, 0 ) 
boston_train$age_indus <- ifelse( ( boston_train$age < 30 & boston_train$indus <= 10) , 1, 0 )
boston_test$age_indus <- ifelse( ( boston_test$age < 30 & boston_test$indus <= 10) , 1, 0 )


#################### 2. 데이터 전처리 ####################

# 1) 결측치

# 1-1. 결측치 확인
sum(is.na(boston_train)) #0개
sum(is.na(boston_test)) #0개


# 1-2. 결측치 위치확인
#(1) 데이터셋명[complete.cases(데이터셋명),]   # 결측치가 없으면 True
#(2) 데이터셋명[!complete.cases(데이터셋명),]  # 결측치가 있으면 True


# 1-3. 결측치 삭제
#boston_train<-na.omit(boston_train)
#boston_test<-na.omit(boston_test) 

# 1-4. 결측치 대체

# (1) 결측할 값 직접지정
#boston_train$대체할변수있는컬럼[is.na(데이터셋$컬럼명)]<-일괄대체할값
# 지정 컬럼에서 na가 있으면 지정하는 값으로 대체

# (2) 통계값으로 대체
#install.packages("DMwR")
#library(DMwR)

#centralImputation(데이터셋명) # NA중앙값 대체 : 숫자의 경우 중앙값, 팩터의 경우 최빈값
#knnImputation(데이터셋명)   # means를 활용한 결측치 대체

# 2) 정규화
#데이터 정규화를 위한 함수생성
normalize <- function(x) {
  return ( (x-min(x)) / (max(x) - min(x) ) )
}

boston_train_norm <- as.data.frame(lapply(boston_train[,-1], normalize))
boston_test_norm <- as.data.frame(lapply(boston_test[,-1],normalize) ) 

#정규화 결과 확인
summary(boston_train_norm) 
summary(boston_test_norm)


#################### 3. 모델링, 데이터 학습, 성능검증 , 평가 ####################

# 1) 모델링 (변수선택)

# 1-1. 다중공선성 확인
#install.packages("car")
library(car)

lml <- lm(price~., data=boston_train_norm) 
vif(lml) # 팽창지수(=다중공선성=vif)
vif(lml) > 10 #vif 5이상이면 TRUE / 5이하면 FALSE

# strict 하게 본다면(vif > 5) indus, rad, tax, age_30, indus_10 의 다중공선성 높음
# 일반적으로 본다면(vif > 10) = 제거해야할 변수 없음 
# 이번 실습은 vif > 10을 기준으로 진행 


# 1-2. 분산이 0에가까운 변수제거
# 데이터의 분산이 0에가깝다 = 서로다른 관찰을 구분하는데 소용이없다. = 제거한다.
# 결과치에서 nzv 컬럼에 TRUE로 뜨는값 제거



#install.packages("caret")
library(caret)
nearZeroVar(boston_test_norm, saveMetrics = TRUE) # all_FALSE (제거대상 없음)
nearZeroVar(boston_train_norm, saveMetrics = TRUE)# all_FALSE (제거대상 없음)

# nzv = TRUE인 변수들 제거
#boston_train <- boston_train[,-nearZeroVar(boston_train)]
#boston_test <- boston_test[,-nearZeroVar(boston_test)]


# 1-3. 상관관계
#install.packages("corrplot")
library(corrplot)
#기본값은 원형, shade=네모칸, ellipse = 타원(양의상관 오른쪽, 음의상관 왼쪽)
# circle = 원형, number = 수치로 표현
corrplot(cor(boston_train_norm), method = "number")


# 1-4. 변수중요도 확인
# 변수중요도 : "해당 변수가 상대적으로 얼마만큼 종속변수에 영향을 주는가?"

# 랜덤 포레스트 방식을 활용

#install.packages("randomForest")
library(randomForest)
#rf <- randomForest(medv~., data=boston_train_norm)
rf <- randomForest(price~., data=boston_train_norm, importance=TRUE)



#중요도 확인방법 2가지

# 1) 중요도 수치로 확인

varImp(rf) 
importance(rf) #IncMSE = 정확도, IncNodePurity = 중요도 = importance

# 2) plot형태로 시각화해서 확인
varImpPlot(rf, main="Varplot of boston_train")

# 1-5. 단계적 회귀분석으로 유효변수골라내기
#1번째시도 (기본적으로 주어진 모든 독립변수 활용하여 모델링)

# vif 확인시 만든 lml과 동일
model1 <- lm(formula=price ~ crim + chas + nox + rm + dis + rad + ptratio + lstat, data = boston_train_norm)




#stepwise(단계적 회귀분석 방법)로 가장 유효한 변수 확인하기
lm2 <- step(model1, direction="both") 
# medv ~ crim + chas + nox + rm + dis + rad + ptratio + lstat

# 결과적 추시가 좋지 않아 단계적 회귀분석을 단독 적용하는 것은 무리라 판단. 상관관계를 감안하여 적용하기로함


#2번째 시도 (상관관계 분석을 통해 알아낸 사실 포함하여 적용)
lml2<-step(lml, direction="both") 
#medv ~ crim + zn + indus + chas + nox + rm + dis + rad + tax +   ptratio + black + lstat + lstat_rm

# 회귀에서 최적의 독립변수조합을 찾는 과정입니다. 

# 여기까지 확인한 후에 다시 1번으로 돌아가 컬럼 추가 및 전처리를 수행함





# 2-1. 모델링

#stepwise + 상관계수 반영한 결과 고려하여 모델링 
boston_reg_model <- lm(price ~ crim + zn + indus + chas + nox + rm + dis + rad + tax +   ptratio  + lstat + lstat_rm, data=boston_train_norm ) 


model_results <-  predict(boston_reg_model, boston_test_norm)
model_results


# 2-2. 결과값 역정규화 (kaggle과 데이터 형식 맞추기)
denormalize <- function(x) { return ( x*45+5) }    #max(train_data$medv)  #min(train_data$medv)
pred_medv_un <- denormalize(model_results)

sample <- cbind(boston_test$x, pred_medv_un)

head(sample)

colnames(sample) <- c("id", "price")
cor(pred_medv_un,boston_test$price)

# write.csv(sample, "Submission_sample16.csv", row.names=FALSE)
(마지막 문제)
result_s <- data.frame(id=boston_test$x,actual=boston_test$price ,pred=pred_medv_un)
result_s

# install.packages("forecast")
library("forecast")

accuracy(result_s$actual,result_s$pred)

#               ME     RMSE      MAE       MPE     MAPE
# Test set -0.977148 5.469168 4.070429 -31.32477 66.12145


