from db import select_data, add_data_article, update_data, get_data, delete_data
import datetime


class Article:

    def __init__(self):
        self.article_for_learning_list = None
        self.counter = 0
        self.max_counter = None
        self.data = None
        self.get_data = None

    def load_from_db(self):
        self.data = select_data(table='article')
        self.max_counter = len(self.data) - 1
        self.counter = 0
        return self.data

    def get_next(self, field_of_knowledge):
        if self.data is None:
            return None
        while self.counter < self.max_counter:
            self.counter += 1
            if self.data[self.counter][2] == field_of_knowledge:
                return self.data[self.counter]
        if self.data[self.counter][2] == field_of_knowledge and self.counter == self.max_counter:
            return self.data[self.counter]
        while self.counter >= 0:
            self.counter -= 1
            if self.data[self.counter][2] == field_of_knowledge:
                return self.data[self.counter]
        return None

    def get_prev(self, field_of_knowledge):
        if self.data is None:
            return None
        while self.counter > 0:
            self.counter -= 1
            if self.data[self.counter][2] == field_of_knowledge:
                return self.data[self.counter]
        if self.counter == 0:
            if self.data[self.counter][2] == field_of_knowledge:
                return self.data[self.counter]
            while self.counter < self.max_counter:
                self.counter += 1
                if self.data[self.counter][2] == field_of_knowledge:
                    return self.data[self.counter]
        return None

    def get_first(self, field_of_knowledge):
        if self.data is None:
            return None
        for i in self.data:
            if i[2] == field_of_knowledge:
                return i
        return None

    def get_current(self):
        if self.data is None:
            return None
        return self.data[self.counter]

    def get_from_db(self, condition):
        self.get_data = None
        self.get_data = get_data(table='article', condition=condition)
        return self.get_data

    def add_to_db(self, value):
        result = add_data_article(table='article', value=value)
        return result

    def update_in_db(self, request_dict, condition):
        result = update_data(table='article', request_dict=request_dict, condition=condition)
        return result

    def delete_from_db(self, condition):
        result = delete_data('article', condition)
        return result

    def article_for_learning(self):
        user_data = select_data(table='user')
        data = self.load_from_db()
        self.article_for_learning_list = []
        index = []
        for i in user_data:
            if datetime.datetime.strptime(i[3], "%Y-%m-%d %H:%M:%S.%f") < datetime.datetime.now():
                if i[2] < 6:
                    index.append(i[1])
        for i in index:
            for y in data:
                if i == y[0]:
                    self.article_for_learning_list.append(y)
        return self.article_for_learning_list
