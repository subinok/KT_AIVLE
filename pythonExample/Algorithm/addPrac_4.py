"""
각 자리가 숫자(0부터 9)로만 이루어진 문자열을 사용자로 부터 입력받아, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 곱하기(x) 혹은 더하기(+) 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하세요.

단, + 보다 x 를 먼저 계산하는 일반적인 방식과 달리 모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정합니다.
"""

str = input('숫자로 이루어진 문자열을 입력하세요: ')
data = []

for i in str:
    prev = data[i-1]
    if i != len(data) - 1:
        next = data[i+1]
        
    if prev == 0:
        result += data[i]
    elif data[i] == 0:
        continue
    else:
        result *= data[i]
         
print(result)