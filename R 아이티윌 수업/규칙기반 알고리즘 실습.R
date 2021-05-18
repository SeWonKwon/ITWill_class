# 1. 버섯 데이터를 R 로 로드한다.

mushroom <- read.csv("mushrooms.csv", stringsAsFactors=T)
head(mushroom)
dim(mushroom) # 8124개의 버섯샘플, 23개의 컬럼중 22개의 특징
str(mushroom)
# 2. mushroom 데이터를 훈련 데이터와 테스트 데이터로 나눈다 
# ( 훈련 데이터 75%,  테스트 데이터 25% ) 

set.seed(11) # 하이퍼 파라미터
train_cnt <- round( 0.75 * dim(mushroom)[1])
train_index <- sample(1:dim(mushroom)[1], train_cnt, replace=F)
# 1 ~ 8124까지의 숫자를 6093번 비복원 추출합니다.
mushroom_train <- mushroom[train_index,  ]
mushroom_test  <- mushroom[-train_index, ]
nrow(mushroom_train)
nrow(mushroom_test)
# 3. 규칙기반 알고리즘인 oneR 을 이용해서 독버섯과 일반버섯을 분류하는 모델을 생성한다.

# install.packages("OneR")
library(OneR) # 한가지 조건만 가지고 분류하는 알고리즘

model1 <- OneR(type~. ,  data=mushroom_train)
model1
summary(model1)# 설명: 버섯 냄새 하나만 가지고 버섯을 분류하고 있습니다.

# 4. 위에서 생성한 모델을 가지고 테스트 데이터로 결과를 확인한다.

result1 <- predict( model1, mushroom_test[   , -1] )
library(gmodels)
g<-CrossTable( mushroom_test[ , 1],  result1)  
g$prop.tbl


#문제214. 위의 모델의 정확도를 출력하세요~

sum(g$prop.tbl*diag(2)) # [1] 

table(mushroom$odor, mushroom$type)

table(mushroom$cap_shape, mushroom$type)

# 예제1. 독버섯 데이터의 컬럼들의 정보획득량을 확인하세요!
library(FSelector)
w1 <- information.gain(type~., mushroom,unit="log2")
w1

#문제215. 위의 결과를 다시 출력하는데 정보획득량이 높은것 부터 출력되게 하시오 !

library(doBy) 
orderBy( ~ -attr_importance, w1)

#▦규칙기반 알고리즘 실습( Riper 알고리즘 ) p243

#install.packages("RWeka")
library(RWeka)
model2 <-  JRip(type~ ., data=mushroom_train)
model2

summary(model2)  
# 작은 이원교차표가 하나 보임 
result2 <- predict( model2, mushroom_test[   , -1] )
library(gmodels)
CrossTable( mushroom_test[ , 1],  result2) 

# JRIP rules:
#   ===========
#   
# (odor = foul) => type=poisonous (1639.0/0.0)
# (gill_size = narrow) and (gill_color = buff) => type=poisonous (883.0/0.0)
# (gill_size = narrow) and (odor = pungent) => type=poisonous (196.0/0.0)
# (odor = creosote) => type=poisonous (134.0/0.0)
# (spore_print_color = green) => type=poisonous (56.0/0.0)
# (stalk_surface_below_ring = scaly) and (stalk_surface_above_ring = silky) => type=poisonous (48.0/0.0)
# (habitat = leaves) and (cap_surface = scaly) and (population = clustered) => type=poisonous (10.0/0.0)
# (cap_surface = grooves) => type=poisonous (2.0/0.0)
# 위의 8가지 규칙이 독버섯이다.
# => type=edible (3125.0/0.0) 나머지는 식용이다.


# 정확도 100%에 해당하는 결과

문제216. (까페에 답글로 올려주세요 ) 와인 데이터를 Riper 알고리즘으로 
분류하는 머신러닝 모델을 생성하고 정확도를 확인하세요!
  
wine <- read.csv("wine.csv", header= T, stringsAsFactors = T)
summary(wine)
str(wine)
dim(wine)

temp<- c()
temp2 <-c()
i<-0
repeat { 
  i<- i+1
set.seed(i) 
train_cnt <- round( 0.75 * dim(wine)[1])
train_index <- sample(1:dim(wine)[1], train_cnt, replace=F)

wine_train <- wine[train_index,  ]
wine_test  <- wine[-train_index, ]
nrow(wine_train)

model3 <-  JRip(Type~ ., data=wine_train)
model3

summary(model3)  

result3 <- predict( model3, wine_test[   , -1] )
library(gmodels)
g2 <- CrossTable( wine_test[ , 1],  result3) 
j <- sum(g2$prop.tbl*diag(3))

print(c(i,j))
if(j>=0.98) # 목표 정확도 설정
{print(c(i,j)) 
break }
else if( i==1200) # 목표 정확도에 도달하지 못했다면 최고값
{result <- data.frame( 'seed'= temp2, '정확도'= temp)
print(result[result$정확도==max(result$정확도),])
break}
}

