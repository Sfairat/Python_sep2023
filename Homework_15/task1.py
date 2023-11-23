import logging
import argparse


def log_info_triangle(text: str):
    FORMAT: str = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
                  'в строке {lineno:03d} функция "{funcName}()" ' \
                  'в {created} секунд записала сообщение: {msg}'
    logging.basicConfig(format=FORMAT, style='{', level=logging.INFO)
    logger = logging.getLogger('main')
    logger.info(text)


def log_warning_triangle(text: str):
    FORMAT: str = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
                  'в строке {lineno:03d} функция "{funcName}()" ' \
                  'в {created} секунд записала сообщение: {msg}'
    logging.basicConfig(format=FORMAT, style='{', level=logging.WARNING)
    logger = logging.getLogger('main')
    logger.warning(text)


def triangle_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('sides', metavar='a b c', type=int, nargs=3)
    args = parser.parse_args()
    print(args)
    return triangle(*args.sides)


def triangle(a: int, b: int, c: int):
    if a + b > c and a + c > b and b + c > a:
        text = 'Треугольник существует'
        log_info_triangle(text)
        if a != b != c:
            text = 'Треугольник разносторонний'
            log_info_triangle(text)
        if (a == b or a == c or b == c) and (a != b != c):
            text = 'Треугольник равнобедренный'
            log_info_triangle(text)
        if a == b == c:
            text = 'Треугольник равносторонний'
            log_info_triangle(text)
    else:
        text = 'Треугольник не существует'
        log_warning_triangle(text)


if __name__ == '__main__':
    triangle_parser()
