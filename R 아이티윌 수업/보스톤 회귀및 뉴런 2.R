traindata <- read.csv("b_train.csv")
testdata <- read.csv("b_test.csv")
summary(traindata)
traindata_1 <- traindata[,-1]

m1 <- lm( medv~., data=traindata_1)
summary(m1)

traindata_1$age_dis <- ifelse(( traindata$age <30 & traindata$indus <= 10),1,0)
testdata$age_dis <- ifelse(( testdata$age <30 & testdata$indus <= 10),1,0)


m1 <- lm( medv ~ crim + zn  + indus +
          + chas + nox + rm + age + dis 
          + rad + tax + ptratio + black 
          + lstat + age_dis ,
          data=traindata_1)
# 우선 rm 에 관하여 설정 해보자
traindata_1$rm57<- ifelse(( traindata_1$rm >=5 & traindata$rm <= 7),1,0)
testdata$rm57<- ifelse(( testdata$rm >=5 & testdata$rm <= 7),1,0)

traindata_1$rm5<- ifelse(( traindata$rm <= 5),1,0)
testdata$rm5<- ifelse(( testdata$rm <= 5),1,0)

traindata_1$rm7<- ifelse(( traindata_1$rm >=7 ),1,0)
testdata$rm7<- ifelse(( testdata$rm >=7 ),1,0)

traindata_1$dis37<- ifelse(( traindata_1$dis >=3.7 ),1,0)
testdata$dis37<- ifelse(( testdata$dis >=3.7 ),1,0)

traindata_1$rm_2<- (traindata_1$rm)^2
testdata$rm_2<- (testdata$rm)^2

traindata_1$black330<- ifelse(( traindata_1$black >=330 ),1,0)
testdata$black330<- ifelse(( testdata$black >=330 ),1,0)

traindata_1$black230<- ifelse(( traindata_1$black >=230 ),1,0)
testdata$black230<- ifelse(( testdata$black >=230 ),1,0)

traindata_1$black360<- ifelse(( traindata_1$black >=360 ),1,0)
testdata$black360<- ifelse(( testdata$black >=360 ),1,0)

# m1 <- lm( medv ~ crim + zn  + indus +
+ chas + nox + rm + age + dis 
+ rad + tax + ptratio + black 
+ lstat + age_dis + rm57,
data=traindata_1)

# 4.74310

# m1 을 다시 설정 해보자 음의 상관관계가 있는것들끼리 묶어서

dis 와 음의 강한 상관관계인 indus, nox, age 를 하나로 묶고
       양 의 상관관계 dis, zn 을 하나로 묶어 보고
tax, crim 를 묶어 보자 .

m1 <- lm( medv ~ indus*nox*age +
          + chas + rm + dis*zn 
          + rad + tax*crim + ptratio + black 
          + lstat + age_dis + rm57,
          data=traindata_1)

# indus, nox, age 하나로 
# dis, zn
# tax, crim
# 4.39512

m1 <- lm( medv ~ indus*nox*age*rm57 +
            + chas + rm + dis*zn 
          + rad + tax*crim + ptratio + black 
          + lstat + age_dis ,
          data=traindata_1)

# 4.53379

m1 <- lm( medv ~ indus*nox*age*age_dis 
            + chas + rm + dis*zn 
          + rad + tax*crim + ptratio + black 
          + lstat + zn*dis*black*rm5*rm7*rm57   ,
          data=traindata_1)

# 양의 상관 관계 
# 
# zn rm dis black
# rm 5, rm 7,rm57 
# 4.42625

m1 <- lm( medv ~ indus*nox*age 
            + chas + rm + dis*zn*black 
          + rad + tax*crim + ptratio + black 
          + lstat + age_dis + rm57*rm5*rm7,
          data=traindata_1)

# 조정해보기
# 4.42393

m1 <- lm( medv ~ indus*nox*age +zn*dis*black
            + chas + rm + dis*zn 
          + rad + tax*crim + ptratio + black 
          + lstat + age_dis + rm57,
          data=traindata_1)

# 4.43271
#dis3.7 변수 만들기

