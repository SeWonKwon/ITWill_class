
func_nuclear <- function(x_num) {
  x = c(10,20,30,40)
  y = c(300,250,200,150)
  a = cov(x,y) / var(x)
  y_mean= mean(y)
  x_mean= mean(x)
  b= y_mean - a*x_mean
  y_hat = b +a*x_num
  print(y_hat)
}
func_nuclear(35)

문제220. 탄닌 함유량과 애벌래의 성장간의 실홈표를 이용해서 탄닌 함유량이 9일때 성장률이 어떻게 되는지 알아내는 함수를 생성하시오 !
  (데이터는 regression.txt)
reg <- read.table("regression.txt", header=T)
reg

reg_func(9)

reg_func <- function(독립,종속,x_num) {
  y = 종속
  x = 독립
  b = cov(x,y) / var(x)
  y_mean= mean(y)
  x_mean= mean(x)
  a= y_mean - b*x_mean
  y_hat = a +b*x_num
  print(y_hat)
}

reg_func(reg$tannin,reg$growth,9)
plot(reg$tannin,reg$growth)


1. 데이터를 로드한다.
reg <- read.table("regression.txt", header = T)
reg
2. 데이터를 시각화 한다.
attach(reg) # growth~tannin 에 reg$growth~reg$tannin 귀찮아서 
#전부 저렇게 컬럼명으로 바뀐다. detach(reg) 하면 살아짐
plot(growth~tannin, data=reg, pch=21, col='blue',bg='blue')

#설명: plot(y~x, data=데이터프레임명)

3. 회귀분석을 해서 회귀계수인 기울기와 절편을 구합니다.
model <- lm(growth ~ tannin, data=reg) 
model
args(lm) # (종속변수 ~ 독립변수, 데이타,)
4. 2번에서 시각화한 산포도 그래프에 회귀직선을 겹쳐서 그립니다.
attach(reg)
plot(growth~tannin, data=reg, pch=21, col='blue',bg='blue')
model <- lm(growth ~ tannin, data=reg)
abline( model, col='red')

#5. 그래프 제목을 회귀 직선의 방정식으로 출력되게 합니다.

model$coefficients[2] # 기울기
model$coefficients[1] # 절편

title( paste('성장률=', model$coefficients[2],'x탄닌+',model$coefficients[1]))

#문제221. 

data_raw <- read.csv("simple_hg.csv",header = T)
data_raw
summary(data_raw)
# cost : 광고비
# input : 매출액

attach(data_raw)
plot(input~cost, data=data_raw, pch=21, col='blue',bg='blue')
model <- lm(input ~ cost, data=data_raw)
abline( model, col='red')
title( paste('매출액액=', model$coefficients[2],'x광고비+',model$coefficients[1]))
yhat <- predict(model, cost=cost)
join <- function(i)
lines(c(cost[i],cost[i]),c(input[i],yhat[i]), col="green")
sapply(1:19,join)
dev.off()

#선생님 코드

launch2 <- read.csv("simple_hg.csv")

attach(launch2)
plot(input ~ cost, data=launch2, pch=21, col='red', bg='red')
m <- lm(input  ~  cost, launch2)
abline(m, col='red')
title(expression‎(italic(input== 2.18649 %*%cost + 62.92913)))
yhat <- predict(m, cost=cost)
join <- function(i)
  lines(c(cost[i],cost[i]),c(input[i],yhat[i]), col="green")
sapply(1:19,join)

#문제222

data_raw <- read.csv("challenger.csv",header = T)

data_raw
str(data_raw)
# distress_ct : o형링 파손수
# temperature : 온도
# field_check_pressure: 압력
# flight_num  : 비행기 번호

attach(data_raw)
plot(distress_ct~temperature, data=data_raw, pch=21, col='blue',bg='blue')
model <- lm(distress_ct~temperature, data=data_raw)
abline( model, col='red')
#title( paste('매출액액=', model$coefficients[2],'x광고비+',model$coefficients[1]))
# yhat <- predict(model, cost=cost)
# join <- function(i)
# lines(c(cost[i],cost[i]),c(input[i],yhat[i]), col="green")
# sapply(50:90,join)

yhat <- predict(model,cost=temperature)
join <- function(i)
lines(c(temperature[i],temperature[i]),c(distress_ct[i],yhat[i]), col="green")
sapply(1:23,join)

sapply(min(data_raw$temperture):max(data_raw$temperature),join)

install.packages("car")
library(car)
data(Boston,package="MASS")
Boston

model <- lm(medv ~ . , data=Boston)
vif(model) > 10










