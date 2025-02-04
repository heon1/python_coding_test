if __name__ == '__main__':
    a, b = map(int, input().split())  # 정수 두개를 입력받는다.
    if (1<=a) and (a<=10000) and (1<=b) and (b<=10000): 
        print(a + b)  # 두 수의 합 출력
        print(a - b)  # 두 수의 차 출력
        print(a * b)  # 두 수의 곱 출력
        print(a // b)  # 두 수의 몫 출력
        print(a % b)  # 두 수의 나머지 출력