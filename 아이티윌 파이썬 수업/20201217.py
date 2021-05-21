# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 09:30:19 2020

@author: stu02
"""

#%% 12기_허정민 코드


from  bs4  import  BeautifulSoup
import  urllib.request   # 웹상의 url 을 파이썬이 인식할 수 있도록 해주는 모듈

def c_scroll():
    for i in range(1,4):
        list_url = 'https://futurechosun.com/page/'+str(i)+'?s=%EB%B4%89%EC%82%AC'
        url = urllib.request.Request(list_url) 
        result = urllib.request.urlopen(url).read().decode("utf-8") 
        soup = BeautifulSoup( result, "html.parser")
       # result1=soup.find('div',class_ ='elementor-post__title').find('a')
        result1=soup.find_all('div',class_ ='elementor-post__title')
        for  i  in  result1:
            print (i.find_all('a')[0].get("href"))
        #print(result1.get("href"))
        '''
        for i in result1:
            for k in i:
                print(type(k))
        '''
        
#%% beautiful soup 기능으로 웹스크롤링할 때 추가로 알아야 할 사항.
# 예제1. 웹스크롤링을 할 사이트에 접속합니다.

https://futurechosun.com/page/1?s=%EB%B4%89%EC%82%AC

#%%예제2. 위의 사이트에서 키워드 '봉사'로 검색을 합니다.
https://futurechosun.com/page/1?s=%EB%B4%89%EC%82%AC
https://futurechosun.com/page/2?s=%EB%B4%89%EC%82%AC
https://futurechosun.com/page/4?s=%EB%B4%89%EC%82%AC

https://futurechosun.com/page/97?s=%EB%B4%89%EC%82%AC

# 패턴은 https://futurechosun.com/page/ +str(page)+?s=%EB%B4%89%EC%82%AC

#%%예제3. 위의 첫페이지의 html 코드를 파이썬으로 불러오는 작업

#1. 웹스크롤링에 필요한 모듈을 임폴트 합니다.

from  bs4  import  BeautifulSoup  # 웹스크롤링 전문 모듈인 beautiful soup 모듈을 이용할 수 있겠금
import  urllib.request # url을 파이썬에서 인식하게 도와주는 모듈

#2. 첫페이지의 url 을 파싱합니다. 파싱이란? 파이썬이 알아 볼수 있는 기계어로 변환


list_url = 'https://futurechosun.com/page/1?s=%EB%B4%89%EC%82%AC'
url = urllib.request.Request(list_url) 
result = urllib.request.urlopen(url).read().decode("utf-8")
print(result)

#3. 웹스크롤링 전문 모듈인 beautiful soup 모듈을 이용할 수 있겠금 
# 내려받은 html 코드를 beautiful soup 을 이용할 수 있게 파싱합니다.
# 이용할 수 있게 한다는 것은 beautiful soup 의 함수인 find_all 을 이용해서 
# 테그 이름과 클래스 이름을 가지고 검색하기 원하는 지점을 빠르게 찾아가기 위해서 입니다.

#%%

from  bs4  import  BeautifulSoup 
import  urllib.request 

list_url = 'https://futurechosun.com/page/1?s=%EB%B4%89%EC%82%AC'
url = urllib.request.Request(list_url) 
result = urllib.request.urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(result, "html.parser") # BeautifulSoup 모듈을 적용해서 원하는 것을 쉽게 접근한다.
print(soup)

#4. 더나은 미래 첫페이지에 보이는 기사들 12개의 기사 url을 알아내기 위해 테그 이름과 클래스 이름이
# 무엇인지 알아내시오~

# <div class="elementor-post__title"> <a href="https://futurechosun.com/archives/52491"> “편견에 주눅 들었던 결혼 이주 여성들… ‘봉사’로 자존감 되찾았다죠” </a></div>

#답: 테그이름은 div 이고 클래스 이름은 elementor-post__title 입니다. 
#$$중요설명: href 와 가장 가까이 있는 테그 이름과 클래스 이름을 알아내야 합니다.

#5. 테그이름 div 에 클래스 이름 elementor-post__title 에 해당하는 BeautifulSoup으로
#파싱된 html 코드들을 모두 긁어 오시오~

#%%앞의 코드들 ....

from  bs4  import  BeautifulSoup 
import  urllib.request 

list_url = 'https://futurechosun.com/page/1?s=%EB%B4%89%EC%82%AC'
url = urllib.request.Request(list_url) 
result = urllib.request.urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(result, "html.parser")
result1 = soup.find_all('div', class_= 'elementor-post__title')
print(type(result1),result1)

#<class 'bs4.element.ResultSet'> 이지만 리스트처럼 움직인다. 리스트랑은 조금 다름

# 0번째 요소 <div class="elementor-post__title"> 
# <a href="https://futurechosun.com/archives/52491"> 
# “편견에 주눅 들었던 결혼 이주 여성들… ‘봉사’로 자존감 되찾았다죠” 
# </a></div>, 

# 1번째 요소 <div class="elementor-post__title"> 
# <a href="https://futurechosun.com/archives/47330"> 
# [글로벌 이슈] 전 세계 코로나19 확산으로… 해외 봉사 ‘올스톱’ 위기 
# </a></div>,

# 우리가 원하는것은 BS로 파싱된 result1 의 결과를 보면 div 테그 안에 있는 a 테그 안에 있는 url 주소만이다. 
# result1은 리스트처럼 움직이기 때문에 하나하나 긁어 오기 위해서는 요소들을 하나씩 빼내와야합니다.
# 하나씩 빼내어 오려면 리스트 안의 요소를 하나씩 빼내올려면 뭘 써야하나요? 
# for loop 문!!

#6. result1 리스트의 요소들( beautiful soup 으로 파싱된 html 코드들)을 for loop문으로 하나씩
# 빼냅니다.

#%% 
from  bs4  import  BeautifulSoup 
import  urllib.request 

list_url = 'https://futurechosun.com/page/1?s=%EB%B4%89%EC%82%AC'
url = urllib.request.Request(list_url) 
result = urllib.request.urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(result, "html.parser")
result1 = soup.find_all('div', class_= 'elementor-post__title')

for i in result1:
    print(i.find_all('a'))
    
#8. 위의 a 테그의 html 코드를 담은 리스트는 요소를 딱 하나만 담고 있다.
# 그래서 리스트안의 그 요소만 딱 뽑아내서 출력을 하시오 !

for i in result1:
    print(i.find_all('a')[0])
    
#9. 그러면 뽑아낸 a 테그의 html 문서에서 href 의 값만 얻어내시오~

for i in result1:
    print(i.find_all('a')[0].get('href'))
    
#%%
#10.그러면 기사 상세 url을 params 라는 리스트에 append 시킨다.
from  bs4  import  BeautifulSoup 
import  urllib.request 

list_url = 'https://futurechosun.com/page/1?s=%EB%B4%89%EC%82%AC'
url = urllib.request.Request(list_url) 
result = urllib.request.urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(result, "html.parser")
result1 = soup.find_all('div', class_= 'elementor-post__title')
params = []
for i in result1:
    params.append(i.find_all('a')[0].get('href'))
        

#%%11. 첫페이지만 가져오는게 아니라 1페이지부터 3페이지까지 24x3 = 73 페이지의 기사 url을 
#params 리스트에 append 시키시오.
from  bs4  import  BeautifulSoup 
import  urllib.request 
from time import sleep
params = []
for i in range(1,4):
    sleep(3)
    list_url = 'https://futurechosun.com/page/'+str(i)+'?s=%EB%B4%89%EC%82%AC'
    url = urllib.request.Request(list_url) 
    result = urllib.request.urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(result, "html.parser")
    result1 = soup.find_all('div', class_= 'elementor-post__title')
    for i in result1:
        params.append(i.find_all('a')[0].get('href'))
        
print(len(params)) #36
#%%
#12. 위의  params 에 중복의 요소가 있으니 제거해 준다.
params = set(params)
params = list(params)
print(len(params))

#%%13. 위의 코드들을 가지고 bs_scroll() 이라는 함수로 생성하시오!

from  bs4  import  BeautifulSoup 
import  urllib.request 
from time import sleep

def bs_scroll():
    params = []
    for i in range(1,4):
        sleep(3)
        list_url = 'https://futurechosun.com/page/'+str(i)+'?s=%EB%B4%89%EC%82%AC'
        url = urllib.request.Request(list_url) 
        result = urllib.request.urlopen(url).read().decode("utf-8")
        soup = BeautifulSoup(result, "html.parser")
        result1 = soup.find_all('div', class_= 'elementor-post__title')
        for i in result1:
            params.append(i.find_all('a')[0].get('href'))
    return params

print(bs_scroll())
    
#%%14. 더 나은 미래의 상세기사 url 하나를 가지고 본문 기사를 출력하시오!

# https://futurechosun.com/archives/52491

# <div class="elementor-widget-container"><p><strong>[우리사회 利주민] 박시은 ‘다빛나’ 대표</strong></p><p>사람은 타인과 사회로부터 상처를 받으면 주눅 들게 된다. 상처를 성장의 발판으로 삼은 사람들의 이야기가 영웅담처럼 읽히는 것도 그만큼 그런 일이 드물고 어렵다는 방증이다. 결혼 이주 여성들의 모임 ‘다빛나’도 그런 노력의 결과물 중 하나다. 다빛나는 중국·베트남·네팔 등에서 온 결혼 이주 여성 26명이 참여하는 자조 모임이다. 기댈 곳 없는 이주 여성끼리 마음을 나누던 모임이 사회봉사를 통해 이주 여성에 대한 인식을 바꾸는 단체로 자라났다.</p><p>다빛나를 이끌어온 사람은 중국 옌지 출신 박시은(41) 대표다. 지난 23일 서울 광장동에서 만난 박 대표는 “봉사는 우리 자신을 위한 일이기도 하다”고 했다. 그는 “결혼 이주 여성은 사회적으로 소외되고 경제적으로 어려운 경우가 많은데, 다른 사람을 도우면서 스스로 ‘무언가 할 수 있는 사람’이라는 자존감도 높아지기 때문”이라고 했다. 박 대표는 “봉사를 통해 이주 여성 스스로 역량을 강화하고, 한국 내 이주민에 대한 인식을 개선하는 게 목표”라고 설명했다.</p><figure id="attachment_52527" aria-describedby="caption-attachment-52527" style="width: 500px" class="wp-caption aligncenter"><noscript><img class="size-full wp-image-52527" src="https://futurechosun.com/wp-content/uploads/201201-0010.jpg" alt="" width="500" height="771" srcset="https://futurechosun.com/wp-content/uploads/201201-0010.jpg 500w, https://futurechosun.com/wp-content/uploads/201201-0010-195x300.jpg 195w, https://futurechosun.com/wp-content/uploads/201201-0010-150x231.jpg 150w" sizes="(max-width: 500px) 100vw, 500px" /></noscript><img class="size-full wp-image-52527 ls-is-cached lazyloaded" src="https://futurechosun.com/wp-content/uploads/201201-0010.jpg" data-src="https://futurechosun.com/wp-content/uploads/201201-0010.jpg" alt="" width="500" height="771" data-srcset="https://futurechosun.com/wp-content/uploads/201201-0010.jpg 500w, https://futurechosun.com/wp-content/uploads/201201-0010-195x300.jpg 195w, https://futurechosun.com/wp-content/uploads/201201-0010-150x231.jpg 150w" data-sizes="(max-width: 500px) 100vw, 500px" sizes="(max-width: 500px) 100vw, 500px" srcset="https://futurechosun.com/wp-content/uploads/201201-0010.jpg 500w, https://futurechosun.com/wp-content/uploads/201201-0010-195x300.jpg 195w, https://futurechosun.com/wp-content/uploads/201201-0010-150x231.jpg 150w"><figcaption id="caption-attachment-52527" class="wp-caption-text">지난달 23일 서울 광장동에서 만난 박시은 다빛나 대표는 “이주민도 존중받아야 하는 평범한 사람이라는 걸 알리기 위해 시작한 봉사가 지금은 이주 여성들의 ‘자존감 지킴이’ 역할을 하고 있다”고 했다. / 이신영 C영상미디어 기자</figcaption></figure><p><strong>“아이들이 차별받을 때 가장 마음 아팠어요”</strong></p><p>박 대표는 대학을 졸업하고 베이징에서 직장생활을 하다 남편을 만났다. 2006년 가족이 함께 한국으로 이주했다. 한국 생활은 녹록지 않았다. 박 대표는 “대학도 나왔고 직장생활도 해서 자신감이 있었지만 한국에서는 차별이 심해 상처를 많이 받았다”고 했다.</p><p>“가장 마음이 아플 땐 아이들이 차별받을 때였죠. ‘저 애 엄마가 중국인이니까 놀지 마라’고 하는 사람도 많았어요. 서울 말씨를 익혔더니 사람들이 제가 중국 출신인 걸 모르고 “저 동네엔 중국인이 많아 더럽고 위험하다’고 서슴없이 말했어요. 거기에 또 상처를 받았어요.”</p><p>주저앉아 있을 순 없었다. 할 수 있는 일부터 하자는 생각으로 심리상담사 자격증반을 수강했다. 꼬박 3년이 걸렸다.</p><p>“자격증을 따면서 스스로 내공이 쌓이니 가족은 물론 주변 사람들의 시선이 달라지는 걸 느꼈어요. 그때 저와 비슷한 고민을 가진 다른 결혼 이주 여성들이 자신감을 되찾을 수 있도록 도와야겠다고 결심했습니다.”</p><p>여러 이주 여성들이 그의 뜻에 동참했고 2018년 함께 다빛나를 설립했다. “처음엔 다문화센터에서 떡 케이크 만들기 교육을 받은 후, 혼자 사는 어르신께 떡 케이크를 만들어 드렸어요. 예상보다 훨씬 좋은 반응에 탄력이 붙었죠. ‘그간 너무 외로웠는데 고맙다’며 눈물을 보이는 어르신도 있었어요.”</p><p><strong>‘다문화’라는 단어에 담긴 편견 깨고 싶어</strong></p><p>봉사활동은 그동안 주눅 들어 있던 결혼 이주 여성들에게 변화를 가져왔다. 박 대표는 “많은 회원이 ‘봉사를 통해 자존감이 올라간다’며 무척 행복해한다”고 했다. “오랜 기간 한국에서 차별받다 보니 부당한 일을 당해도 항의조차 못 할 정도로 주눅이 든 사람들이 많았어요. 그런데 봉사를 하니 ‘나도 누군가에게 감사 인사를 받는 사람’이라며 얼굴이 확 밝아졌죠.”</p><p>봉사활동의 범위도 넓어졌다. 독거 노인들에게 반려 식물을 선물하고, 지역 취약 계층 아동을 대상으로 세계 문화 체험 교육도 진행했다. 수공예품을 만들어 판 뒤 아동센터 등에 기부하기도 했다. 박 대표는 “요즘은 복지단체에서 먼저 ‘좀 도와줄 수 있느냐’며 연락이 올 정도”라며 자랑했다. 최근에는 천주교에서 준비 중인 이주민 동료 상담 기관 ‘엔피코’ 설립에도 참여하고 있다. 박 대표는 “말과 문화도 통하고, 서로의 상황을 깊이 공감하는 이주민끼리 서로를 지지해주는 모델”이라고 했다.</p><p>최근 다빛나는 ‘다문화가 빛나는 나눔’에서 ‘다 함께 빛나는 나눔’으로 단체의 뜻을 바꿨다. 박 대표는 “‘다문화’라는 단어에 들어 있는 차별적인 시선 때문”이라고 했다. “호주 출신 방송인 샘 해밍턴 가족은 ‘다문화’가 아니라 ‘글로벌 가족’이라고 부르잖아요. 사전적 의미로는 그 가족도 다문화 가족인데도요. 다문화라는 단어에는 한국보다 못사는 나라에서 온 도움이 필요한 사람들이란 시선이 담겨서가 아닐까요? 다문화라는 단어에 갇히지 않고, ‘한국 출신 한국인’들과도 손을 잡는다는 의미로 ‘다 함께 빛나는 나눔’이라고 부르기로 했습니다.”</p><p>다빛나의 목표는 두 가지다. 첫째는 결혼 이주 여성들의 당당한 자립. 둘째는 봉사활동이다. 궁극적으로는 결혼 이주 여성에 대한 편견을 없애고 싶다고 했다. 최근엔 일자리 창출 사업도 시작했다. 재단법인 ‘밴드’의 도움으로 지난달부터 사회적기업 ‘화유 플라워’에 이주 여성 2명을 파견하고 있다.</p><p>“대표님이 ‘이주 여성 분들이 아주 손이 빨라서 일에 큰 도움이 된다’며 놀라워하세요. 이렇게 한번 저희에게 기회를 주면, 제 몫을 충분히 한다는 걸 보여줄 수 있어요. 당당한 한 명의 주민으로 결혼 이주 여성이 존중받을 수 있게 꾸준히 활동을 이어갈 계획입니다.”</p><p>박선하 더나은미래 기자 sona@chosun.com</p></div>
# 위의 테그로 해봤더니 깔끔하게 떨어 지지 않아서 
#<div class="elementor-element elementor-element-24e82692 elementor-widget__width-initial elementor-widget elementor-widget-theme-post-content" data-id="24e82692" data-element_type="widget" data-widget_type="theme-post-content.default"><div class="elementor-widget-container"><p><strong>[우리사회 利주민] 박시은 ‘다빛나’ 대표</strong></p><p>사람은 타인과 사회로부터 상처를 받으면 주눅 들게 된다. 상처를 성장의 발판으로 삼은 사람들의 이야기가 영웅담처럼 읽히는 것도 그만큼 그런 일이 드물고 어렵다는 방증이다. 결혼 이주 여성들의 모임 ‘다빛나’도 그런 노력의 결과물 중 하나다. 다빛나는 중국·베트남·네팔 등에서 온 결혼 이주 여성 26명이 참여하는 자조 모임이다. 기댈 곳 없는 이주 여성끼리 마음을 나누던 모임이 사회봉사를 통해 이주 여성에 대한 인식을 바꾸는 단체로 자라났다.</p><p>다빛나를 이끌어온 사람은 중국 옌지 출신 박시은(41) 대표다. 지난 23일 서울 광장동에서 만난 박 대표는 “봉사는 우리 자신을 위한 일이기도 하다”고 했다. 그는 “결혼 이주 여성은 사회적으로 소외되고 경제적으로 어려운 경우가 많은데, 다른 사람을 도우면서 스스로 ‘무언가 할 수 있는 사람’이라는 자존감도 높아지기 때문”이라고 했다. 박 대표는 “봉사를 통해 이주 여성 스스로 역량을 강화하고, 한국 내 이주민에 대한 인식을 개선하는 게 목표”라고 설명했다.</p><figure id="attachment_52527" aria-describedby="caption-attachment-52527" style="width: 500px" class="wp-caption aligncenter"><noscript><img class="size-full wp-image-52527" src="https://futurechosun.com/wp-content/uploads/201201-0010.jpg" alt="" width="500" height="771" srcset="https://futurechosun.com/wp-content/uploads/201201-0010.jpg 500w, https://futurechosun.com/wp-content/uploads/201201-0010-195x300.jpg 195w, https://futurechosun.com/wp-content/uploads/201201-0010-150x231.jpg 150w" sizes="(max-width: 500px) 100vw, 500px" /></noscript><img class="size-full wp-image-52527 ls-is-cached lazyloaded" src="https://futurechosun.com/wp-content/uploads/201201-0010.jpg" data-src="https://futurechosun.com/wp-content/uploads/201201-0010.jpg" alt="" width="500" height="771" data-srcset="https://futurechosun.com/wp-content/uploads/201201-0010.jpg 500w, https://futurechosun.com/wp-content/uploads/201201-0010-195x300.jpg 195w, https://futurechosun.com/wp-content/uploads/201201-0010-150x231.jpg 150w" data-sizes="(max-width: 500px) 100vw, 500px" sizes="(max-width: 500px) 100vw, 500px" srcset="https://futurechosun.com/wp-content/uploads/201201-0010.jpg 500w, https://futurechosun.com/wp-content/uploads/201201-0010-195x300.jpg 195w, https://futurechosun.com/wp-content/uploads/201201-0010-150x231.jpg 150w"><figcaption id="caption-attachment-52527" class="wp-caption-text">지난달 23일 서울 광장동에서 만난 박시은 다빛나 대표는 “이주민도 존중받아야 하는 평범한 사람이라는 걸 알리기 위해 시작한 봉사가 지금은 이주 여성들의 ‘자존감 지킴이’ 역할을 하고 있다”고 했다. / 이신영 C영상미디어 기자</figcaption></figure><p><strong>“아이들이 차별받을 때 가장 마음 아팠어요”</strong></p><p>박 대표는 대학을 졸업하고 베이징에서 직장생활을 하다 남편을 만났다. 2006년 가족이 함께 한국으로 이주했다. 한국 생활은 녹록지 않았다. 박 대표는 “대학도 나왔고 직장생활도 해서 자신감이 있었지만 한국에서는 차별이 심해 상처를 많이 받았다”고 했다.</p><p>“가장 마음이 아플 땐 아이들이 차별받을 때였죠. ‘저 애 엄마가 중국인이니까 놀지 마라’고 하는 사람도 많았어요. 서울 말씨를 익혔더니 사람들이 제가 중국 출신인 걸 모르고 “저 동네엔 중국인이 많아 더럽고 위험하다’고 서슴없이 말했어요. 거기에 또 상처를 받았어요.”</p><p>주저앉아 있을 순 없었다. 할 수 있는 일부터 하자는 생각으로 심리상담사 자격증반을 수강했다. 꼬박 3년이 걸렸다.</p><p>“자격증을 따면서 스스로 내공이 쌓이니 가족은 물론 주변 사람들의 시선이 달라지는 걸 느꼈어요. 그때 저와 비슷한 고민을 가진 다른 결혼 이주 여성들이 자신감을 되찾을 수 있도록 도와야겠다고 결심했습니다.”</p><p>여러 이주 여성들이 그의 뜻에 동참했고 2018년 함께 다빛나를 설립했다. “처음엔 다문화센터에서 떡 케이크 만들기 교육을 받은 후, 혼자 사는 어르신께 떡 케이크를 만들어 드렸어요. 예상보다 훨씬 좋은 반응에 탄력이 붙었죠. ‘그간 너무 외로웠는데 고맙다’며 눈물을 보이는 어르신도 있었어요.”</p><p><strong>‘다문화’라는 단어에 담긴 편견 깨고 싶어</strong></p><p>봉사활동은 그동안 주눅 들어 있던 결혼 이주 여성들에게 변화를 가져왔다. 박 대표는 “많은 회원이 ‘봉사를 통해 자존감이 올라간다’며 무척 행복해한다”고 했다. “오랜 기간 한국에서 차별받다 보니 부당한 일을 당해도 항의조차 못 할 정도로 주눅이 든 사람들이 많았어요. 그런데 봉사를 하니 ‘나도 누군가에게 감사 인사를 받는 사람’이라며 얼굴이 확 밝아졌죠.”</p><p>봉사활동의 범위도 넓어졌다. 독거 노인들에게 반려 식물을 선물하고, 지역 취약 계층 아동을 대상으로 세계 문화 체험 교육도 진행했다. 수공예품을 만들어 판 뒤 아동센터 등에 기부하기도 했다. 박 대표는 “요즘은 복지단체에서 먼저 ‘좀 도와줄 수 있느냐’며 연락이 올 정도”라며 자랑했다. 최근에는 천주교에서 준비 중인 이주민 동료 상담 기관 ‘엔피코’ 설립에도 참여하고 있다. 박 대표는 “말과 문화도 통하고, 서로의 상황을 깊이 공감하는 이주민끼리 서로를 지지해주는 모델”이라고 했다.</p><p>최근 다빛나는 ‘다문화가 빛나는 나눔’에서 ‘다 함께 빛나는 나눔’으로 단체의 뜻을 바꿨다. 박 대표는 “‘다문화’라는 단어에 들어 있는 차별적인 시선 때문”이라고 했다. “호주 출신 방송인 샘 해밍턴 가족은 ‘다문화’가 아니라 ‘글로벌 가족’이라고 부르잖아요. 사전적 의미로는 그 가족도 다문화 가족인데도요. 다문화라는 단어에는 한국보다 못사는 나라에서 온 도움이 필요한 사람들이란 시선이 담겨서가 아닐까요? 다문화라는 단어에 갇히지 않고, ‘한국 출신 한국인’들과도 손을 잡는다는 의미로 ‘다 함께 빛나는 나눔’이라고 부르기로 했습니다.”</p><p>다빛나의 목표는 두 가지다. 첫째는 결혼 이주 여성들의 당당한 자립. 둘째는 봉사활동이다. 궁극적으로는 결혼 이주 여성에 대한 편견을 없애고 싶다고 했다. 최근엔 일자리 창출 사업도 시작했다. 재단법인 ‘밴드’의 도움으로 지난달부터 사회적기업 ‘화유 플라워’에 이주 여성 2명을 파견하고 있다.</p><p>“대표님이 ‘이주 여성 분들이 아주 손이 빨라서 일에 큰 도움이 된다’며 놀라워하세요. 이렇게 한번 저희에게 기회를 주면, 제 몫을 충분히 한다는 걸 보여줄 수 있어요. 당당한 한 명의 주민으로 결혼 이주 여성이 존중받을 수 있게 꾸준히 활동을 이어갈 계획입니다.”</p><p>박선하 더나은미래 기자 sona@chosun.com</p></div></div>
# 두번쨰 테그로 검색해서 찾아냄
from  bs4  import  BeautifulSoup 
import  urllib.request 
list_url = 'https://futurechosun.com/archives/52491'
url = urllib.request.Request(list_url) 
result = urllib.request.urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(result, "html.parser")
result1 = soup.find_all('div', class_= 'elementor-element elementor-element-24e82692 elementor-widget__width-initial elementor-widget elementor-widget-theme-post-content')

for i in result1:
    # for j in i:
    #     print(j)
    print(i.find_all('p'))

#15. (점심시간 문제) 위의 코드를 가지고 bs_detail_scroll() 함수로 생성하시오 !
#%%
def bs_detail_scroll():
    params = []
    for i in bs_scroll():
        list_url = i
        url = urllib.request.Request(list_url) 
        result = urllib.request.urlopen(url).read().decode("utf-8")
        soup = BeautifulSoup(result, "html.parser")
        result1 = soup.find_all('div', class_= 'elementor-element elementor-element-24e82692 elementor-widget__width-initial elementor-widget elementor-widget-theme-post-content')
        
        for i in result1:
            for j in i.find_all('p'):
                params.append(j.get_text())
    return params
    

print(bs_detail_scroll())

#%% 16. 지금 방금 생성한 bs_detail_scroll() 함수의 코드안에 bs_scroll() 함수를 호출하는 
# 코드를 추가해서 bs_scroll()함수가 리턴하는 36개의 상세기사 url에 대한 기사 본문이 전부 출력되게 하시오!


from  bs4  import  BeautifulSoup 
import  urllib.request 
from time import sleep

def bs_scroll():
    params = []
    for i in range(1,4):
        sleep(3)
        list_url = 'https://futurechosun.com/page/'+str(i)+'?s=%EB%B4%89%EC%82%AC'
        url = urllib.request.Request(list_url) 
        result = urllib.request.urlopen(url).read().decode("utf-8")
        soup = BeautifulSoup(result, "html.parser")
        result1 = soup.find_all('div', class_= 'elementor-post__title')
        for i in result1:
            params.append(i.find_all('a')[0].get('href'))
    return params

def bs_detail_scroll():
    params = []
    for i in bs_scroll():
        list_url = i
        url = urllib.request.Request(list_url) 
        result = urllib.request.urlopen(url).read().decode("utf-8")
        soup = BeautifulSoup(result, "html.parser")
        result1 = soup.find_all('div', class_= 'elementor-element elementor-element-24e82692 elementor-widget__width-initial elementor-widget elementor-widget-theme-post-content')
        for i in result1:
            for j in i.find_all('p'):
                params.append(j.get_text())
    return params

print(bs_detail_scroll())

#%% 17. bs_detail_scroll() 함수의 params2 리스트를 추가해서 params2 리스트에 36개의 기사가 append 되게 하시오!

from  bs4  import  BeautifulSoup 
import  urllib.request 
from time import sleep

def bs_scroll():
    params = []
    for i in range(1,3):
        sleep(3)
        list_url = 'https://futurechosun.com/page/'+str(i)+'?s=%EB%B4%89%EC%82%AC'
        url = urllib.request.Request(list_url) 
        result = urllib.request.urlopen(url).read().decode("utf-8")
        soup = BeautifulSoup(result, "html.parser")
        result1 = soup.find_all('div', class_= 'elementor-post__title')
        for i in result1:
            params.append(i.find_all('a')[0].get('href'))
    return params

def bs_detail_scroll():
    params = []
    for i in bs_scroll():
        list_url = i
        url = urllib.request.Request(list_url) 
        result = urllib.request.urlopen(url).read().decode("utf-8")
        soup = BeautifulSoup(result, "html.parser")
        result1 = soup.find_all('div', class_= 'elementor-element elementor-element-24e82692 elementor-widget__width-initial elementor-widget elementor-widget-theme-post-content')
        for i in result1:
            for j in i.find_all('p'):
                params.append(j.get_text())
    

# print(len(bs_detail_scroll()))
#%%
#18. 위에서 수집한 기사가 들어 있는 params2 리스트의 내용을 c 드라이브 밑에 data 밑에 bongsa.txt 로 생성되게 하시오.

from  bs4  import  BeautifulSoup 
import  urllib.request 
from time import sleep

def bs_scroll():
    params = []
    for i in range(1,2):
        sleep(3)
        list_url = 'https://futurechosun.com/page/'+str(i)+'?s=%EB%B4%89%EC%82%AC'
        url = urllib.request.Request(list_url) 
        result = urllib.request.urlopen(url).read().decode("utf-8")
        soup = BeautifulSoup(result, "html.parser")
        result1 = soup.find_all('div', class_= 'elementor-post__title')
        for i in result1:
            params.append(i.find_all('a')[0].get('href'))
    return params

def bs_detail_scroll():
    f = open("c:\\data\\bongsa.txt",'w',encoding="UTF-8")
    for i in bs_scroll():
        list_url = i
        url = urllib.request.Request(list_url) 
        result = urllib.request.urlopen(url).read().decode("utf-8")
        soup = BeautifulSoup(result, "html.parser")
        result1 = soup.find_all('div', class_= 'elementor-element elementor-element-24e82692 elementor-widget__width-initial elementor-widget elementor-widget-theme-post-content')
        for i in result1:
            for j in i.find_all('p'):
                f.write(str(j.get_text())+'\n')
    f.close()
        
bs_detail_scroll()
#%%이데일리 사이트 웹스크롤링 하기

# 예제1. 이데일리에서 "첫눈"으로 검색한 기사를 검색하시오.

# https://www.edaily.co.kr/search/news/?keyword=%ec%b2%ab%eb%88%88&page=1
# https://www.edaily.co.kr/search/news/?keyword=%ec%b2%ab%eb%88%88&page=2

# https://www.edaily.co.kr/search/news/?keyword=%ec%b2%ab%eb%88%88&page=7

# 예제2. 위의 url 의 첫 페이지의 html 코드를 BeautifulSoup으로 파싱하시오~

from  bs4  import  BeautifulSoup 
import  urllib.request 

list_url = 'https://www.edaily.co.kr/search/news/?keyword=%ec%b2%ab%eb%88%88&page=1'
url = urllib.request.Request(list_url) 
result = urllib.request.urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(result,"html.parser")
print(soup)

#예제3. 상세기사 url을 찾기 위한 테그 이름과 클래스 이름을 찾아보시오.

# <div class="newsbox_04">
#                                         <a href="/news/read?newsId=01423526625998520&amp;mediaCodeNo=258" title="김성규 &quot;MV에 눈 맞는 장면 多…첫눈 보며 운명이구나 싶어&quot;">
                                          

#%%예제4. 위의 div 테그와 newsbox_04 클래스를 가지고 href 의 상세기사 url을 출력하시오!

from  bs4  import  BeautifulSoup 
import  urllib.request 

list_url = 'https://www.edaily.co.kr/search/news/?keyword=%ec%b2%ab%eb%88%88&page=1'
url = urllib.request.Request(list_url) 
result = urllib.request.urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(result,"html.parser")
result1 = soup.find_all('div', class_='newsbox_04')
# print(result1) # 해보니 result1 안에 너무 많으니까
for i in result1:
    print(i.find_all('a')[0].get('href'))
    
    # i.find_all('a') 는 리스트형이어서 [0]을 붙여주면 하나의 요소가 된다. 아래처럼
    # 저 리스트 안에 요소가 두개가 있다. [0] 이라고 붙여주면 요소(즉, html 코드)가 된다.
    # 그리고 나서 거기에 get('href') 값만 가져온다.
    
#%%
# <a href="/news/read?newsId=04008166625996880&amp;mediaCodeNo=257" title="10일 새벽 서울에 첫 눈 내리나">
# <span class="newsbox_visual">
# <img alt="10일 새벽 서울에 첫 눈 내리나" onerror="this.onerror=null;this.src='http://image.edaily.co.kr/images/photo/files/NP/S/2020/12/PS20120901052.jpg';" src="https://image.edaily.co.kr/images/photo/files/NP/S/2020/12/PS20120901052kb.jpg"/>
# </span>
# <ul class="newsbox_texts">
# <li>10일 새벽 서울에 첫 눈 내리나</li>
# <li>[이데일리 송주오 기자] 10일 새벽에 서울에 비 또는 눈이 내릴 전망이다. 지난 2일 올 겨울 첫눈이 내린 강원 평창군 대관령에서 주민이 눈길을 조심스럽게 걸어가고 있다.(사진=연합뉴스)기상청은 9일 오후 9시부터 경기 북부와 강원 영서 중·북부에, 오는 10일 오전 3시부터는 서울과 경기 남부, 충남 북부에 비 또는 눈이 올 것으로 예상했다. 서울에 눈이 내릴 경우 이번 겨울 첫 눈으로 기록된다. 이날까지 첫눈이 기록된 곳은 수원, 대전, 인천, 청주 등이다. 기상청은 서울과 인근 지역에서 기온에 따라 눈이 내리거나 눈과 비가 섞인 진눈깨비 형태의 눈이 내릴 것으로 내다봤다. 예상 강수량은 5㎜ 미만, 적설량은 1∼3㎝다.10일 낮부터 밤 사이에는 중부지방과 전북 서해안에 산발적으로 빗방울이 떨어지거나 눈이 날리는 곳이 있겠다. 지형적인 영향을 받는 곳은 1㎜ 내외의 강수량이 기록될 예정이다.10일 아침기온은 이날보다 5~6도 높아 평년보다 따뜻할 것으로 보인다. 또 주말까지 일부 중부내륙지역과 남부 산지를 제외한 대부분 지역의 아침 기온은 영상을 기록할 전망이다. 0일 아침 최저기온은 영하 4∼5도, 낮 최고기온은 6∼14도로 예상된다.</li>
# </ul>
# </a>, <a href="/jroom/main?jid=juoh413">
# <span class="author">송주오 기자</span>
# </a>
    
    
    
#%%   만약에 다른 것을 찾고 싶다면 <a href="/jroom/main?jid=juoh413">을 찾아보려면
# [1] 로 해주면 된다.

from  bs4  import  BeautifulSoup 
import  urllib.request 

list_url = 'https://www.edaily.co.kr/search/news/?keyword=%ec%b2%ab%eb%88%88&page=1'
url = urllib.request.Request(list_url) 
result = urllib.request.urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(result,"html.parser")
result1 = soup.find_all('div', class_='newsbox_04')
# print(result1) # 해보니 result1 안에 너무 많으니까
for i in result1:
    print(i.find_all('a')[1].get('href'))
    
#%% 예제5.
from  bs4  import  BeautifulSoup 
import  urllib.request 

list_url = 'https://www.edaily.co.kr/search/news/?keyword=%ec%b2%ab%eb%88%88&page=1'
url = urllib.request.Request(list_url) 
result = urllib.request.urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(result,"html.parser")
result1 = soup.find_all('div', class_='newsbox_04')
# print(result1) # 해보니 result1 안에 너무 많으니까
for i in result1:
    print('http://edaily.co.kr/'+i.find_all('a')[0].get('href'))
    
#%%예제6. 함수로 만드시오.
from  bs4  import  BeautifulSoup 
import  urllib.request 

def dea_scroll():
    params = []
    list_url = 'https://www.edaily.co.kr/search/news/?keyword=%ec%b2%ab%eb%88%88&page=1'
    url = urllib.request.Request(list_url) 
    result = urllib.request.urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(result,"html.parser")
    result1 = soup.find_all('div', class_='newsbox_04')
    # print(result1) # 해보니 result1 안에 너무 많으니까
    for i in result1:
        params.append('http://edaily.co.kr/'+i.find_all('a')[0].get('href'))    
    return params

print(dea_scroll())

#%%예제7. 위의 상세기사 url 하나를 가지고 기사 본문을 출력하시오!
from  bs4  import  BeautifulSoup 
import  urllib.request 

list_url = 'http://edaily.co.kr//news/read?newsId=01423526625998520&mediaCodeNo=258'
url = urllib.request.Request(list_url) 
result = urllib.request.urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(result,"html.parser")   
result1 = soup.find_all('div',class_='news_body')
for i in result1:
    print(i.get_text())

# <div class="news_body" itemprop="articleBody">
#                             <table cellspacing="5" cellpadding="0" width="670" align="CENTER" bgcolor="ffffff" border="0" style="margin:5px 5px 5px 5px"><tbody><tr><td style="PADDING-RIGHT: 2px; PADDING-LEFT: 2px; PADDING-BOTTOM: 2px; PADDING-TOP: 2px;" bgcolor="ffffff"><table cellspacing="5" cellpadding="0" bgcolor="ffffff" border="0"><tbody><tr><td style="max-width: 100%;"><iframe src="https://movideo.ai/sc/aiScript?from=https%3A//www.edaily.co.kr/news/read%3FnewsId%3D01423526625998520%26mediaCodeNo%3D258&amp;a=78" id="mobonFrm" scrolling="no" height="398px" style="display: block; width: 580px; position: relative; z-index: 1; left: 50%; transform: translate(-50%, 0px); border: 0px;"></iframe><img src="https://spnimage.edaily.co.kr/images/photo/files/NP/S/2020/12/PS20121400161.jpg" border="0" style="display:none !important"></td></tr></tbody></table></td></tr></tbody></table><div class="ad_texbanner"><iframe src="//io1.innorame.com/imp/xbGRWKmXGnZq.iframe" width="619" height="93" allowtransparency="true" marginwidth="0" marginheight="0" hspace="0" vspace="0" frameborder="0" scrolling="no" style="z-index: 2147483647;"></iframe></div>[이데일리 스타in 김현식 기자] 그룹 인피니트 멤버 김성규가 솔로 컴백 소감을 밝혔다. <br><br>김성규는 14일 오후 4시에 연 세 번째 미니앨범 ‘인사이드 미’(INSIDE ME) 발매 기념 온라인 미디어 쇼케이스에서 “오랜만에 앨범으로 인사드리게 돼 떨리고 설렌다”고 말했다.<br><br><div id="view_ad02" class="view_ad02"><div id="dablewidget_xlzQ0A7Z" data-widget_id="xlzQ0A7Z" style="height: auto; overflow: visible;"><iframe width="100%" height="152" title="null" frameborder="0" scrolling="no" name="dableframe-0.5994929218143121" src="https://api.dable.io/widgets/id/xlzQ0A7Z/users/57204808.1608016605760?from=https%3A%2F%2Fwww.edaily.co.kr%2Fnews%2Fread%3FnewsId%3D01423526625998520%26mediaCodeNo%3D258&amp;url=https%3A%2F%2Fwww.edaily.co.kr%2Fnews%2Fread%3FnewsId%3D01423526625998520%26mediaCodeNo%3D258&amp;ref=https%3A%2F%2Fwww.edaily.co.kr%2Fsearch%2Fnews%2F%3Fkeyword%3D%25ec%25b2%25ab%25eb%2588%2588%26page%3D1&amp;cid=57204808.1608016605760&amp;uid=57204808.1608016605760&amp;site=edaily.co.kr&amp;id=dablewidget_xlzQ0A7Z&amp;category1=%EC%97%B0%EC%98%88&amp;category2=%EC%9D%8C%EC%95%85&amp;category3=%EC%9D%8C%EC%95%85%EA%B3%84%EC%86%8C%EC%8B%9D&amp;ad_params=%7B%7D&amp;pixel_ratio=1&amp;client_width=0&amp;network=non-wifi&amp;lang=ko&amp;pre_expose=1&amp;is_top_win=1&amp;top_win_accessible=1" style="border: 0px;" data-ready="1"></iframe></div></div>이어 “어제 첫눈을 보고 이건 하늘의 계시이자 운명이구나 싶었다. 신곡 뮤직비디오에 눈을 맞는 장면이 많기 때문”이라면서 “덕분에 기분 좋게 앨범 활동을 시작할 수 있겠다는 생각이 든다”며 미소 지었다.<br><br><div id="view_ad01" class="view_ad01"><iframe src="//tm.interworksmedia.co.kr/ads.sx/4F97F58D" marginwidth="0" marginheight="0" frameborder="0" scrolling="no" allowtransparency="true" allowfullscreen="true" width="300" height="250"></iframe></div>앨범명에 대해선 “매번 앨범을 낼 때마다 드리는 말씀이지만, 좀 더 성숙된 모습을 보여드리고 싶었다”며 “지금의 제 모습과 제 안에 있는 것들을 보여드리자는 의미에서 앨범명을 ‘인사이드 미’로 정했다”고 설명했다.<br><br>김성규는 이날 오후 6시 새 앨범 전곡 음원을 공개한다. 앨범에는 타이틀곡 ‘아임 콜드’(I‘m Cold)를 포함해 총 6곡이 담겼다.<br><br>
#%%예제8. 예제7의 본문 을 가져오는 함수를 만드시오. 

def eda_detail_scroll():
    list_url = 'http://edaily.co.kr//news/read?newsId=01423526625998520&mediaCodeNo=258'
    url = urllib.request.Request(list_url) 
    result = urllib.request.urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(result,"html.parser")   
    result1 = soup.find_all('div',class_='news_body')
    params = []
    for i in result1:
        params.append(i.get_text())
    return params

print(eda_detail_scroll())

#%% 예제9. 처음에 만들었떤 한수인 eda_scroll() 함수를 수정하는데 페이지 1개가 아니라
# 페이지 3개의 상세기사 url 인 params 리스트에 담겨지게 수정하시오.
from  bs4  import  BeautifulSoup 
import  urllib.request 

def dea_scroll():
    params = []
    for page in range(1,4):
        list_url = 'https://www.edaily.co.kr/search/news/?keyword=%ec%b2%ab%eb%88%88&page='+str(page)
        url = urllib.request.Request(list_url) 
        result = urllib.request.urlopen(url).read().decode("utf-8")
        soup = BeautifulSoup(result,"html.parser")
        result1 = soup.find_all('div', class_='newsbox_04')
        # print(result1) # 해보니 result1 안에 너무 많으니까
        for i in result1:
            params.append('http://edaily.co.kr/'+i.find_all('a')[0].get('href')) 
            
    return params

print(len(dea_scroll()))    
#60

#%%예제10. eda_detail_scroll() 함수 안에서 eda_scroll() 함수를 호출하여 상세기사 url을 
    # 60개를 다 가져와서 60개 기사를 출력할 수 있도록 코드를 수정하시오.
    
    
def eda_detail_scroll():
    for i in dea_scroll():
        list_url = i
        url = urllib.request.Request(list_url) 
        result = urllib.request.urlopen(url).read().decode("utf-8")
        soup = BeautifulSoup(result,"html.parser")   
        result1 = soup.find_all('div',class_='news_body')
        
        for i in result1:
            print(i.get_text())
            
eda_detail_scroll()

#%%예제11. 위의 출력되고 있는 기사 본문이 c 드라이브 밑에data 밑에 eda.txt로 저장되게 하시오.
from  bs4  import  BeautifulSoup 
import  urllib.request 

def dea_scroll():
    params = []
    for page in range(1,4):
        list_url = 'https://www.edaily.co.kr/search/news/?keyword=%ec%b2%ab%eb%88%88&page='+str(page)
        url = urllib.request.Request(list_url) 
        result = urllib.request.urlopen(url).read().decode("utf-8")
        soup = BeautifulSoup(result,"html.parser")
        result1 = soup.find_all('div', class_='newsbox_04')
        # print(result1) # 해보니 result1 안에 너무 많으니까
        for i in result1:
            params.append('http://edaily.co.kr/'+i.find_all('a')[0].get('href')) 
            
    return params

def eda_detail_scroll():
    f = open("c:\\data\\eda.txt",'w',encoding='UTF8')
    for i in dea_scroll():
        list_url = i
        url = urllib.request.Request(list_url) 
        result = urllib.request.urlopen(url).read().decode("utf-8")
        soup = BeautifulSoup(result,"html.parser")   
        result1 = soup.find_all('div',class_='news_body')
        
        for i in result1:
            f.write(str(i.get_text())+'\n')
    f.close()
            
eda_detail_scroll()

#%%연합뉴스에서 인공지능으로 검색한 기사들을 스크롤링 하기

#1. 엽합 뉴스에서 인공지능 으로 검색했을 때 url 을 알아내시오.

#2. 위의 url html 코드를 beautiful soup 으로 파싱하여 출력하시오 !

from  bs4  import  BeautifulSoup 
import  urllib.request 

list_url = 'https://www.yna.co.kr/search/index?query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&ctype=A&page_no=1'
url = urllib.request.Request(list_url) 
result = urllib.request.urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(result,"html.parser")

#3. 위의 사이트에서 상세기사 url을 알아내기 위한 테그이름과 클래스 이름을 알아내시오.

답: div class_="cts_atclst"

#%% 4. 위의 테그이름과 클래스 이름을 가지고 상세 기사 url 을 출력하시오!

from  bs4  import  BeautifulSoup 
import  urllib.request 

list_url = 'https://www.yna.co.kr/search/index?query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&ctype=A&page_no=2'
url = urllib.request.Request(list_url) 
result = urllib.request.urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(result,"html.parser")
result1 = soup.find_all('ul')

# result1 = soup.select('html > body > div > div > div > div > div > div ')
# for i in result:
#     print(i)
print(soup)

# https://www.yna.co.kr/view/AKR20201217129000017?section=search

#%% 문제422.(오늘의 마지막 문제) 머신러닝 때 나이브 베이즈 확률을 배울때 사용하기 위해서 네이버 영화 평점 게시판의 게시글들을 스크롤링해서
# 영화이름을 텍스트 파일로 해서 저장하시오 ~

# 코드와 텍스트 파일을 첨부해서 올리세요 ~

# 영화는 자유롭게 선택하세요~

#위대한 유산 

#%%
from  bs4  import  BeautifulSoup 
import  urllib.request 
import re

#규칙성 확인!
# https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=19076&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=1
# https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=19076&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=4
#

def mc_scroll():
    params = []
    for page in range(1,3):
        list_url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=19076&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=1'+str(page)
        url = urllib.request.Request(list_url) 
        result = urllib.request.urlopen(url).read().decode("utf-8")
        soup = BeautifulSoup(result,"html.parser")
# <div class="score_reple">												
        result1 = soup.find_all('div', class_='score_reple')
        for i in result1:
            k = re.sub(r'[^ ㄱ-ㅣ가-힣A-Za-z0-9]', '', i.find_all('span')[0].get_text())
            params.append(k) 
            
    return params
print(mc_scroll())



#%% 특수 문자 없애는 코드
import re


    ##document = re.sub(r'[.,!?"\':;~()]', '', document) #특수기호 제거, 정규 표현식

    document = re.sub(r'[^ ㄱ-ㅣ가-힣A-Za-z]', '', document) #특수기호 제거, 정규 표현식    

    #print(document) stale and uninspired
#%% 파일로 저장해 봅시다.
from  bs4  import  BeautifulSoup 
import  urllib.request 
import re
from time import sleep

def mc_scroll():
    params = []
    f=open("c:\\data\\tge.txt",'w',encoding='UTF8')
    for page in range(1,50):
        sleep(3)
        list_url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=19076&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=1'+str(page)
        url = urllib.request.Request(list_url) 
        result = urllib.request.urlopen(url).read().decode("utf-8")
        soup = BeautifulSoup(result,"html.parser")
# <div class="score_reple">												
        result1 = soup.find_all('div', class_='score_reple')
        for i in result1:
            k = re.sub(r'[^ ㄱ-ㅣ가-힣A-Za-z0-9]', '', i.find_all('span')[0].get_text())
            # print(k)
            f.write(str(k)+'\n') 
    f.close()     
    
mc_scroll()
#%%

def eda_detail_scroll():
    f = open("c:\\data\\eda.txt",'w',encoding='UTF8')
    for i in dea_scroll():
        list_url = i
        url = urllib.request.Request(list_url) 
        result = urllib.request.urlopen(url).read().decode("utf-8")
        soup = BeautifulSoup(result,"html.parser")   
        result1 = soup.find_all('div',class_='news_body')
        
        for i in result1:
            f.write(str(i.get_text())+'\n')
    f.close()
            
eda_detail_scroll()

#%%완성된 코

from  bs4  import  BeautifulSoup 
import  urllib.request 
import re
from time import sleep

def mc_scroll():
    f = open("c:\\data\\GreatExpectations.txt",'w',encoding='UTF8')
    for page in range(1,50):
        
        list_url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=19076&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page='+str(page)
        url = urllib.request.Request(list_url) 
        result = urllib.request.urlopen(url).read().decode("utf-8")
        soup = BeautifulSoup(result,"html.parser")
        result1 = soup.find_all('div', class_='score_reple')
        for i in result1:
            k = re.sub(r'[^ ㄱ-ㅣ가-힣A-Za-z0-9]', '', i.find_all('span')[0].get_text())
            f.write(str(k)+'\n') 
    f.close()     
    
mc_scroll()
#%% 준혁이 코드


from bs4 import BeautifulSoup
import urllib.request
import re

# document = re.sub(r'[.,!?"\':;~()]', '', document) #특수기호 제거, 정규 표현식
# document = re.sub(r'[^ ㄱ-ㅣ가-힣A-Za-z]', '', document) #특수기호 제거, 정규 표현식    

list_url = 'https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=189624&target=after&page=1'
url = urllib.request.Request(list_url)
result = urllib.request.urlopen(url).read()
soup = BeautifulSoup(result, "html.parser")
result2 = soup.find_all('td', class_="title")

# print(result2)
for i in result2:
    print(i.get_text(" ",strip='True').split('-'))
    # print(i.find_all('a')[0].get('br'))

#%% 누나 코드


from bs4 import BeautifulSoup
import urllib.request

for i in range(1,3):
    ra=[]
    list_url = 'https://movie.naver.com/movie/point/af/list.nhn?&page='+str(i)
    f = open("c:\\data\\cinema.txt",'w',encoding = 'UTF8')
    url = urllib.request.Request(list_url)
    result = urllib.request.urlopen(url).read().decode("cp949")
    soup = BeautifulSoup(result,"html.parser")
 

    result1 = soup.find_all('td',class_ ="title")
    
    
    for i in result1:
        ra.append(str(i.get_text("  ", strip=True)) + "\n")
    print(ra)

    
#%%
['검객  별점 - 총 10점 중  10  신고\n', 
 '백두산  별점 - 총 10점 중  10  시간 순삭인데? 킬링 타임용으로 추천 합니다.  신고\n',
 '콜  별점 - 총 10점 중  6  전종서의 연기가 너무 소름끼쳤다. 너무 강렬해서 영화 본 그날 밤 꿈속에 나타남... 무서워.  신고\n',
 '소년시절의 너  별점 - 총 10점 중  10  신고\n',

#%%

for i in ra:
    # print(i.split('-')[0][:-4]) 
    print(i.split('-'))
    
# 
    
# ra2 = []

# for i in ra:
#     ra2.append([(i.split('-')[0][:-4]),(i.split('-')[1][12:-3])])

# print(ra2)

# for i in ra2:
#     print(i)





















































