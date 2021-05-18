# 다중 공선성 실험

install.packages("car")
library(car)

# 설명 다중 공선성을 보이는 변수들은 팽창계수가 10이상인 변수들 입니다.

2. 데이터를 로드합니다.

  test <- read.csv("test_vif1.csv")
  View(test)
  summary(test)
3. 독립변수들끼리의 상관관계를 확인합니다.

  cor( test[,c("아이큐","공부시간")])
  #           아이큐  공부시간
  # 아이큐   1.0000000 0.7710712
  # 공부시간 0.7710712 1.0000000
  
  cor(test) 
  
  설명: 두 독립변수의 상관관계가 1에 가까운 강한 양의 상관관계를 보이고 있습니다.

4. 회귀 분석 모델을 생성합니다.

test<- test[,-1]
m1 <- lm( test$시험점수~., data=test)
summary(m1)  

5. 다중 공선성을 보이는지 확인합니다.

vif(m1)

  아이큐  공부시간 
2.466401  2.466401 

현업기준 : 팽창계수(vif) 가 보통 10보다 큰것으로 골라내고 엄격하게 하려면
            5보다 큰것을 골라냅니다. 느슨하게 하려면 15~20 으로 주로 골라내냅니다.

vif(m1) > 10

설명: 위의 예제는 팽창계수가 10보다 크지 않ㅇ으므로 다중공선성을 보이고 있지 않다.

# 문제246. test_vif2.csv 를 로드하면 등급 평균이 추가되어 있는데 이 데이터를
# 로드해서 다중회귀분석을 하고 다중공선성을 보이는 독립변수들이 있는지 확인하시오!
test <- read.csv("test_vif2.csv", header = T)
View(test)
summary(test)
test<- test[,-1]
cor(test) # 전부 보기
cor(test[,c("아이큐","공부시간","등급평균")]) # 독립변수 까리 보기
m1 <- lm( test$시험점수~., data=test)
summary(m1)  
vif(m1)

vif(m1) > 10

※ 중요하게 확인해야할 내용 : 
  다중 공선성을 보이는 독립변수들의 p-value 값이 어떻게 나타나고 있는지 확인해야합니다.
  그 독립변수의 p-value 가 0.05 이내를 나타내느지 확인해야 합니다.
  그래야 유의한 변수이기 때문입니다.

1. 먼저 데이터를 로드합니다.
test <- read.csv("test_vif2.csv", header = T)
View(test)
summary(test)
2. 상관관계를 확인합니다.
test<- test[,-1]
cor(test) # 전부 보기
cor(test[,c("아이큐","공부시간","등급평균")]) # 독립변수 까리 보기
3. 회귀분석을 합니다.
m1 <- lm( test$시험점수~., data=test)
summary(m1) 

Coefficients:
  Estimate Std. Error t value Pr(>|t|)  
(Intercept) 50.30669   35.70317   1.409   0.2085  
아이큐       0.05875    0.55872   0.105   0.9197  
공부시간     0.48876    0.17719   2.758   0.0329 *
  등급평균     7.37578    8.63161   0.855   0.4256  
---
  Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

설명: 아이큐와 등급평균의 p-value 가 크게 나왔습니다. 즉 각각의 독립변수들은
      종속변수에 유의한 영향을 미치지 않고 있습니다. 그렇기 때문에
      아이큐와 등급평균 둘다 시험점수에 미치는 의미가 없거나 

4. 다중공선성 여부를 확인합니다.
vif(m1)

vif(m1) > 10

m2 <- lm(test$시험점수~test$공부시간, data=test)
summary(m2)

5. 이럴때는 아이쿠와 등급평균이 둘다 간한 상관관계를 보여서 회귀분석 결과에 좋지 않은 결과를
    보였음므로 둘중에 하나를 제외하고 회귀분석을 해야합니다.
    그래서 둘중에 어떤것을 제외시켜야 할지는 각각 테스트 해보고 결정계수가
    높은것을 선택하면 됩니다.

1번 : 아이큐, 공부시간
2번 : 등급평균, 공부시간

model <- lm(test$시험점수 ~ ., data=test[,c(1,2,3)])
summary(model) # 결정계수 0.90

