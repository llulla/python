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

# #풀이
# from random import *
# cnt=0 # 총 탑승 승객 수
# for i in range(1,51): #1~50 이라는 수(승객)
#     time=randrange(5,51) # 5분~50분 소요시간
#     if 5<= time <=15: #5분 ~15분 이내의 손님, 탑승 승객 수 증가 처리
#         print("[o] {0}번째 손님 (소요시간 : {1}분".format(i,time))
#         cnt+=1
#     else :
#         print("[ ] {0}번째 손님 (소요시간 : {1}분".format(i,time))
# print("총 탑승 승객 : {0}분".format(cnt))

"""quiz) 표준 체중을 구하는 프로그램을 작성하시오

* 표준 체중 : 각 개인의 키에 적당한 체중

(성별에 따른 공식)
남자 : 키(m) x 키(m) x 22
여자 : 키(m) x 키(m) x 21

조건1 : 표준 체중은 별도의 함수 내에서 계산
  *함수명 : std_weight
  *전달값 : 키(height) 성별(gender) 

조건2 : 표준 체중은 소수점 둘째자리까지 표시

(출력예제)
키 175cm 남자의 표준 체중은 67.38kg 입니다."""

# #내가한거
# weight=0
# def std_weight(gender, height):
#     global weight
#     weight = int(height)
#     weight *= weight
#     if gender =="남자":
#          weight=weight*22 *0.0001
#          return weight
#     elif gender =="여자":
#          weight=weight*21 *0.0001
#          return weight
#     else :
#         print("잘못입력했습니다. 다시 입력해주세요") 

# gender= input("성별을 입력하세요 (남자, 여자) : ")
# height= input("키를 입력하세요(cm) : ")
# weight = round(std_weight(gender,height),2)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

# #풀이

# def std_weight(height, gender):
#     if gender == "남자":
#         return height*height *22
#     else :
#         return height*height *21

# height = 164
# gender = "여자"
# weight = round(std_weight(height /100, gender),2 )
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))


"""quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

- x 주차 주간보고 - 
부서 : 
이름 : 
업무 요약 : 

1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오

조건 : 파일명은 '1주차.txt', 2주차.txt" ... 와 같이 만듭니다."""

# #내가 한거
# import pickle
# weekly=1
# while weekly <51:
#     with open("{0}주차.txt".format(weekly), "w", encoding="utf8") as week_file:
#         week_file.write("- {0} 주차 주간보고 - \n부서 :\n이름 :\n업무 요약 :".format(weekly))
#     weekly+=1

# #풀이
# for i in range(1,51):
#     with open(str(i)+"주차.txt","w", encoding="utf8") as report_file:
#         report_file.write("- {0} 주차 주간보고 - ".format(i))
#         report_file.write("\n부서 : ")
#         report_file.write("\n이름 : ")
#         report_file.write("\n업무 요약 :)
        
"""quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

(출력예제)
총 3대의 매물이 있습니다.
강남 아파트 매매 10억 2010년
마포 오피스텔 전세 5억 2007년
송파 빌라 월세 500/50 2000년

[코드]
class House:
    #매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        pass
    
    #매물 정보 표시
    def show_detail(self):
        pass"""


class House:
    #매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house = house_type
        self.deal = deal_type
        self.price = price
        self.complet = completion_year
    #매물 정보 표시
    def show_detail(self):
        print(self.location, self.house, self.deal, self.price, self.complet)
    
houses = [] 
gang = House("강남", "아파트", "매매", "10억", "2010년")
mapo = House("마포", "오피스텔", "전세", "5억", "2007년")
song = House("송파", "빌라", "월세", "500/50", "2000년")

houses.append(gang)
houses.append(mapo)
houses.append(song)

print("총 {0}대의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()

