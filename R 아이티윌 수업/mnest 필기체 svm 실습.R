# https://cafe.daum.net/oracleoracle/SeFi/596

### [쉬움주의] 컴퓨터가 사람이 쓴 필기체를 이해할 수 있도록 학습시킬려면 ?

# install.packages("caret")
install.packages("doParallel")
# install.packages("kernlab")
# install.packages("ggplot2")
# install.packages("lattice")

library(ggplot2)
library(lattice)
library(kernlab)
library(caret)
library(doParallel)

# Enable parallel processing.

cl <- makeCluster(detectCores())
registerDoParallel(cl)
cl
# Load the MNIST digit recognition dataset into R
# http://yann.lecun.com/exdb/mnist/
# assume you have all 4 files and gunzip'd them
# creates train$n, train$x, train$y  and test$n, test$x, test$y
# e.g. train$x is a 60000 x 784 matrix, each row is one digit (28x28)
# call:  show_digit(train$x[5,])   to see a digit.
# brendan o'connor - gist.github.com/39760 - anyall.org

load_mnist <- function() {
  load_image_file <- function(filename) {
  ret = list()
  f = file(filename,'rb')
  readBin(f,'integer',n=1,size=4,endian='big')
  ret$n = readBin(f,'integer',n=1,size=4,endian='big')
  nrow = readBin(f,'integer',n=1,size=4,endian='big')
  ncol = readBin(f,'integer',n=1,size=4,endian='big')
  x = readBin(f,'integer',n=ret$n*nrow*ncol,size=1,signed=F)
  ret$x = matrix(x, ncol=nrow*ncol, byrow=T)
  close(f)
  ret
    
  }
  
  load_label_file <- function(filename) {
      f = file(filename,'rb')
      readBin(f,'integer',n=1,size=4,endian='big')
      n = readBin(f,'integer',n=1,size=4,endian='big')
      y = readBin(f,'integer',n=n,size=1,signed=F)
      close(f)
      y
    
  }
  
  train <<- load_image_file('train-images.idx3-ubyte')
  test <<- load_image_file('t10k-images.idx3-ubyte')
  train$y <<- load_label_file('train-labels.idx1-ubyte')
  test$y <<- load_label_file('t10k-labels.idx1-ubyte')  
  
  }

show_digit <- function(arr784, col=gray(12:1/12), ...) {
  image(matrix(arr784, nrow=28)[,28:1], col=col, ...)
  }

# 훈련데이터와 테스트 데이터를 구성하기 위한 데이터 프레임 생성
train <- data.frame()
test <- data.frame()

# Load data.

load_mnist()

length(train$y)
length(test$y)

# Normalize: X = (X - min) / (max - min) => X = (X - 0) / (255 - 0) => X = X / 255.

train$x <- train$x / 255

# Setup training data with digit and pixel values with 60/40 split for train/cv.

inTrain = data.frame(y=train$y, train$x)
inTrain$y <- as.factor(inTrain$y)
str(inTrain)
# 훈련데이터 6만개를 60%, 40%로 나눠서 6은 
# 훈련시킬때 쓰고 4는 테스트 할 때 쓰려고 나눈다.
trainIndex = createDataPartition(inTrain$y, p = 0.60,list=FALSE)
training = inTrain[trainIndex,]
cv = inTrain[-trainIndex,]
nrow(training)
nrow(cv)
# SVM. 95/94.

fit <- train(y ~ ., data = head(training, 1000), method = 'svmRadial', tuneGrid = data.frame(sigma=0.0107249, C=1))
results <- predict(fit, newdata = head(cv, 1000))
results

confusionMatrix(results, head(cv$y, 1000))

show_digit(as.matrix(training[5,2:785]))

# Predict the digit.

predict(fit, newdata = training[5,])

# Check the actual answer for the digit.

training[5,1]

# 문제. 훈련 데이터의102 번째 행이 무엇인지 확인하고 만든 svm 모델에 102번째 훈련
# 데이터를 넣고 무엇으로 예측하는지 확인하시오 !

show_digit(as.matrix(training[102,2:785]))
# Predict the digit.
predict(fit, newdata = training[102,])
# Check the actual answer for the digit.
training[102,1]



