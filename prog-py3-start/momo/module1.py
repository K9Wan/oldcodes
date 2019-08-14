# module1.py
def prog(n):
    if n <= 1:
        return 'gaegul'
    return prog(n - 1) + ' gaegul'

maru = 'bulgom'

if __name__ == '__main__':
    print('module1 starting')
    print(prog(7))
