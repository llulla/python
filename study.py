#수식

# number = 2
# print(number)
# number += 8
# print(number)
# number *= 2
# print(number)
# number /= 2
# print(number)

# from random import *

# #1 ~45 사이의 임의값
# print(int(random() *45) + 1) 
# print(randrange(1,46)) 
# print(randint(1,45))

#=======================================
#문자열

# sentence = '나는 소년'
# print(sentence)
# sentence2 = "파이썬 쉬워"
# print(sentence2)
# sentence3 = """
# 나는 소년이고, 파이썬은 쉽다"""
# print(sentence3)


#슬라이싱
#   필요한 정보 잘라오는 것

# jumin = "990121-1212123"
# print("성별 : " + jumin[7])
# print("연 : "+ jumin[0:2])
# print("월 : "+ jumin[2:4])
# print("일 : "+ jumin[4:6])
# print("생년월일 : "+ jumin[:6])
# print("뒷자리 : "+ jumin[7:])
# print("뒷자리 (역순) : "+ jumin[-7:])


##문자열 처리 함수

# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python", "Java"))

# index = python.index("n")
# print(index)
# index = python.index("n", index +1)
# print(index)

# print(python.find("Java"))  #값이 없을 경우 -1 반환
# #print(python.index("Java")) #      "       error

# print(python.count("n"))


# #문자열 포맷

# print("a" + "b")
# print("a", "b")

# #방법 1
# print("나는 %d살입니다." %20)
# print("나는 %s을 좋아해요." %"파이썬")
# print("Apple은 %c로 시작해요." %"A")
# print("나는 %s색과 %s색을 좋아해요" %("파란", "빨간"))

# #방법 2
# print("나는 {}살입니다.".fromat(20))
# print("나는 {}색과 {}색을 좋아해요.".forat("파란","빨간"))
# print("나는 {1}색과 {0}색을 좋아해요.".forat("파란","빨간"))

# #방법 3
# print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))

# #방법 4
# age=20
# color ="빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요")


# #탈출문자

# print("백문이 불여일견\n백견이 불여일타")
# print("저는 \"나도코딩\"입니다.")

# print("D:\\study_2107\\python")

# print("Red Apple\rPine") #커서를 앞으로 이동 후 뒤에꺼 작성
# print("Redd\bApple")
# print("Red\tApple")

# 리스트 []

# # 지하철 칸별로 10명, 20명, 30명
# subway1 =10
# subway2 =20
# subway3 =30

# subway =[10,20,30]
# print(subway)

# subway=["유재석", "조세호", "박명수"]
# print(subway.index("유재석"))

# subway.append("하하") #리스트 맨 뒤에 추가

# subway.insert(1,"정형돈") #인덱스 번호로 지정해서 추가
# print(subway)

# print(subway.pop()) #리스트 맨뒤에서 하나 삭제

# # 같은 이름의 사람이 몇명있는지
# subway.append("유재석")
# print(subway.count("유재석"))

# #정렬
# num_list = [5,3,2,6,4,1]
# num_list.sort()
# print(num_list)

# num_list.reverse() #순서 뒤집기 가능
# print(num_list)

# num_list.clear() # 전체 삭제
# print(num_list)

# mix_list = ["조세호", 28, True]

# #리스트 확장
# num_list.extend(mix_list)
# print(num_list)

#사전
# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# #print(cabinet[5]) #값이 없을경우 바로 에러종료
# print(cabinet.get(5))
# print(3 in cabinet) # tree
# print(5 in cabinet) = 

# cabinet = {"A-3":"유재석", 100:"김태호"}

# print(cabinet)
# cabinet["A-3"] = "김종국"
# cabinet["C-20"]="조세호"
# print(cabinet)

# #간 손님
# del cabinet["A-3"]
# print(cabinet)

# #key들만 출력
# print(cabinet.keys())

# #value들만 출력
# print(cabinet.values())

# #key, value 쌍으로 출력
# print(cabinet.items())

# #싹 지우기
# cabinet.clear()
# print(cabinet)


# #튜플 
# #   추가 제거 불가능, 고정된 값에 대해서만 사용가능

# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# (name, age, hobby) = ("김종국", 20,"코딩")
# #이렇게 구조체 개념으로 사용 가능
# print(name, age, hobby)


# #집합 (set)
# #   중복 안됨, 순서 없음

# my_set= {1,2,3,4,5,6}
# print(my_set)
# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# #교집합
# print(java & python)
# print(java.intersection(python))

# #합집합
# print(java | python)
# print(java.union(python))

# #차집합 (java는 가능 python 불가)
# print(java-python)
# print(java.difference(python))

# #python 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)

# #java를 까먹음
# python.remove("김태호")
# print(java)


# # 자료구조의 변경
# #커피숍
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))


"""제어문"""


# #if

# weather = input("오늘 날씨는 어때요?")
# if weather =="비" or weather=="눈":
#     print("우산을 챙기세요")
# elif weather =="미세먼지":
#     print("마스크를 챙기세요")
# else :
#     print("준비물 필요 없어요")

# temp = int(input("기온은 어때요? "))
# if 30<=temp:
#     print("더워요")
# elif 10<= temp and temp <30:
#     print("괜찮네요")
# elif 0<= temp <10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요.3")


# #for
# for waiting_no in range(1,16): # randrange()
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["아이언맨", "토르","그루트"]
# for customer in starbucks:
#     print("{}님, 주문하신 음료 나왔습니다.".format(customer))

