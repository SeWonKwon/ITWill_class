# 와인 데이터 로드
wine <- read.csv("wine.csv")

#1. wine 태이블 파악
head( wine )
nrow(wine)
unique(wine$Type)
summary(wine)
ncol(wine)
#데이터 소개


# 2. 정규화
normalize <- function(x) {
  return ( (x-min(x)) / (max(x) - min(x))  )
}

wine2  <- as.data.frame(lapply(wine[2:14],normalize))
wine2
summary(wine2)


# 3. 셔플 ( caret을 이용하면 셔플도 되기때문에 shuffle 작업은 안해줘도 된다. )
set.seed(62)
wine_shuffle <- wine[sample(nrow(wine2)),]
wine_shuffle

# 테스트 와 트레인 셋 구분 caret 이용
library(caret)
set.seed(62)                     # caret 도 seed 가 필요하다.
train_num <- createDataPartition( wine_shuffle$Type, p=0.8, list=F) # p=0.8 은 8:2로 나눈다.
str(train_num)
train_data <- wine2[train_num,]
test_data <- wine2[ -train_num,]
nrow(train_data)
nrow(test_data)

#※ 주의 사항 : knn 함수 실행시 train=, test= 에 데이터 프레임 넣을때 숫자만 있어야 합니다. 
# 트레인과 테스트 데이타에 Species 가 있으면 knn을 못 돌려서 확인해 본 작업이에요.
table(train_data$Type)
table(test_data$Type)
train_data$Type

# 라벨 지정 ( 정규화 되기전의 것을 이용한다.) 
wine_train_label <- wine[train_num,1]
wine_test_label <- wine[-train_num,1]
wine_test_label 


length(wine_train_label)
length(wine_test_label)
table(wine_train_label)
table(wine_test_label)


library(class) 
result1 <- knn(train=train_data, test=test_data,   cl=wine_train_label, k=7)

# 결과 확인
x <-  data.frame('실제'=wine_test_label, '예측'=result1)
table(x) 

library(gmodels)
g2 <-  CrossTable(x=wine_test_label, y=result1 )
g2$prop.tbl
print( g2$prop.tb[1] + g2$prop.tb[5] + g2$prop.tb[9] )  # 정확도
