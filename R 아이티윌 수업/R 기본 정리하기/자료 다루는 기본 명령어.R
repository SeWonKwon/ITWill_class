setwd("c:\\dtat")
emp<- read.csv("emp3.csv")
dept<- read.csv("dept.csv")
emp2<- read.table("emp3.csv")
emp2
### 자료를 처리하는 기본 명령어
print(emp)
print(dept)
dept
emp

mode(emp)
class(emp)
# 자료변수명[행(조건),렬]
emp[ emp$sal==3000, c("ename","sal")]
emp[ emp$job=='SALESMAN', "ename"]

#자료 특성확인하기
mode(emp)
class(emp)
str(emp)
str(emp$sal)
summary(emp)
nrow(emp)
ncol(emp)
dim(emp)
dim(emp)[1] # nrow 와 같다
dim(emp)[2] # ncol 과 같다.
table(emp$deptno)
length(emp)
sum(emp$sal)
mean(emp$sal)
colSums( is.na(emp)) # 결측치에서 더 확인하기 ! 

# print 류의 함수
x<-1
y<-2
c(x,y)
c(x,'dd',y)
print(c(emp$ename,'과',emp$job)) # 벡터형으로 우리과 원하는 결과 값이 아니다.
print(paste(emp$ename,'과',emp$job))


### 연산자 및 산술 함수

# 1. 산술 연산자 :  *  /  +  -  
# 2. 비교 연산자 :  >, <, >=, <=, ==, !=  
# 3. 논리 연산자 :
#                 &  :  and ( 백터화 된 연산)
#                 && :  and ( 백터화 되지 않은 연산) 
#                 |    : or  ( 백터화된 연산 )
#                 ||   : or  ( 백터화 되지 않은 연산) 
#                 !    : not

# 산술 비교 논리 연산자
x <- c(1,2,3)
x
(x>c(1,1,1))&(x<=c(1,2,3))

y<-1
y
(y>-2)&&(y<2)

# 기타 비교 연산자

# %in%, grep, is.na,is.nan, A & B
emp[emp$job %in% c('SALESMAN','ANALYST'), c("ename","job")]
emp[grep ("^K",emp$ename),] # 시작 ^K : K로 시작하는
emp[grep ("T$",emp$ename),] # 끝 T$ : T로 끝나는
emp[grep ("^.M",emp$ename),] # 번째 ^.M : ^앞에서 . 아무거나 한글짜 오고 M
emp[grep ("T.$",emp$ename),] # 번째 T.$ : $뒤에서 . 아무거나 한글짜 오고 T
emp[is.na(emp$comm),]
is.na(emp)
sum(is.na(emp))
emp[ ! is.na(emp$comm),  c("ename", "sal", "comm") ]

# 중복 제거
library(data.table)
data.table("부서번호"=unique(emp$deptno))
unique(emp$deptno)
table(emp$deptno)

# 정렬 작업, 순서 , 랭크, 
library(data.table) # order 는 data.table 라이브러리이다.
emp[ order(emp$sal, decreasing=T), c("ename", "sal") ]

library(doBy)
orderBy(~-sal,emp[emp$job=="ANALYST",c("ename","sal","empno")])

orderBy(~-sal,emp[emp$deptno==30,c("ename","sal","empno","deptno")])
orderBy(~-sal,emp[dept$deptno==30,c("ename","sal","empno","deptno")])

library(doBy)
orderBy(~-sal,emp[,c("ename","sal")])
orderBy(~sal,emp[,c("ename","sal")])

# 객체 처리 함수 apply(), subset()

#subset()
subset ( 데이타 프레임명, 컬럼별 조건절 )

df <- data.frame(x=c(1,2,3),y=c("일","이","삼"),z=c("one","two","three"))
df

a <- subset(df,x>1)
a
b <- subset(df,y!="삼"&x>1)
b

# apply(), lapply(), sapply(), tapply() Function

apply(X, MARGIN, FUN) # array, data.frame, matrix--> vector,list,array
Here:
  -x: an array or matrix
  -MARGIN:  take a value or range between 1 and 2 to define where to apply the function:
  -MARGIN=1`: the manipulation is performed on rows
  -MARGIN=2`: the manipulation is performed on columns
  -MARGIN=c(1,2)` the manipulation is performed on rows and columns
  -FUN: tells which function to apply. Built functions 
         like mean, median, sum, min, max and 
         even user-defined functions can be applied
         
lapply(X, FUN) # list, vector ,  data.frame, array --> list
Arguments:
          -X: A vector or an object
          -FUN: Function applied to each element of x

sapply(X, FUN) # list, vector , data.frame --> vector or matrix
Arguments:
          -X: A vector or an object
          -FUN: Function applied to each element of x

tapply(X, INDEX, FUN = NULL)
Arguments:
          -X: An object, usually a vector
          -INDEX: A list containing factor
          -FUN: Function applied to each element of x
