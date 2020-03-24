"""
집합에 관련된 것들을 쉽게 처리하기 위해 만들어진 자료형이다.
중복을 허용하지 않는다
순서가 없다
"""

s = set([1,2,3])
print(s)
l1 = list(s)
print(l1)
t1 = tuple(s)
print(t1)

s2 = set("Hello")
print(s2)

s3 = set([1,2,3,4,5,6])
s4 = set([4,5,6,7,8,9])
print(s3 & s4)
print(s3.intersection(s4))
print(s3 | s4)
print(s3.union(s4))
print(s3 - s4)
print(s3.difference(s4))

s1 = set([1,2,3])
s1.add(4)
print(s1)
s1.update([4,5,6])
print(s1)
s1.remove(2)
print(s1)