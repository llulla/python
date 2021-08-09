class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit,Flyable):
    def __init__(self):
        # super().__init__()  #두개 이상의 부모클래스를 상속 받지 못함
        # 두개 이상의 부모 클래스를 상속 받기 위해서는 아래와 같이 사용
        Unit.__init__(self)
        Flyable.__init__(self)

dropship = FlyableUnit()
