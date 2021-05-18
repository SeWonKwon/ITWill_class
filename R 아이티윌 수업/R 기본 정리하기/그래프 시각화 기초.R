setwd("c:\\data")
emp <- read.csv("emp3.csv")
getwd()

data()
library(doBy)
data(beets) # doBy 의 내장 대이터 불러오기
summary(beets)

# 그래프 저장하기
par(mfrow = c(1,1)) # Plots 영역에 1개의 그래프 표시
pdf("C:\\data\\batch.pdf") # 지전된경로의 파일에 결과를 출력
hist(beets$sugpct) # 히스토그램 그리기
dev.off() # 출력 파일 닫기 

# 그래프 그리기 2개이상  같이 출력하기

par(mfrow = c(1,2)) # 2개 일때
plot(beets$harvest)
plot(beets$sow)
dev.off()

par(mfrow = c(1,3)) # 3개 일때
plot(beets$harvest)
plot(beets$sow)
hist(beets$yield)
dev.off()

#그래프의 종류
# '막대 그래프', '원형 그래프', '라인 그래프' ,'히스토그램 그래프', 
# '박스 그래프', '테이블과 통계정보',
# '산포도 그래프', '범주형 원형 그래프'
barplot() # 막대 그래프
hist() # 히스토 그래프
pie() # 파이 그래프
line() # 직선 그래프
plot() # 산포도 그래프
boxplot() # 박스 그래프

#그래프 겹쳐 그리기
data(iris)
plot(iris$Sepal.Length,col=2)
par(new=T)
plot(iris$Sepal.Width, col=3)
par(new=T)
plot(iris$Petal.Length, col=4)







### plot() 






###
