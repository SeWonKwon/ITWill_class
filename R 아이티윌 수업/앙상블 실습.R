# ■ 이론설명 1 . 모델 성능개선을 위해 11장에서 소개하고 있는 5가지 내용은 무엇인가?
#   
# 1.
# 2.
# 3.
# 4.
# 5.

이론설명2. 앙상블 기법은 무엇입니까?
  
  
  ■ 실습1. 정확도가 60% 밖에 되지 않는 분류기 모형들이 즐비한데 이 모형들을

최소한 몇개를 써야 정확도를 90% 를 능가하게 만들수 있을까 ?

  ret_err <- function(n,err) {
    sum <- 0 
    
    for(i in floor(n/2):n) { 
      sum <- sum + choose(n,i) * err^i * (1-err)^(n-i)
    }
    sum
  }
  for(j in 1:100) {
    err <- ret_err(j , 0.4)
    cat(j,'--->',1-err,'\n') 
    if(1-err >= 0.9) break
  }
  
  
  
  # ■ 실습1. 독일 은행 데이터로  채무 불이행자를 예측하는 배깅 실습 
  
  
  
  #1. 데이터를 로드한다.
  
  credit <- read.csv("credit.csv", stringsAsFactor=TRUE)
  str(credit) 
  
  #2. 데이터에 각 컬럼들을 이해한다. 
  
  #라벨 컬럼 :  default  --->  yes : 대출금 상환 안함 
  #no  : 대출금 상환 
  
  prop.table( table(credit$default)  )
  summary( credit$amount)
  
  #3. 데이터가 명목형 데이터인지 확인해본다.
  
  str(credit) 
  
  #4. 데이터를 shuffle 시킨다.
  
  set.seed(31)
  credit_shuffle <-  credit[ sample( nrow(credit) ),  ]
  
  #5. 데이터를 9 대 1로 나눈다.
  
  train_num <- round( 0.9 * nrow(credit_shuffle), 0) 
  
  credit_train <- credit_shuffle[1:train_num ,  ]
  
  credit_test  <- credit_shuffle[(train_num+1) : nrow(credit_shuffle),  ]
  
  # 배깅으로 성능 높이기 
  
  #install.packages("ipred")
  library(ipred)
  set.seed(300)
  
  # mybag <- bagging( default ~ . , data=credit_train, nbagg=25)
  #※ 설명:  nbagg=25 은 앙상블에 사용되는 bag의 갯수를 25개
  mybag <- bagging( default ~ . , data=credit_train, nbagg=50)
  mybag
  
  credit_pred <- predict( mybag,  credit_test[   , -17] )
  credit_pred
  
  table( credit_pred, credit_test$default ) 
  prop.table(  table( credit_pred==credit_test$default)  )
  
  
  #■ 정확도
  
  g <- CrossTable( credit_test$default, credit_pred )
  
  x <- sum(g$prop.tbl *diag(2))   # 정확도 확인하는 코드
  x
  
  
  # 문제1. bag 의 갯수를 50개로 늘리고 확인해 봅니다.
  
  
  
  답:

    ;mybag <- bagging( default ~ . , data=credit_train, nbagg=50)
  