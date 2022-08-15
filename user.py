from db import select_data, add_data_user, get_data, update_data, delete_data


class User:

    def __init__(self):
        self.data = None
        self.get_data = None
        self.load_from_db()

    def load_from_db(self):
        self.data = select_data(table='user')

    def add_to_db(self, value):
        add_data_user(table='user', value=value)

    def get_from_db(self, condition):
        self.get_data = None
        self.get_data = get_data(table='user', condition=('article_id', condition))
        return self.get_data

    def update_in_db(self, request_dict, condition):
        result = update_data(table='user', request_dict=request_dict, condition=condition)
        return result

    def delete_from_db(self, condition):
        result = delete_data(table='user', condition=condition)
        return result


