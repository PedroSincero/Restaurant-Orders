import csv;


# def how_many_times_the_customer_asked(client, order):
#     raise NotImplementedError

# def dishes_that_the_customer_did_not_order(client):
#     raise NotImplementedError

# def days_the_customer_doesnt_show_up(client):
#     raise NotImplementedError

def csv_importer(path_to_file):
    log = {}
    with open(path_to_file) as file:
        # log = csv.DictReader(file, ",", '"')
        reader = csv.reader(file, delimiter=",", quotechar='"')
        for row in reader:
            if row[0] not in log:
                log[row[0]] = [[row[1], row[2]]]
                print(log)
            else:
                log[row[0]].append([row[1], row[2]])
    return log

def analyze_log(path_to_file):
    
    raise NotImplementedError


# def most_requested_dish_by(client):
#     raise NotImplementedError
csv_importer("data/orders_1.csv")