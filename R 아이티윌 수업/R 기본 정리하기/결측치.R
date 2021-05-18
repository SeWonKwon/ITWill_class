# 결측치 에 관련한 것들

sum(10, 20, 20 , NA, na.rm = T) # 결측치 제거후 합계 연산

is.na(x) # NA 여부

x[is.na(x),] # x가 데이터 프레임일때 NA 를 찾는 코드드

sum(is.na(emp)) 결측치가 몇개 인지 보는 명령어
sum(is.na(emp$comm))
emp[is.na(emp$comm),] # 결측치가 있는 행 출력 컬럼별로
emp[is.na(emp$mgr),]
table(is.na(emp)) # 결측치가 총 몇개인지 보는 명령어
sum(!is.na(emp)) # 결측치가 아닌것 보기
colSums( is.na(emp)) # 컬럼별로 보기
