print(abs(3))
print(abs(-3))
print(abs(-1.3))

print(all([1,2,3]))
print(all([1, 2, 3, 0]))

print(any([1,2,3,0])) #하나라도 참이면 참
print(any([0,""]))

print(chr(97))
print(chr(126))

print(dir([1,2,3]))
print(dir({'1':'a'}))

print(divmod(7, 3))
print(divmod(1.3, 0.2))

for i, name in enumerate(['body', 'foo', 'bar']):
  print(i, name)
  
def positive(numberList):
  result = []
  for num in numberList:
    if num > 0:
      result.append(num)
    return result
  
print(positive([1, -3, 2, 0, -5, 6]))

def positive(x):
  return x >0

print(list(filter(positive,[1,-3,2,0,-5,6])))

#a = input()

#b = input("Enter: ")

print(int('3'))

print(int(3.5))

class person: pass

a = person()
print(isinstance(a, person))

b = 3
print(isinstance(b, person))