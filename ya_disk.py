import requests

with open('token.txt') as file:
    token = file.read()

url = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(token)}


def create_folder_in_Ya():
    folder_name = input('Введите имя создаваемой папки : ')
    response = requests.put(url=url, params={'path': '/'+folder_name}, headers=headers)
    answer = response.status_code
    if answer == 201:
        print(f'папка  c именем "{folder_name}" успешно создана на Яндекс диске')
    elif answer == 409:
        print(f'папка с таким именем уже существует')
    return answer


def is_folder_in_Ya():
    folder_name = input('Введите имя папки  для проверки : ')
    response = requests.get(url=url, params={'path': '/'+folder_name}, headers=headers)
    answer = response.status_code
    if answer == 200:
        print(f'папка с именем "{folder_name}" есть на Яндекс диске')
    elif answer == 404:
        print(f'папки с именем "{folder_name}" нет на Яндекс диске')
    return answer


def delete_folder():
    folder_name = input('Введите имя папки  для удаления : ')
    response = requests.delete(url=url, params={'path': '/' + folder_name}, headers=headers)
    answer = response.status_code
    if answer == 204:
        print(f'папка с именем "{folder_name}" успешно удалена с Яндекс диска')
    elif answer == 404:
        print(f'папки с именем "{folder_name}" нет на Яндекс диске')
    return answer


if __name__ == '__main__':
    create_folder_in_Ya()
    is_folder_in_Ya()
    delete_folder()
