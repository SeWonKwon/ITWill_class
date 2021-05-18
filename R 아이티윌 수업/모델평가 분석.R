#1. 데이터를 로드한다.

credit <- read.csv("credit.csv", stringsAsFactor=TRUE)
str(credit) 

#2. 데이터에 각 컬럼들을 이해한다. 

#라벨 컬럼 :  default  --->  yes : 대출금 상환 안함 
#no  : 대출금 상환 

prop.table( table(credit$default)  )
summary( credit$amount)

#3. 데이터가 명목형 데이터인지 확인해본다.

str(credit) 

#4. 데이터를 shuffle 시킨다.
set.seed(31)
credit_shuffle <-  credit[ sample( nrow(credit) ),  ]

#5. 데이터를 9 대 1로 나눈다.
train_num <- round( 0.9 * nrow(credit_shuffle), 0) 
credit_train <- credit_shuffle[1:train_num ,  ]
credit_test  <- credit_shuffle[(train_num+1) : nrow(credit_shuffle),  ]
nrow(credit_test)

#6. C5.0 패키지와 훈련 데이터를 이용해서 모델을 생성한다.
# install.packages("C50")
library(C50)
credit_model <- C5.0( credit_train[ ,-17] , credit_train[  , 17] )

#7. 위에서 만든 모델을 이용해서 테스트 데이터의 라벨을 예측한다.

credit_result <-  predict( credit_model, credit_test[  , -17] )

#8. 이원 교차표로 결과를 확인한다.
# install.packages("gmodels")
library(gmodels)

CrossTable( credit_test[   , 17], credit_result )

#■ 실제값과 예측값 대입

actual_type <- credit_test[  , 17] # 실제 테스트 데이터의 라벨
predict_type <-  credit_result
positive_value <- 'yes' # 관심범주 yes 는 돈 못갚은 사람 
negative_value <- 'no'

#■ 정확도

g <- CrossTable( actual_type, predict_type )
x <- sum(g$prop.tbl *diag(2))   # 정확도 확인하는 코드
x

#■ 카파통계량 

# install.packages("vcd")
library(vcd)

table( actual_type, predict_type)
Kappa( table( actual_type, predict_type)  ) 

#■ 민감도

head(credit_results)

# install.packages("caret")
library(caret)
sensitivity( predict_type, actual_type,
             positive=positive_value)

#■ 특이도
specificity(  predict_type, actual_type,
              negative=negative_value)  

#■ 정밀도
posPredValue( predict_type, actual_type,
              positive=positive_value) 

#■ 재현율 
sensitivity( predict_type, actual_type,
             positive=positive_value) 


#---------------------------------------
# 문제304

credit <- read.csv("credit.csv", stringsAsFactor=TRUE)

set.seed(659)
credit_shuffle <-  credit[ sample( nrow(credit) ),  ]
train_num <- round( 0.9 * nrow(credit_shuffle), 0) 
credit_train <- credit_shuffle[1:train_num ,  ]
credit_test  <- credit_shuffle[(train_num+1) : nrow(credit_shuffle),  ]
library(C50)
credit_model <- C5.0( credit_train[ ,-17] , credit_train[  , 17], trials = 100 )
credit_result <-  predict( credit_model, credit_test[  , -17] )

library(gmodels)

CrossTable( credit_test[   , 17], credit_result )

#■ 실제값과 예측값 대입

actual_type <- credit_test[  , 17] # 실제 테스트 데이터의 라벨
predict_type <-  credit_result
positive_value <- 'yes' # 관심범주 yes 는 돈 못갚은 사람 
negative_value <- 'no'

#■ 정확도

g <- CrossTable( actual_type, predict_type )
x <- sum(g$prop.tbl *diag(2))   # 정확도 확인하는 코드
x

#■ 카파통계량 
library(vcd)

table( actual_type, predict_type)
a<-Kappa( table( actual_type, predict_type)  ) 
a$Unweighted[1]
#■ 민감도