# #while

# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비되었습니다. {1}번 남았어요".format(customer,index))
#     index -=1
#     if index ==0:
#         print("커피 폐기처분")

# #무한 루프
# customer ="ironman"
# index =1
# while True:
#     print("{0}, 커피가 준비되었습니다. \t 호출 {1}회".format(customer,index))
# index += 1

# customer = "thor"
# person ="Unknown"

# while person != customer:
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요? ")

# # continue, break

# absend = [2,5] # 결석
# no_book =[7]
# for student in range (1,11):
#     if student in absend:
#         continue
#     elif student in no_book:
#         print("오늘 수업 끝, {0}은 교무실로 오세요".format(student))
#         break
#     print("{0}, 책을 일어봐". format(student))
    


# #출석번호가 1,2,3,4 dkvdp 100을 붙이기로함.

# student = [1,2,3,4,5]
# print(student)
# student=[i+100 for i in student]
# print(student)

# #학생이름을 길이로 변환
# students =["iron man", "thor", "groot"]
# students =[len(i) for i in students]
# print(students)

# #학생이름을 대문자로 변환
# students =["iron man", "thor", "groot"]
# students =[i.upper() for i in students]
# print(students)


# # 함수

# def open_account():
#     print("새로운 계좌가 생성되었습니다.")
# def deposit(balance, money):
#     print("입금이 완료되었습니다. 작액은 {0}원입니다.".format(balance + money))
#     return balance + money
# def withdraw(balance, money):
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
#         return balance, money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(moeny))
# def withdraw_night(balance, money):
#     commission = 100
#     return commission, balance - money -commission
# balance = 0
# balance = deposit(balance, 1000)
# print(balance)

# commission, balance = withdraw_night(balance,500)
# print("수수료 {0}원, 잔액은 {1}원입니다.".format(commission,balance))


# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
#         .format(name,age,main_lang))

# profile("유재석", 20,"파이썬")
# profile("김태호", 24,"자바")

# def profile1(name, age=17, main_lang="파이썬"):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
#         .format(name,age,main_lang))
# profile1("유재석")
# profile1("김태호")

# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name="유재석", main_lang="파이썬",age=20)
# profile(name="김태호",age=50, main_lang="java")

# def profile(name, age, lang1, lang2, lang3):
#     print ("이름 : {0}\t 나이 : {1}".format(name,age),end=" ")
#     print(lang1, lang2, lang3)

# profile ("유재석", 20, "python", "c", "java")
# profile ("김태호", 50, "Kotlin", "swift","")


# def profile(name, age, *lang):
#     print ("이름 : {0}\t 나이 : {1}".format(name,age),end=" ")
#     for language in lang:
#         print(language, end=" ")
#     print()

# profile ("유재석", 20, "python", "c", "java","swift")
# profile ("김태호", 50, "Kotlin", "swift")


# gun = 10

# def checkpoint(soldiers):
#     global gun 
#     gun = gun-soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun

# print("전체 초 : {0}".format(gun))
# # checkpoint(2)
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))


# 표준입출력

# print("python", "java", "c",sep=" vs ")
# print("python", "java", "c",sep="?",end=", ") # 문장의 끝부분을 ?로 바꿔달라
# print("무엇이 더 재밌을까?")
# import sys
# print("python", "java", "c",file=sys.stdout)
# print("python", "java", "c",file=sys.stderr)

# scores = {"math":0, "Eng":50, "code":100}
# for subject, score in scores.items():
#     print(subject.ljust(8), str(score).rjust(4),sep=":")

# #은행 대기 순번표
# for num in range(1,21):
#     print("대기번호 : "+str(num).zfill(3))

# answer = input("아무 값이나 입력하세요 : ")
# print(type(answer))
# print("입력하신 값은 "+answer+"입니다")   #사용자에게 입력을 받을 때는 무조건 문자열 형태로 정해짐


# #빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))
# #양수일 때는 +로 표시 음수일때는 -로 표시
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))

# #왼쪽 정렬하고, 빈칸을 _로 채움
# print("{0: <+10}".format(500))
# #3자리마다 , 찍어주기
# print("{0:,}".format(1000000000000000000000000000000000))
# print("{0:+,}".format(-1000000000000000000000000000000000))
# #3자리마다 콤마 찍기, 부호도 분이고, 자릿수도 확보하기
# #돈이 많으면 행복하니까 빈 자리는 ^로 채워주세요
# print("{0:^<+30}".format(100000000000000))
# #소수점 출력
# print("{0:f}".format(5/3))
# # 소수점 특정 자릿수 까지만 표시 (3번째자리에서 반올림)
# print("{0:.2f}".format(5/3))


#파일입출력

# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50",file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 = 70")
# score_file.write("\n코딩 = 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(),end="") #줄별로 읽기, 한줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(),end="")
# print(score_file.readline(),end="")
# print(score_file.readline(),end="")
# print(score_file.readline(),end="")
# score_file.close

# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() #list 형태로 저장
# for line in lines:
#     print(line,end="")
# score_file.close()


#pickle

# import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"박명서", "나이":30, "추미":["축구","독서","코딩"]}
# print(profile)
# pickle.dump(profile,profile_file) # profiled 에 있는 정보를 file에 저장
# profile_file.close()

# profile_file = open("profile.pickle","rb")
# profile = pickle.load(profile_file) #file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

#with

# import pickle
# with open("profile.pickle", "rb") as profile_file: #profile_file이라는 변수에 저장한거임
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())