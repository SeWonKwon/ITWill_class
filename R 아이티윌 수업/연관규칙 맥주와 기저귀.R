1. 데이터를 로드한다. 

x <- data.frame(
  beer=c(0,1,1,1,0),
  bread=c(1,1,0,1,1),
  cola=c(0,0,1,0,1),
  diapers=c(0,1,1,1,1),
  eggs=c(0,1,0,0,0),
  milk=c(1,0,1,1,1) )
x 

#     beer bread cola diapers eggs milk
# 1    0     1    0       0    0    1
# 2    1     1    0       1    1    0
# 3    1     0    1       1    0    1
# 4    1     1    0       1    0    1
# 5    0     1    1       1    0    1

2. arules 패키지를 설치한다. 
설명: 아프리오 알고리즘을 사용할 수 있는 패키지인 arules 설치

install.packages("arules")  
library(arules)

trans <-  as.matrix( x, "Transaction") 
trans 

3. apriori 함수를 이용해서 연관관계를 분석한다. 
rules1 <- apriori(trans, parameter=list(supp=0.2, conf=0.6, target="rules") )
rules1

inspect(sort(rules1)) 

4. 위의 맥주와 기저귀 연관 관계를 시각화 하기 

install.packages("sna")
install.packages("rgl")
library(sna)
library(rgl)

b2 <- t(as.matrix(trans)) %*% as.matrix(trans) 
#희소행렬을 만든다.
b2
library(sna)
library(rgl)
diag(b2)
b2.w <- b2 - diag(diag(b2))
# 대각선 데이터를 0으로 만드는 법
b2.w

gplot(b2.w , displaylabel=T , vertex.cex=sqrt(diag(b2)) , vertex.col = "green" , edge.col="blue" , boxed.labels=F , arrowhead.cex = .3 , label.pos = 3 , edge.lwd = b2.w*2) 

■ apriori 알고리즘 예제2 ( 보습학원과 연관된 업종은 ? )

1. 데이터를 로드합니다.
build <- read.csv("building.csv" , header = T)
View(build)
head(build)
2. na 를 0 으로 변경합니다. 
table(is.na(build))
build[is.na(build)] <- 0  

3. 필요한 변수만 선별합니다.
build <- build[-1]
build 

4. 연관규칙 패키지를 다운로드 받습니다. 
install.packages("arules")
library(arules) 

5. 연관규칙 모델을 생성합니다.
trans <- as.matrix(build , "Transaction")

#설명: 지지도 0.2 이상이고 신뢰도 0.6 이상인 규칙을 만들어라 ~
rules1 <- apriori(trans , parameter = list(supp=0.2 , conf = 0.6 , target = "rules"))
rules1 

6. 연관규칙을 확인합니다. 
a<-inspect(sort(rules1))
View(a)
     

7. 시각화를 합니다. 

# 여러 규칙들 중에서 보습학원 부분만 따로 검색
rules2 <- subset(rules1 , subset = lhs %pin% '보습학원' & confidence > 0.7)
View(inspect(sort(rules2)) )


rules3 <- subset(rules1 , subset = rhs %pin% '편의점' & confidence > 0.7)
rules3

View(inspect(sort(rules3)) )

# 설명 :     %in% (select itemsets matching any given item) 조건은 적어도 하나의 제품이라도 존재하면 연관규칙을 indexing 해온다는 뜻입니다. 
# 이에 반해 %pin% (partial matching) 는 부분 일치만 하더라도, %ain% (select only itemsets matching all given item) 는 완전한 일치를 할 때만 indexing을 하게 됩니다. 

#visualization

b2 <- t(as.matrix(build)) %*% as.matrix(build) 
install.packages("sna")
install.packages("rgl")

library(sna)
library(rgl)

b2.w <- b2 - diag(diag(b2))

rownames(b2.w)

colnames(b2.w)

gplot(b2.w , displaylabel=T , vertex.cex=sqrt(diag(b2)) , vertex.col = "green" , edge.col="blue" , boxed.labels=F , arrowhead.cex = .3 , label.pos = 3 , edge.lwd = b2.w*2) 

args(subset)


■ 

1. 요번주에 친구를 만난 횟수를 사회행렬로 구성함

paper <- read.csv("paper1.csv" , header = T)
paper[is.na(paper)] <- 0 
View(paper) 

rownames(paper) <- paper[,1] 
paper <- paper[-1]
paper2 <- as.matrix(paper) 
View(paper2)
2. 요번주에 개별적으로 책을 읽은 시간 데이터를 로드한다.

book <- read.csv("book_hour.csv" , header = T)
paper2
book

library(sna) 
x11()

gplot(paper2 , displaylabels = T, boxed.labels = F ,
      vertex.cex = sqrt(book[,2]) , vertex.col = "blue" , vertex.sides = 20 ,
      edge.lwd = paper2*2 , edge.col = "green" , label.pos = 3)
colnames(paper2)
paper3 <- subset(paper2, subset = rownames(paper2)=="광희")
paper4 <- paper2[]
View(paper3)
rules3 <- subset(rules1 , subset = rhs %pin% '편의점' & confidence > 0.7)

x11()

gplot(paper3 , displaylabels = T, boxed.labels = F ,
      vertex.cex = sqrt(book[,2]) , vertex.col = "blue" , vertex.sides = 20 
      , edge.col = "green" , label.pos = 3)
