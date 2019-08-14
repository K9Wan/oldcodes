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
 
 
def prog_move() -> None:
    global floor, height, width, i, j
    direction=random.choice(DIRECTION)
    i+=direction[0]
    if i<0:
        i+=1
    elif i>=height:
        i-=1
    else:
        pass
    j+=direction[1]
    if j<0:
        j+=1
    elif j>=width:
        j-=1
    else:
        pass
    floor[i][j]=(floor[i][j])+1
 
if __name__ == '__main__':
    # 높이와 너비를 받습니다
    height = int(input())
    width = int(input())
 
    # 무대를 구성합니다
    floor = [[0 for _ in range(width)] for _ in range(height)]
 
    # 현재 위치를 초기화합니다
    i=height//2
    j=width//2
 
    # 현재 위치를 방문합니다
    floor[i][j] = 1
 
    # 미친 듯이 돌아다닙니다
    check=True
    while(check):
        check=False
        prog_move()
        for row_list in floor:
            for cell in row_list:
                if cell==0:
                    check=True
 
    # 현재 위치를 출력합니다
    print(i, j)
 
    # 무대의 각 칸을 밟은 횟수를 출력합니다
    for row_list in floor:
        for cell in row_list:
            print(cell, end=' ')
        print()