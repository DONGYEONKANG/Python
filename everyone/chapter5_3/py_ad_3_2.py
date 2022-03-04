"""
Section 3
Concurrency, CPU Bound vs I/O bound - Blocking vs Non-Blocking IO
Keyword - Blocking IO, Non-Blocking IO, Sync, Aync

"""
"""

blocking I/O vs Non-blocking I/O

    blocking I/O 
    - 시스템 콜 요청시 -> 커널 IO 작업 완료 시 까지 응답 대기(예를 들어 카톡을 보내고 답장이 올때까지 가만히 있느다.. 다른 것들을 하지 않는다.)
    - 제어권(IO작업) -> 커널 소유 -> 응답(Response)전 까지 대기(Block) -> 다른 작업 수행 불가
    
    Non-blocking I/O
    - 시스템 콜 요청시 -> 커널 IO 작업 완료 여부 상관없이 즉시 응답
    - 제어권(IO작업) -> 유저 프로세스 -> 다른 작업 수행 가능(지속) -> 주기적으로 시스템 콜 통해서 IO 작업 완료 여부 확인
     
    Async vs Sync
        
        Async : IO 작업 완료 여부에 대한 Noty는 커널(호출되는 함수) -> 유저프로세스(호출하는 함수)(예를 들어 세탁소에 세탁을 맡기면, 세탁소에서 다 되면 연락하는 것)
        Sync : IO 작업 완료 여부에 대한 Noty는 유저 프로세스(호출하는 함수) -> 커널(호출 되는 함수)(세탁소에 세탁을 맡기면, 세탁소에 직접 전화 해 확인하는 것)
        
        
    I/O: 파일을 읽거나 쓰거나, 웹 상에서 자료를 가지고 오거나, 데이터베이스 내용가지고 엑셀에 사용하는 등등..
    
    Sync block I/O
    - System call 요청!
    - Kernel I/O가 작업을 완료할 때 까지 기다린다.
    - 유저가 직접 완료되었는지 확인 후 응답 받는다.
    
    Sync non-block I/O
    - System call 주기적으로 요청
    - Kernel I/O의 작업을 기다리지 않고, 다른 작업을 진행한다.
    
    ASync block I/O
    - System call 요청!
    - Kernel I/O가 작업을 완료할 때 까지 기다린다.
    - Kernel에서 완료됬다고 말해준다.(callback)
    
    Async non-block I/O(가장 많이 사용된다.)
    - System call 요청!
    - Kernel I/O의 작업을 기다리지 않고, 다른 작업을 진행한다.
    - 운영체제가 완료됬다고 말해준다.(callback)
    
"""