### 알고리즘 관련 여러 문제들

```python
"""
게임 기업 입사문제 어떤 자연수 n이 있을 때, d(n)을 n의 각 자릿수 숫자들과 n 자신을 더한 숫자라고 정의하자.
예를 들어 d(91) = 9 + 1 + 91 = 101 이 때, n을 d(n)의 제네레이터(generator)라고 한다. 위의 예에서 91은 101의 제네레이터이다. 
어떤 숫자들은 하나 이상의 제네레이터를 가지고 있는데, 101의 제네레이터는 91 뿐 아니라 100도 있다. 그런데 반대로, 
제네레이터가 없는 숫자들도 있으며, 이런 숫자를 인도의 수학자 Kaprekar가 셀프 넘버(self-number)라 이름 붙였다. 
예를 들어 1,3,5,7,9,20,31 은 셀프 넘버 들이다. 1 이상이고 5000 보다 작은 모든 셀프 넘버들의 합을 구하라.
"""
myList = []

for i in range(1,5000):
    cnt = 0
    for j in str(i):
        cnt += int(j) 
    cnt += i
    myList.append(cnt)


print(sum(set(range(1,5000)) - set(myList)))

```

```python
# 다음 입사문제
# 1차원의 점들이 주어졌을 때, 그 중 가장 거리가 짧은 것의 쌍을 출력하는 함수를 작성하시오.
# (단 점들의 배열은 모두 정렬되어있다고 가정한다.)
# 예를들어 S={1, 3, 4, 8, 13, 17, 20} 이 주어졌다면, 결과값은 (3, 4)가 될 것이다.

s = [1,3,4,8,13,17,20]


def short_list(s):
    myList=[]                    
    myList2=[]                   
    dis = 0                     
    myList.append(s[1]-s[0])    
    for i in range(len(s)-1):   
        dis = s[i+1] - s[i]      
        if dis < myList[-1]:   
            myList.append(dis)   
            myList2.append((s[i],s[i+1]))   

    print(myList2[-1])              
    
    
short_list(s)
    
```

```python
# 회문(palindrome)? 순서를 거꾸로 해서 읽어도 제대로 읽을때와 같은 단어 or 문장
# rotator, sos, abba (nurses run)
# 문제: 임의의 단어(문장)을 입력받아 회문 여부를 출력 => True or False 출력


pal = input("단어 혹은 문장을 입력하세요 : ")     
pal2 = "" 


for i in pal:     # pal = nurses run
    if i != " ":
        pal2 += i   # pal2 = nursesrun
    

if pal2 == pal2[::-1]:
    print("True")
else:
    print("False")
    
```

```python
# 4. 모스 부호 해독
# 문자열 형식으로 입력받은 모스 부호(dot:. dash:-)를 해독하여 영어 문장으로 출력하는 프로그램을 작성하시오.
#
# 글자와 글자 사이는 공백 1개, 단어와 단어 사이는 공백 2개로 구분한다.
# 예를 들어 다음 모스 부호는 "HE SLEEPS EARLY"로 해석해야 한다.
# 모스부호 규칙 표

# input :  .... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--


mos = input("모스 부호를 입력하세요 : ")
dic = {
    '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
    '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
    '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
    '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
    '-.--':'Y','--..':'Z'
}

mos1 = mos.split(" ")

for i in mos1:
    if i == "":
        print(" ", end="")
    elif i in dic:
        char = dic.get(i) 
        print(char, end="")

```

```python
# # ngram 기반 두 문장 유사도 구하기(n=2, 3)
# # "오늘 멀티캠퍼스에서 너무 쉬운 프로그래밍을 공부했다"
# # "멀티캠퍼스에서 공부했던 오늘의 프로그래밍은 너무 쉬웠다"
#
#
#
# #오늘,늘멀,멀티,티캠—
#
# #멀티,티캠,캠퍼….
#
# # —>중복된 문자 제거
#
#   중복된 문자 수 / 긴문장글자 수



def seperate(a, b, n):
    a1 = a.replace(" ","")
    b1 = b.replace(" ","")
    li1=[]
    li1 = list(a1[i:i+n] for i in range(len(a1)-1))
    li2=[]
    li2 = list(b1[i:i+n] for i in range(len(b1)-1))
    li3 = li1 + li2
    cnt = (len(li3) - len(set(li3)))
    
    if len(a) > len(b) :
        longcnt = len(list(a[i:i+n] for i in range(len(a)-1)))
    else:
        longcnt = len(list(a[i:i+n] for i in range(len(a)-1)))
        
    return cnt / longcnt


str1 = "오늘 멀티캠퍼스에서 너무 쉬운 프로그래밍을 공부했다"
str2 = "멀티캠퍼스에서 공부했던 오늘의 프로그래밍은 너무 쉬웠다"


print(f"두 문장의 유사도 : {seperate(str1, str2, 2) * 100} % 입니다.")
print(f"두 문장의 유사도 : {seperate(str1, str2, 3) * 100} % 입니다.")


```

