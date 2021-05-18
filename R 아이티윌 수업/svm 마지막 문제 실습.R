
# 데이터 로드
bi <- read.csv("binary.csv")
head(bi)
str(bi)

# 종속변수를 factor형으로 변환
bi$admit <- factor(bi$admit,, labels = c("Y", "N"))
str(bi)


# 커널 변경
library(e1071)
library(vcd)
a<-c()
b<-c()
c<-c()
d<-c()

for(i in c(120:130)){
for (j in seq(7,9,0.1)){
support <- svm(admit~., data=bi, type = "C-classification",
               kernel = "radial",
               cost = i, gamma = j)
# summary(support)
# plot(support, data=bi, gpa ~ gre, 
#      slice=list(rank=1))
# str(bi)

pred <- predict(support, bi)

tab <- table(Predicted=pred, Actual = bi$admit)
# tab

t<-sum(diag(tab))/sum(tab)
k<-Kappa( table( bi$admit, pred)  )

a<- append(a,i)
b<- append(b,j)
c<- append(c,t)
d<- append(d,k$Unweighted[1])

}}


result <- data.frame(cost=a,gamma=b,accu=c,kappa=d)
max(result$accu)
min(result$accu)
View(result)
View(result[result$accu==max(result$accu)&result$kappa==max(result$kappa),])
-----------------------------------------------------------------------------
library(e1071)
library(vcd)
library(caret)  
# 데이터 로드
bi <- read.csv("binary.csv")

# 종속변수를 factor형으로 변환
bi$admit <- factor(bi$admit,, labels = c("Y", "N"))
# 셔플
set.seed(123)
bi_shuffle <- bi[sample(nrow(bi)),]
# 
set.seed(123)
folds <- createFolds(bi_shuffle$admit, k = 10)


a<-c()
b<-c()
c<-c()
d<-c()

for(i in c(1:40,2)){
  for (j in seq(0,3,0.1)){
    
    cv_results <- sapply(folds, function(x) {
    bi_train <- bi_shuffle[-x, ]
    bi_test <- bi_shuffle[x, ]
    support <- svm(admit~., data=bi_train, type = "C-classification",
                   kernel = "radial",
                   cost = i, gamma = j)
    pred <- predict(support, bi_test)
    bi_actual <- bi_test$admit
    ka <- kappa(table(bi_actual, pred))
    
    x<-data.frame(bi_actual,pred)
    y <-sum(x$bi_actual==x$pred)/length(x$bi_actual)
    
    return(c(y,ka[1]))
    })
    cv<- matrix(unlist(cv_results),nrow=2,ncol=10)
    t<-apply(cv,1,mean)[1]
    k<-apply(cv,1,mean)[2]
    
    a<- append(a,i)
    b<- append(b,j)
    c<- append(c,t)
    d<- append(d,k)
    
  }}

result <- data.frame(cost=a,gamma=b,accu=c,kappa=d)
result_accu<- result[result$accu==max(result$accu),]
View(result_accu[result_accu$kappa==max(result_accu$kappa),]) 
#	cost gamm  aaccu     kappa
# 12  0.3   0.7173765  0.2066329
result_kappa <- result[result$kappa==max(result$kappa),]
View(result_kappa[result_kappa$accu==max(result_kappa$accu),])
#	cost gamm  aaccu     kappa
# 6    2.6  0.6920528  0.2265648



-------------------------------------
#자동 성능 개선

bi <- read.csv("binary.csv")
head(bi)
str(bi)

# 종속변수를 factor형으로 변환
bi$admit <- factor(bi$admit,, labels = c("Y", "N"))
str(bi)

m <- train(admit~., data= bi, method="svmRadial")
m
m$bestTune

-----------------------------------------
  
  
  # 데이터 로드
bi <- read.csv("binary.csv")
head(bi)
str(bi)

# 종속변수를 factor형으로 변환
bi$admit <- factor(bi$admit,, labels = c("Y", "N"))
str(bi)


# 커널 변경
library(e1071)
support <- svm(admit~., data=bi, type = "C-classification", kernel = "radial",
               cost = 12, gamma = 0.3)

pred <- predict(support, bi)

tab <- table(Predicted=pred, Actual = bi$admit)
tab

sum(tab*diag(2))/sum(tab)
k<-Kappa( table( bi$admit, pred)  )
kappa<- kappa(tab)
kappa[1]
k


kappa


1-sum(diag(tab))/sum(tab)


