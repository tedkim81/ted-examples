import os
import google.generativeai as genai

genai.configure(api_key=os.environ['API_KEY'])

model = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    tools='code_execution')

response = model.generate_content((
    '처음 50개의 소수의 합은 얼마입니까? '
    '계산을 위한 코드를 생성 및 실행하고 50개의 소수의 합이 얼마인지 알려주세요.'))

print(response.text)

"""
[출력]

처음 50개의 소수의 합을 구하는 데 도움을 드리겠습니다. 

소수는 1과 자기 자신으로만 나누어지는 1보다 큰 정수입니다. 처음 몇 개의 소수는 2, 3, 5, 7, 11, 13, 17, 19, 23, 29...입니다.

처음 50개의 소수를 찾고 그 합을 계산하는 코드를 작성하겠습니다.


``` python
def is_prime(n):
    # n이 소수이면 True를 반환하고 그렇지 않으면 False를 반환합니다.
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = []
count = 0
num = 2
while count < 50:
    if is_prime(num):
        primes.append(num)
        count += 1
    num += 1

print(f'처음 50개의 소수는: {primes}')
print(f'처음 50개의 소수의 합은: {sum(primes)}')

```
```
처음 50개의 소수는: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229]
처음 50개의 소수의 합은: 5117

```
따라서 처음 50개의 소수의 합은 **5117**입니다.
"""