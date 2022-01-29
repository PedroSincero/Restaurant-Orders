import csv;
from collections import Counter

def days_the_customer_doesnt_show_up(client):
    raise NotImplementedError

def csv_importer(path_to_file):
    log = {}
    with open(path_to_file) as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            if row[0] not in log:
                log[row[0]] = [[row[1], row[2]]]
            else:
                log[row[0]].append([row[1], row[2]])
    return log

def get_all_dishes(path_to_file):
    result = set()
    with open(path_to_file) as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            if row[1] not in result:
                result.add(row[1])
    return result

def get_all_days(path_to_file):
    result = set()
    with open(path_to_file) as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            if row[2] not in result:
                result.add(row[2])
    return result

def days_customer_shows_up(orders):
    result = set()
    for order in orders:
        if order[1] not in result:
            result.add(order[1])
    return result

def most_requested_dish_by(orders, client):
    result = []
    customer_orders = orders[client]
    for i in customer_orders:
        result.append(i[0])
    return Counter(result).most_common(1)[0][0]

def many_dishes_eat(orders, dish):
    result = 0
    for order in orders:
        if order[0] == dish:
            result += 1
    return result

def customer_dish(orders):
    result = set()
    for order in orders:
        if order[0] not in result:
            result.add(order[0])
    return result


def analyze_log(path_to_file):
    orders_client = csv_importer(path_to_file)
    biggest_order_Maria = most_requested_dish_by(orders_client, 'maria')

    how_many_times_Arnaldo_ordered_hamburgers = many_dishes_eat(orders_client['arnaldo'], 'hamburguer')

    # refatorar 1
    joao_order_dish = customer_dish(orders_client['joao'])
    all_dishes = get_all_dishes(path_to_file)
    joao_never_asked = all_dishes.difference(joao_order_dish)
    
    # refatorar 2
    joao_order_days = days_customer_shows_up(orders_client['joao'])
    all_days = get_all_days(path_to_file)
    joao_never_days = all_days.difference(joao_order_days)

    result = [
        biggest_order_Maria,
        how_many_times_Arnaldo_ordered_hamburgers,
        joao_never_asked,
        joao_never_days
    ]

    with open('data/mkt_campaign.txt', 'w') as file:
        for row in result:
            file.write(f"{str(row)}\n")

# result = csv_importer("data/orders_1.csv")
# # most_requested_dish_by(result, 'maria')
# print(result)