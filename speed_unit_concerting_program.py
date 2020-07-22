# -*- coding: utf-8 -*-

import sys

class Przelicznik:

    def metrstokmh(self):
        self.km = int(input('Enter the number of meters / second: '))
        if self.km  > 0 :
            self.km = self.km * 3,6
            print('Value in km / h: ', self.km)
        else:
            print('Enter a value greater than 0', round(self.km, 2))

    def kmtoms(self):
        self.m = int(input('Enter the number of kilometers / hour: '))
        if self.m > 0 :
            self.m = self.m * 1000/3600
            print('Value in ms / s: ', round(self.m, 2))
        else:
            print('Enter a value greater than 0')


przelicznik = Przelicznik()

while True:
    print('Press 1 to convert meters / seconds to kilometers / hour')
    print('Press 2 to convert kilometers / hour to meters / second')
    print('Press 3 to end the program.')
    wybor_uzytkownika = int(input('>>> '))
    if wybor_uzytkownika is 1:
        przelicznik.metrstokmh()
    elif wybor_uzytkownika is 2:
        przelicznik.kmtoms()
    elif wybor_uzytkownika is 3:
        sys.exit()



