from collections.abc import Callable

from engine.inventory.item import Item
from engine.inventory.items import (
    ARMORS,
    FOOD,
    GROUPTRINKETS,
    INGREDIENTS,
    KEY,
    RECIPES,
    RELICS,
    TRINKETS,
    VALUABLES,
    WEAPONS,
)


def _get_class_values(Class: Callable) -> list[Item]:
    """
    Return a list of class attribute values of type Item.

    For example:
    ```
    class VALUABLES:
        AdamantiteOre = Item(...)
        ShinyPearl = Item(...)
        ...

    print(ItemMapper._get_class_values(VALUABLES))
    ```
    This prints: `[Adamantite Ore(VALUABLE), Shiny Pearl(VALUABLE), ...]`,
    where each value in the list is an Item.
    """
    return [v for k, v in vars(Class).items() if not k.startswith("__")]


class ItemMapper:
    """Static namespace for guid to Item mapping."""

    # Key is guid, value is the Item
    items: dict[str, Item] = {
        v.guid: v
        for v in (
            _get_class_values(VALUABLES)
            + _get_class_values(WEAPONS)
            + _get_class_values(ARMORS)
            + _get_class_values(TRINKETS)
            + _get_class_values(GROUPTRINKETS)
            + _get_class_values(FOOD)
            + _get_class_values(INGREDIENTS)
            + _get_class_values(KEY)
            + _get_class_values(RECIPES)
            + _get_class_values(RELICS)
        )
    }
