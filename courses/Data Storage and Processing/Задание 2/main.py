import csv


def process_data(file_path, names):
    names_index = {name: [] for name in names}

    with open(file_path) as file:
        data = csv.reader(file, delimiter=';')
        next(data)  # skip header

        for name_month_data in data:
            name = name_month_data[1]

            if name in names_index:
                names_index[name].append(int(name_month_data[2]))  # number_of_persons

    for (name, name_data) in names_index.items():
        name_data.sort()

        # calc quantiles
        middle_index = int(len(name_data) / 2)

        q1 = get_median(name_data[:middle_index])
        # q2 = get_median(name_data)
        q3 = get_median(name_data[middle_index:])
        iqr = q3 - q1

        low_bound = q1 - 1.5 * iqr
        high_bound = q3 + 1.5 * iqr

        ejection = any(
            month_data < low_bound or month_data > high_bound
            for month_data in name_data
        )

        yield name, ejection


def get_median(name_data):
    length = len(name_data)
    median_index = int(length / 2)

    if length % 2 == 0:
        first = name_data[median_index]
        second = name_data[median_index + 1]
        median = int((first + second) / 2)
    else:
        median_index += 1
        median = name_data[median_index]

    return median


if __name__ == '__main__':
    initial_data = [
        {
            'file_path': './boys.csv',
            'names': ['Денис', 'Глеб', 'Леон', 'Тихон']
        },
        {
            'file_path': './girls.csv',
            'names': ['Карина', 'Евгения', 'Яна']
        }
    ]

    for params in initial_data:
        for result in process_data(**params):
            print(*result)