m1 <- lm( medv ~ indus*nox*age + dis37
            + chas + rm + dis*zn 
          + rad + tax*crim + ptratio + black 
          + lstat + age_dis + rm57,
          data=traindata_1)

#4.39307

m1 <- lm( medv ~ indus*nox*age + dis37*rm5*rm7
          + chas + rm + dis*zn 
          + rad + tax*crim + ptratio + black 
          + lstat + age_dis + rm57,
          data=traindata_1)

#4.49282

#rm_2 변수 추가 해보자
m1 <- lm( medv ~ indus*nox*age + dis37
          + chas + rm + dis*zn 
          + rad + tax*crim + ptratio + black 
          + lstat*rm_2 + age_dis + rm57,
          data=traindata_1)

# 3.87908

m1 <- lm( medv ~ indus*nox*age + dis37
          + chas + rm + dis*zn 
          + rad + tax*crim + ptratio + black 
          + lstat*rm_2*rm5*rm7*rm57 + age_dis + rm57,
          data=traindata_1)

# 3.84775

m1 <- lm( medv ~ indus*nox*age + dis37
          + chas + rm + dis*zn 
          + rad + tax*crim + ptratio + black 
          + lstat*rm_2*rm5*rm7*rm57*black + age_dis + rm57,
          data=traindata_1)

# 4.03101

# black 아예 제거 해보자 
m1 <- lm( medv ~ indus*nox*age + dis37
          + chas + rm + dis*zn 
          + rad + tax*crim + ptratio  
          + lstat*rm_2*rm5*rm7*rm57 + age_dis + rm57,
          data=traindata_1)

# 3.84734
# black 330 을 만들고 black 330 * black 을 곱해서 변수 생성 약한 양의 상관관계

m1 <- lm( medv ~ indus*nox*age + dis37
          + chas + rm + dis*zn + black330*black
          + rad + tax*crim + ptratio  
          + lstat*rm_2*rm5*rm7*rm57 + age_dis + rm57,
          data=traindata_1)

# 3.91302

# black330 만 두어 볼까?

m1 <- lm( medv ~ indus*nox*age + dis37
          + chas + rm + dis*zn + black330
          + rad + tax*crim + ptratio  
          + lstat*rm_2*rm5*rm7*rm57 + age_dis + rm57,
          data=traindata_1)

#3.87310

#black 230 으로 해보자 

m1 <- lm( medv ~ indus*nox*age + dis37
          + chas + rm + dis*zn + black230
          + rad + tax*crim + ptratio  
          + lstat*rm_2*rm5*rm7*rm57 + age_dis + rm57,
          data=traindata_1)

# 3.87727

m1 <- lm( medv ~ indus*nox*age + dis37
          + chas + rm + dis*zn + black360
          + rad + tax*crim + ptratio  
          + lstat*rm_2*rm5*rm7*rm57 + age_dis + rm57,
          data=traindata_1)

# 3.84226

# crim 변수 조정 해보자 . crim16_42 변수 를 추가해 보자 

m1 <- lm( medv ~ indus*nox*age + dis37
          + chas + rm + dis*zn + black360+ crim16_42
          + rad + tax*crim + ptratio  
          + lstat*rm_2*rm5*rm7*rm57 + age_dis + rm57,
          data=traindata_1)

#3.85567

m1 <- lm( medv ~ indus*nox*age*crim16_42 + dis37
          + chas + rm + dis*zn + black360+
          + rad + tax*crim + ptratio  
          + lstat*rm_2*rm5*rm7*rm57 + age_dis + rm57,
          data=traindata_1)

# 3.76596

m1 <- lm( medv ~ indus*nox*age*crim16_42 + dis37
          + chas + rm + dis*zn 
          + rad + tax*crim + ptratio  
          + lstat*rm_2*rm5*rm7*rm57*black360 + age_dis + rm57,
          data=traindata_1)

#3.90900

m1 <- lm( medv ~ indus*nox*age*crim16_42*tax + dis37
          + chas + rm + dis*zn + black360+
            + rad + ptratio  
          + lstat*rm_2*rm5*rm7*rm57 + age_dis + rm57,
          data=traindata_1)

# 3.80183

