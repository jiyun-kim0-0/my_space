
#최소공약수
#유클리드 호제법

def gcd(a,b):
    if a % b == 0:
        #a가 b의 배수라면, (a>b)
        return b #최소공약수
    
    else: #b와 a를 b로 나눈 나머지의 최소 공약수를 반환하도록 함
        return gcd(b, a%b)
    

print(gcd(192,162))

#재귀 함수 / 반복문을 쓸 경우를 구분해야 한다. 상황에 각각 장단점이 존재함.
#컴퓨터가 함수를 연속적으로 호출하면 메모리 내부에 스택 프레임이 쌓임.
#따라서, 스택을 사용해야 할 때 구현상 스택 라이브러리 대신 재귀함수를 이용하는 경우가 많음.