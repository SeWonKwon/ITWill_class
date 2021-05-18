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
