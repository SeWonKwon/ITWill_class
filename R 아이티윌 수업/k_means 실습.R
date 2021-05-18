c <- c(3,4,1,5,7,9,5,4,6,8,4,5,9,8,7,8,6,7,2,1)
row <- c("A","B","C","D","E","F","G","H","I","J")
col <- c("X","Y")
data <- matrix( c, nrow= 10, ncol=2, byrow=TRUE, dimnames=list(row,col))

data 

2. 위에서 만든 데이터 셋으로 plot 그래프를 그린다.

plot(data) 

km <- kmeans( data, 2)  

km$cluster

cbind(data, km$cluster)

km$centers 
km$center

3. km 파라미터값들을 가지고 다시 한번 시각화하시오 ! 
  plot( (km$center),  col=c(7,3), pch=22, bg="dark blue",
        xlim=range(0:10), ylim=range(0:10) )
  plot( round(km$center),  col=km$center, pch=22, bg="dark blue",
        xlim=range(0:10), ylim=range(0:10) )
dev.off()

4. 원래 데이터를 위의 그래프에 합쳐서 출력하시오 !
  
  plot( round(km$center),  col=km$center, pch=22, bg="dark blue",
        xlim=range(0:10), ylim=range(0:10) )

par(new=T)

plot( data, col=km$cluster + 1, xlim=range(0:10), ylim=range(0:10) )

문제
h <- c(165,180)
w <- c(50,65)

d <- data.frame(키=h, 몸무게=w)


sum(abs(d[1,]-d[2,]))


■ k-means 기본실습 1

순서:
1. 기본 데이터셋을 만든다.
2. 위에서 만든 데이터 셋으로 plot 그래프를 그린다. 
3. k-means 패키지를 설치한다.
4. k-means 함수로 데이터를 분류한다. 
5. 분류한 파라미터값을 가지고 다시한번 시각화를 한다.
6. 원래 데이터로 그린 plot 그래프와 분류한 그래프를 같이 출력한다. 

예제:
  1. 기본 데이터 셋을 만든다 
c <- c(3,4,1,5,7,9,5,4,6,8,4,5,9,8,7,8,6,7,2,1)
row <- c("A","B","C","D","E","F","G","H","I","J")
col <- c("X","Y")

data <- matrix( c, nrow= 10, ncol=2, byrow=TRUE, dimnames=list(row,col))
data

2. 위에서 만든 데이터셋으로 plot 그래프를 그린다

plot(data)

3. k-means 패키지를 설치한다
#install.packages("stats")
library(stats)

4. kmeans 함수로 데이터를 분류한다.

※ k 개 구하는 공식 : k=sqrt(n/2)   

km <- kmeans(data,2)
km

km[2]# 각 군집의 중앙 좌표값

cbind(data, km$cluster)

5. 분류한 파라미터값을 가지고 다시 한번 시각화를 한다.  

plot(round(km$center), col=km$center, pch=22, bg=km$center, xlim=range(0:10),ylim=range(0:10))

6. 원래 데이터를 그린 plot 그래프와 위의 그래프를 합쳐서 출력한다.

plot(round(km$center), col=km$center, pch=22,  bg=km$center, xlim=range(0:10),ylim=range(0:10))
par(new=T)
plot( data, col=km$cluster+1, xlim=range(0:10), ylim=range(0:10) )

7. 위의 data 를 factoextra 패키지를 이용해서 시각화 한다.
install.packages("factoextra")
library(factoextra)
km <- kmeans(data,2)

fviz_cluster( km, data = data, stand=F)

문제283. zoo

zoo <- read.csv("zoo.csv")
View(zoo)

zoo_n <- zoo[,2:17] # 동물이름과 라벨을 제외한 컬럼으로만 구성

zoo_model <- kmeans(zoo_n, 7)

zoo_model
zoo_model$cluster

x <- cbind(zoo[,18],zoo_model$cluster)
x
library(factoextra)
zoo_model <- kmeans(zoo_n, 7)
fviz_cluster( zoo_model, data = zoo_n, stand=F)

# 두번째 실습 ( 과일 데이터)

1. 사과, 베이컨, 바나나, 당근, 셀러리, 치즈, 토마토 데이터를 준비한다. x축은 단맛, y축은 아삭한 정도

c <- c(10,9,1,4,10,1,7,10,3,10,1,1,6,7)
row <- c("APPLE","BACON","BANANA","CARROT","SAL","CHEESE","TOMATO")
col <- c("X","Y")
data <- matrix( c, nrow= 7, ncol=2, byrow=TRUE, dimnames=list(row,col))
data

plot(data)

2. 야채, 과일, 단백질 3가지를 k-means 가 잘 분류 했는지 시긱화 해서 확인한다. 

km <- kmeans(data,  3) 
km

cbind(data, km$cluster)

plot(round(km$center), col=km$center, pch=22,  bg=km$center, xlim=range(0:10),ylim=range(0:10))
par(new=T)  # 그래프 겹치기 
plot( data, col=km$cluster+1, xlim=range(0:10), ylim=range(0:10), pch=22, bg=km$cluster+1 )

