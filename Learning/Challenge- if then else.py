name = input('Whats your name?: ')
age = int(input('How old are you, {0}: '.format(name)))

if 18 <= age <=30:
    print('Welcome to the party, {0}'.format(name))
else:
    print('You cant stay in this party, {0}:/'.format(name))