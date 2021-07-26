# 이름	먹는 데 걸리는 시간	매점 내 잔여 수량
# 콜라	300초	10개
# 초콜릿	130초	30개
# 과자	120초	20개
# 젤리	20초	30개


# 입력 예시 1
# 300
# 출력 예시 1
# 1


# 입력 예시 2
# 450
# 출력 예시 2
# 3


def solution(seconds):
    menu_time_list = [300, 130, 120, 20]

    i = 0

    for menu in menu_time_list:

        i += seconds // menu

    return i


print(solution(450))
