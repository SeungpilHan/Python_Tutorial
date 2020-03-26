a = [1,2,3,4]
while a:
  print(a.pop())
  
if []:
  print("true")
else:
  print("false")
  
if [1,2,3]:
  print("true")
else:
  print("false")

a = 1
b = "python"
c = [1,2,3]

a, b = ('python', 'life')
(a, b) = 'python', 'life'
[a, b] = ['python', 'life']
a = b = 'python'

a = 3
b = 5
a, b = b, a
print(a, b)

a = 3
del(a)

a = [1,2,3]
b = a[:]
a[1] = 4
print(a)
print(b)

money = 1
if money:
  print("택시를 타라")
else:
  print("걸어가라")
  
game = 0
if game:
  print("하는 중")
else:
  print("쉬는중")
  
  
