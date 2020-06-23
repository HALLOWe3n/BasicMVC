# Created by PyCharm Professional.
# User: romandemyanchuk
# Date: 18.06.2020
# Time: 23:33
# To change this template use File | Settings | File and Code Templates.


class Controller:

    def __init__(self, model: object, view: object):
        self.model = model
        self.view = view

    def __setattr__(self, key, value):
        """
        Override
        -------
        Setting values only on inner attributes

        :param key: attribute class
        :param value: value to attribute
        :return: None
        """

        if key == 'model':
            self.__dict__[key] = value

        elif key == 'view':
            self.__dict__[key] = value

        else:
            raise AttributeError('Creating attributes outside the class is not allowed')

    def show_items(self, bullet_points: bool = False):
        items = self.model.read_items()
        item_type = self.model.item_type

        if bullet_points:
            self.view.show_bullet_point_list(item_type=item_type, items=items)
        else:
            self.view.show_number_point_list(item_type=item_type, items=items)

    def show_item(self, item_name: str):
        try:
            item = self.model.read_item(name=item_name)
            item_type = self.model.item_type
            self.view.show_item(item_type=item_type, item=item, )
        except:
            pass

