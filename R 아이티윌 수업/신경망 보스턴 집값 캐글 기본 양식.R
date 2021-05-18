normalize <- function(x) {
  return ( (x-min(x)) / (max(x) - min(x) ) )
}

unnormalize <- function(x) { return ( x*45 + 5)}

traindata <- read.csv("b_train.csv")
testdata <- read.csv("b_test.csv")


traindata_norm <- as.data.frame(lapply(traindata,normalize) )
testdata_norm <- as.data.frame(lapply(testdata,normalize) )


library(neuralnet) 

boston_model <- neuralnet(formula = medv ~ crim + zn + indus+
                            chas + nox + rm + age+
                            dis + rad + tax + ptratio +
                            black + lstat ,
                            data = traindata_norm)

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