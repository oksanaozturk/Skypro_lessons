# **Задание 1. Все блоки try**Заполните все блоки `try`, `except`, `else`, `finally` так,
# чтобы функция делала следующие действия:
# - считывает файл в бинарном режиме (`mode='rb'`)
# - возвращает считанные данные
# - выводит время, затраченное на считывание файлаКод вне перечисленных блоков не должен быть.

import time


def read_file_timed(file):
    """Возвращает содержимое файла и измеряет требуемое время."""

    start_time = time.perf_counter()
    try:
        with open(file, 'rb') as f:
            content = f.read()

    except FileNotFoundError:
        print(f"Can not find file '{file}'")

    else:
        return content

    finally:
        end_time = time.perf_counter()
        if file is True:
            print(f"Time required for '{file}' is ", end_time - start_time)
        else:
            print(f"Time required for '{file}' is ", 0.0)


binary_data = read_file_timed('bigfile')
# Time required for 'bigfile' is 0.06553506851196289#

# попытка считать отсутствующий файл
# binary_data = read_file_timed('file_not_exist')
# Can not find file 'file_not_exist'
# Time required for 'file_not_exist' is 0.0