model2 <- lm(test$시험점수 ~ ., data=test[,c(1,3,4)])
summary(model2) # 결정계수 0.91

결정:
  
  중요하다고 생각되는 독립변수의 회귀계수에 대한 검정결과가 유의 하지 않게
  나왔다면 즉 p-value 가 크게 나왔다면 다중 공선성을 의심해봐야합니다.

문제247. 미국 국민의 의료비 데이터로 의료비를 예측하는 회귀모델을 생성했는데
         이 회귀모델을 이용해서 의료비를 쉽게 예측할 수 있는 IBM 의 왓슨과 질문을 던지는
         코드를 구현하시오 !
  
  나이가 어떻게 되십니까? 
  부양가족수가 몇명입니까?
  흡연을 하십니까? (yes/no) 
  비만지수가 어떻게 되십니까? (16~53) 
  사는 지역이 어디십니까? (southwest/southeast/northwest/northeast) 

AI 가 예측한 의료비는 13270 달러 입니다. 

reg_func <- function(){
  
  x1=as.integer( readline('나이가 어떻게 되십니까? '))
  x2=as.integer( readline('성별이 어떻게 되십니까? 여자면 1 남자면 0'  ) )
  x3=as.integer( readline('비만지수가 어떻게 되십니까? (16~53) ') )
  x4= as.integer( readline('부양가족수가 몇명입니까? (0~5)' ) )
  smoke=as.character( readline('흡연을 하십니까?(yes/no)') )
  region=as.character(readline('사는 지역이 어디십니까? (southwest/southeast/northwest/northeast) ') )
  
  if  ( smoke=='yes' ) {  smoke_x <- 23847.5 } 
  else if  ( smoke=='no')  { smoke_x <- 1      }
  
  region_x <- 0
  
  if  ( region =='northeast' ) {   region_x <- 1  }
  else if  ( region =='northwest' ) { region_x <- -352.8 }
  else if  ( region =='southeast' )  { region_x <- -1035.6 }
  else if  ( region =='southwest ' ) { region_x <- -959.3  }
  
  y <-  256.8*x1 + 131.4*x2 + 339.3*x3 + 475.7*x4 + smoke_x + region_x 
  
  print (  paste( ' ai 가 예측한 의료비는 ' , y , ' 입니다 ')) 
  
}

reg_func()


■ 회귀 트리 

1. 회귀트리란 ? 수치를 예측하는 트리 ( tree )





tee <- c(1,1,1,2,2,3,4,5,5,6,6,7,7,7,7)
2. 원본 데이터를 A 속성으로 나누었을때의 데이터
at1 <- c(1,1,1,2,2,3,4,5,5)
at2 <- c(6,6,7,7,7,7)
3. 원본 데이터를 B 속성으로 나누었을떄의 데이터
bt1 <- c(1,1,1,2,2,3,4)
bt2 <- c(5,5,6,6,7,7,7,7)
4. A 속성으로 나누었을때의 SDR 을 구한다.
sdr_a <- sd(tee) - (length(at1)/length(tee)*sd(at1) + 
                      length(at2)/length(tee)*sd(at2) )

sdr_a 
sd(tee)


sdr_b <- sd(tee) - ( length(bt1) / length(tee) * sd(bt1) + length(bt2) / length(tee) * sd(bt2) )
sdr_b


■ 와인 데이터 실습 . 회귀 트리

1. 데이터를 로드한다. 

첨부파일 whitewines.csv

wine <- read.csv("whitewines.csv")

#fixed.acidity       : 고정 산도
#volatile.acidity    : 휘발성 산도
#citric.acid         : 시트르산
#residual.sugar      : 잔류 설탕
#chlorides           : 염화물
#free.sulfur.dioxide : 자유 이산화황
#total.sulfur.dioxide: 총 이산화황
#density             : 밀도
#pH                  : pH
#sulphates           : 황산염
#alcohol             : 알코올
#quality             : 품질
summary(wine)
unique(wine$quality)

#2. 와인의 quality 데이터가 정규분포에 속하는 안정적인 데이터 인지 확인

hist(wine$quality)
# 설명 : 어느 한쪽으로 데이터가 치우치지 않은 안정적인 모양을 보이고 있습니다.

