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