3. 야채, 과일, 단백질 3가지를 k-means 가 잘 분류 했는지 시각화 해서 확인한다. 

# install.packages("factoextra")
library(factoextra)

km <- kmeans(data,3)

fviz_cluster( km, data = data, stand=F)


문제284. wisc_bc_data.csv

data <- read.csv("wisc_bc_data.csv")

View(data)
str(data)
ncol(data)
data_n <- data[,3:32]
View(data_n)
ncol(data_n)

km <- kmeans(data_n,2)
km
rownames(km) <- data[,2]
str(km)
  
  
fviz_cluster( km, data = data_n, stand=F)

result <- data.frame(cbind(data[,2],km$cluster))
result

View(result)
result$X2<- ifelse(result$X2==1,"B","M")
result
table(result$X1,result$X2)

■ k 평균 군집화 실습2 (국영수 점수를 가지고 학생 분류 )
국영수 점수 데이터를 가지고 k 값을 4 두고 학생들을 분류하시오!
1. 수학,영어 둘다 잘하는 학생들
2. 수학은 잘하는데 영어를 못하는 학생들
3. 영어는 잘하는데 수학을 못하는 학생들
4. 수학,영어 둘다 못하는 학생들 

1. 데이터를 로드한다. 

academy <- read.csv("academy.csv")
View(academy)
academy <- academy[  ,  c(3,4) ]

2. k 값을 4로 주고 비지도학습 시켜 모델을 생성한다. 

km <- kmeans( academy,  4)  
km
km$center
  
3. 시각화를 한다.
library(factoextra)
fviz_cluster(km , data=academy,  stand=F) 

4. 학생번호, 수학점수, 영어점수, 분류번호가 같이 출력되게하시오 !

academy_2 <- read.csv("academy.csv")

x<-cbind( academy_2[   ,c(1,3,4)], km$cluster) 
View(x)

문제285.

academy_2 <- read.csv("academy.csv")

x<-cbind( academy_2[   ,c(1,3,4)], km$cluster) 

x[km$cluster==1, 1]





?ave

Subsets of x[] are averaged, where each subset 
consist of those observations with the same factor levels.


문제286. 부서번호, 부서번호별 평균 월급을 출력하시오 !
  
  emp <- read.csv("emp3.csv", header=T)

aggregate(sal~deptno, emp, mean)

문제 287. 사원 테이블에서 자기가 속하는 부서번호의 평균 월급이  ave 함수로 출력하시오 !
  
ave(emp$sal, emp$deptno)

문제288. 이름, 월급, 부서번호, 자기가 속한 부서번호의 평균월급을 출력하시오 !
  
  SQL> select ename, sal, deptno, 
              avg(sal) over (partition by deptno ) as avgsal
         from emp;
         
  
         # R>
           emp$avgsal <- ave(emp$sal, emp$deptno)

         emp[ , c("ename","sal","avgsal")]
         

  문제289. 사원 테이블에 결측치가 얼마나 있는지 확인해봅니다.
         
         
         colSums( is.na(emp))
         
         
  문제290. 사원 테이블의 커미션의 결측치를 자기가 속한 부서번호의 평균월급으로 치환하시오!
           
  emp$comm[is.na(emp$comm)]<- ave(emp$sal, emp$deptno, FUN=function(x) mean(x))
  
         View(emp)         


# 실습  sns 의 글
         
         2006년도에 잘 알려진 sns 의 30000명의 미국 고등학생 데이터
         
1. 데이터를 로드한다.

corpus 패키지를 가지고 만들어낸 데이터이고 원래 raw 데이터는 sns 의 글들입니다.
이책의 부록실습에 있으니까 참고하세요 ~~
teens <-  read.csv("snsdata.csv")
nrow(teens)
ncol(teens)
View(teens)
설명: 30000건이나 되는 데이터 입니다. sns 글에서 특정단어에 대한 언급이 있었으면
      1로 표시하고 없었으면 0 으로 표시합니다.

2. 성별이 남자가 몇명이고 여자가 몇명인지 확인한다.
table(teens$gender)

문제291. 남녀 성별의 비율이 어떻게 되는지 출력하시오 !
  
  prop.table(table(teens$gender))

3. 성별에 NA 가 몇개인지도 출력되게하시오 
table(teens$gender, useNA="ifany")
prop.table(table(teens$gender, useNA="ifany"))

4. 고등학생 데이터라는 정확한 데이터 분석을 위해서 나이가 13세 ~ 20세 가 아니면 다 NA 처리해라 !  
teens$age <- ifelse(teens$age>=13 & teens$age <20, teens$age, NA)

문제292. teens 데이터에 결측치가 얼마나 있는지 확인하시오.

colSums(is.na(teens))

5. 유클리드 거리 계산을 위해 성별에 관련한 더미변수 2개를 생성한다.

teens$female <- ifelse(teens$gender=="F" & !is.na(teens$gender),  1, 0)
teens$no_gender <- ifelse(is.na(teens$gender),1,0)
table(teens$gender, useNA="ifany")
table(teens$female, useNA="ifany")
table(teens$no_gender, useNA="ifany")

