# Copyright 2012 splinter authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
from abc import ABC
from abc import abstractmethod
from typing import Any
from typing import Optional


class ElementAPI(ABC):
    """Specification for how a Splinter driver handles Elements.

    Any element in the page can be represented as an instance of ``ElementAPI``.

    Once you have an instance, you can easily access attributes like a ``dict``:

        >>> element = browser.find_by_id("link-logo").first
        >>> assert element['href'] == 'https://splinter.readthedocs.io'

    You can also interact with the instance using the methods and properties listed below.
    """

    def __getitem__(self, attribute: str) -> Any:
        raise NotImplementedError

    @property
    def shadow_root(self):
        """Get the shadow root of an element's shadow DOM."""
        raise NotImplementedError

    @property
    @abstractmethod
    def text(self) -> str:
        """All of the text within the element. HTML tags are stripped."""
        raise NotImplementedError

    @property
    def value(self) -> str:
        """Value of the element, usually a form element."""
        raise NotImplementedError

    @value.setter
    def value(self, new_value: str) -> None:
        raise NotImplementedError

    def click(self) -> None:
        """Click the element."""
        raise NotImplementedError

    def check(self) -> None:
        """Check the element, if it's "checkable" (e.g.: a checkbox).

        If the element is already checked, this method does nothing. For unchecking
        elements, take a loot in the :meth:`uncheck <ElementAPI.uncheck>` method.
        """
        raise NotImplementedError

    def uncheck(self) -> None:
        """Uncheck the element, if it's "checkable" (e.g.: a checkbox).

        If the element is already unchecked, this method does nothing. For checking
        elements, take a loot in the :meth:`check <ElementAPI.check>` method.
        """
        raise NotImplementedError

    @property
    def checked(self) -> bool:
        """Get the checked status of the element.

        Example:

            >>> element.check()
            >>> assert element.checked
            >>> element.uncheck()
            >>> assert not element.checked
        """
        raise NotImplementedError

    @property
    def visible(self) -> bool:
        """Get the current visibility status of the element.

        Returns:
            bool
        """
        raise NotImplementedError

    def is_visible(self, wait_time: Optional[int] = None) -> bool:
        """Check if an element is visible within the given wait time.

        Arguments:
            wait_time (int): Time in seconds to check for the element.

        Returns:
            bool
        """
        raise NotImplementedError

    def is_not_visible(self, wait_time: Optional[int] = None) -> bool:
        """Check if an element is not visible within the given wait time.

        Arguments:
            wait_time (int): Time in seconds to check for the element.

        Returns:
            bool
        """
        raise NotImplementedError

    def has_class(self, class_name: str) -> bool:
        """Indicates whether the element has the given class."""
        raise NotImplementedError

    def mouse_over(self) -> None:
        """Move the mouse over the element."""
        raise NotImplementedError

    def mouse_out(self) -> None:
        """Move the mouse away from the element."""
        raise NotImplementedError

    def clear(self) -> None:
        """Reset the field value."""
        raise NotImplementedError

    def fill(self, value: str) -> None:
        """Fill the element with text content.

        Arguments:
            value (str): Value to enter into the element.
        """
        raise NotImplementedError

    def type(self, value: str, slowly: bool = False) -> str:  # NOQA: A003
        """Type the ``value`` in the element.

        If ``slowly`` is True, this function returns an iterator which will type one character per iteration.

        It's useful to test javascript events like keyPress, keyUp, keyDown, etc.

        Example:

            >>> from selenium.webdriver.common.keys import Keys
            >>> ElementAPI.type(Keys.RETURN)

        """
        raise NotImplementedError

    def select(self, value: str, slowly: bool = False) -> None:
        """Select an ``<option>`` element in the element using the ``value`` of the ``<option>``.

        Example:

            >>> element.select("NY")
        """
        raise NotImplementedError

    def screenshot(
        self,
        name: Optional[str] = None,
        suffix: Optional[str] = None,
        full: bool = False,
        unique_file: bool = True,
    ) -> str:
        """Take a screenshot of the element."""
        raise NotImplementedError
