import logging
import argparse
from random import randint


def log_info_riddle(text: str):
    FORMAT: str = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
                  'в строке {lineno:03d} функция "{funcName}()" ' \
                  'в {created} секунд записала сообщение: {msg}'
    logging.basicConfig(format=FORMAT, style='{', level=logging.INFO)
    logger = logging.getLogger('main')
    logger.info(text)


def log_warning_riddle(text: str):
    FORMAT: str = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
                  'в строке {lineno:03d} функция "{funcName}()" ' \
                  'в {created} секунд записала сообщение: {msg}'
    logging.basicConfig(format=FORMAT, style='{', level=logging.WARNING)
    logger = logging.getLogger('main')
    logger.warning(text)


def riddle_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('nums', type=int, nargs=1)
    args = parser.parse_args()
    print(args)
    return riddle(*args.nums)


def riddle(input_num: int):
    num = randint(0, 1000)
    count = 1

    if(input_num >= 0 and input_num <= 1000):
        for i in range(2, 11):
            if(input_num != num):
                count = count + 1
                if(input_num > num):
                    text = 'меньше'
                    log_info_riddle(text)
                    input_num = int(input(f'Попытка {count}. Введите число от 0 до 1000: '))
                elif(input_num < num):
                    text = 'больше'
                    log_info_riddle(text)
                    input_num = int(input(f'Попытка {count}. Введите число от 0 до 1000: '))
            else:
                text = 'Угадал!'
                log_info_riddle(text)
                break
    else:
        text = 'Введено не верное число'
        log_warning_riddle(text)
    if(count == 10):
        text_1 = 'Попытки закончились. Попробуйте снова.'
        log_info_riddle(text_1)
        text_2 = f'Загаданное число {num}.'
        log_info_riddle(text_2)


if __name__ == '__main__':
    riddle_parser()