head(credit_results)
# install.packages("caret")
library(caret)
sensitivity( predict_type, actual_type,
             positive=positive_value)

#■ 특이도
specificity(  predict_type, actual_type,
              negative=negative_value)  

#■ 정밀도
posPredValue( predict_type, actual_type,
              positive=positive_value) 

#■ 재현율 
sensitivity( predict_type, actual_type,
             positive=positive_value) 


#----------------------------------------------------------
#1. 데이터를 로드한다.

credit <- read.csv("credit.csv", stringsAsFactor=TRUE)
str(credit) 

#2. 데이터에 각 컬럼들을 이해한다. 

#라벨 컬럼 :  default  --->  yes : 대출금 상환 안함 
#no  : 대출금 상환 

prop.table( table(credit$default)  )
summary( credit$amount)

#3. 데이터가 명목형 데이터인지 확인해본다.

str(credit) 

#4. 데이터를 shuffle 시킨다.

set.seed(31)
credit_shuffle <-  credit[ sample( nrow(credit) ),  ]

#5. 데이터를 9 대 1로 나눈다.

train_num <- round( 0.9 * nrow(credit_shuffle), 0) 

credit_train <- credit_shuffle[1:train_num ,  ]

credit_test  <- credit_shuffle[(train_num+1) : nrow(credit_shuffle),  ]


#6. C5.0 패키지와 훈련 데이터를 이용해서 모델을 생성한다.

library(C50)

credit_model <- C5.0( credit_train[ ,-17] , credit_train[  , 17] )

#7. 위에서 만든 모델을 이용해서 테스트 데이터의 라벨을 예측한다.

credit_result <-  predict( credit_model, credit_test[  , -17] )

#8. 이원 교차표로 결과를 확인한다.

library(gmodels)

CrossTable( credit_test[   , 17], credit_result )




#■ 실제값과 예측값 대입

credit_test_prob <- predict(credit_model, credit_test[   , -17], type = "prob")


credit_test_prob


# combine the results into a data frame

credit_results <- data.frame(actual_type =credit_test[  , 17], # 테스트 데이터의 실제정답
                             predict_type = credit_result, # 테스트 데이터에 대한 예측값
                             prob_yes = round(credit_test_prob[ , 2], 5),
                             prob_no = round(credit_test_prob[ , 1], 5))



credit_results


#3. 예측 데이터 프레임을 csv 로 저장합니다.

# uncomment this line to output the sms_results to CSV

write.csv(credit_results, "final_results.csv", row.names = FALSE)



#■ 실제값과 예측값 대입

actual_type <- credit_test[  , 17] # 관심ㅂ
predict_type <-  credit_result
positive_value <- 'yes'
negative_value <- 'no'

#■ 정확도

g <- CrossTable( actual_type, predict_type )

x <- sum(g$prop.tbl *diag(2))   # 정확도 확인하는 코드
x

#■ 카파통계량 

#install.packages("vcd")
library(vcd)

table( actual_type, predict_type)

Kappa( table( actual_type, predict_type)  ) 



#■ 민감도

head(credit_results)

#install.packages("caret")
library(caret)
sensitivity( predict_type, actual_type,
             positive=positive_value)

#■ 특이도
specificity(  predict_type, actual_type,
              negative=negative_value)  

#■ 정밀도
posPredValue( predict_type, actual_type,
              positive=positive_value) 

#■ 재현율 
sensitivity( predict_type, actual_type,
             positive=positive_value) 

#■ ROC 곡선 그리기 

#install.packages("ROCR")
library(ROCR)
head(credit_results) # 3번째 컬럼과 4번째컬럼의 확률을 확인한다.
pred <- prediction(predictions = credit_results$prob_yes,              
                   labels = credit_results$actual_type)
pred 
# 설명 : prediction( predictions = 관심범주의 확률, labels = 실제 정답 )
# ROC curves

