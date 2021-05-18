# 1. 변수 이름 작성 규칙

goods.code <- 'a001'
goods.name <- '냉장고'
goods.price <- 6400000
godds.des <- '최고사양, 동급 최강'

goods.price
# 2. 스칼라 변수 scalar vs 벡터 변수
age <- 35 # 스칼라 하나의 값을 가짐 
g1.age <- c(35,23,34) # 벡터 둘 이상의 값을 가짐짐

g1.age

# 4.2 자료형

숫자형 : 정수 , 실수
문자형 : 문자, 문자열
논리형 : booleans TRUE 또는 T, FALSE 또는 F
결측 데이터 : 결측치 NA(Not Availabl), 비숫자 NaN(Not a Number)

# (1) 자료형 확인

is.numeric(x) # 수치형 여부
is.logical(x) # 논리형
is.character(x) # 문자형 여부
is.data.frame(x) # 데이터 프레임 여부
is.na(x) # NA 여부

is.integer(x) # 정수형 여부
is.double(x) # 실수형 여부
is.complex(x) # 복소수형 여부
is.factor(x) # 범주형 여부
is.nan(x) # NaN 여부

ls() # 현재 사용 중인 변수 ( 객체 ) 보기

# 자료형 변환
as.numeric() # 수치형 변환
as.logical() # 논리형 변환
as.character() # 문자형 변환
as.data.frame()
as.list()
as.array()
as.integer()
as.double() # 실수형 변환
as.complex() # 복소수형 변환
as.factor() # 요인형 변환
as.vector() # 벡터형 변환
as.Data() # 날짜형 변환

#복소수 자료 생성과 형 변환
z <- 5.3 -3i
is.complex(z)
Re(z)
Im(z)

x <- -3
is.complex(x)
x2 <- as.complex(x)
x2

# (3) 자료형(mode)과 자료구조(class) 보기

mode(x)
class(x)
mode(z)
class(z)

# (4) Factor 형 변환 : 요인형!

# Nominal : 범주의 순서는 알파벳 순서로 정렬
# Ordinal : 범주의 순서는 사용자가 지정한 순서대로 정렬

gender <- c("man","woman","woman","man", "man")
class(gender) # character 문자형
mode(gender)
# defalut as.factor 는 Nominal 로 설정된다. 
Ngender <- as.factor(gender) # Factor 형 변환환

class(Ngender) # class (자료구조) 는 Factor형
mode(Ngender)  # mode (자료의 성격)은 Numeric

table(Ngender)
plot(Ngender)

Ngender

# factor() 함수를 이용해서 Factor 형 변환
args(factor) # factor() 함수의 매개변수 보기

function (x = character(), # 대상
          levels, # 레벨 설정
          labels = levels, # 레이블 설정 (보이는값)
          exclude = NA, # 제외 할것 설정
          ordered = is.ordered(x), # 순서 설정 지정해주는 levles 에 따라간다.
          nmax = NA)  # 최대 갯수
  
  
data()
library(doBy)
data(beets) # doBy 의 내장 대이터 불러오기
summary(beets)
plot(beets$sow)
table(beets$sow)

g1 <- factor(beets$sow, levels=c('sow1','sow2','sow3','sow4','sow5','sow6'), labels = c("1구역","2구역","3구역","4구역","5구역","6구역"))
g2 <- factor(beets$sow, levels=c('sow1','sow2','sow3','sow4','sow5'), labels = c("1구역","2구역","3구역","4구역","5구역"))
g1
g2
table(g1)
table(g2)
g3 <- factor(beets$sow, exclude = ('sow3'))
g3
table(g3)
g4 <- factor(beets$sow, levels=c('sow6','sow5','sow4','sow3','sow2','sow1'), 
                                                ordered = T)
g4

# (5) 날짜형 변환 p48

as.Date("20/02/28", "%y/%m/%d")
class(as.Date("20/02/28", "%y/%m/%d"))


### Vector 자료구조
# 1차원의 선형 자료구조 형태
# 변수[첨자] 접근 가능 index 는 1부터 시작
# 같은 자료형의 데이터만 저장 할수 있다. 

