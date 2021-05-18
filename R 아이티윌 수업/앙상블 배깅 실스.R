credit <- read.csv("credit.csv", stringsAsFactor=TRUE)
set.seed(31)
x<-0
l<-list()


a<-sample(1:1000,1)
set.seed(a)
credit_shuffle <-  credit[ sample( nrow(credit) ),  ]
train_num <- round( 0.9 * nrow(credit_shuffle), 0) 
credit_train <- credit_shuffle[1:train_num ,  ]
credit_test  <- credit_shuffle[(train_num+1) : nrow(credit_shuffle),  ]

# library(ipred)
mybag <- bagging( default ~ . , data=credit_train, nbagg=50) #bag = 50 개 

credit_pred <- predict( mybag,  credit_test[   , -17] )

# library(gmodels)
g <- CrossTable( credit_test$default, credit_pred )
x <- sum(g$prop.tbl *diag(2))
x

