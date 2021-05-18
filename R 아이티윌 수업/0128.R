ind <- sample( c(1,2) , 150, replace= T, prob = c(0.7,0.3) ) 
table(ind)
wine[sample(nrow(wine2)),]

wine_shuffle <- wine[sample(nrow(wine2)),]
data(iris)

iris[c(2,5,73,121), ]


library(party)
data <- read.csv("wine.csv", header = T, stringsAsFactors = T) # 데이터 불러오기
#데이타 파악하기
summary(dataw)
nrow(dataw)
colnames(dataw)
table(dataw$Type)

set.seed(3)
dataw <- data[sample(nrow(data)),]
ind <- sample(2,nrow(dataw),replace=T,prob=c(0.7,0.3)) 

traindata <- dataw[ind==1,]
testdata <- dataw[ind==2,]
nrow(traindata)
nrow(testdata)
(traindata$Type)
summary(ind==1)
table(traindata$Type)
table(testdata$Type)
#8. 의사결정트리 모델(나무)을 생성합니다.

#myformula <- Species ~ Sepal.Length + Sepal.Width + Petal.Length + Petal.Width
또는 
myformula <- Type ~ . 
dataw_ctree <- ctree(myformula,data=traindata)
#설명: party 패키지의 ctree 함수를 이용해서 의사결정 모델을 생성합니다.
table(predict(dataw_ctree),traindata$Type)

print(dataw_ctree)    


plot(dataw_ctree)
plot(dataw_ctree,type="simple")

testpred <- predict(dataw_ctree, newdata=testdata)

table(testpred,testdata$Type)

g3<-CrossTable( testdata$Type,  testpred ) 


print(g3$prop.tbl)
print( g3$prop.tb[1] + g3$prop.tb[5] + g3$prop.tb[9] )