```python
"""
0~9의 문자로 된 숫자를 입력받았을 때, 이 입력값이 0~9의 모든 숫자를 각각 한 번씩만 사용한 것인지 확인하는 함수를 작성하시오.

입력 예시: 0123456789 01234 01234567890 6789012345 012322456789
출력 예시: True False False True False
"""


def checkNum(num):
    ans = []
    for i in num:
        for j in range(10):
            cnt = i.count(str(j))
            if cnt != 1:
                ans.append(False)     
                break;
            elif j==9:
                ans.append(True)

    return ans

num = input().split(' ')
checkNum(num)
```

```python
# 4)가장 많이 등장한 단어가 무엇인가요?(공백으로 나누었을 때 기준)
# 5)가장 많이 등장한 글자는 무엇이며, 총 몇 번 등장했나요?

news = """
연합뉴스TV
[날씨] 추위 대신 미세먼지 말썽…밤까지 중부 중심 눈
기사입력 2021.01.12. 오후 1:40 기사원문 스크랩 본문듣기  설정
화나요 후속기사원해요 좋아요 평가하기9 댓글9
글자 크기 변경하기
 인쇄하기
보내기
동영상 뉴스
[앵커]

오늘은 추위가 풀리는 대신 서쪽 지역의 공기 질이 나쁘겠습니다.

중부지방을 중심으로 눈도 내리겠습니다.

기상캐스터 연결해서 날씨 정보 더 자세히 알아보겠습니다.

김민지 캐스터.

[캐스터]

네, 추위가 한층 풀렸습니다.

어제보다 옷차림을 조금 더 가볍게 하고 나왔는데도 크게 춥지 않습니다.

내륙에 내려졌던 한파특보는 모두 해제가 됐고요.

오늘 한낮에 전국에 영상권으로 올라서겠습니다.

한낮에 서울은 1도, 대전 3도, 대구 5도 등 어제보다 5도 정도 기온이 높겠습니다.

따뜻한 서풍이 불어오면서 추위의 힘이 약해지는 건데요.

이 서풍을 타고 또 미세먼지가 들어오겠습니다.

대기 정체로 먼지가 쌓이면서 오늘은 서쪽 지역을 중심으로 미세먼지 농도 나쁨 수준 보이겠고요.

밤에 중국발 오염물질까지 들어와서 내일은 전국적으로 공기 질 상황이 나쁘겠습니다.

오늘 전국에 구름이 많습니다.

차츰 중부를 중심으로 눈이 내리겠습니다.

수도권과 충남, 전북에 1~3cm, 강원 영서와 충북, 경북과 제주 산지에 최고 5cm의 눈이 내려 쌓이겠습니다.

대부분 오늘 밤이면 그칠 텐데요.

강원 영서 지역은 내일 새벽까지 눈이 이어지겠습니다.

지금은 눈발 정도만 날리고 있습니다.

눈이 쌓이면서 퇴근길 무렵에는 길이 많이 미끄럽겠습니다.

조심히 이동하시기 바랍니다.

날씨 전해 드렸습니다."""

# 4)

import re
dic = {}
words = re.compile('[\u3131-\u3163\uac00-\ud7a30-9]+')
result = words.findall(news)

for i in result:
    dic[i] = result.count(i)

for key, value in dic.items():
    if value == max(dic.values()):
        print(f'[{key}] 단어가 {value}번 나왔습니다.')


```

```python
# 5)가장 많이 등장한 글자는 무엇이며, 총 몇 번 등장했나요?

import re
dic = {}
list1 = []
words = re.compile('[\u3131-\u3163\uac00-\ud7a3]+')
result = words.findall(news)


for i in result:
    for j in i:
        list1.append(j)
        
for i in result:
    dic[i] = list1.count(i)
        
for key, value in dic.items():
    if value == max(dic.values()):
        print(f'[{key}] 글자가 {value}번 나왔습니다.')
```

```python
# 다른 풀이
words=re.findall('[ㄱ-ㅎ가-힣a-zA-Z0-9]+',new)

res={}

for i in words:

    if res.get(i):

        res[i] +=1

    else:

        res[i] =1
    

# print(max(res.values()))

print(max(res, key=res.get))
```

