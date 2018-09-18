import csv
from collections import namedtuple

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

NameMonthStatistics = namedtuple('NameMonthStatistics', ['number_of_persons', 'year', 'month'])


def process_data(file_path, names):
    with open(file_path) as file:
        data = csv.reader(file, delimiter=';')
        next(data)  # skip header

        names_index = {name: [] for name in names}

        for name_month_data in data:
            name = name_month_data[1]

            if name in names_index:
                month_statistics = NameMonthStatistics(
                    number_of_persons=int(name_month_data[2]),
                    year=int(name_month_data[4]),
                    month=name_month_data[5]
                )
                names_index[name].append(month_statistics)

        for (name, name_data) in names_index.items():
            name_data.sort(key=lambda n: n.number_of_persons)

            # calc quantiles
            middle_index = int(len(name_data) / 2)

            q1 = get_median(name_data[:middle_index])
            # q2 = get_median(name_data)
            q3 = get_median(name_data[middle_index:])
            iqr = q3 - q1

            low_bound = q1 - 1.5 * iqr
            high_bound = q3 + 1.5 * iqr

            ejection = any(
                month_data.number_of_persons < low_bound or month_data.number_of_persons > high_bound
                for month_data in name_data
            )

            print(name, ejection)


def get_median(name_data):
    length = len(name_data)
    median_index = int(length / 2)

    if length % 2 == 0:
        first = name_data[median_index].number_of_persons
        second = name_data[median_index + 1].number_of_persons
        median = int((first + second) / 2)
    else:
        median_index += 1
        median = name_data[median_index].number_of_persons

    return median


def main():
    for d in initial_data:
        process_data(**d)


if __name__ == '__main__':
    main()
