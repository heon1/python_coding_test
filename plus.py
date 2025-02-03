if __name__ == '__main__':
    a, b = map(int, input().split())  # 두 숫자를 정수로 받아온다.
    if (0<a) and (a<10) and (0<b) and (b<10):  # 정해진 조건에서 a, b 를 받을 경우 
        print(a + b)  # 두 변수를 합쳐서 출력
    else:
        pass