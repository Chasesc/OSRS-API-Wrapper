import json

from pathlib import Path
from . import const


class Item(object):
    _items = {}
    _name_to_id = {}

    def __init__(self, id, name, description, is_mem, type, type_icon, price_info):
        self.id = id
        self.name = name
        self.description = description
        self.is_mem = is_mem
        self.type = type
        self.type_icon = type_icon
        self.price_info = price_info

        self.icon = const.GE_ICON + str(self.id)
        self.large_icon = const.GE_LARGE_ICON + str(self.id)

    def price(self):
        return self.price_info.price()

    @staticmethod
    def id_to_name(id):
        if not Item._items:
            Item._load_data()

        try:
            return Item._items[str(id)]["name"]
        except KeyError:
            return None

    @staticmethod
    def get_ids(name):
        if not Item._items:
            Item._load_data()

        try:
            return Item._name_to_id[name.lower()]
        except KeyError:
            matches = []
            for item in Item._name_to_id:
                if name in item:
                    matches.append(Item._name_to_id[item])

            return matches

    @staticmethod
    def _load_data():
        with open(Path(__file__).parent / "items_osrs.json") as file:
            Item._items = json.load(file)
            for id in Item._items:
                n = Item._items[id]["name"].lower()
                tradeable = Item._items[id]["tradeable"]

                if tradeable:
                    Item._name_to_id[n] = int(id)


def main():
    print(Item.get_ids("abyssal whip"))  # exact match
    print(Item.get_ids("abyssal"))  # returns a list of items that contain 'abyssal'
    print(Item.get_ids("rune axe"))  # exact match


if __name__ == "__main__":
    main()
