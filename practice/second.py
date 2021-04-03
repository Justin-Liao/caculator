
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'allpeople.csv')
All = 'Name, Height, Weight, BMI\n'  # +'_'*40+'\n'
all = []
count = int(input('Number of people imput : '))
print('_'*40)
for _ in range(count):
    name = input('  Name : ')
    height = int(input('  Height(cm) : '))
    weight = int(input('  Weight(kg): '))
    print('_'*40)
    BMI = weight/(height*height)*10000
    all.append([name, height, weight, BMI])
# print(all)
for person in all:
    All += str(person[0])+' , '+str(person[1])+' , ' + \
        str(person[2])+' , '+str(person[3])+'\n'
# print(All)
allpeople = open('allpeople.csv', 'w')
allpeople.write(All)
allpeople.close()
allpeople = open('allpeople.csv', 'r')
print(allpeople.readline())
print(allpeople.readline())
