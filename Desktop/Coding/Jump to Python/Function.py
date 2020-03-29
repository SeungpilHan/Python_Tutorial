#def는 함수를 만들 때 사용하는 예약어이며, 함수명은 함수를 만드는 사람이 임의로 만들 수 있다.
def sum(a, b):
  return a + b
a = 3
b = 5
c = sum(a, b)
print(c)

def sum(a, b):
  result = a + b
  return result

a = sum(3, 3)
print(a)

def say():
  return 'hi!'
a = say()
print(a)