m1 <- lm( medv ~ indus*nox*age*crim16_42*tax*crim + dis37
          + chas + rm + dis*zn + black360+
            + rad + ptratio  
          + lstat*rm_2*rm5*rm7*rm57 + age_dis + rm57,
          data=traindata_1)

#4.21193

m1 <- lm( medv ~ indus*nox*age*crim16_42 + dis37
          + chas + rm + dis*zn + black360+
            + rad + tax + ptratio  
          + lstat*rm_2*rm5*rm7*rm57 + age_dis + rm57,
          data=traindata_1)

# 3.83

m1 <- lm( medv ~ indus*nox*age*crim16_42*tax + dis37
          + chas + rm + dis*zn + black360+
            + rad + tax*crim + ptratio  
          + lstat*rm_2*rm5*rm7*rm57 + age_dis + rm57,
          data=traindata_1)

# 3.68739
# zn 10

m1 <- lm( medv ~ indus*nox*age*crim16_42*tax + dis37
          + chas + rm + dis*zn + black360+
            + rad + tax*crim + ptratio
          + lstat*rm_2*rm5*rm7*rm57 + age_dis + rm57
          + zn10,
          data=traindata_1)

# 3.9

m1 <- lm( medv ~ indus*nox*age*crim16_42*tax + dis37
          + chas + rm + dis*zn + black360+
            + rad + tax*crim + ptratio  
          + lstat*rm_2*rm5*rm7*rm57 + age_dis + rm57
          + zn20,
          data=traindata_1)

# 3.72682

# zn 전부 제거 해보자 

m1 <- lm( medv ~ indus*nox*age*crim16_42*tax + dis37
          + chas + rm + dis + black360+
            + rad + tax*crim + ptratio  
          + lstat*rm_2*rm5*rm7*rm57 + age_dis + rm57,
          data=traindata_1)

# 3.67284

m1 <- lm( medv ~ indus*nox*age*crim16_42*tax + dis37
          + chas + rm + dis*zn20 + black360+
            + rad + tax*crim + ptratio  
          + lstat*rm_2*rm5*rm7*rm57 + age_dis + rm57,
          data=traindata_1)

# 3.71059

m1 <- lm( medv ~ indus*nox*age*crim16_42*tax + dis37
          + chas + rm + dis + black360+
            + rad + tax*crim + ptratio  
          + lstat*rm_2*rm5*rm7*rm57 + age_dis + rm57,
          data=traindata_1)

#3.67284

m1 <- lm( medv ~ indus*nox*age*crim16_42*tax*zn20 + dis37
          + chas + rm + dis + black360+
            + rad + tax*crim + ptratio  
          + lstat*rm_2*rm5*rm7*rm57 + age_dis + rm57,
          data=traindata_1)

# 3.71060

m1 <- lm( medv ~ indus*nox*age*crim16_42*tax + dis37*zn20
          + chas + rm + dis + black360+
            + rad + tax*crim + ptratio  
          + lstat*rm_2*rm5*rm7*rm57 + age_dis + rm57,
          data=traindata_1)
# 3.67062

m1 <- lm( medv ~ indus*nox*age*crim16_42*tax + dis37
          + chas + rm + dis + black360*zn10+
            + rad + tax*crim + ptratio  
          + lstat*rm_2*rm5*rm7*rm57 + age_dis + rm57,
          data=traindata_1)

# 3.65537

m1 <- lm( medv ~ indus*nox*age*crim16_42*tax + dis37
          + chas + rm + dis + black360*zn10*zn20+
            + rad + tax*crim + ptratio  
          + lstat*rm_2*rm5*rm7*rm57 + age_dis + rm57,
          data=traindata_1)

# 3.65094

m1 <- lm( medv ~ indus*nox*age*crim16_42*tax*indus7*indus17 + dis37
          + chas + rm + dis + black360*zn10*zn20+
            + rad + tax*crim + ptratio  
          + lstat*rm_2*rm5*rm7*rm57 + age_dis + rm57,
          data=traindata_1)

# 3.60642

