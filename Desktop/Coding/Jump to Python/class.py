result = 0

def adder(num):
  global result
  result += num
  return result

print(adder(3))
print(adder(5))

class Service:
  secret = "영구는 배꼽이 두개다"
  def __init__(self, name): #__init__ 인스턴스를 만들 때 항상 실행된다.
    self.name = name
  def sum(self, a, b):
    result = a + b
    print("%s님 %s + %s = %s입니다." % (self.name, a, b, result))  
pey = Service("한승필")
print(pey.secret)
pey.sum(2, 4)
