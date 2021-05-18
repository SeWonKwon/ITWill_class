mushroom <- read.csv("mushrooms.csv", header=T, stringsAsFactors=TRUE)
View(mushroom)
summary(mushroom)
str(mushroom) # Factor 인지 확인

unique(mushroom$type)


table(mushroom$type)


prop.table(table(mushroom$type))

mush_test <- mushroom[8123, ]
mush_test 
write.csv( mush_test, "mush_test.csv",row.names=FALSE )

nrow(mushroom)
mushrooms <- mushroom[ -8123,  ] 
nrow(mushrooms)
 
for ( i in 1:10 ) { 
  for ( j in c(0.0005,0.0003,0.0001,0.00001)){
   set.seed(i)
 train_cnt <- round( 0.75*dim(mushrooms)[1] )
train_index <- sample( 1:dim(mushrooms)[1], train_cnt, replace=F)
 
  

  mushrooms_train <- mushrooms[ train_index,  ]
  mushrooms_test <- mushrooms[- train_index,  ] 

  library(e1071)         #모든 컬럼들
  model1 <- naiveBayes(type~ . ,  data=mushrooms_train)
  result1 <- predict( model1, mushrooms_test[  , -1] )
  library(gmodels)
  model2 <- naiveBayes(type~ . ,  data=mushrooms_train, laplace=j)
  result2 <- predict( model2, mushrooms_test[ , -1] )
  g3 <- CrossTable( mushrooms_test[ ,1], result2) 
 
  print(i)
  print(is.float(j))
  
  print( g3$prop.tb[1] + g3$prop.tb[4] )
  }
}  # 정확도

