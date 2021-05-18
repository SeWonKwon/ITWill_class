실습 :  미국 대학원 입학 데이터를 로지스틱 회귀로 분류했을때와 서포트 벡터머신으로 분류 했을때의 차이 테스트

1. 로지스틱 회귀로 했을때 

# Logistic Regression

# Read data file
mydata <- read.csv("c:\\data\\binary.csv", header = T)
str(mydata)
mydata$admit <- as.factor(mydata$admit)
mydata$rank <- as.factor(mydata$rank)

# Two-way table of factor variables
xtabs(~admit + rank, data = mydata)

# Partition data - train (80%) & test (20%)
set.seed(1234)
ind <- sample(2, nrow(mydata), replace = T, prob = c(0.8, 0.2))
train <- mydata[ind==1,]
test <- mydata[ind==2,]

# Logistic regression model
mymodel <- glm(admit ~ gpa + rank, data = train, family = 'binomial')
summary(mymodel)

# Prediction
p1 <- predict(mymodel, train, type = 'response')
head(p1)
head(train)

# Misclassification error - train data
pred1 <- ifelse(p1>0.5, 1, 0)
tab1 <- table(Predicted = pred1, Actual = train$admit)
tab1
1 - sum(diag(tab1))/sum(tab1)

# Misclassification error - test data
p2 <- predict(mymodel, test, type = 'response')
pred2 <- ifelse(p2>0.5, 1, 0)
tab2 <- table(Predicted = pred2, Actual = test$admit)
tab2
1 - sum(diag(tab2))/sum(tab2)

# Goodness-of-fit test
with(mymodel, pchisq(null.deviance - deviance, df.null-df.residual, lower.tail = F))



#------------------------------------

###Caret Packages -- train() 
##0.1 Load data
binary <- read.csv("binary.csv")
binary$admit <- factor( binary$admit, labels=c("Y", "N"))
str(binary)
##0.2 Devide Db

set.seed(1)
library(caret)
k <- createDataPartition(binary$admit, p=0.80, list=F)
trainset <- binary[k, ]
testset <- binary[-k, ]
nrow(trainset)    #301
nrow(testset)    #99


##3. svmLinear ---------------------------------------------
# install.packages("kernlab")
library(kernlab)

ctrl <- trainControl(method="cv", number=10,
                     selectionFunction="oneSE")

grid <- expand.grid(C=c(1,2,3,4,5))

m <- train(admit~., data=trainset, method="",
           metric="Accuracy",
           trControl=ctrl,
           tunegrid=grid)
# svmRadial, svmPoly, svmLinear

m    #check model details


#predict
pred <- predict(m, testset)

#Definition of label column vector & Labeldata
actual_type <- testset$admit
predict_type <- pred
positive_val <- "Y"
negative_val <- "N"

#1) Accuracy
tab <- table(Predicted=pred, Actual=testset$admit)
tab
sum(diag(tab)) / sum(tab)    #testset_Accuracy

#2) Kappa statistics
#install.packages("vcd")
library(vcd)
table( actual_type, predict_type)
Kappa( table( actual_type, predict_type)  ) 


