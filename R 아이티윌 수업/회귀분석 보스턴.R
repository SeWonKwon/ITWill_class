normalize <- function(x) {
  return ( (x-min(x)) / (max(x) - min(x) ) )
}

traindata <- read.csv("b_train.csv")
testdata <- read.csv("b_test.csv")
str(traindata)
str(testdata)
head(traindata[2:14])
head(traindata[15])
head(testdata[1:14])

traindata_norm <- as.data.frame(lapply(traindata,normalize) )
traindata_norm2 <- cbind(traindata_norm[,2:14],traindata[15])
head(traindata_norm2)

testdata_norm <- as.data.frame(lapply(testdata,normalize) )
summary(traindata_norm)
summary(traindata)
colSums( is.na(traindata))
str(traindata$chas)
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

concrete <- read.csv("b_train.csv")
concrete <- traindata_norm
for (i in 1:length(colnames(concrete))){
  
  a = grubbs.flag(concrete[,colnames(concrete)[i]])
  b = a[a$Outlier==TRUE,"Outlier"]
  print ( paste( colnames(concrete)[i] , '--> ',  length(b) )  )
  
}

traindata
summary(traindata)
colnames(traindata)
colnames(testdata)

library(neuralnet) 
colnames(traindata)
data_model <- neuralnet(formula= medv ~ 
                          crim + zn + indus + chas + nox +
                          rm + age + dis +
                          rad + tax + ptratio + black + lstat ,  
                        data =traindata_norm)   
unnoromlize <- function(x) {
                        x*(max(traindata$medv)-min(traindata$medv))
                        + min(traindata$medv)
                            }
unnoromlize2 <- function(x) {
                      x*45+ 5 }
unnoromlize2(0.45)
plot(data_model)
data_model

nrow(traindata)
nrow(testdata)

head(traindata[2:15])

head(testdata_norm[1:14])
model_results <-  compute(data_model, testdata_norm[2:14])
model_results

predicted_medv <-  model_results$net.result
predicted_medv

model_results
model_results2 <- as.data.frame(lapply(model_results$net.result,unnoromlize2) )
model_results2
model_results2 <- as.array(model_results2,nrow=1)
last_result <- as.data.frame(cbind(testdata[1],model_results2))
last_result
cor(predicted_strength, concrete_test$strength)


concrete_model2 <- neuralnet(formula=strength ~ cement + slag + ash  +
                               water +superplastic + coarseagg  + fineagg  + age,
                             data =concrete_train , hidden=c(7:2) )  
plot(concrete_model2)

head(concrete_test[1:8])
model_results <-  compute(concrete_model2, concrete_test[1:8])
predicted_strength2 <-  model_results$net.result
cor(predicted_strength2, concrete_test$strength)

concrete_model2 <- neuralnet(formula=strength ~ cement + slag + ash  +
                               water +superplastic + coarseagg  + fineagg  + age,
                             data =concrete_train , hidden=c(5:2) )  
plot(concrete_model2)


model_results <-  compute(concrete_model2, concrete_test[1:8])
predicted_strength2 <-  model_results$net.result
cor(predicted_strength2, concrete_test$strength)