# 생성 : c(), seq(), rep()
c(1,2)
seq(1,10,3)
rep(1:3,3)
rep(1:3, each =3)
example(rep)
as.vector(a)
is.vector(a)

# 처리 
union() # 합집합
setdiff() # 차집합
intersect() # 교집합

#  컬럼명 지정

age <- c(30,35,40)
names(age)<- c("김씨","이씨","권씨")
age

# 지우기
age<-NULL
age

# 인덱싱

a <- seq(1,20,3)
a[1:3]
a[2:3]
a[-1]  # - 은 제외 하고 
a[-c(2:3)]


### Matrix 자료 구조  
# matrix() 함수 이용
# 생성, matrix(), as.matrix(), is.matrix()

args(matrix)
matrix(data = NA,        # 행렬 객체의 대상 자료
       nrow = 1,         # 행렬 객체의 행수 지정
       ncol = 1,         # 행렬 객체의 열수 지정
       byrow = FALSE,    # 행 우선 순위 여부 지정(FALSE 또는 TRUE)
       dimnames = NULL)  # dimnames : 차원 지정

a <- rep(1:3,3) 
a
matrix(a, nrow = 3, byrow=TRUE, dimnames = list(c("1행","2행","3행"),c("1열","2열","3열") ) )

c <- c(10,9,1,4,10,1,7,10,3,10,1,1,6,7)
row <- c("APPLE","BACON","BANANA","CARROT","SAL","CHEESE","TOMATO")
col <- c("X","Y")
data <- matrix( c, nrow= 7, ncol=2, byrow=TRUE, dimnames=list(row,col))
data

ma <- matrix(
  month.abb[c(12, 1:11)],
  nrow = 3,
  dimnames = list(
    c("start", "middle", "end"),
    c("Winter", "Spring", "Summer", "Fall")
                  )
             )
ma

colnames(ma) <- c("겨울","봄","여름","가을")
ma

rownames(ma) <- c("초","중","말")
ma

# 인덱싱
ma[1,]
ma[,1]
ma[-1,]

# length(ma), ncol(x)
# 자료 갯수 보기

# apply() 함수 

args(apply)
apply (X,      # 행렬 객체
       MARGIN, # 1 또는 2의 값을 갖는다. (1: 행 단위, 2: 열 단위)
       FUN)    # 행렬 자료에 적용할 함수

a <- matrix(rep(1:3,3), nrow=3)
a
apply(a,1,mean)
apply(a,2,mean)
apply(a,1,max)
apply(a,2,length)

f <- function(x) {
  x * c(1,2,3)    }
apply(a,1,f)
apply(a,2,f)

### Array
# 행, 열, 면 의 3차원 배열 형태의 객체
# index 가능
# array
# 생성
a <- c(1:12)
arr <- array(a,c(3,2,2))
args(array)
array (data = NA, dim = length(data), dimnames = NULL)

a <- c(1:12)
arr <- array(a,c(3,2,2))
arr  

arr[,,2]
arr[1,2,2]


### data.frame
# 리스트와 벡터의 혼합형으로 컬럼단위로 서로 다른 데이터 저장이 가능하다.
# 처리함수 : str(), ncol(), nrow(), apply(), summary(), subset()
#생성 : data.frame(), read.table(), read.csv()
args(data.frame)
data.frame(x_1=,x_2=..... x_n, # 데이터, column 이름과 자료를 같이 입력 또는 x
           row.names = NULL, # 행이름
           
           check.rows = FALSE, # 
           check.names = TRUE, #
           fix.empty.names = TRUE, 
           stringsAsFactors = FALSE # 명목형 데이터 Factor 로 읽을까?! ) 


# 변경
rownames()
colnames()
# 삽입
cbind
rbind

# 객체 처리 함수 
str()
summary()
apply()
subset()


### list 형 자료구조
# 리스트는 성격이 다른 자료형(문자열, 숫자형, 논리형 등) 과 
# 자료구조(벡터, 행렬, 리스트, 데이터 프레임 등)를 객체로 생성할 수 있다. 

# 하나의 메모리 영역에는 키(key)와 값(value) 한 쌍으로 저장된다.
# dict 자료구조와 유사


