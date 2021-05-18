
# ■ 7장. 서포트 벡터 머신 실습

#1. Data


data(iris)
str(iris)
library(ggplot2)
qplot( Petal.Length, Petal.Width, data=iris, color=Species)

#2. support Vector Machine

str1
library(e1071)
mymodel <- svm(Species~. , data=iris)
summary(mymodel)
plot(mymodel, data=iris, Petal.Width~Petal.Length,
     slice = list(Sepal.Width=3
                  , Sepal.Length=3.5))

#3. Confusion Matrix and Misclassification Error

pred <- predict(mymodel, iris)

tab <- table(Predicted = pred, Actual = iris$Species)
tab
1- sum(diag(tab))/sum(tab)

#4.커널변경1 (kernel="linear")

library(e1071)
mymodel <- svm(Species~. , data=iris , kenel="linear" )
summary(mymodel)
plot(mymodel, data=iris, Petal.Width~Petal.Length,
     slice = list(Sepal.Width=3, Sepal.Length=4))

pred <- predict(mymodel, iris)

tab <- table(Predicted = pred, Actual = iris$Species)
tab
1- sum(diag(tab))/sum(tab)

# 5. 커널변경2 (kernel="polynomial")
# 
# 관련 영상: https://www.youtube.com/watch?v=3liCbRZPrZA
# 




library(e1071)
mymodel <- svm(Species~. , data=iris , kenel="polynomial" )
summary(mymodel)
plot(mymodel, data=iris, Petal.Width~Petal.Length,
     slice = list(Sepal.Width=3, Sepal.Length=4))

pred <- predict(mymodel, iris)

tab <- table(Predicted = pred, Actual = iris$Species)
tab
1- sum(diag(tab))/sum(tab)


#6. 커널변경3 (kernel="sigmoid")

library(e1071)
mymodel <- svm(Species~. , data=iris , kenel="sigmoid" )
summary(mymodel)
plot(mymodel, data=iris, Petal.Width~Petal.Length,
     slice = list(Sepal.Width=3, Sepal.Length=4))

pred <- predict(mymodel, iris)

tab <- table(Predicted = pred, Actual = iris$Species)
tab
1- sum(diag(tab))/sum(tab)


#7. 성능개선

set.seed(123)
tmodel <- tune( svm, Species~. , data=iris, range=list(epsilon=seq(0,1,0.1), cost=2^(2:9) )) 
plot(tmodel)
summary(tmodel)

#best model 
mymodel <- tmodel$best.model
summary(mymodel)
plot( mymodel,  data=iris, Petal.Width~Petal.Length, slice=list(Sepal.Width=3, Sepal.Length=4))

pred <- predict(mymodel, iris)
tab <- table(Predicted = pred, Actual = iris$Species)
tab
1- sum(diag(tab))/sum(tab)

#오늘의 마지막 문제. 미국 대학원 입학 데이터를 서포트 벡터 머신으로 분류하고 정확 확인하시오 !


#1. Data
library(ggplot2)
data_bi<- read.csv("binary.csv", stringsAsFactors = T)
summary(data_bi)
str(data_bi)
data_bi$admit<- factor(data_bi$admit,
                          levels=c(0,1),
                          labels=c('Yes','No')
                          )
View(data_bi)
str(data_bi)
data_bi$admit

#2. support Vector Machine
library(e1071)
mymodel <- svm(admit~. , data=data_bi)
summary(mymodel)
# plot(mymodel, data=data_bi, gre~rank)
# plot(mymodel, data=data_bi, Petal.Width~Petal.Length,
#      slice = list(Sepal.Width=3, Sepal.Length=4))

#3. Confusion Matrix and Misclassification Error

pred <- predict(mymodel, data_bi)

tab <- table(Predicted = pred, Actual = data_bi$admit)
tab
1- sum(diag(tab))/sum(tab)

#4.커널변경1 (kernel="linear")

library(e1071)
mymodel <- svm(admit~. , data=data_bi, kenel="sigmoid" )
# mymodel <- svm(Species~. , data=iris , kenel="linear" )
summary(mymodel)
# plot(mymodel, data=iris, Petal.Width~Petal.Length,
     # slice = list(Sepal.Width=3, Sepal.Length=4))

pred <- predict(mymodel, data_bi)

tab <- table(Predicted = pred, Actual = data_bi$admit)
tab
1- sum(diag(tab))/sum(tab)


dd# 5. 커널변경2 (kernel="polynomial")
# 
# 관련 영상: https://www.youtube.com/watch?v=3liCbRZPrZA
# 




library(e1071)
mymodel <- svm(admit~. , data=data_bi, kenel="polynomial")
# mymodel <- svm(Species~. , data=iris , kenel="polynomial" )
summary(mymodel)
plot(mymodel, data=iris, Petal.Width~Petal.Length,
     slice = list(Sepal.Width=3, Sepal.Length=4))

pred <- predict(mymodel, data_bi)

tab <- table(Predicted = pred, Actual = data_bi$admit)
tab
1- sum(diag(tab))/sum(tab)


#6. 커널변경3 (kernel="sigmoid")

library(e1071)
mymodel <- svm(Species~. , data=iris , kenel="sigmoid" )
summary(mymodel)
plot(mymodel, data=iris, Petal.Width~Petal.Length,
     slice = list(Sepal.Width=3, Sepal.Length=4))

pred <- predict(mymodel, iris)

tab <- table(Predicted = pred, Actual = iris$Species)
tab
1- sum(diag(tab))/sum(tab)


#7. 성능개선

set.seed(123)
tmodel <- tune( svm, admit~. , data=data_bi, range=list(epsilon=seq(0,1,0.1), cost=2^(2:9) )) 
plot(tmodel)
summary(tmodel)

#best model 
tmodel$best.model
mymodel <- tmodel$best.model
summary(mymodel)
# plot( mymodel,  data=iris, Petal.Width~Petal.Length, slice=list(Sepal.Width=3, Sepal.Length=4))

pred <- predict(mymodel, data_bi)
tab <- table(Predicted = pred, Actual = data_bi$admit)
tab
1- sum(diag(tab))/sum(tab)

#오늘의 마지막 문제. 미국 대학원 입학 데이터를 서포트 벡터 머신으로 분류하고 정확 확인하시오 !
;





