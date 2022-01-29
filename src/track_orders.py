from .analyze_log import (
    most_requested_dish_by,
    format_order,
    never_dishes,
    never_days
)

from statistics import mode
from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []
        # self.data = format_order(self.orders)

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        return self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        data = format_order(self.orders)
        return most_requested_dish_by(data, costumer)

    def get_never_ordered_per_costumer(self, costumer):
        data = format_order(self.orders)
        return never_dishes(data, costumer)

    def get_days_never_visited_per_costumer(self, costumer):
        data = format_order(self.orders)
        return never_days(data, costumer)

    def get_busiest_day(self):
        # Agradecimentos a Denis Rossati - Turma 10 Tribo B por me mostrar o | mode |
        return mode([order[2] for order in self.orders])

    def get_least_busy_day(self):
        all_days = [order[2] for order in self.orders]
        return Counter(all_days).most_common()[-1][0]
