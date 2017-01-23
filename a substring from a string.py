#Author: kingsley
def check(string, name):
no = 0
y = len(name)-1
for i in range(0,len(string)-y):
  if string[i] + name[1:] == name:
    no += 1
print("Number of times " + name + " occur is: " + str(no))
