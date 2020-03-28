test_list = [1,2,3]
for i in test_list:
  print(i)
  
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
  print(first + last)
  
makes = [67, 80, 50, 30, 90]
number = 0
for mark in makes:
  number = number + 1
  if mark >= 60:
    print("%d번 학생은 합격입니다." % number)
  else:
    print("%d번 학생은 불합격입니다." % number)
    
makes = [90, 25, 60, 45, 80]
number = 0
for mark in makes:
  number = number + 1
  if mark < 60: continue
  print("%d번 학생 축하합니다. 합격입니다." %number)
  
#range 숫자 함수를 자동으로 만드어 준다.
a = range(10)
print(a)
b = range(1,11)
print(b)

for i in range(2, 10):
  for j in range(1, 10):
    print(i*j, end = " ")
  print("")
    
a = [1,2,3,4]
result = []
for num in a:
  result.append(num * 3)
  print(result)
  
a = [1, 2, 3, 4]
result = []
for num in a:
  result = [num * 3 for num in a]
  print(result)
  
result = [num * 3 for num in a if num % 2 == 0]
print(result)

result = [x*y for x in range(2, 10) for y in range(1,10)]
print(result)

a = "Life is too short, you need python"

if "wife" in a:print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a:print("shirt")
elif "need" in a:print("need")
else: print("none")

i = 0
while True:
  i += 1
  if i > 5: break
  print('*' * i)