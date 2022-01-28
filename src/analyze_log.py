import csv;
from collections import Counter

# def how_many_times_the_customer_asked(client, order):
#     raise NotImplementedError

# def dishes_that_the_customer_did_not_order(client):
#     raise NotImplementedError

# def days_the_customer_doesnt_show_up(client):
#     raise NotImplementedError

def csv_importer(path_to_file):
    log = {}
    with open(path_to_file) as file:
        reader = csv.reader(file, delimiter=",", quotechar='"')
        for row in reader:
            if row[0] not in log:
                log[row[0]] = [[row[1], row[2]]]
                # print(log)
            else:
                log[row[0]].append([row[1], row[2]])
    return log

def analyze_log(path_to_file):
    orders_client = csv_importer(path_to_file)
    biggest_order_Maria = most_requested_dish_by(orders_client, 'maria')
    raise NotImplementedError


def most_requested_dish_by(orders, client):
    result = []
    customer_orders = orders[client]
    for i in customer_orders:
        result.append(i[0])
    return Counter(result).most_common(1)[0][0]

result = csv_importer("data/orders_1.csv")
most_requested_dish_by(result, 'maria')