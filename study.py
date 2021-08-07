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
