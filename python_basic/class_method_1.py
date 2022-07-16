# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트
# 큐모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리 


# 일반적인 코딩 

# 차량1

car_company_1 = "Ferrari"
car_detail_1 = [
    {"color": "White"},
    {"horsepower": 400},
    {"price": 8000}
]

# 차량2
car_company_2 = "BMW"
car_detail_2 = [
    {"color": "Black"},
    {"horsepower": 270},
    {"price": 5000}
]

# 차량2
car_company_3 = "Audi"
car_detail_3 = [
    {"color": "Sliver"},
    {"horsepower": 300},
    {"price": 6000}
]

# 리스트 구조
# 관리하기가 불편
# 인덱스 접근 시 실수 가능성, 삭제 불편
car_company_list = ["Ferrari", "Bmw", "Audi"]
car_detail_list = [
    {"color": "White", "horsepower": 400, "price": 8000},
    {"color": "Black", "horsepower": 270, "price": 5000},
    {"color": "Sliver", "horsepower": 300, "price": 6000},
]

del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)


# 딕셔너리 구조
# 코드 반복 지속, 중첩 문제(키), 키 조회 예외 처리 등

car_dicts = [
    {"car_company": "Ferrai", "car_detail": {"color":"white", "horsepower":400, "price":8000}},
    {"car_company": "BMW", "car_detail": {"color":"Black", "horsepower":270, "price":5000}},
    {"car_company": "Audi", "car_detail": {"color":"Sliver", "horsepower":300, "price":6000}},
]



del car_dicts[1]
print(car_dicts)

print()
print()

# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용
class Car:
    def __init__(self, company, details):
        self._company = company
        self._details = details
    
    # 비공식적인, 사용자 중심
    def __str__(self):
        return "str : {} - {}".format(self._company, self._details)
    
    # 객체의 타입, 개발자 입장..
    def __repr__(self):
        return "repr: {} - {}".format(self._company, self._details)
    
car1 = Car("Ferrari", {"color":"white", "horsepower":400, "price":8000})
car2 = Car("BMW", {"color":"Black", "horsepower":270, "price":5000})
print(car1)
print(car1.__dict__) # 클래스의 네임스페이스를 알 수 있다.

# 리스트 선언
car_list = []
