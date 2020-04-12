f= open("새파일.txt", 'w')
for i in range(1, 11):
  data = "%d번째 줄 입니다.\n" % i
  f.write(data)
f.close()

f = open("새파일.txt", 'r')
line = f.readline()
print(line)
f.close()

f = open("새파일.txt", 'r')
while True:
  line = f.readline()
  if not line: break
  print(line)
f.close()

f = open("새파일.txt", 'r')
lines = f.readlines()
for line in lines:
  print(line)
f.close() 
