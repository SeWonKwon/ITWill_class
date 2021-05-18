normalize <- function(x) {
  return ( (x-min(x)) / (max(x) - min(x) ) )
}
unnormalize <- function(x) { return ( x*45 + 5)}
traindata <- read.csv("b_train.csv")
testdata <- read.csv("b_test.csv")
summary(traindata)
traindata_norm <- as.data.frame(lapply(traindata,normalize) )
testdata_norm <- as.data.frame(lapply(testdata,normalize) )
str(traindata_norm)
colnames(traindata_norm)
colnames(testdata_norm)
ncol(testdata_norm)
boxplot(traindata)

# traindata_norm2 <- cbind(traindata_norm[,2:14],traindata[15])


library(neuralnet) 

# boston_model <- neuralnet(formula = medv ~ crim + zn + indus+
#                             chas + nox + rm + age+
#                             dis + rad + + tax + ptratio +
#                             black + lstat ,
#                             data = traindata_norm,  hidden = c(6,3) , stepmax =1000000, learningrate =0.02)
# test3

# boston_model <- neuralnet(formula = medv ~ crim + zn + indus+  
#                              chas + nox + rm + age+
#                              dis + rad + + tax + ptratio +
#                              black + lstat ,  
#                            data = traindata_norm,  hidden = c(8,6,3) , stepmax =1000000, learningrate =0.001)   

#test4
# boston_model <- neuralnet(formula = medv ~ crim + zn + indus+  
#                             chas + nox + rm + age+
#                             dis + rad + + tax + ptratio +
#                             black + lstat ,  
#                           data = traindata_norm,  hidden = c(8,4) , stepmax =1000000, learningrate =0.01)   

#test5

# boston_model <- neuralnet(formula = medv ~ crim + zn + indus+
#                             chas + nox + rm + age+
#                             dis + rad + + tax + ptratio +
#                             black + lstat ,
#                             data = traindata_norm,  hidden = c(7,4) , stepmax =1000000, learningrate =0.02)
# # test6
# 
# boston_model <- neuralnet(formula = medv ~ crim + zn + indus+
#                             chas + nox + rm + age+
#                             dis + rad + + tax + ptratio +
#                             black + lstat ,
#                           data = traindata_norm,  hidden = c(6,3) , 
#                           act.fct = 'tanh',
#                           stepmax =1000000, 
#                           learningrate =0.02)
# test7

boston_model <- neuralnet(formula = medv ~ crim + zn + indus+
                            chas + nox + rm + age+
                            dis + rad + + tax + ptratio +
                            black + lstat ,
                            data = traindata_norm,  hidden = c(6,3) , stepmax =1000000, learningrate =0.02)
# test8

boston_model <- neuralnet(formula = medv ~ crim + zn + indus+
                            chas + nox + rm + age+
                            dis + rad + + tax + ptratio +
                             lstat ,
                          data = traindata_norm,  hidden = c(6,3) , stepmax =1000000, learningrate =0.02)
# test9

boston_model <- neuralnet(formula = medv ~ crim + zn + indus+
                            chas + nox + rm + age+
                            dis + rad + tax + ptratio +
                            lstat ,
                          data = traindata_norm,  hidden = c(9,4) , stepmax =1000000, learningrate =0.02)
# test10

boston_model <- neuralnet(formula = medv ~ crim + zn + indus+
                            chas + nox + rm + age+
                            dis + rad +  tax + ptratio +
                            black + lstat ,
                          data = traindata_norm,  hidden = c(13,6,3) ,
                          
                          stepmax =1000000,
                          learningrate =0.02)
plot(boston_model )

# test11
boston_model <- lnet(formula = medv ~ crim + zn + indus+
                            chas + nox + rm + age+
                            dis + rad +  tax + ptratio +
                            black + lstat ,
                          data = traindata_norm,  hidden = c(13,6,3) ,
                          
                          stepmax =1000000,
                          learningrate =0.01)
plot(boston_model )

#test12

boston_model <- lnet(formula = medv ~ crim + zn + indus+
                       chas + nox + rm + age+
                       dis + rad +  tax + ptratio +
                       black + lstat ,
                     data = traindata_norm,  hidden = c(10,5,2) ,
                     
                     stepmax =1000000,
                     learningrate =0.03)
plot(boston_model )
#test13

boston_model <- neuralnet(formula = medv ~ crim + zn + indus+
                            chas + nox + rm + age+
                            dis + rad + tax + ptratio + 
                             lstat ,
                            data = traindata_norm,  hidden = c(6,3) , stepmax =1000000, learningrate =0.02)
