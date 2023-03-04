"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""


import numpy as np
import random

random_number = random.randint(1, 101)

def game_core(number:int=1)->int:
    """Рандомно угадываем число
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count=0
    begins = 1
    ends = 100
    
    while True:
        count+=1
        mid = (begins+ends)//2
        if mid == random_number:
            print(f'число {mid} найден за {count} попыток!')
            break  #выход из цикла, если угадали
        elif mid > random_number:
            ends = mid
        else:
            begins = mid   
    return (count)


def score_game(game_core)->int:
    """За какое количество попыток в среднем из 1000 подходов 
    угадывает наш алгоритм

    Args:
        game_core ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_1s=[]   #список для сохранения количества попыток
    np.random.seed(1)   #фиксируем сид для воспроизводимости
    random_array=np.random.randint(1, 101, size=(1000))  #загадали список чисел
    
    for number in random_array:
        count_1s.append(game_core(number))
        
    score=int(np.mean(count_1s))  #находим среднее количество попыток
    
    print(f'Ваш алгоритм угадывает число в среднем за : {score} попыток')
    return(score)
#RUN
if __name__ == "__main__":
    score_game(game_core)