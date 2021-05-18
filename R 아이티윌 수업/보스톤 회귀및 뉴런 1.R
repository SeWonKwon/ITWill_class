traindata <- read.csv("b_train.csv")
testdata <- read.csv("b_test.csv")


traindata_norm <- traindata
testdata_norm <- testdata


library(neuralnet) 

boston_model <- neuralnet(formula = medv ~ crim + zn + indus+
                            chas + nox + rm + age+
                            dis + rad + tax + ptratio +
                            black + lstat ,
                          data = traindata_norm, learningrate = 0.0000001)
plot(boston_model)

boston_model <- neuralnet(formula = medv ~ crim  ,
                          data = traindata_norm, learningrate = 0.0000001)

model_results <-  compute(boston_model, testdata_norm[2:14])

model_results

predicted_medv <-  model_results$net.result

result <- data.frame( ID = testdata$ID, MEDV = predicted_medv)
result$MEDV <-  (lapply(result$MEDV,unnormalize) )

result$MEDV <- vapply(result$MEDV, paste, collapse = ", ", character(1L))
result

cat( , file = "c:\\data\\boston_test19.txt") 
write.table(result, "c:\\data\\boston_test19.txt", 
            sep = ",", 
            row.names = FALSE, 
            quote = FALSE, 
            append = TRUE)




------------------------------------------------------
  
  

  library(psych)
pairs.panels( traindata[ ,-1] )


install.packages("corrplot")
library(corrplot)

boston_cor <- cor(traindata[,-1])
boston_cor
corrplot(boston_cor, method="circle")
corrplot(boston_cor, method="number")

str(traindata)


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

wisc <- read.csv("b_train.csv")
wisc$chas <- as.integer(wisc$chas)
str(wisc$chas)
mode(wisc$chas)
class(wisc$chas)
for (i in 1:length(colnames(wisc))){
  
  a = grubbs.flag(wisc[,colnames(wisc)[i]])
  b = a[a$Outlier==TRUE,"Outlier"]
  print ( paste( colnames(wisc)[i] , '--> ',  length(b) )  )
  
}
example(xor)
