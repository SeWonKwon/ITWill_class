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
mymodel <- svm(admit~gpa+rank, data=data_bi, kenel="polynomial")
summary(mymodel)

pred <- predict(mymodel, data_bi)

tab <- table(Predicted = pred, Actual = data_bi$admit)
tab
1- sum(diag(tab))/sum(tab)
# 0.2775

#3. 성능개선

set.seed(13)
tmodel <- tune( svm, admit~., data=data_bi,
                range=list(epsilon=seq(0.5,1,0.1), cost=3^(1:3) ),
                kernel = "radial",
                type = "C-classification") 
plot(tmodel) # cost=29 epsilon= 0.9
summary(tmodel)

#best model 
tmodel$best.model
mymodel <- tmodel$best.model
summary(mymodel)

pred <- predict(mymodel, data_bi)
tab <- table(Predicted = pred, Actual = data_bi$admit)
tab
1- sum(diag(tab))/sum(tab)

# 0.265

#4. 자동 튜닝

#2. 랜덤 포레스트를 이용해서 훈련을 시키는데 자동파라미터 튜닝도 같이 진행합니다. 
m <- train( admit~ . , data=data_bi, method="svmLinear" )
m <- train( admit~ . , data=data_bi, method="svmRadial" )
m
m$bestTune

p <- predict( m , data_bi )
table(p, data_bi$admit)


library(gmodels)
y <- CrossTable(data_bi$admit ,p)
y
sum(y$prop.tbl * diag(2))
# 0.682

#%% 준혁이 코드

bi<- read.csv("binary.csv", stringsAsFactors = T)
summary(bi)
str(bi)
bi$admit<- factor(data_bi$admit,
                       levels=c(0,1),
                       labels=c('Yes','No'))


library(e1071)
support <- svm(admit~., data=bi, type = "C-classification", kernel = "radial",
               cost = 29, gamma = 0.9)
summary(support)
plot(support, data=bi, gpa ~ gre, 
     slice=list(rank=1))
str(bi)

pred <- predict(support, bi)

tab <- table(Predicted=pred, Actual = bi$admit)
tab

1-sum(diag(tab))/sum(tab)