# 설명 : 기존 컬럼인 gender 컬럼의 데이터에는 NA 가 포함되어있어서 유클리드 거리계산을 제대로
#        제대로 수행 할수 없겠지만 성별과 관련해서 파생변수로 만든 femal과 no_gender 는 NA가
#        없으므로 유클리드 거리계산을 가능하게 할 수 있는 데이터 입니다. 

6. 나이가 결측치로 나온 데이터를 졸업년도로 나이를 추정해서 결측치를 채워넣는 작업 

# 나이의 결측치도 5523건이나 되므로 성별처럼 파생변수를 생성하던지 아니면 다른 값으로 치환하면 됩니다.
# 보통 숫자는 3가지중(평균, 최빈, 회귀로 추정한 값)에 하나로 치환합니다. 

ave_age <- ave(teens$age, teens$gradyear,   FUN=function(x) mean(x, na.rm=TRUE) )
teens$age <- ifelse( is.na(teens$age), ave_age, teens$age)
sum(is.na(emp$age))

문제293. 졸업 년도, 졸업 년도(gradyear)별 평균나이를 출력하시오 !

  aggregate(age~gradyear, teens2, mean, na.rm=TRUE) # teen2 는 내가 급조한 원 데이터

문제294. teens 데이터 프레임에 결측치 있는지 확인하시오 !
  
  colSums(is.na(teens))


7. sns 에 나타났던 관심사 횟수를 표현하는 36개의 수치형 데이터 컬럼을 정규화 시킨다.
ncol(teens) # 1~4 번은 정보 41,42 는 더미

interests <- teens[5:40]
interests_z <- as.data.frame(lapply(interests, scale))
# 설명: scale 함수를 이용해서 정규화를 시크는데 scale 함수는 평균 0 이고 1인 데이터로 정규화.
summary(interests_z)

8. kmeans 함수로 5개의 클래스로 분류 한다.

set.seed(2345)
teen_clusters <- kmeans(interests_z, 5)
teen_clusters 

9. 각 클래스의 갯수가 각각 어떻게 되는지 확인한다.
teen_clusters$size

10. 클러스터의 중심점의 좌표를 확인한다
teen_clusters$centers 

11. 어떻게 클러스터링 되었는지 확인한다.
teen_clusters$cluster


설명: 군집화를 했으면 그 군집화환 결과의 타당성을 조사해야 하는데 기술통계를 이용해서 
      타당성을 조사합니다. 

princesses(공주형), brains(두뇌형), criminals(범죄형),
          Atheltes( 운동형 ), basket cases(무력함형)
          전


문제295. ( 오늘의 마지막 문제 ) 저자의 해석을 알아내기 위해 아래는 각 군집별로 female(여성),
          이 몇명인지 출력한 결과 입니다. 아래의 결과를 출력하세요.

힌트 : attach(emp)
        tapply (sal, job, length)
teens$clusters <- teen_clusters$cluster
teens$female
attach(teens)
tapply(female,clusters,sum )

tapply(teens$female,teen_clusters$cluster, sum)
unique(teens$gender)

tapply(ifelse(teens$gender=="F",1,0),teen_clusters$cluster, sum)

table(teens$gender)

str(teens$gender)

?count

Gn<-tapply(teens$gender=="F",teen_clusters$cluster, length)
teens$gender=="F"


tapply(teens$gender=="F",teen_clusters$cluster, table)

tapply(interests$basketball,teen_clusters$cluster, table)

View(interests)
interests$cluster <- teen_clusters$cluster

table(interests$cluster)

G1 <- interests[interests$cluster==1,]
View(G1)


b<-colnames(interests)
Gsa<- data.frame(row.names = b)
k<-0

Gnames <- c("G1","G2","G3","G4","G5")
for ( j in Gnames){
  k<- k+1
  j<- interests[interests$cluster==k,]
  print(head(j))
a<-c()

for (i in colnames(j))
          {
  a <-append(a,(sum(j[,i])))
  
}
print(a)

Gs <- data.frame( j = a, row.names = b)
Gsa <- cbind(Gsa,Gs)
          }
colnames(Gsa)<-Gnames

  
Gsa
Gsa_p <- Gsa
Gn<-tapply(teens$gender,teen_clusters$cluster, length)
Gn <- as.vector(Gn)
Gn[1]
Gsa_p$G1 <- Gsa$G1/Gn[1]
Gsa_p$G2 <- Gsa$G2/Gn[2]
Gsa_p$G3 <- Gsa$G3/Gn[3]
Gsa_p$G4 <- Gsa$G4/Gn[4]
Gsa_p$G5 <- Gsa$G5/Gn[5]
Gsa_p  
Gnames <- c("공주","똑똑이","운동선수","범죄자","무력이")
colnames(Gsa_p)<-Gnames
  
library(doBy)
orderBy(~-G1, Gsa_p )

View(Gsa_p)

a
b
Gs <- data.frame(paste("G",j) = a,row.names = b)
Gs


