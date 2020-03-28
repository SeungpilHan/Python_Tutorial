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
  
x = 3
y = 2
print(x > y)
  
money = 2000
if money >= 3000:
  print("택시를 타세요")
else:
  print("걸어가세요")
  
money = 4000
card = "sinhan"
if money >= 3000 and "sinhan":
  print("택시를 탈 수 있습니다.")
else:
  print("걸어가세요")
  
print(1 in [1,2,3])
print(1 not in [1,2,3])

#주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 돈도 없고 카드도 없으면 걸어서 가라.
money = 0
card = 2
if money:
  print("택시를 타라")
else:
  if card:
    print("택시를 타라")
  else:
    print("걸어서 가라")
    
pocket = ['paper', 'cellphone']
card = 1
if 'money' in pocket:
  print("택시를 타세요")
else:
  if card:
    print("택시를 타세요")
  else:
    print("걸어가세요")
    
pocket = ['paper', 'cellphone']
card = 1
if 'money' in pocket:
  print("택시를 타세요")
elif card:
  print("택시를 타세요")
else:
  print("걸어서 가세요")
  
if 'money' in pocket:
  pass
else:
  print("카드를 꺼내라")
  
