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


def sum_many(*args):
  sum = 0
  for i in args:
    sum = sum + i
  return sum

def say():
  print('HI!')

def sum_many(*args):
  sum = 0
  for i in args:
    sum = sum + i
  return sum
result = sum_many(1,2,3)
print(result)
result = sum_many(1,2,3,4,5,6,7,8,9,10)
print(result)

def say_myself(name, old, man=True):
  print("나의 이름은 %s입니다." % name)
  print("나이는 %d살입니다." % old)
  if man:
    print("남자입니다.")
  else:
    print("여자입니다.")
say_myself("한승필", 28)

a = 1
def vertest(a):
  a = a + 1

vertest(a)
print(a)

a = 1
def vartest(a):
  a = a + 1
  return a

a = vartest(a)
print(a)

a = 1
def vartest():
  global a
  a = a + 1
  
vartest()
print(a)
