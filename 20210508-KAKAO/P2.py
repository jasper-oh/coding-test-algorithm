# 2021/05/22 CheckAgain and find solution
# Check another solution for making awesomeness!

# Maybe making 다익스트라 algo for making fast?
# 대기실은 5개이며, 각 대기실은 5x5 크기입니다.
# 거리두기를 위하여 응시자들 끼리는 맨해튼 거리가 2이하로 앉지 말아주세요.
# 단 응시자가 앉아 있는 자리 사이가 파티션으로 막혀 있을 경우에는 허용합니다.

# places의 행 길이(대기실 개수) = 5
# places의 각 행은 하나의 대기실 구조를 나타냅니다.
# places의 열 길이(대기실 세로 길이) = 5
# places의 원소는 P,O,X로 이루어진 문자열입니다.
# places 원소의 길이(대기실 가로 길이) = 5
# P는 응시자가 앉아있는 자리를 의미합니다.
# O는 빈 테이블을 의미합니다.
# X는 파티션을 의미합니다.
# 입력으로 주어지는 5개 대기실의 크기는 모두 5x5 입니다.
# return 값 형식
# 1차원 정수 배열에 5개의 원소를 담아서 return 합니다.
# places에 담겨 있는 5개 대기실의 순서대로, 거리두기 준수 여부를 차례대로 배열에 담습니다.
# 각 대기실 별로 모든 응시자가 거리두기를 지키고 있으면 1을, 한 명이라도 지키지 않고 있으면 0을 담습니다.

# [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
#  -> [1,0,1,1,1]
