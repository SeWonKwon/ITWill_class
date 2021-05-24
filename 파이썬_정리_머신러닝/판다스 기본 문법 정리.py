### 판다스 기본 자료 검색
import pandas as pd
df = pd.read_csv("c:\\data\\emp3.csv")

pd.set_option('display.max_columns', 500)# 출력창 설정
# 기본 내용 검색하기
print(df.shape) # 행과 열 몇개인지 보기
print(df.head())
print(df.tail())

# 행과 열 인덱스로 검색하기 . 
# DataFrame 확인
print(df.shape) # raw와 columns
print(df.info()) #  R의 str(df)
print(df.describe()) # R에서의 summary(df) 의 결과와 유사합니다. 

# 행을 선택하는 방법 emp[행][열] --> emp[조건][컬럼명]
print(df.iloc[0:5, ]) 
print(df.iloc[-5: ,])

# 열을 선택하는 방법
print(df.iloc[ :, [0,1] ]) 
print(df.iloc[ :, : ]) 

# 컬럼 및 로우 보기 ( 갯수 관련 )

print(len(df))           # 열의 갯수
print(df.shape[0])        # 열의 갯수

print(df.columns)
print((len(df.columns))) # 컬럼의 갯수
print(df.shape[1])       # 컬럼의 갯수


print(df.size) # 총 몇개의 자료로 구성되어 있나. 아래와 같다.
print(df.shape[0]*df.shape[1])

#%% 특정 열, 컬럼 검색하기
print(df.columns)
