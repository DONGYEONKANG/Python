# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트
# 큐모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리 
# 변수 - 인스턴스 변수, 클래스 변수
# 메서드 - 인스턴스 메서드, 클래스 매서드, 정적 메서드
# 인스턴스 메서드 - self를 인자로 받는데 이는 객체 자신이다.
# 클래스 메서드 - class자체를 인자로 받는다. 
# 스테틱 메서드

class Car:
    """
    Car class 
    Author: Kim
    Date: 20xx.xx.xx
    Description : Class, Static, Instance Method
    """
    
    # 클래스 변수(모든 인스턴스가 공유)
    price_per_raise = 1.0
    
    def __init__(self, company, details):
        self._company = company
        self._details = details
    
    # 비공식적인, 사용자 중심
    def __str__(self):
        return "str : {} - {}".format(self._company, self._details)
    
    # 객체의 타입, 개발자 입장..
    def __repr__(self):
        return "repr: {} - {}".format(self._company, self._details)
    
    # Instance Method
    # Self: 갹체의 고유한 속성 값을 사용
    def detail_info(self):
        print("Current ID: {}".format(id(self)))
        print("Car Detail Info : {} {}".format(self._company, self._details.get("price")))
        
    # Instance Method
    def get_price(self):
        return "Before Car Price -> company : {}, price : {}".format(self._company, self._details.get("price"))
    
    # Instance Method
    def get_price_culc(self):
        return "Before Car Price -> company : {}, price : {}".format(self._company, self._details.get("price") * Car.price_per_raise) 
    
    # Class Method
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print("please Enter 1 or More")
            return
        cls.price_per_raise = per
        
        print("Succeed! price increased")
        
    # Static Method
    @staticmethod
    def is_bmw(inst):
        if inst._company == "BMW":
            return "OK! This car is {}".format(inst._company)
        else:
            return "Sorry"
    
        
        

# Self 의미
car1 = Car("Ferrari", {"color":"white", "horsepower":400, "price":8000})
car2 = Car("BMW", {"color":"Black", "horsepower":270, "price":5000})

# 전체 정보
car1.detail_info()
car2.detail_info()

# 가격정보, 인상 전
print(car1.get_price())
print(car2.get_price())

# 가격 인상(클래스 메소드 미사용)
Car.price_per_raise = 1.4

# 가격 인상(클래스 메소드 사용)
Car.raise_price(1.6)


# 가격정보, 인상 후
print(car1.get_price_culc())
print(car2.get_price_culc())


# static method(호출)
print(Car.is_bmw(car1))
print(Car.is_bmw(car2))
