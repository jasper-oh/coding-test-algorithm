# 문제 설명
# 커싸 원두 재고량 계산하기
# 난이도: ★★

# 배경
# 좌석 문제를 해결한 김토스님은, 업무를 시작하기 전에 팀 리더와 간단한 커피챗을 하기위해 커피 사일로로 이동합니다.
# (커피 사일로: 사내 커피숍)

# 커피를 주문하고 기다리는 중에 커피 사일로에서 커피 원두 재고량 확인에 어려움을 겪고 있다는 사실을 듣게됩니다.

# 이에 김토스님은 본인의 개발역량을 발휘하여 재고량을 간단히 확인할 수 있는 방법을 제공해드리려 합니다.

# 문제
# 이러한 문제 상황에서, 2021년 5월 2일의 커피 재고를 테이블 형태로 반환하는 SQL 쿼리를 작성해주세요.

# 결과는 toss_coffee.id 기준으로 오름차순 정렬해주세요.

# 커피 사일로에서 보관하고 있는 원두와 관련된 테이블의 정보는 아래와 같습니다.

# 커피 원두 목록
# CREATE TABLE toss_coffee (
#     id   BIGINT      NOT NULL AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(15) NOT NULL
# );
# 커피 원두의 발주/소모 이력
# CREATE TABLE toss_coffee_log (
#     id        BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
#     coffee_id BIGINT,
#     date      DATE,
#     amount    BIGINT,
#     FOREIGN KEY (coffee_id) REFERENCES toss_coffee(id)
# );
# 출력 예시
# id	name	amount
# 1	브라질 산토스	1010
# 2	콜롬비아 수프리모	0
# ...	...	...
# 3	자메이카 블루마운틴	0
