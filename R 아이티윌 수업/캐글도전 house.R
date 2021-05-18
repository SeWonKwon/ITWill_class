#0. 데이터 로드
d_r_train <- read.csv("c:\\data\\house_k\\train.csv")
d_r_test <- read.csv("c:\\data\\house_k\\test.csv")
d_r_train
d_r_test

#1. 데이터 체크
str(d_r_train)
str(d_r_test)
View(d_r_train)
summary(d_r_train)
mean(d_r_train$SalePrice) # 종속변수
colSums(is.na(d_r_train))
colSums(is.na(d_r_test))

x11()
plot(d_r_train$SalePrice,d_r_train$MSSubClass)








#상관 관계 보기
library(corrplot)