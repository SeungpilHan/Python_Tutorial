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

