"""# quiz 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하세요

# 조건 1 : 랜덤으로 날짜를 뽑아야함
# 조건 2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# 조건 3 : 매월 1~3일은 스터디 준비를 해야함으로 제외

# (출력문 예제)
# 오프라인 스터디 모임 날짜는 매월 x일로 선정되었습니다.
"""
# from random import *

# print("오프라인 스터디 모임 날짜는 매월 "+str(randint(4,28))+"일로 선정되었습니다.")

"""# quiz 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

예) http://naver.com
규칙1 : http:// 부분은 제외 -> naver.com
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 -> naver
규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성

예) 생성된 비밀번호 nav51!
"""
# 내가 한거
# add = "http://naver.com"
# add1 = add[7:]
# print(add1)

# print(add1.find("."))
# add2 = add1[:5]
# print(add2)

# add3 = add2[:3] + str(len(add2)) + str(add2.count("e"))+"!"
# print(add3)

# #풀이

# url = "http://naver.com"
# my_str = url.replace("http://","") #규칙 1
# print(my_str)
# my_str = my_str[:my_str.index(".")] #규칙 2
# print(my_str)
# password = my_str[:3] + str(len(my_str))+str(my_str.count("e"))+"!"
# print("{0}의 비밀번호는 {1}입니다.".format(url, password))



"""quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
추첨 프로그램을 작성하세요

조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
조건2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
조건3 : random 모듈의 shuffle과 sample을 활용

(출력 예제)
--당첨자 발표--
치킨 당첨자 : 1
커피 당첨자 : [2,3,4]
--축하합니다.--

활용 예제
from random import *
lst = [1,2,3,4,5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst,1) #
"""

# from random import *
# users = range(1,21)
# users = list(users)
# print(users)

# shuffle(users)
# winner = sample(users,4)

# print(winner, type(winner))

# print("--당첨자 발표--\n치킨 당첨자 : {}\n커피 당첨자 : {}\n--축하합니다.--".format(winner[0], winner[1:]))

"""quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사입니다.
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오

조건1 : 승객별 운행 소요 시간은 5~50분 사이의 난수로 정해집니다.
조건2 : 당신은 소요시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

(출력문 예제)
[0] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분)
[0] 3번째 손님 (소요시간 : 5분)
...
[ ] 50번째 손님 (소요시간 : 16분)

총 탑승 승객 : 2분 """

# from random import *
# count=0

# for client_no in range(1,51):
#     times=randint(5,50)
#     if times <=15:
#         print("[o] {}번째 손님 (소요시간 : {}분)".format(client_no, times))
#         count+=1
#     else:
#         print("[ ] {}번째 손님 (소요시간 : {}분)".format(client_no, times))
# print("총 탑승 승개 : {}분".format(count))

#풀이
from random import *
cnt=0 # 총 탑승 승객 수
for i in range(1,51): #1~50 이라는 수(승객)
    time=randrange(5,51) # 5분~50분 소요시간
    if 5<= time <=15: #5분 ~15분 이내의 손님, 탑승 승객 수 증가 처리
        print("[o] {0}번째 손님 (소요시간 : {1}분".format(i,time))
        cnt+=1
    else :
        print("[ ] {0}번째 손님 (소요시간 : {1}분".format(i,time))
print("총 탑승 승객 : {0}분".format(cnt))