# 3. wine 데이터를 train 데이터와 test 데이터로 나눈다.

wine_train <- wine[1:3750,  ] # 77%
wine_test  <- wine[3751:4898, ] # 23%
nrow(wine_train)
nrow(wine_test)

# 4. train 데이터를 가지고 model 을 생성한다. 
install.packages("rpart")
library(rpart)
model <-  rpart( quality ~ . , data=wine_train)
model 


설명: * 표시가 있는 노드는 잎노드로 노드에서 예측이 이루어진다는 것을 
     의미합니다. 와인 데이터의 예측 등급입니다.
     5.97 이라는 등급으로 예를 들면 alcohol < 10.85 이고 
     volatie.acidity < 0.2275 이면 모든 와인 샘플의 품질값은 5.97 로 예상된다.
     등급이 3~9 사이로 구성되어 있었습니다.
      
# 5. 위에서 나온 모델로 트리를 시각화 하시오 !
install.packages("rpart.plot")
library(rpart.plot)
rpart.plot( model, digits=3)
rpart.plot(model, digits=3, fallen.leaves=T, type=3, extra=101)

6. 위에서 만든 모델로 테스트 데이터의 라벨을 예측하시오 !
  result <- predict(model, wine_test) 
result
7. 테스트 데이터의 실제 라벨(품질) 과 예측결과(품질) 을 비교한다

g1 <-cbind( round(result), wine_test$quality)
g1 <-as.data.frame(g1)
nrow(g1[g1[1]==g1[2],])/nrow(g1) 

8. 테스트 데이터의 라벨과 예측 결과와 상관관계가 어떻게 되는지  확인한다.

cor(result, wine_test$quality)
설명: 이전에 knn, naivebayes, decision tree 의 경우에는 이원 교차표를 
그래서 정확도를 확인했는데 이번에는 수치 예측이므로 상관관계를 살펴보고
오차율을 살펴보며 모델의 성능을 확인해야합니다.
#0.5369 상관관계 : 높을수록 좋다.
9. 두 데이터간의 오차율을 확인 

MAE <-  function( actual, predicted) {
  mean(  abs( actual - predicted) ) 
}
# 실제값에서 예측값을 뺀 절대 값들의 평균


MAE( result, wine_test$quality) # 0.5872

설명: 이 모델의 경우 다른 모델인 서포트 벡터 머신에서는 오차가 0.45인데 0.58이면
      상대적으로 좀 큰 오차이므로 개선의 여지가 필요해 보입니다.

개선 방법 : 회귀 트리 -----> 모델 트리

## 내가 그냥 해본 Jrip 의사결정 트리로 해본거.
plot(wine$alcohol,wine$quality)
plot(wine$chlorides,wine$quality)
library(RWeka)
wine2 <- read.csv("whitewines.csv", header = T, stringsAsFactors = T)
wine2$quality <- as.factor(wine2$quality)

train_cnt <- round( 0.75 * dim(wine2)[1])
train_index <- sample(1:dim(wine2)[1], train_cnt, replace=F)
summary(wine2)
unique(wine2$quality)

wine2_train <- wine2[train_index,  ]
wine2_test  <- wine2[-train_index, ]
nrow(wine2_train)
model3 <-  JRip(quality ~ ., data=wine2_train)
model3

summary(model3)  
head(wine2_test)
ncol(wine2_test)
result3 <- predict( model3, wine2_test[   , -12] )
library(gmodels)
g2 <- CrossTable( wine2_test[ , 12],  result3) 
g2
g2$prop.tbl
j <- sum(g2$prop.tbl*diag(7))
g2$prop.tb[1]+g2$prop.tb[9]+g2$prop.tb[17]+g2$prop.tb[25]+g2$prop.tb[33]+g2$prop.tb[41]
#0.5367647
# 모델 트리로 해보기

#$$ 그림

g2$prop.tb[17]
#1. 회귀트리 실습의 1번 부터 3번 실습 까지 반복합니다

1.1. 데이터를 로드한다. 

