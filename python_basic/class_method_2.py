# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트
# 큐모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리 


# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용
class Car:
    """
    Car class 
    Author: Kim
    Date: 20xx.xx.xx
    """
    
    # 클래스 변수를 생각해봐야한다.
    # 클래스 변수는 초기화 변수 시이에 선언해얗안다.
    # 클래스 변수는 모든 인스턴스가 공유
    car_count = 0
    
    def __init__(self, company, details):
        self._company = company
        self._details = details
        Car.car_count += 1
    
    # 비공식적인, 사용자 중심
    def __str__(self):
        return "str : {} - {}".format(self._company, self._details)
    
    # 객체의 타입, 개발자 입장..
    def __repr__(self):
        return "repr: {} - {}".format(self._company, self._details)
    
    def __del__(self):
        Car.car_count -= 1
    
    def detail_info(self):
        print("Current ID: {}".format(id(self)))
        print("Car Detail Info : {} {}".format(self._company, self._details.get("price")))
        
    
    
# Self 의미
car1 = Car("Ferrari", {"color":"white", "horsepower":400, "price":8000})
car2 = Car("BMW", {"color":"Black", "horsepower":270, "price":5000})


# ID 확인
print(id(car1))
print(id(car2)) 

print(car1._company == car2._company)
print(car1 is car2)

# dir & __dict__ 확인, object를 상속 받기에 dir에 많은 속성이 가지고 있다. ~> 매직 메서드등..
print(dir(car1))
print(dir(car2))

print()
print()

print(car1.__dict__)
print(car2.__dict__)

# car docstring
print(Car.__doc__)
print()

# 실행
car1.detail_info()

# 비교
print(car1.__class__, car2.__class__)
print(id(car1.__class__), id(car2.__class__)) # main 클래스의 id 같다. 같은 부모다.


# 에러, detail info에는 self가 필요하다.
Car.detail_info(car2) # self를 직접 넣을 수 있다. class이름으로 접근 가능하다.

# class 변수 접근/공유확인
print(car1.__dict__) # 클래스 변수가 보이지 않는다.
print(car1.car_count) 
print(car2.car_count)


del car2
# 삭제 확인
print(Car.car_count)


# 인스턴스 네임스페이스에 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 변수 생성 가능) -> 상위(클래스 변수, 부모 클래스 변수)