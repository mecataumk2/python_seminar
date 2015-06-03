file_test = open('sample.txt', 'rt') 

print type(file_test)
print file_test

lines = file_test.readlines()

print type(lines)


range_1 = range(100, 105)
print type(range_1)
print range_1

 
for number in range_1:
    print number

 
for line in lines[1:3]:
   # print line
   # a=line.split(",")
   split = line.split(",")
   email = split[3]
   print email
  #  print a[3]


#a=line.split(",")
#print a




#if isinstance(line, str) and '@' in str
#    print line