perf <- performance(pred, measure = "tpr", x.measure = "fpr")
perf
# 설명 : performance(100개의 데이터 포인트, y축값, x축값)
plot(perf, main = "ROC curve for SMS spam filter", col = "orange", lwd = 2)

# add a reference line to the graph
# 대각선 출력 

abline(a = 0, b = 1, lwd = 2, lty = 2)

# a 는 절편 , b 는 기울기

# calculate AUC
# Area under Curve
perf.auc <- performance(pred, measure = "auc")
str(perf.auc)
unlist(perf.auc@y.values)


#■ F척도를 구하시오 ~  (뎃글로 달아주세요 )
#위에서 구한 정밀도와 재현율을 아래의 변수에 각각 입력하여 구하시오 !


#1. F1 score 공식
# Fmeasure <- 2 * precision * recall / (precision + recall)

#2. 패키지를 이용하는 방법 
#install.packages("MLmetrics")
library(MLmetrics)

F1_Score(actual_type, predict_type, positive = positive_value)



#--------------------------------------
게시글 827. [쉬움주의] Roc 커브 R 코드!

install.packages('aod')
install.packages('ggplot2')
library(aod)
library(ggplot2)

binary <- read.csv("http://www.karlin.mff.cuni.cz/~pesta/prednasky/NMFM404/Data/binary.csv")
str(binary)

#Logistic Regression Model
install.packages("nnet")
library(nnet)

mymodel <- multinom(admit~.,data = binary)

#mis classification rate
p <- predict(mymodel,binary)
tab <- table(p,binary$admit)
tab
1-sum(253,29)/400

# Model Performance Evaluation
install.packages("ROCR")
library(ROCR)
pred <- predict(mymodel,binary,type = "prob")
pred
hist(pred)

pred <- prediction(pred,binary$admit)
eval <- performance(pred,"acc") 
eval
args(performance)
plot(eval)

# perf <- performance(pred, measure = "tpr", x.measure = "fpr")랑 acc랑 비교해봐!!
perf <- performance(pred, measure = "tpr", x.measure = "fpr")
plot(perf)

abline(h=0.71,v=.45)
# 설명 : h 는 수평선, v 가 수직선의 지점

#Identifying the best cutoff  and Accuracy
eval
slot(eval,"y.values")

max <- which.max(slot(eval,"y.values")[[1]])
max # 맥스 값에 해당하는 인덱스 값.

acc <- slot(eval,"y.values")[[1]][[max]]
cut <- slot(eval,"x.values")[[1]][[max]]
print(c(Accuracy=acc,Cutoff = cut))

#Receiver Operating Chraracteristic (ROC) curve

pred <- predict(mymodel,binary,type = "prob")
pred <- prediction(pred,binary$admit)
roc <- performance(pred,"tpr","fpr")
plot(roc,colorize = T,
     main = "ROC Curve",
     ylab = "Sensitivity",
     xlab = "1-Specificity")
abline(a=0,b=1)

#AUC
auc <- performance(pred,"auc")
auc <- unlist(slot(auc,"y.values"))
round(auc,3)

legend(0.6,0.2,auc,title = "AUC",cex = .50)

# -----------------------------------------------------
307번

credit <- read.csv("credit.csv", stringsAsFactor=TRUE)
str(credit) 

#2. 데이터에 각 컬럼들을 이해한다. 

#라벨 컬럼 :  default  --->  yes : 대출금 상환 안함 
#no  : 대출금 상환 

prop.table( table(credit$default)  )
summary( credit$amount)

#3. 데이터가 명목형 데이터인지 확인해본다.

str(credit) 

#4. 데이터를 shuffle 시킨다.

set.seed(31)
credit_shuffle <-  credit[ sample( nrow(credit) ),  ]

#5. 데이터를 9 대 1로 나눈다.

train_num <- round( 0.9 * nrow(credit_shuffle), 0) 

credit_train <- credit_shuffle[1:train_num ,  ]

credit_test  <- credit_shuffle[(train_num+1) : nrow(credit_shuffle),  ]


