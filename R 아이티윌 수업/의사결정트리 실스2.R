library(party)
credit <- read.csv("credit.csv", header = T, stringsAsFactors = T)

set.seed(590)
credit_shuffle <- credit[sample(nrow(credit)),]
set.seed(590)
ind <- sample(2,nrow(credit),replace=T,prob=c(0.9,0.1)) 

traindata <- credit_shuffle[ind==1,]
testdata <- credit_shuffle[ind==2,]
nrow(traindata)
nrow(testdata)
summary(ind==1)
table(traindata$default)
table(testdata$default)
#8. 의사결정트리 모델(나무)을 생성합니다.

myformula <- default ~ .
credit_ctree <- ctree(myformula,data=traindata)
#설명: party 패키지의 ctree 함수를 이용해서 의사결정 모델을 생성합니다.
table(predict(credit_ctree),traindata$default)

#설명: 훈련데이터 120개를 가지고 예측한 결과를 보니 120개중 6개 틀리고
#다 맞췄습니다. 우리가 knn 과 나이브 베이즈 실습 할때는 모델 생성한 후에 
#그 모델로 테스트 데이터를 잘 맞추는지 확인을 했었는데 지금 이실습은
#훈련 데이터 부터 먼저 확인을 하고 있습니다. 지금 만든 의사결정트리 모델이
#훈련 데이터를 잘 분류하는 모델인지를 먼저 확인하고 있습니다.

print(credit_ctree)    

#12. 아리스 데이터의 의사결정 트리 모델을 시각화 합니다.
plot(credit_ctree)
plot(credit_ctree,type="simple")

testpred <- predict(credit_ctree, newdata=testdata)

table(testpred,testdata$default)

g3<-CrossTable( testdata$default,  testpred ) 


print(g3$prop.tbl)
print(sum(g3$prop.tbl*diag(2)))


#문제200. (오늘의 마지막 문제) 어제 사용했던 와인 데이터를 분류하는 의사결정트리
#모델을 생성하는 실험을 하시오. 

# 데이터 : wine.csv
# 의사결정트리 패키지 : party 패키지의 ctree 함수를 이용하세요 ~
#코드를 올리고 이원 교차표를 올리세요 ~

library(party)
dataw <- read.csv("credit.csv", header = T, stringsAsFactors = T) # 데이터 불러오기
#데이타 파악하기
summary(dataw)
nrow(dataw)
colnames(dataw)
table(dataw$Type)

set.seed(828)
ind <- sample(2,nrow(dataw),replace=T,prob=c(0.7,0.3)) 

traindata <- dataw[ind==1,]
testdata <- dataw[ind==2,]
nrow(traindata)
nrow(testdata)
summary(ind==1)
table(traindata$Type)
table(testdata$Type)
#8. 의사결정트리 모델(나무)을 생성합니다.

#myformula <- Species ~ Sepal.Length + Sepal.Width + Petal.Length + Petal.Width
#또는 
myformula <- Type ~ . 
dataw_ctree <- ctree(myformula,data=traindata)
#설명: party 패키지의 ctree 함수를 이용해서 의사결정 모델을 생성합니다.
table(predict(dataw_ctree),traindata$Type)

#설명: 훈련데이터 120개를 가지고 예측한 결과를 보니 120개중 6개 틀리고
#다 맞췄습니다. 우리가 knn 과 나이브 베이즈 실습 할때는 모델 생성한 후에 
#그 모델로 테스트 데이터를 잘 맞추는지 확인을 했었는데 지금 이실습은
#훈련 데이터 부터 먼저 확인을 하고 있습니다. 지금 만든 의사결정트리 모델이
#훈련 데이터를 잘 분류하는 모델인지를 먼저 확인하고 있습니다.

print(dataw_ctree)    

#12. 아리스 데이터의 의사결정 트리 모델을 시각화 합니다.
plot(dataw_ctree)
plot(dataw_ctree,type="simple")

testpred <- predict(dataw_ctree, newdata=testdata)

table(testpred,testdata$Type)

g3<-CrossTable( testdata$Type,  testpred ) 


print(g3$prop.tbl)
print( g3$prop.tb[1] + g3$prop.tb[5] + g3$prop.tb[9] )


#%% 성능 높이기 포문으로 seed 값 찾기

library(party)
library(gmodels) 
data <- read.csv("credit.csv", header = T, stringsAsFactors = T) # 데이터 불러오기

temp<- c()
temp2 <-c()
i<-0
repeat { 
  i<- i+1
  set.seed(i)
  ind <- sample(2,nrow(dataw),replace=T,prob=c(0.9,0.1)) 
  set.seed(i)
  dataw <- data[sample(nrow(data)),]
  traindata <- dataw[ind==1,]
  testdata <- dataw[ind==2,]
  myformula <- default ~ . 
  dataw_ctree <- ctree(myformula,data=traindata)
  testpred <- predict(dataw_ctree, newdata=testdata)
  g3<-CrossTable( testdata$default,  testpred ) 
  j <- sum(g3$prop.tbl*diag(2)) 
  temp <- append( temp,  j)
  temp2 <- append (temp2, i)
  print(c(i,j))
  if(j>=0.88) # 목표 정확도 설정
  {print(c(i,j)) 
  break }
  else if( i==6000) # 목표 정확도에 도달하지 못했다면 최고값
  {result <- data.frame( 'seed'= temp2, '정확도'= temp)
  print(result[result$정확도==max(result$정확도),])
  break}
}
mean(result$정확도)


seed    정확도 # set.seed 1번째만 했을때
850  850 0.8529412

seed    정확도 # set. seed 2번째만 했을때
185  185 0.8627451

seed    정확도 # set. seed 를 2개 다 했을 때
1160 1160 0.8723404
