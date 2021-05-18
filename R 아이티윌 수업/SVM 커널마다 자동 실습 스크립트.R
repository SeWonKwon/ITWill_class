
library(e1071)
library(vcd)
binary <- read.csv("binary.csv")
binary$admit <- factor( binary$admit, labels=c("Y", "N"))

set.seed(1)
library(caret)
k <- createDataPartition(binary$admit, p=0.80, list=F)
trainset <- binary[k, ]
testset <- binary[-k, ]
nrow(trainset)    #301
nrow(testset)

kernel_list = c("linear","polynomial","sigmoid","radial")

for ( i in kernel_list){
set.seed(123)
tmodel <- tune( svm, admit~. , data=trainset, kernel=i, 
                range=list(epsilon=seq(0,1,0.2), cost=2^(2:5) )) 

mymodel <- tmodel$best.model

pred <- predict(mymodel, testset)
tab <- table(Predicted = pred, Actual = testset$admit)

a<-(1- sum(diag(tab))/sum(tab))
b<-Kappa( tab )

print(data.frame(kernel=i, error=a, kappa=b$Unweighted[1])) }


