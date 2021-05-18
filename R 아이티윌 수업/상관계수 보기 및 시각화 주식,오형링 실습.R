# 피어슨 상관 계수 보기
# 실습 자료 : 오형링 파손
launch <-  read.csv("challenger.csv", header=T )
launch 

cor( launch$temperature, launch$distress_ct )
cor(launch)

library(psych)
pairs.panels(launch)
# 실습 자료 주식 
k <- read.csv("K_index.csv", header=T, stringsAsFactors=F)
s<- read.csv("S_stock.csv", header=T, stringsAsFactors=F)
h<- read.csv("H_stock.csv", header=T, stringsAsFactors=F)

cor( na.omit(k$k_rate) , na.omit(s$s_rate) )  # 0.51
cor( na.omit(k$k_rate) , na.omit(h$h_rate) )  # 0.3262777

# 단순 회귀분석 
# 실습 자료 
# K_index.csv,  S_stock_csv,  H_stock.csv 
# (코스피등락율) (삼성전자)    (현대자동차)

k <- read.csv("K_index.csv", header=T, stringsAsFactors=F)
s<- read.csv("S_stock.csv", header=T, stringsAsFactors=F)
h<- read.csv("H_stock.csv", header=T, stringsAsFactors=F)
all_data <- merge( merge(k,s, by='date'), h, by='date')  # 3개의 테이블 조인 
head(all_data)
attach(all_data)
plot( k_rate, s_rate, col='blue')
model_s <- lm( s_rate ~ k_rate, data=all_data)
abline( model_s, col='red') 
title(paste( '삼성등락율=', model_s$coefficients[2], 'x 코스피등락율 + ', model_s$coefficients[1] )  )

#