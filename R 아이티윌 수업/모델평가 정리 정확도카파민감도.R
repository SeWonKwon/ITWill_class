
832  [쉬움주의] 유방암 데이터 자동 튜닝 문제1_종미코드를 준비하고  
k =21 과 k=11

45분까지 쉬세요 ~~
  
  wbcd <-  read.csv("wisc_bc_data.csv", header=T, stringsAsFactors=FALSE)
  wbcd$diagnosis <- factor( wbcd$diagnosis,
                            levels= c("B","M"),
                            labels=c("Benign", "Maliganant") ) 
  set.seed(1)
  wbcd_shuffle <- wbcd[ sample(569),    ] # 설명:  wbcd[  행,  열 ]
  wbcd_shuffle
  wbcd2 <-  wbcd_shuffle[ , -1 ]
   
  
  normalize <-  function(x) {
    return  ( (x-min(x)) / ( max(x) - min(x) ) )
  }
  
  wbcd_n <- as.data.frame( lapply( wbcd2[ , 2:31], normalize)  )
  
  
  nrow( wbcd_n ) # 569 
  train_num <- round( 0.9 * nrow(wbcd_n), 0 )
  train_num  # 512 
  
  wbcd_train <- wbcd_n[ 1:train_num,  ]   
  wbcd_test  <- wbcd_n[ (train_num+1) : nrow(wbcd_n),  ]  
  nrow(wbcd_test)   # 57
  
  wbcd_train_label <-  wbcd2[ 1:train_num,  1 ] 
  wbcd_test_label <- wbcd2[ (train_num+1) : nrow(wbcd_n), 1  ] 
  wbcd_test_label
  
  # install.packages("class")
  library(class)
  
  result1 <- knn(train=wbcd_train, test=wbcd_test,   cl=wbcd_train_label, k=21)
  result1
  
  data.frame( result1, wbcd_test_label)
  sum( result1 == wbcd_test_label )
  
  x <-  data.frame('실제'=wbcd_test_label, '예측'=result1)
  table(x) 
  positive_value <- "Maliganant"  
  negative_value <- 'Benign'
  actual_type <- wbcd_test_label
  predict_type <- result1
  result1
  x<-c() # 변수 생성
  
  #정확도
  library(gmodels)
  g <- CrossTable( actual_type, predict_type )
  a<-sum(g$prop.tbl *diag(2))   # 정확도 확인하는 코드
  x<-append(x,a)
    #카파통계량 
  # install.packages("vcd")
  library(vcd)
  # table( actual_type, predict_type)
  a<-Kappa( table( actual_type, predict_type)  ) 
  x<-append(x,a$Unweighted[1])
    #■ 민감도
  # install.packages("caret")
  library(caret)
  a<-sensitivity( predict_type, actual_type,
               positive=positive_value)
  x<-append(x,a)
    #■ 특이도
  a<-specificity(  predict_type, actual_type,
                negative=negative_value)  
  x<-append(x,a)
    #■ 정밀도
  a<-posPredValue( predict_type, actual_type,
                positive=positive_value) 
  x<-append(x,a)
    #■ 재현율 
  a<-sensitivity( predict_type, actual_type,
               positive=positive_value) 
  x<-append(x,a)  
    #■ F1 score
  # install.packages("MLmetrics")
  library(MLmetrics)
  a<-F1_Score( actual_type,  predict_type, positive = positive_value)
  x<-append(x,a)
  
  row_n = c('정확도','카파통계량','민간도','특이도','정밀도','재현율','F1 score')
  result_table_11<- data.frame(k11=x,row.names = row_n)
  result_table_11
  
  result_table_21<- data.frame(k21=x,row.names = row_n)
  result_table_21

  result_table <- cbind(result_table_11,result_table_21)
  View(result_table)  
  