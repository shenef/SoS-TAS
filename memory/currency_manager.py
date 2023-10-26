import logging
from typing import Self

from memory.core import mem_handle

logger = logging.getLogger(__name__)


class CurrencyManager:
    """Memory manager than handles money."""

    def __init__(self: Self) -> None:
        """Initialize a new CurrencyManager object."""
        self.memory = mem_handle()
        self.base = None
        self.money = 0

    def update(self: Self) -> None:
        if self.memory.ready_for_updates:
            try:
                if self.base is None:
                    singleton_ptr = self.memory.get_singleton_by_class_name("CurrencyManager")
                    if singleton_ptr is None:
                        return

                    self.base = self.memory.get_class_base(singleton_ptr)
                    if self.base == 0x0:
                        return
                    pass

                else:
                    self._read_currencies()
                    pass
            except Exception as _e:
                logger.debug(f"CurrencyManager Reloading {type(_e)}")
                self.__init__()

    def _read_currencies(self: Self) -> None:
        """
        Read the currencies from the inventory manager.

        Only one currency actually exists, but the manager has a list of currencies.

        For now, just check the first one.
        """
        if self.memory.ready_for_updates:
            try:
                # currencyQuantities -> _entries + 0x20 for first entry
                ptr = self.memory.follow_pointer(self.base, [0x28, 0x18, 0x0])
                if ptr:
                    self.money = self.memory.read_int(ptr + 0x30)

            except Exception:
                self.money = 0


_currency_manager_mem = CurrencyManager()


def currency_manager_handle() -> CurrencyManager:
    """Return a handle to the currency manager."""
    return _currency_manager_mem
