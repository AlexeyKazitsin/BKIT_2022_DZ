data_1 = [4, -30, 100, -100, 123, 1, 0, -1, -4]


def sort_1(data):
    result = sorted(data, key=abs, reverse=True)
    return result


def sort_2(data):
    result_with_lambda = sorted(data, key=lambda x: abs(x), reverse=True)
    return result_with_lambda


def main_s():
    result = sort_1(data_1)
    print(result)

    result_with_lambda = sort_2(data_1)
    print(result_with_lambda)


if __name__ == "__main__":
    main_s()
