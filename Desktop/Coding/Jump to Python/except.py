try:
  4 / 0
except ZeroDivisionError as e:
  print(e)
  
try:
  f = open('foo.txt', 'r')
except FileNotFoundError as e:
  print(str(e))
else:
  data = f.read()
  f.close()
  
f = open('foo.txt', 'w')
try:
  print('error') #무언가를 실행한다.
finally:
  f.close()
  
try:
  f = open("나 없는 파일",'r')
except FileNotFoundError:
  pass

class Bird:
  def fly(self):
    raise NotImplementedError
  
class Eagle(Bird):
  def fly(self):
    print("very fast")

eagle = Eagle()
eagle.fly()