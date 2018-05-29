def record1(self):
    with open('guess_record1.txt','w+') as f:
        f.readline()
        f.writelines(self)
num2 = 'a'
def record1(self):
    with open('guess_record1.txt', 'a+') as f:
        f.write(self + '\n')
record1(num2)