# chas   제거하자 
m1 <- lm( medv ~ indus*nox*age*crim16_42*tax*indus7*indus17 + dis37
          + rm + dis + black360*zn10*zn20+
          + rad + tax*crim + ptratio  
          + lstat*rm_2*rm5*rm7*rm57 + age_dis + rm57,
          data=traindata_1)

# 3.59424

m1 <- lm( medv ~ indus*nox*age*crim16_42*tax*indus7*indus17 + dis37
          + rm + dis + black360*zn10*zn20+
            + rad + tax*crim + ptratio  
          + lstat*rm_2*rm5*rm7*rm57 + age_dis + rm57
          +chas*rm,
          data=traindata_1)

# 3.64

m1 <- lm( medv ~ indus*nox*age*crim16_42*tax*indus7*indus17 + dis37
          + rm + dis + black360*zn10*zn20+
            + rad + tax*crim + ptratio  
          + lstat*rm_2*rm5*rm7*rm57 + age_dis + rm57
          +chas*rm57,
          data=traindata_1)

# 3.6

# nox 를 nox6 으로 대체
m1 <- lm( medv ~ indus*nox6*age*crim16_42*tax*indus7*indus17 + dis37
          + rm + dis + black360*zn10*zn20+
            + rad + tax*crim + ptratio  
          + lstat*rm_2*rm5*rm7*rm57 + age_dis + rm57,
          data=traindata_1)
# 3.79

# nox 제거 
m1 <- lm( medv ~ indus*age*crim16_42*tax*indus7*indus17 + dis37
          + rm + dis + black360*zn10*zn20+
            + rad + tax*crim + ptratio  
          + lstat*rm_2*rm5*rm7*rm57 + age_dis + rm57,
          data=traindata_1)

# 3.906

m1 <- lm( medv ~ indus*nox5*age*crim16_42*tax*indus7*indus17 + dis37
          + rm + dis + black360*zn10*zn20+
            + rad + tax*crim + ptratio  
          + lstat*rm_2*rm5*rm7*rm57 + age_dis + rm57,
          data=traindata_1)

# 3.98


m1 <- lm( medv ~ indus*nox*age*crim16_42*tax*indus7*indus17 + dis37
          + rm + dis + black360*zn10*zn20+
            + rad + tax*crim + ptratio  
          + lstat*rm_2*rm5*rm7*rm57 + age_dis + rm57
          +nox5*nox6 ,
          data=traindata_1)

# 3.96

m1 <- lm( medv ~ indus*nox*age*crim16_42*tax*indus7*indus17 + dis37
          + rm + dis + black360*zn10*zn20+
            + rad + tax*crim + ptratio  
          + lstat*rm_2*rm5*rm7*rm57 + age_dis + rm57
          +age80,
          data=traindata_1)

# 3.55048

m1 <- lm( medv ~ indus*nox*age*crim16_42*tax*indus7*indus17 + dis37
          + rm + dis + black360*zn10*zn20+
            + rad + tax*crim + ptratio  
          + lstat*rm_2*rm5*rm7*rm57 + age_dis + rm57
          +age80 + dis4,
          data=traindata_1)

# 3.55277

m1 <- lm( medv ~ indus*nox*age*crim16_42*tax*indus7*indus17 + dis37
          + rm + dis + black360*zn10*zn20+
            + rad + tax*crim + ptratio  
          + lstat*rm_2*rm5*rm7*rm57 + age_dis + rm57
          +age80*dis4,
          data=traindata_1)

# 3.54015

m1 <- lm( medv ~ indus*nox*age*crim16_42*tax*indus7*indus17 + dis37
          + rm + dis + black360*zn10*zn20+
            + rad + tax*crim + ptratio  
          + lstat*rm_2*rm5*rm7*rm57 + age_dis + rm57
          +age80*dis4*age_dis,
          data=traindata_1)

# 3.54935

m1 <- lm( medv ~ indus*nox*age*crim16_42*tax*indus7*indus17 + dis37
          + rm + dis + black360*zn10*zn20+
          + rad*rad4 + tax*crim + ptratio  
          + lstat*rm_2*rm5*rm7*rm57 + age_dis + rm57
          +age80*dis4 ,
          data=traindata_1)

