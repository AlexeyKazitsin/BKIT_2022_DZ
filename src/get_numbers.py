import requests
import matplotlib.pyplot as plt


def make_url(cnt):
    base_url = 'http://127.0.0.1:5000/num/'
    res = base_url + str(cnt)
    return res


def get_data(cnt):
    url = make_url(cnt)
    r = requests.get(url)
    return r.json()


if __name__ == '__main__':
    y = get_data(int(input('Сколько чисел Фибоначчи?')))
    print(y)
    print(len(y))
    x = list(range(1, len(y) + 1))
    fig = plt.figure(figsize=(10, 5))
    plt.bar(x, y)
    plt.xlabel('Ось абсцисс')
    plt.ylabel('Ось ординат')
    plt.title('Первые {} чисел последовательности Фибоначчи'.format(len(y)))
    plt.show()

    plt.plot(x, y)
    plt.show()