#6. C5.0 패키지와 훈련 데이터를 이용해서 모델을 생성한다.

library(C50)

credit_model <- C5.0( credit_train[ ,-17] , credit_train[  , 17] )

#7. 위에서 만든 모델을 이용해서 테스트 데이터의 라벨을 예측한다.

credit_result <-  predict( credit_model, credit_test[  , -17] )

#8. 이원 교차표로 결과를 확인한다.

library(gmodels)

CrossTable( credit_test[   , 17], credit_result )




#■ 실제값과 예측값 대입

credit_test_prob <- predict(credit_model, credit_test[   , -17], type = "prob")


credit_test_prob


# combine the results into a data frame

credit_results <- data.frame(actual_type =credit_test[  , 17], # 테스트 데이터의 실제정답
                             predict_type = credit_result, # 테스트 데이터에 대한 예측값
                             prob_yes = round(credit_test_prob[ , 2], 5),
                             prob_no = round(credit_test_prob[ , 1], 5))



credit_results


#3. 예측 데이터 프레임을 csv 로 저장합니다.

# uncomment this line to output the sms_results to CSV

write.csv(credit_results, "final_results.csv", row.names = FALSE)



#■ 실제값과 예측값 대입

actual_type <- credit_test[  , 17] # 관심ㅂ
predict_type <-  credit_result
positive_value <- 'yes'
negative_value <- 'no'

#■ 정확도

g <- CrossTable( actual_type, predict_type )

x <- sum(g$prop.tbl *diag(2))   # 정확도 확인하는 코드
x

#■ 카파통계량 

#install.packages("vcd")
library(vcd)

table( actual_type, predict_type)

Kappa( table( actual_type, predict_type)  ) 



#■ 민감도

head(credit_results)

#install.packages("caret")
library(caret)
sensitivity( predict_type, actual_type,
             positive=positive_value)

#■ 특이도
specificity(  predict_type, actual_type,
              negative=negative_value)  

#■ 정밀도
posPredValue( predict_type, actual_type,
              positive=positive_value) 

#■ 재현율 
sensitivity( predict_type, actual_type,
             positive=positive_value) 

#■ ROC 곡선 그리기 

#install.packages("ROCR")
library(ROCR)
head(credit_results) # 3번째 컬럼과 4번째컬럼의 확률을 확인한다.
pred <- prediction(predictions = credit_results$prob_yes,              
                   labels = credit_results$actual_type)
pred 
# 설명 : prediction( predictions = 관심범주의 확률, labels = 실제 정답 )
# ROC curves

perf <- performance(pred, measure = "tpr", x.measure = "fpr")
perf
# 설명 : performance(100개의 데이터 포인트, y축값, x축값)
plot(perf, main = "ROC curve for SMS spam filter", col = "orange", lwd = 2)

# add a reference line to the graph
# 대각선 출력 

abline(a = 0, b = 1, lwd = 2, lty = 2)

# a 는 절편 , b 는 기울기

# calculate AUC
# Area under Curve
perf.auc <- performance(pred, measure = "auc")
str(perf.auc)
unlist(perf.auc@y.values)








eval <- performance(pred,"acc") 
eval
args(performance)
plot(eval)
abline(h=0.80,v=.76)

# perf <- performance(pred, measure = "tpr", x.measure = "fpr")랑 acc랑 비교해봐!!
perf <- performance(pred, measure = "tpr", x.measure = "fpr")
plot(perf)


# 설명 : h 는 수평선, v 가 수직선의 지점

#Identifying the best cutoff  and Accuracy
eval
slot(eval,"y.values")

max <- which.max(slot(eval,"y.values")[[1]])
max # 맥스 값에 해당하는 인덱스 값.
max
acc <- slot(eval,"y.values")[[1]][[max]]
cut <- slot(eval,"x.values")[[1]][[max]]
print(c(Accuracy=acc,Cutoff = cut))

perf <- performance(pred, measure = "tpr", x.measure = "fpr")
plot(perf,col='blue')

