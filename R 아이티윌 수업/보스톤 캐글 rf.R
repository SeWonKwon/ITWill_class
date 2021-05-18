setwd("c:\\data\\")
traindata <- read.csv("train.csv")
testdata <- read.csv("test.csv")
summary(traindata)
traindata_1 <- traindata[,-1]

traindata_1$age_dis <- ifelse(( traindata$age <30 & traindata$indus <= 10),1,0)
testdata$age_dis <- ifelse(( testdata$age <30 & testdata$indus <= 10),1,0)

traindata_1$rm57<- ifelse(( traindata_1$rm >=5 & traindata$rm <= 7),1,0)
testdata$rm57<- ifelse(( testdata$rm >=5 & testdata$rm <= 7),1,0)

traindata_1$rm5<- ifelse(( traindata$rm <= 5),1,0)
testdata$rm5<- ifelse(( testdata$rm <= 5),1,0)

traindata_1$rm7<- ifelse(( traindata_1$rm >=7 ),1,0)
testdata$rm7<- ifelse(( testdata$rm >=7 ),1,0)

traindata_1$dis37<- ifelse(( traindata_1$dis >=3.7 ),1,0)
testdata$dis37<- ifelse(( testdata$dis >=3.7 ),1,0)

traindata_1$rm_2<- (traindata_1$rm)^2
testdata$rm_2<- (testdata$rm)^2

# black 은 양의 상관에서 360 점에서 부터 이상치를 많이 보유 하고 있다.
traindata_1$black360<- ifelse(( traindata_1$black >=360 ),1,0)
testdata$black360<- ifelse(( testdata$black >=360 ),1,0)
# crim 은 음의 상관관계이면 16 42 구간에서만 
traindata_1$crim16_42<- ifelse(( traindata_1$crim >=16 & traindata$crim <= 42),1,0)
testdata$crim16_42<- ifelse(( testdata$crim >=16 & testdata$crim <= 42),1,0)

# indus 변수 조정 해보자 indus7 indus17
traindata_1$indus7<- ifelse(( traindata_1$indus > 7),1,0)
testdata$indus7<- ifelse(( testdata$indus > 7 ),1,0)

traindata_1$indus17<- ifelse(( traindata_1$indus > 20),1,0)
testdata$indus17<- ifelse(( testdata$indus > 20 ),1,0)

traindata_1$age80<- ifelse(( traindata_1$age > 80),1,0)
testdata$age80<- ifelse(( testdata$age > 80 ),1,0)
# zn 변수 조정 이상 치만 제거해 보자 10 과 20 구간 
traindata_1$zn10<- ifelse(( traindata_1$zn >=10 ),1,0)
testdata$zn10<- ifelse(( testdata$zn >=10 ),1,0)

traindata_1$zn20<- ifelse(( traindata_1$zn > 20),1,0)
testdata$zn20<- ifelse(( testdata$zn > 20 ),1,0)
# dis
traindata_1$dis4<- ifelse(( traindata_1$dis < 4),1,0)
testdata$dis4<- ifelse(( testdata$dis < 4 ),1,0)

traindata_1$rad4<- ifelse(( traindata_1$rad > 22),1,0)
testdata$rad4<- ifelse(( testdata$rad > 22 ),1,0)

library(caret)
# boston_reg_model <- train(price ~ crim + zn + chas + nox + rm + dis + rad + tax + ptratio + b + lstat + lstat_rm + lstat_age, data = boston_train_norm, method = "lm") #회귀분석 방법을 사용하겠다.
# m1 <- train(price ~ crim + zn + chas + nox + rm 
#                           + dis + rad + tax + ptratio + b + lstat 
#                           + lstat_rm + lstat_age, 
#                           data = boston_train_norm, 
#                           method = "rf") #랜덤포레스트 방법을 사용하겠다.
# m1 <- train( medv~ indus*nox*age*crim16_42*tax*indus7*indus17 + dis37
#              + rm + dis + black360*zn10*zn20
#              + rad*rad4 + tax*crim + ptratio
#              + lstat*rm_2*rm5*rm7*rm57 + age_dis + rm57
#              +age80*dis4*dis37 ,
#              data=traindata_1,
#              method = "rf")



m1 <- train( medv~ 
               indus+nox + age
          + crim16_42 + tax + indus7 + indus17 + dis37
          + rm + dis + black360+zn10+zn20
          + rad*rad4 + tax*crim + ptratio
          + lstat*rm_2 + rm5+rm7+rm57 + age_dis + rm57
          +age80+dis4+dis37 ,
          data=traindata_1,
          method = "rf")

summary(m1)
result<- data.frame(predict(m1, testdata))

result2 <- cbind(testdata$ID,result$predict.m1..testdata.)

colnames(result2) <- c('ID','MEDV')
head(result2)

result2<-data.table(result2)

write.csv(result2, file="0002.csv",row.names = F)

















# 
# library(caret)
# #boston_reg_model <- train(price ~ ., data = boston_train_norm, method = "lm") #회귀분석 방법을 사용하겠다.
# #boston_reg_model <- train(price ~ ., data = boston_train_norm, method = "rf") #랜덤포레스트 방법을 사용하겠다.
# 
# #stepwise ver
# boston_reg_model <- train(price ~ crim + zn + chas + nox + rm + dis + rad + tax + ptratio + b + lstat + lstat_rm + lstat_age, data = boston_train_norm, method = "lm") #회귀분석 방법을 사용하겠다.
# #boston_reg_model <- train(price ~ crim + zn + chas + nox + rm + dis + rad + tax + ptratio + b + lstat + lstat_rm + lstat_age, data = boston_train_norm, method = "rf") #랜덤포레스트 방법을 사용하겠다.
# 
