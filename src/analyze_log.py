import csv;
from collections import Counter

# def days_the_customer_doesnt_show_up(client):
#     raise NotImplementedError

def csv_importer(path_to_file):
    log = {}
    with open(path_to_file) as file:
        reader = csv.reader(file, delimiter=",", quotechar='"')
        for row in reader:
            if row[0] not in log:
                log[row[0]] = [[row[1], row[2]]]
            else:
                log[row[0]].append([row[1], row[2]])
    return log

def get_all_dishes(path_to_file):
    result = set()
    with open(path_to_file) as file:
        reader = csv.reader(file, delimiter=",", quotechar='"')
        for row in reader:
            if row[1] not in result:
                result.add(row[1])
    return result

def analyze_log(path_to_file):
    orders_client = csv_importer(path_to_file)
    biggest_order_Maria = most_requested_dish_by(orders_client, 'maria')
    how_many_times_Arnaldo_ordered_hamburgers = how_many_times_the_customer_asked(orders_client, 'arnaldo')
    joao_order = customer_dish(orders_client['joao'])
    all_dishes = get_all_dishes(path_to_file)
    
    raise NotImplementedError


def most_requested_dish_by(orders, client):
    result = []
    customer_orders = orders[client]
    for i in customer_orders:
        result.append(i[0])
    return Counter(result).most_common(1)[0][0]

def how_many_times_the_customer_asked(orders, client):
    result = []
    customer_orders = orders[client]
    for i in customer_orders:
        result.append(i[0])
    return Counter(result).most_common(1)[0][1]

def customer_dish(orders):
    result = set()
    for order in orders:
        if order[0] not in result:
            result.add(order[0])
    return result

def dishes_that_the_customer_did_not_order(orders, client):

    raise NotImplementedError


result = csv_importer("data/orders_1.csv")
# most_requested_dish_by(result, 'maria')
print(result)

# def all_dishes(orders):
#     result = set()