wine <- read.csv("wine.csv", header= T, stringsAsFactors = T)
summary(wine)
str(wine)
dim(wine)


set.seed(4) 
train_cnt <- round( 0.80 * dim(wine)[1])
train_index <- sample(1:dim(wine)[1], train_cnt, replace=F)
  
wine_train <- wine[train_index,  ]
wine_test  <- wine[-train_index, ]
nrow(wine_train)
  
model3 <-  JRip(Type~ ., data=wine_train)
model3
  
summary(model3)  
  
result3 <- predict( model3, wine_test[   , -1] )
library(gmodels)
g2 <- CrossTable( wine_test[ , 1],  result3) 
j <- (g2$prop.tbl*diag(3))
print(j)
print(sum(j))

model1 <- OneR(Type~. ,  data=wine_train)
model1
summary(model1)# 설명: 버섯 냄새 하나만 가지고 버섯을 분류하고 있습니다.

# 4. 위에서 생성한 모델을 가지고 테스트 데이터로 결과를 확인한다.

result1 <- predict( model1, wine_test[   , -1] )
library(gmodels)
g<-CrossTable( wine_test[ , 1],  result1)  
g$prop.tbl


# 신성이 코드

##0. repeat
accuracy <- c()
seed <- c()
i <- 1
repeat {
  set.seed(i)
  seed <- append(seed, i)
  #------------------------------------------------------------------------------------------------------------
  ##1. Load data 
  wine <- read.csv("wine.csv", header=T, stringsAsFactor=T)
  
  ##2. Check data
  str(wine)    #'data.frame': 178 obs. of  14 variables:
  #label column : $ Type           : Factor w/ 3 levels "t1","t2","t3": 1 1 ...
  
  
  ##3. set train_data : test_data = 0.75 : 0.25
  library(caret)
  #set.seed(49)    #hyper parameter
  k <- createDataPartition(wine$Type, p=0.75, list=F)
  train_data <- wine[k,  ]
  test_data <- wine[-k,  ]
  
  
  ##4. Make model / pred
  library(RWeka)
  model <- JRip(Type~. , data=train_data)
  summary(model)
  
  
  ##5. Pred with test_data : CrossTable
  res <- predict( model, test_data[  ,-1])
  
  library(gmodels)
  g <- CrossTable( test_data[ , 1],  res)
  x <- sum(g$prop.tbl *diag(3))   
  x    #[1] 1
  #------------------------------------------------------------------------------------------------------------
  ## repeat
  accuracy <- append(accuracy, x)
  temp <- data.frame(seed, accuracy)
  print(i)
  print(x)
  if (x==1 | i==1000) break
  i <- i+1
}
print(i)    #value : satisfying condition
#=============================================================

## Find hyper parameter
library(dplyr)
temp$rnk <- dense_rank(-temp$accuracy)
temp[temp$rnk==1,   ]    
View(temp)

# 문제218. (점심시간 문제 ) iris 데이터를 규칙 기반 알고리즘으로 분류하시오~
# 가장 적절한 seed 값을 신성이 코드로 알아내시오 ~~

data("iris")
iris
summary(iris)
str(iris)
dim(iris)

temp<- c()
temp2 <-c()
i<-0
repeat { 
  set.seed(i)
  i<-i+1
  train_index <- createDataPartition(iris$Species, p=0.75, list=F)
  train_index
  iris_train <- iris[train_index,  ]
  iris_test  <- iris[-train_index, ]
  iris_train
  table(iris_train$Species)
  library(RWeka)
  model <-  JRip(Species~ ., data=iris_train)
  model
  result <- predict( model, iris_test[   , -5] )
  library(gmodels)
  g2 <- CrossTable( iris_test[ , 5],  result) 
  j <- sum(g2$prop.tbl*diag(3))
  j
  temp <- append( temp,  j)
  temp2 <- append (temp2, i)
  print(c(i,j))
  if(j==1) 
  {print(c(i,j)) 
    break }
  else if( i==200) 
  {result2 <- data.frame( 'seed'= temp2, '정확도'= temp)
  print(result2[result2$정확도==max(result2$정확도),])
  break}
}

set.seed(2)
iris2 <- iris[sample(nrow(iris)),]
iris2

train_index <- createDataPartition(iris2$Species, p=0.75, list=F)


iris_train <- iris2[train_index,  ]
iris_test  <- iris2[-train_index, ]
iris_train
table(iris_train$Species)
train_index <- sample(1:dim(wine)[1], train_cnt, replace=F)
model <-  JRip(Species~ ., data=iris_train)
model

result <- predict( model, iris_test[   , -5] )
library(gmodels)
g2 <- CrossTable( wine_test[ , 5],  result3) 
j <- sum(g2$prop.tbl*diag(3))
j