# test14
boston_model <- neuralnet(formula = medv ~ crim + zn + indus+
                            chas + nox + rm + age+
                            dis + rad + tax + ptratio + black
                            lstat ,
                          data = traindata_norm,  hidden = c(8,4) , stepmax =1000000, learningrate =0.02)
# test15
boston_model <- neuralnet(formula = medv ~ crim + zn + indus+
                            chas + nox + rm + age+
                            dis + rad + tax + ptratio +
                            black + lstat ,
                            data = traindata_norm,  hidden = c(6,3) , stepmax =1000000, learningrate =0.02)
# test16
boston_model <- neuralnet(formula = medv ~ crim + zn + indus+
                            chas + nox + rm + age+
                            dis + rad + tax + ptratio +
                            black + lstat ,
                          data = traindata_norm,  hidden = c(6,3) , stepmax =1000000, learningrate =0.03)
# test 17 
boston_model <- neuralnet(formula = medv ~ crim + zn + indus+
                            chas + nox + rm + age+
                            dis + rad + tax + ptratio +
                            black + lstat ,
                          data = traindata_norm,  hidden = c(6,3) , stepmax =1000000, learningrate =0.012)
# test18
boston_model <- neuralnet(formula = medv ~ crim + zn + indus+
                            chas + nox + rm + age+
                            dis + rad + tax + ptratio +
                            black + lstat ,
                          data = traindata_norm,  hidden = c(7,3) , stepmax =1000000, learningrate =0.018)
# test19
boston_model <- neuralnet(formula = medv ~ crim + zn + indus+
                            chas + nox + rm + age+
                            dis + rad + tax + ptratio +
                            black + lstat ,
                          data = traindata_norm,  hidden = c(6,2) , stepmax =1000000, learningrate =0.02)
# test20
boston_model <- neuralnet(formula = medv ~ crim + zn + indus+
                            chas + nox + rm + age+
                            dis + rad + tax + ptratio +
                            black + lstat ,
                          data = traindata_norm,  hidden = c(7,3) , stepmax =1000000, learningrate =0.02)
# test21

boston_model <- neuralnet(formula = medv ~ crim + zn + indus+
                            chas + nox + rm + age+
                            dis + rad + tax + ptratio +
                            black + lstat ,
                          data = traindata_norm,  hidden = c(7,4) , stepmax =1000000, learningrate =0.02)
# test22

boston_model <- neuralnet(formula = medv ~ crim + zn + indus+
                            chas + nox + rm + age+
                            dis + rad + tax + ptratio +
                            black + lstat ,
                          data = traindata_norm,  hidden = c(6,3) , stepmax =1000000, learningrate =0.02)
# test23

boston_model <- neuralnet(formula = medv ~ crim + zn + indus+
                            chas + nox + rm + age+
                            dis + rad + tax + ptratio +
                            black + lstat ,
                          data = traindata_norm,  hidden = c(8,4) , stepmax =1000000, learningrate =0.02)

#test24

boston_model <- neuralnet(formula = medv ~ crim + zn + indus+
                            chas + nox + rm + age+
                            dis + rad + tax + ptratio +
                            black + lstat ,
                          data = traindata_norm,  hidden = c(8,2) , stepmax =1000000, learningrate =0.02)

#test25

boston_model <- neuralnet(formula = medv ~ crim + zn + indus+
                            chas + nox + rm + age+
                            dis + rad + tax + ptratio +
                            black + lstat ,
                          data = traindata_norm,  hidden = c(8,6,2) , stepmax =1000000, learningrate =0.01)

#test28


model_results <-  compute(boston_model, testdata_norm[2:14])

model_results

predicted_medv <-  model_results$net.result

# predicted_medv_unnorm <- as.data.frame(lapply(model_results$net.result,unnormalize) )
# as.data.frame(predicted_medv_unnorm)

result <- data.frame( ID = testdata$ID, MEDV = predicted_medv)
result$MEDV <-  (lapply(result$MEDV,unnormalize) )

result$MEDV <- vapply(result$MEDV, paste, collapse = ", ", character(1L))
result

cat( , file = "c:\\data\\0001.txt") 
write.table(result, "c:\\data\\0001.txt", 
                          sep = ",", 
                         row.names = FALSE, 
                           quote = FALSE, 
                           append = TRUE)

test3 <- result
test4 <- result
test5 <- result
test6 <- result
test7 <- result
test8 <- result
test3
test4
test5
test6
test7
test8
c(test3$MEDV,test4$MEDV)
