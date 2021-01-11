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
# 모스 부호 해독
# 문자열 형식으로 입력받은 모스 부호(dot:. dash:-)를 해독하여 영어 문장으로 출력하는 프로그램을 작성하시오.
#
# 글자와 글자 사이는 공백 1개, 단어와 단어 사이는 공백 2개로 구분한다.
# 예를 들어 다음 모스 부호는 "HE SLEEPS EARLY"로 해석해야 한다.
# …. .  … .-.. . . .—. …  . .- .-. .-.. -.—
# 모스부호 규칙 표
# .... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--


mos = input()
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

