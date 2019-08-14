# 6주차 과제 1
import random
 
 
# 소괄호로 이루어진 tuple은 읽기 전용 list입니다
# (-1, 1)[0]처럼 indexing할 수 있습니다
DIRECTION = [
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
    (-1, 0)
]
 
floor = None
 
height = None
width = None
i = None
j = None
 
 
def roach_move() -> None:
    global floor, height, width, i, j
 
    next_i = -1
    next_j = -1
 
    # 올바른 위치로만 무작위로 이동합니다
    while next_i < 0 or next_i >= height or next_j < 0 or next_j >= width:
        direction = random.choice(DIRECTION)
        next_i = i + direction[0]
        next_j = j + direction[1]
 
    i = next_i
    j = next_j
 
    # 방문 횟수를 증가시킵니다
    floor[i][j] += 1
 
 
if __name__ == '__main__':
    # 높이와 너비를 받습니다
    height = int(input())
    width = int(input())
 
    # 무대를 구성합니다
    floor = [[0 for _ in range(width)] for _ in range(height)]
 
    # 현재 위치를 초기화합니다
    i = height // 2
    j = width // 2
 
    # 현재 위치를 방문합니다
    floor[i][j] = 1
 
    # 미친 듯이 돌아다닙니다
    count = 1
    floor_area = height * width
    while count < floor_area:
        roach_move()
        if floor[i][j] == 1:
            count += 1
 
    # 현재 위치를 출력합니다
    print(i, j)
 
    # 무대의 각 칸을 밟은 횟수를 출력합니다
    for row_list in floor:
        for cell in row_list:
            print(cell, end=' ')
        print()
 