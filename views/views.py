# Created by PyCharm Professional.
# User: romandemyanchuk
# Date: 18.06.2020
# Time: 22:29
# To change this template use File | Settings | File and Code Templates.


class ViewBasic:
    """
    Basic Viewer class for realise model-view-controller pattern
    """

    def __setattr__(self, key, value):
        """
        Ban on setting attributes
        """
        raise AttributeError

    @staticmethod
    def show_bullet_point_list(item_type: str, items: list) -> None:
        print(f'--- {item_type.upper()} LIST ---')
        for item in items:
            print(f'* {item}')

    @staticmethod
    def show_number_point_list(item_type: str, items: list) -> None:
        print(f'--- {item_type.upper()} LIST ---')
        for i, item in enumerate(items):
            print(f'{i + 1} {item}')

    @staticmethod
    def show_item(item_type: str, item: str, item_info: str) -> None:
        print('//////////////////////////////////////////////////////////////')
        print(f'Good news, we have some {item.upper()}!')
        print(f'{item_type.upper()} INFO: {item_info}')
        print('//////////////////////////////////////////////////////////////')

    @staticmethod
    def display_missing_item_error(item: str, err) -> None:
        print('**************************************************************')
        print(f'We are sorry, we have no {item.upper()}!')
        print(f'{err.args[0]}')
        print('**************************************************************')

    @staticmethod
    def display_item_not_yet_stored_error(item: str, item_type: str, err: Exception) -> None:
        print('**************************************************************')
        print(f'We don\'t have any {item.upper()} in our {item_type} list. Please insert it first!')
        print(f'{err.args[0]}')
        print('**************************************************************')

    @staticmethod
    def display_item_stored(item: str, item_type: str) -> None:
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print(f'Hooray! We have just added some {item.upper()} to our {item_type} list!')
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

    @staticmethod
    def display_change_item_type(older, newer) -> None:
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')
        print(f'Change item type from "{older}" to "{newer}"')
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')

    @staticmethod
    def display_item_updated(item, o_price, o_quantity, n_price, n_quantity) -> None:
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')
        print(f'Change {item} price: {o_price} --> {n_price}')
        print(f'Change {item} quantity: {o_quantity} --> {n_quantity}')
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')

    @staticmethod
    def display_item_deletion(name: str) -> None:
        print('--------------------------------------------------------------')
        print(f'We have just removed {name} from our list')
        print('--------------------------------------------------------------')