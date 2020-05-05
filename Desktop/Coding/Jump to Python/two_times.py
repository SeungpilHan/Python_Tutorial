def two_times(numberList):
  result = []
  for number in numberList:
    result.append(number*2)
  return result

result = two_times([2,4,5,6])
print(result)

print(list(map(lambda a:a*2, [1,2,3,4])))

print(max([1,2,3]))
print(max("python"))

print(min([1, 2, 3]))
print(min("python"))


print(ord('a'))

print(pow(2,4))

print(list(range(5)))
print(list(range(5,10)))
print(list(range(1, 10, 2)))

print(sorted([3,1,2]))

print(tuple("abc"))
print(tuple([1,2,3]))

print(type("abc"))

print(list(zip([1,2,3],[4,5,6])))