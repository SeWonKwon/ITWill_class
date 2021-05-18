


credit <- read.csv("credit.csv", stringsAsFactor=TRUE)
str(credit) 


prop.table( table(credit$default)  )
summary( credit$amount)
str(credit) 

# set.seed(31)
credit_shuffle <-  credit[ sample( nrow(credit) ),  ]

train_num <- round( 0.9 * nrow(credit_shuffle), 0) 

credit_train <- credit_shuffle[1:train_num ,  ]

credit_test  <- credit_shuffle[(train_num+1) : nrow(credit_shuffle),  ]
library(ipred)
# set.seed(300)

# mybag <- bagging( default ~ . , data=credit_train, nbagg=25)
mybag <- bagging( default ~ . , data=credit_train, nbagg=50)
mybag

credit_pred <- predict( mybag,  credit_test[   , -17] )
credit_pred

table( credit_pred, credit_test$default ) 
prop.table(  table( credit_pred==credit_test$default)  )


#■ 정확도
library(gmodels)
g <- CrossTable( credit_test$default, credit_pred )

x <- sum(g$prop.tbl *diag(2))   # 정확도 확인하는 코드
x


# 문제1. bag 의 갯수를 50개로 늘리고 확인해 봅니다.


mybag <- bagging( default ~ . , data=credit_train, nbagg=50)