slot(perf,"y.values")
slot(perf,"x.values")
max
tpr <- slot(perf,"y.values")[[1]][[max]]
fpr <- slot(perf,"x.values")[[1]][[max]]
print(c(tpr,fpr))
abline(h=0.37, v=0.028)
abline(h=tpr,v=fpr)
abline(a = 0, b = 1, lwd = 2, lty = 2, col='orange')



#%%%  F1 Score


#■ F척도를 구하시오 ~  (뎃글로 달아주세요 )
#위에서 구한 정밀도와 재현율을 아래의 변수에 각각 입력하여 구하시오 !


#1. F1 score 공식
# Fmeasure <- 2 * precision * recall / (precision + recall)

#2. 패키지를 이용하는 방법 
# install.packages("MLmetrics")
library(MLmetrics)
F1_Score(actual_type, predict_type, positive = positive_value)



#-------------------------------------
문제309.

#1. 데이터를 로드한다.

credit <- read.csv("credit.csv", stringsAsFactor=TRUE)
str(credit) 

#2. 데이터에 각 컬럼들을 이해한다. 

#라벨 컬럼 :  default  --->  yes : 대출금 상환 안함 
#no  : 대출금 상환 

prop.table( table(credit$default)  )
summary( credit$amount)

#3. 데이터가 명목형 데이터인지 확인해본다.

str(credit) 

#4. 데이터를 shuffle 시킨다.

set.seed(659)
credit_shuffle <-  credit[ sample( nrow(credit) ),  ]

#5. 데이터를 9 대 1로 나눈다.

train_num <- round( 0.9 * nrow(credit_shuffle), 0) 

credit_train <- credit_shuffle[1:train_num ,  ]

credit_test  <- credit_shuffle[(train_num+1) : nrow(credit_shuffle),  ]


#6. C5.0 패키지와 훈련 데이터를 이용해서 모델을 생성한다.

library(C50)

credit_model <- C5.0( credit_train[ ,-17] , credit_train[  , 17] , trials=100)

#7. 위에서 만든 모델을 이용해서 테스트 데이터의 라벨을 예측한다.

credit_result <-  predict( credit_model, credit_test[  , -17] )

#8. 이원 교차표로 결과를 확인한다.

library(gmodels)

CrossTable( credit_test[   , 17], credit_result )




#■ 실제값과 예측값 대입

credit_test_prob <- predict(credit_model, credit_test[   , -17], type = "prob")


credit_test_prob


# combine the results into a data frame

credit_results <- data.frame(actual_type =credit_test[  , 17],
                             predict_type = credit_result,
                             prob_yes = round(credit_test_prob[ , 2], 5),
                             prob_no = round(credit_test_prob[ , 1], 5))



credit_results


#3. 예측 데이터 프레임을 csv 로 저장합니다.

# uncomment this line to output the sms_results to CSV

write.csv(credit_results, "final_results.csv", row.names = FALSE)



#■ 실제값과 예측값 대입

actual_type <- credit_test[  , 17]
predict_type <-  credit_result
positive_value <- 'yes'
negative_value <- 'no'


#■ ROC 곡선 그리기 

#install.packages("ROCR")
library(ROCR)
head(credit_results) # 3번째 컬럼과 4번째컬럼의 확률을 확인한다.
pred <- prediction(predictions = credit_results$prob_yes,              
                   labels = credit_results$actual_type)
pred 

# ROC curves

perf <- performance(pred, measure = "tpr", x.measure = "fpr")

plot(perf, main = "ROC curve for SMS spam filter", col = "blue", lwd = 2)

# add a reference line to the graph
# 대각선 출력 

abline(a = 0, b = 1, lwd = 2, lty = 2)

# calculate AUC
perf.auc <- performance(pred, measure = "auc")
str(perf.auc)
unlist(perf.auc@y.values)

library(MLmetrics)
F1_Score(actual_type, predict_type, positive = positive_value)



