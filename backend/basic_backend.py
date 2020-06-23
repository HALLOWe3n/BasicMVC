# Created by PyCharm Professional.
# User: romandemyanchuk
# Date: 18.06.2020
# Time: 11:59
# To change this template use File | Settings | File and Code Templates.


from backend.mvc_exceptions import ItemAlreadyStored, ItemNotStored

items = list()


# MARK
# ----
# Create Operations
def create_items(app_items: list) -> None:
    global items
    items = app_items


def create_item(name: str, price: int, quantity: int) -> None:
    global items
    # result = list(filter(lambda x: x['name'] == name, items))
    result = [x for x in items if x['name'] == name]

    if result:
        raise ItemAlreadyStored(f'{name} already stored!')

    else:
        items.append({
            'name': name,
            'price': price,
            'quantity': quantity
        })


# MARK
# ----
# READ Operations

def read_items():
    global items
    return [item for item in items]


def read_item(name: str) -> dict:
    global items
    item = list(filter(lambda x: x['name'] == name, items))
    # item = [x for x in items if x['name'] == name]

    if item:
        return item[0]
    else:
        raise ItemNotStored(f'Can\'t read "{name}" because it\'s not stored!')


# MARK:
# ----
# UPDATE operation
def update_item(name: str, price: int, quantity: int):
    global items
    idxs_items = list(filter(lambda x: x[1]['name'] == name, enumerate(items)))

    if not idxs_items:
        raise ItemNotStored(f'Can\'t update "{name}" because it\'s not stored')

    i = idxs_items[0][0]
    items[i] = {'name': name, 'price': price, 'quantity': quantity}


# MARK:
# ----
# DELETE operation
def delete_item(name: str):
    global items
    idxs_items = list(filter(lambda x: x[1]['name'] == name, enumerate(items)))

    if not idxs_items:
        raise ItemNotStored(f'Can\'t delete "{name}" because it\'s not stored')

    i = idxs_items[0][0]
    del items[i]


# MARK:
# ----
# RUN
def main():
    my_items = [
        {'name': 'bread', 'price': 0.5, 'quantity': 20},
        {'name': 'milk', 'price': 1.0, 'quantity': 10},
        {'name': 'wine', 'price': 10.0, 'quantity': 5},
    ]

    # CREATE
    create_items(app_items=my_items)
    create_item(
        name='beer',
        price=20,
        quantity=2
    )

    # READ
    print(read_items())
    print(read_item(name='milk'))

    # UPDATE
    update_item(name='milk', price=233, quantity=33)
    print(read_items())
    # -------
    # none correct item, raise Exception
    # update_item(name='strawberry', price=16, quantity=332)

    # DELETE
    delete_item(name='milk')
    print(read_items())
    print(read_item(name='milk'))


if __name__ == '__main__':
    main()