첨부파일 whitewines.csv
wine <- read.csv("whitewines.csv")
#fixed.acidity       : 고정 산도
#volatile.acidity    : 휘발성 산도
#citric.acid         : 시트르산
#residual.sugar      : 잔류 설탕
#chlorides           : 염화물
#free.sulfur.dioxide : 자유 이산화황
#total.sulfur.dioxide: 총 이산화황
#density             : 밀도
#pH                  : pH
#sulphates           : 황산염
#alcohol             : 알코올
#quality             : 품질

1.2. 와인의 quality 데이터가 정규분포에 속하는 안정적인 데이터 인지 확인
hist(wine$quality)

1.3. wine 데이터를 train 데이터와 test 데이터로 나눈다.
wine_train <- wine[1:3750,  ]
wine_test  <- wine[3751:4898, ]

2. 모델트리를 구현하기 위한 패키지 설치
install.packages("Cubist")
library(Cubist)


3. 와인의 품질을 예측하는 모델을 생성한다. 
m.cubist <- cubist(x= wine_train[-12], y=wine_train$quality) 
m.cubist

4. 만든 모델과 테스트 데이터로 예측을 한다.
p.cubist <- predict( m.cubist, wine_test) 
p.cubist

5. 예측값(p.m5p) 과 테스트 데이터의 라벨간의 상관관계를 확인한다

cor( p.cubist , wine_test$quality ) # 0.6201015

6. 예측값(p.m5p) 과 테스트 데이터의 라벨간의 평균절대오차를 확인 한다.

MAE( wine_test$quality, p.cubist)   # 0.5339725

 설명: 회귀트리일때는 오차가 0.58 이었는데 모델트리는 오차가 0.53 으로 
        좀더 개선이 되었습니다.

6장 정리 : 다중 회귀분석에서는 미국 국민 의료비 데이터로 미국민의 의료비를
           예측하는 회귀 모델을 생성했었습니다. 회귀모델의 성능을 높이기
           위해서 파생변수를 생성했었습니다.
           회귀트리와 모델트리는 분류를 하는데 회귀의 개념이 섞인 분류입니다.
      머신러닝의 종류3가지 ? 
        1. 지도학습 : 분류 : knn,naivebayes, decision tree,
                              oneR, riper, regression tree, model treering
                      회귀 : 단순회귀분석
                             다중회귀분석
        2. 비지도 학습 
        3. 강화학습


문제249. 미국 보스톤 지역의 집값을 예측하는 머신러닝 모델을 생성하는데
          회귀트리를 먼저 생성하고 상관관계와 오차를 확인하고
         모델트리를 생성해서 상관관계와 오차가 더 향상이 되었는지 확인하는 
          테스트를 수행하시오 !
  
  1. 데이터를 로드한다. 

첨부파일 boston.csv
boston <- read.csv("boston.csv")

2. 본래 데이터의 최소값, 최대값 비교
summary(boston$MEDV)

3. 훈련과 테스트 데이터 생성
boston_train <- boston[1:495, ]
boston_test <- boston[496:506, ]
str(boston_train)

4. 회귀트리 모델을 생성한다.

model <-  rpart( MEDV ~ . , data=boston_train)
model 

5. 생성된 모델과 테스트 데이터로 예측한다.
result <- predict(model, boston_test) 

6. 결과와 실제 테스트 라벨과의 상관정도를 확인한다.

cor(result, boston_test$MEDV)

7. 결과와 실제 테스트 라벨과의 평균절대오차를 확인한다. 

MAE <-  function( actual, predicted) {
  mean(  abs( actual - predicted) ) 
}

MAE( result, boston_test$MEDV) 

8.이번에는 보스톤 하우징 데이터를 모델트리로 구현해서 성능을 높여본다. 
str(boston_train)
ncol(boston_train)
library(RWeka)
m.cubist <- cubist(x= boston_train[-14], y=boston_train$MEDV) 
m.cubist

4. 만든 모델과 테스트 데이터로 예측을 한다.
p.cubist <- predict( m.cubist, boston_test) 
p.cubist
cor( p.cubist , boston_test$MEDV )
MAE( boston_test$MEDV, p.cubist) 

m.m5p <- cubist(MEDV ~ . , data=boston_train)
m.m5p <- M5P(MEDV ~ . , data=boston_train)
p.m5p <- predict( m.m5p, boston_test) 
cor( p.m5p , boston_test$MEDV )
MAE( boston_test$MEDV, p.m5p) 









