# Created by PyCharm Professional.
# User: romandemyanchuk
# Date: 18.06.2020
# Time: 21:30
# To change this template use File | Settings | File and Code Templates.

from backend import basic_backend
from backend.mvc_exceptions import ItemAlreadyStored, ItemNotStored


class ModelBasic:
    """
    Basic Model for realise model-view-controller pattern
    ___
    Business logic class
    """

    def __init__(self, application_items: list):
        self._item_type: str = 'products'
        self.create_items(application_items)

    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def change_type(self, new_item_type: str):
        self._item_type = new_item_type

    def __setattr__(self, key, value):
        """
        Override
        -------
        Setting values only on inner attributes

        :param key: attribute class
        :param value: value to attribute
        :return: None
        """
        if key == '_item_type':
            self.__dict__[key] = value
        else:
            raise AttributeError('Creating attributes outside the class is not allowed')

    def create_item(self, name: str, price: int, quantity: int):
        basic_backend.create_item(name=name, price=price, quantity=quantity)

    def create_items(self, app_items: list):
        basic_backend.create_items(app_items=app_items)

    def read_item(self, name: str) -> dict:
        return basic_backend.read_item(name=name)

    def read_items(self) -> list:
        return basic_backend.read_items()

    def update_item(self, name: str, price: int, quantity: int):
        basic_backend.update_item(name=name, price=price, quantity=quantity)

    def delete_item(self, name: str):
        basic_backend.delete_item(name=name)
