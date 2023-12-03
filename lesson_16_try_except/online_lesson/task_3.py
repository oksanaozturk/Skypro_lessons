# Задача 1*Напишите программу, которая будет проверять доступность сайтов из списка.
# Если какой-то сайт недоступен (вернул ошибку 404 или 500),
# то программа должна выбросить исключение и продолжить проверку остальных сайтов.
# В конце работы программы выведите список недоступных сайтов.
import requests

websites_to_check = [
    "https://www.google.com",
    "https://www.invalidwebsite.com",
    "https://www.eample.com"
]


def check_availability(list_of_sites):
    for site in list_of_sites:
        list_of_not_availability = []
        try:
            response = requests.get(site)
            response.raise_for_status()

        except (requests.HTTPError, requests.ConnectionError):
            print(site, 'Is not availability')
            list_of_not_availability.append(site)
        

check_availability(websites_to_check)

