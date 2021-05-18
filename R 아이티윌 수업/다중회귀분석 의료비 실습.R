
insurance <- read.csv("insurance.csv")
insurance$age2 <- insurance$age^2
insurance$age3 <- insurance$age^3
insurance$bmi30 <- ifelse( insurance$bmi >= 30, 1, 0 )
insurance$bmi20 <- ifelse( insurance$bmi >= 20, 1, 0 )
insurance$bmi40 <- ifelse( insurance$bmi >= 40, 1, 0 )
insurance$regionsouthwest <- ifelse( insurance$region=="southwest",1,0)
insurance$age30<-ifelse(insurance$age>=30,1,0)
insurance$children1<-ifelse(insurance$children>1,1,0)

# 변수에 대하여 산포도를 보고 특성을 파악
hist(insurance$expenses)
hist(insurance$bmi)
plot(insurance$age,insurance$expenses)
plot(insurance$bmi,insurance$expenses)
plot(insurance$smokeryes,insurance$expenses)
plot(insurance$children,insurance$expenses)
insurance$regionf <- as.factor(insurance$region)
plot(insurance$regionf,
     insurance$expense)
model<-lm(expense~.,data=insurance)

insurance$smokeryes<-ifelse(insurance$smoker=="yes",1,0)
insurance$regionsouthwest
model5 <- lm(expenses ~ age2 + children + bmi + bmi40+ sex + (bmi30+bmi40)*smoker + 
               region + age*bmi*sex*smoker + (age2+bmi)*smoker,
             data = insurance ) 
summary(model5) # 871

model5 <- lm(expenses ~ age2 + children + bmi 
             + bmi20+ sex + (bmi30+bmi20)*smoker 
             + region + age*bmi*sex*smoker + (age2+bmi)*smoker,
             data = insurance ) 
summary(model5) # 8709

model5 <- lm(expenses ~ age2 + children + bmi 
             + bmi40+ sex + (bmi20+bmi30+bmi40)*smoker 
             + region + age*bmi*sex*smoker + (age2+bmi)*smoker,
             data = insurance ) 
summary(model5) # 8711

model5 <- lm(expenses ~ age2 + children + bmi 
             + bmi40+ sex + (bmi20+bmi30+bmi40)*smoker 
             + region + age*bmi*sex*smoker + (age2*bmi)*smoker,
             data = insurance ) 
summary(model5) #8712

model5 <- lm(expenses ~ age2 + children + bmi 
             + bmi40+ sex + age2*(bmi20+bmi30+bmi40)*smoker 
             + region + age*bmi*sex*smoker + (age2*bmi)*smoker,
             data = insurance ) 
summary(model5) #8713

model5 <- lm(expenses ~ age2 + children + bmi 
             + bmi40+ sex + age2*(bmi20+bmi30+bmi40)*smoker*region 
             + region + age*bmi*sex*smoker + (age2*bmi)*smoker,
             data = insurance ) 
summary(model5) # 8744

model5 <- lm(expenses ~ age2 + children + bmi 
             + bmi40+ sex + age2*(bmi20+bmi30+bmi40)*smoker*region*children 
             + region + age*bmi*sex*smoker + (age2*bmi)*smoker,
             data = insurance ) 
summary(model5) #8784

model5 <- lm(expenses ~ age2 + children  
             + sex + age2*(bmi20*bmi30*bmi40)*smoker*region*children 
             + region + age*bmi*sex*smoker + (age2*bmi)*smoker,
             data = insurance ) 
summary(model5) # 8784

model5 <- lm(expenses ~ age2 + children  
             + sex 
             + age2*(bmi20*bmi30*bmi40)*smoker*region*children
             + region + age*bmi*sex*smoker*children1 + (age2*bmi)*smoker,
             data = insurance ) 
summary(model5) # 0.8799

model5 <- lm(expenses ~    
              
             age2*(bmi20*bmi30*bmi40)*smoker*region*children*sex
             + age*bmi*sex*smoker*children ,
             data = insurance ) 
summary(model5) #0.8869

model5 <- lm(expenses ~  
               age2*(bmi20*bmi30*bmi40)*smoker*region*children*sex*bmi
             + age*bmi*sex*smoker*children ,
             data = insurance ) 
summary(model5) #0.9034

summary(insurance)

# 최종 결과물

insurance <- read.csv("insurance.csv")
insurance$age2 <- insurance$age^2
insurance$bmi20 <- ifelse( insurance$bmi >= 24, 1, 0 )
insurance$bmi30 <- ifelse( insurance$bmi >= 30, 1, 0 )
insurance$bmi40 <- ifelse( insurance$bmi >= 37, 1, 0 )

model5 <- lm(expenses ~  
               age2*(bmi20*bmi30*bmi40)*sex*smoker*region*children*bmi
             + age*(bmi20*bmi30*bmi40)*sex*smoker*children*bmi ,
             data = insurance ) 
summary(model5)
# Multiple R-squared:  0.9172,	Adjusted R-squared:  0.8685

model5 <- lm(expenses ~  
               age2*(bmi20*bmi30*bmi40)*smoker*region*children*sex*bmi
             + age*(bmi20*bmi30*bmi40)*sex*smoker*children ,
             data = insurance ) 
summary(model5) 
# Multiple R-squared:  0.9158,	Adjusted R-squared:  0.8708





model5 <- lm(expenses ~  
               age2*(bmi20*bmi30*bmi40)*smoker*region*children*sex*bmi
             + age*bmi*sex*smoker*children ,
             data = insurance ) 
summary(model5) #0.9034
21 30 37  9085
22 30 37  9102
23 30 37  9114
24 30 37  9149

model5 <- lm(expenses ~  
               age2*(bmi20*bmi30*bmi40)*smoker*region*children*sex*bmi
             + age*(bmi20*bmi30*bmi40)*sex*smoker*children ,
             data = insurance ) 
summary(model5) 
# Multiple R-squared:  0.9158,	Adjusted R-squared:  0.8708

model5 <- lm(expenses ~  
               age2*(bmi20*bmi30*bmi40)*smoker*region*children*sex*bmi
             ,
             data = insurance ) 
summary(model5)
# Multiple R-squared:  0.9133,	Adjusted R-squared:  0.8713

