print('Hello, DjangoGirls!')

if 3>2:
    print('It works')


def hi():
    print('hi')
    print('hello there')

hi()

def hi2(name):
    if name == 'Sonja':
        print('Hello, Sonja!')
    elif name == 'Daniela':
        print('Hello, Daniela!')
    else:
        print('Hello, anonymous!')


hi2('Andrea')

def hi3(nomb):
    print ('Hola ' + nomb + '!')

hi3('Andrea')

girls = ['Dani', 'Cinthya', 'Kami']

for name in girls:
    hi3(name)
    if name==girls[-1]:
        print('Last Girl')
    else:
        print('Next Girl')
for i in range(1,6):
    print(i)