# 3.50604

m1 <- lm( medv ~ indus*nox*age*crim16_42*tax*indus7*indus17 + dis37
          + rm + dis + black360*zn10*zn20+
            + rad*rad4 + tax*crim*tax600 + ptratio  
          + lstat*rm_2*rm5*rm7*rm57 + age_dis + rm57
          +age80*dis4 ,
          data=traindata_1)

# 3.55

m1 <- lm( medv ~ indus*nox*age*crim16_42*tax*tax600*indus7*indus17 + dis37
          + rm + dis + black360*zn10*zn20+
            + rad*rad4 + tax*crim + ptratio  
          + lstat*rm_2*rm5*rm7*rm57 + age_dis + rm57
          +age80*dis4 + tax600,
          data=traindata_1)
#3.6

m1 <- lm( medv ~ indus*nox*age*crim16_42*tax*indus7*indus17*ptratio20 + dis37
          + rm + dis + black360*zn10*zn20+
            + rad*rad4 + tax*crim + ptratio  
          + lstat*rm_2*rm5*rm7*rm57 + age_dis + rm57
          +age80*dis4 ,
          data=traindata_1)
# 3.9

m1 <- lm( medv ~ indus*nox*age*crim16_42*tax*indus7*indus17 + dis37
          + rm + dis + black360*zn10*zn20+
            + rad*rad4 + tax*crim + ptratio  
          + lstat_2*rm_2*rm5*rm7*rm57 + age_dis + rm57
          +age80*dis4 ,
          data=traindata_1)

# 3.54922

m1 <- lm( medv ~ indus*nox*age*crim16_42*tax*indus7*indus17 + dis37
          + rm + dis + black360*zn10*zn20+
            + rad*rad4 + tax*crim + lstat1030*ptratio  
          + lstat_2*rm_2*rm5*rm7*rm57 + age_dis + rm57
          +age80*dis4 ,
          data=traindata_1)

# 3.54652

m1 <- lm( medv ~ indus*nox*age*crim16_42*tax*indus7*indus17 + dis37
          +  + dis + black360*zn10*zn20+
            + rad*rad4 + tax*crim + lstat1030*ptratio  
          + rm*lstat_2*rm_2*rm5*rm7*rm57 + age_dis + rm57
          +age80*dis4 ,
          data=traindata_1)

# 4.14



m1 <- lm( medv ~ indus*nox*age*crim16_42*tax*indus7*indus17 + dis37
          + rm + dis + black360*zn10*zn20+
            + rad*rad4 + tax*crim + ptratio  
          + lstat1030*lstat*rm_2*rm5*rm7*rm57 + age_dis + rm57
          +age80*dis4
          ,
          data=traindata_1)
#3.6

m1 <- lm( medv ~ indus*nox*age*crim16_42*tax*indus7*indus17 + dis37
          + rm * dis * black360*zn10*zn20 
          + rad*rad4 + tax*crim + ptratio  
          + lstat*rm_2*rm5*rm7*rm57 + age_dis + rm57
          +age80*dis4 +lstat1030,
          data=traindata_1)

m1 <- lm( medv ~ indus*nox*age*crim16_42*tax*indus7*indus17 + dis37
          + rm + dis + black360*zn10*zn20
          + rad*rad4 + tax*crim + ptratio  
          + lstat*rm_2*rm5*rm7*rm57 + age_dis + rm57
          +age80*dis4*dis37 ,
          data=traindata_1)

# 3.49305

m1 <- lm( medv ~ indus*nox*age*crim16_42*tax*indus7*indus17 + dis37
          + rm + dis + black360*zn10*zn20
          + rad*rad4 + tax*crim + ptratio  
          + lstat*rm_2*rm5*rm7*rm57 + dis*rm*age_dis*rm57 + 
          +age80*dis4*dis37 ,
          data=traindata_1)



result<- data.frame(predict(m1, testdata))

result2 <- cbind(testdata$ID,result$predict.m1..testdata.)
# result2

colnames(result2) <- c('ID','MEDV')
head(result2)

result2<-data.table(result2)

# result2

write.csv(result2, file="0002.csv",row.names = F)












