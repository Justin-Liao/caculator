# CarName,Time,Speed,Acceleration,AccelerationResult,TimeToBeat

CarAcceleration = []
TimeToBeat = 1.23
carNumber = int(input('Input car number: '))
for i in range(carNumber):
    print('Please input car '+str(i+1)+' data:')
    CarName = str(input('  Input car name : '))
    Time = float(input('  Input time     : '))
    Speed = float(input('  Input speed    : '))
    Acceleration = Speed/Time
    if Acceleration >= TimeToBeat:
        CarAcceleration.append([str(CarName), str(Acceleration)])

# print(CarAcceleration)
txt = ''
for index in range(carNumber):
    txt += ('_'*25)+'\n'+' car name: ' + \
        CarAcceleration[index][0] + '\n'+' car speed: ' + \
        CarAcceleration[index][1]+' m/s^2'+'\n'

file = open('success_result.txt', 'w')
file.write(txt)
file.close()
