"""Calculator Math class to be complement to somando.py
missing finish yet"""

from random import randint
import time


class CalculatorMath:
    """Calculator the math to user.
    Return total hits and last correct answer"""
    def __init__(self, hit=0, tempo=time.time()):
        self.hit = hit
        self.tempo = tempo
        self.range_int = 7
        self.range_end = 3
        self.result = result
        self.answer_user = answer_user
        self.fist_number = int(randint(0, self.range_end))
        self.second_number = int(randint(self.range_end, self.range_int))

    def __str__(self):
        """Planing yet"""
        return self.hit, self.tempo

    def process_math(self):
        """Process math choice randomly de math to be executed"""
        type_math = randint(0,1)
        if type_math == 0:
            self.process = plus_math()

    def plus_math(self):
        """Plus calculate when choice randomly to be compared to the user answer.
        Return result to be compared"""
        self.result = self.fist_number + self.second_number
        print(f'{self.fist_number} + {self.second_number} = ')
        return self.result

    def sub_math(self):
        """Sub calculate when choice randomly to be compared to the user answer.
        Return result to be compared"""
        self.result = fist_number - second_number
        print(f'{fist_number} - {second_number} = ')
        return self.result

    def get_right(self):
        """Get the user answer to be compared to the result choice randomly before, so
        if user get the right answer pass to another calculate until get the wrong
        answer"""
        self.answer_user = str(input(f'  Resposta =  '))
        if self.answer_user.isnumeric():
            self.answer_user = int(self.answer_user)
            if self.result == self.answer_user:
                print(f'{self.hit + 1} acertos')
                self.hit += 1
                self.range_end += 2
                self.range_int += 3
            else:
                pass
        else:
            pass
        print('ERRADO')
        print(f'RESPOSTA CERTA ERA {self.result}'.center(40))
        print()
        return self.hit, self.tempo


print(CalculatorMath.__dict__)
