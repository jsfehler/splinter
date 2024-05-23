# Copyright 2012 splinter authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
from abc import ABC
from abc import abstractmethod
from typing import Any
from typing import Optional
from typing import Type

from splinter.abc import CookieManagerAPI
from splinter.element_list import ElementList


class DriverAPI(ABC):
    """The API for splinter drivers."""

    driver_name: str = ""

    @property
    def title(self) -> str:
        """Title of current page."""
        raise NotImplementedError(
            f"{self.driver_name} cannot access the title of the current page.",
        )

    @abstractmethod
    def __enter__(self) -> Any:
        """Drivers can be used as Context Managers.

        Example:

            >>> with browser('chrome') as b:
            >>>     b.find_by_id(...)
        """
        raise NotImplementedError

    @abstractmethod
    def __exit__(self, exc_type, exc_value, traceback) -> None:
        """Called when exiting a Context Manager block created by this class."""
        raise NotImplementedError

    @property
    def html(self) -> str:
        """Source of current page."""
        raise NotImplementedError

    @property
    def url(self) -> str:
        """URL of current page."""
        raise NotImplementedError(
            f"{self.driver_name} cannot access the URL of the current page.",
        )

    @abstractmethod
    def visit(self, url: str) -> None:
        """Use the browser to navigate to the given URL.

        Arguments:
            url (str): URL path.
        """
        raise NotImplementedError

    def new_tab(self, url: str) -> None:
        """The browser will navigate to the given URL in a new tab.

        Arguments:
            url (str): URL path.
        """
        raise NotImplementedError(f"{self.driver_name} can't open a new tab.")

    def back(self) -> None:
        """The browser will navigate to the previous URL in the history.

        If there is no previous URL, this method does nothing.
        """
        raise NotImplementedError(
            "%s doesn't support moving back in history." % self.driver_name,
        )

    def forward(self) -> None:
        """The browser will navigate to the next URL in the history.

        If there is no URL to forward, this method does nothing.
        """
        raise NotImplementedError(
            "%s doesn't support moving forward in history." % self.driver_name,
        )

    def reload(self) -> None:
        """Revisits the current URL."""
        raise NotImplementedError(
            "%s doesn't support reloading the page." % self.driver_name,
        )

    def get_alert(self) -> Any:
        """Change the context for working with alerts and prompts.

        For more details, check the :doc:`docs about iframes, alerts and prompts </iframes-and-alerts>`
        """
        raise NotImplementedError("%s doesn't support alerts." % self.driver_name)

    def get_iframe(self, name: Any) -> Any:
        """Change the context for working with iframes.

        For more details, check the :doc:`docs about iframes, alerts and prompts </iframes-and-alerts>`
        """
        raise NotImplementedError("%s doesn't support frames." % self.driver_name)

    def execute_script(self, script: str, *args: str) -> Any:
        """Execute a piece of JavaScript in the browser.

        Arguments:
            script (str): The piece of JavaScript to execute.

        Example:

            >>> browser.execute_script('document.getElementById("body").innerHTML = "<p>Hello world!</p>"')
        """
        raise NotImplementedError(
            "%s doesn't support execution of arbitrary JavaScript." % self.driver_name,
        )

    def evaluate_script(self, script: str, *args: str) -> Any:
        """
        Similar to :meth:`execute_script <DriverAPI.execute_script>` method.

        Execute javascript in the browser and return the value of the expression.

        Arguments:
            script (str): The piece of JavaScript to execute.

        Example:

            >>> assert 4 == browser.evaluate_script('2 + 2')
        """
        raise NotImplementedError(
            "%s doesn't support evaluation of arbitrary JavaScript." % self.driver_name,
        )

    def find_by_css(self, css_selector: str) -> ElementList:
        """
        Return an instance of :class:`ElementList <splinter.element_list.ElementList>`,
        using a CSS selector to query the current page content.

        Arguments:
            css_selector (str): CSS Selector to use in the search query.

        """
        raise NotImplementedError(
            "%s doesn't support finding elements by css selector." % self.driver_name,
        )

    def find_by_xpath(self, xpath: str) -> ElementList:
        """
        Return an instance of :class:`ElementList <splinter.element_list.ElementList>`,
        using a xpath selector to query the current page content.

        Arguments:
            xpath (str): Xpath to use in the search query.

        """
        raise NotImplementedError(
            "%s doesn't support finding elements by xpath selector." % self.driver_name,
        )

    def find_by_name(self, name: str) -> ElementList:
        """Find elements on the current page by their name.

        Return an instance of :class:`ElementList <splinter.element_list.ElementList>`.

        Arguments:
            name (str): name to use in the search query.

        """
        raise NotImplementedError(
            "%s doesn't support finding elements by name." % self.driver_name,
        )

    def find_by_id(self, id: str) -> ElementList:  # NOQA: A002
        """Find an element on the current page by its id.

        Even when only one element is find, this method returns an instance of
        :class:`ElementList <splinter.element_list.ElementList>`

        Arguments:
            id (str): id to use in the search query.
        """
        raise NotImplementedError(
            "%s doesn't support finding elements by id." % self.driver_name,
        )

    def find_by_value(self, value: str) -> ElementList:
        """Find elements on the current page by their value.

        Returns an instance of :class:`ElementList <splinter.element_list.ElementList>`

        Arguments:
            value (str): value to use in the search query.
        """
        raise NotImplementedError(
            "%s doesn't support finding elements by value." % self.driver_name,
        )

    def find_by_text(self, text: str) -> ElementList:
        """Find elements on the current page by their text.

        Returns an instance of :class:`ElementList <splinter.element_list.ElementList>`

        Arguments:
            text (str): text to use in the search query.
        """
        raise NotImplementedError(
            "%s doesn't support finding elements by text." % self.driver_name,
        )

    def find_by_tag(self, tag: str) -> ElementList:
        """Find all elements of a given tag in current page.

        Returns an instance of :class:`ElementList <splinter.element_list.ElementList>`

        Arguments:
            tag (str): tag to use in the search query.
        """
        raise NotImplementedError(
            "%s doesn't support finding elements by tag." % self.driver_name,
        )

    def find_option_by_value(self, value: str) -> ElementList:
        """
        Find ``<option>`` elements by their value.

        Returns an instance of :class:`ElementList <splinter.element_list.ElementList>`

        Arguments:
            value (str): value to use in the search query.
        """
        raise NotImplementedError(
            "%s doesn't support finding options by value." % self.driver_name,
        )

    def find_option_by_text(self, text: str) -> ElementList:
        """
        Finds ``<option>`` elements by their text.

        Returns an instance of :class:`ElementList <splinter.element_list.ElementList>`

        Arguments:
            text (str): text to use in the search query.
        """
        raise NotImplementedError(
            "%s doesn't support finding options by text." % self.driver_name,
        )

    def set_find_strategy(self, strategy):
        """Change the strategy used by browser.find().

        Arguments:
            strategy (str): The strategy used for finding elements. Can be one of either:
                'css', 'name', 'xpath'

        Returns:
            Browser: The current browser instance
        """
        raise NotImplementedError(f"{self.driver_name} doesn't support set_find_strategy()")

    def find(self, locator):
        """Find an element.

        The default strategy used is 'name'. To change the strategy, see:
        browser.set_find_strategy()

        Arguments:
            locator (str): The string used to locate an element.

        Returns:
            The found element
        """
        raise NotImplementedError(f"{self.driver_name} doesn't support find()")

    def is_text_present(self, text: str, wait_time: Optional[int] = None) -> bool:
        """Check if a piece of text is on the page.

        Arguments:
            text (str): text to use in the search query.
            wait_time (int): Number of seconds to search for the text.

        Returns:
            bool: True if finds a match for the ``text`` and False if not.
        """
        raise NotImplementedError(
            "%s doesn't support checking if some text is present in the html. " % self.driver_name,
        )

    def type(self, name: str, value: str, slowly: bool = False) -> str:  # NOQA: A003
        """Type a value into an element.

        It's useful to test javascript events like keyPress, keyUp, keyDown, etc.

        Arguments:
            name (str): name of the element to enter text into.
            value (str): Value to enter into the element.
            slowly (bool): If True, this function returns an iterator which will type one character per iteration.
        """
        raise NotImplementedError(
            "%s doesn't support typing on fields by name." % self.driver_name,
        )

    def fill(self, name: str, value: str) -> None:
        """Fill the field identified by ``name`` with the content specified by ``value``.

        Arguments:
            name (str): name of the element to enter text into.
            value (str): Value to enter into the element.
        """
        raise NotImplementedError(
            "%s doesn't support filling fields by name." % self.driver_name,
        )

    def fill_form(
        self,
        field_values,
        form_id: Optional[str] = None,
        name: Optional[str] = None,
    ) -> None:
        """
        Fill the fields identified by ``name`` with the content specified by ``value`` in a dict.

        Currently, fill_form supports the following fields: text, password, textarea, checkbox,
        radio and select.

        Checkboxes should be specified as a boolean in the dict.

        Arguments:
            field_values (dict): Values for all the fields in the form, in the pattern of {field name: field value}
            form_id (str): Id of the form to fill. Can be used instead of name.
            name (str): Name of the form to fill.
            ignore_missing (bool): Ignore missing keys in the dict.
        """
        raise NotImplementedError(
            "%s doesn't support filling forms with a dict." % self.driver_name,
        )

    def choose(self, name: str, value: str) -> None:
        """Choose a value in a radio buttons group.

        Arguments:
            name (str): name of the element to enter text into.
            value (str): Value to choose.

        Example:

            You have two radio buttons in a page, with the name ``gender`` and values 'F' and 'M'.

            >>> browser.choose('gender', 'F')

            Then the female gender will be chosen.
        """
        raise NotImplementedError(
            "%s doesn't support choosing options." % self.driver_name,
        )

    def check(self, name: str) -> None:
        """Check a checkbox by its name.

        Arguments:
            name (str): name of the element to check.

        Example:

            >>> browser.check("agree-with-terms")

        If you call ``browser.check`` n times, the checkbox keeps checked, it never get unchecked.

        To uncheck a checkbox, take a look in the :meth:`uncheck <DriverAPI.uncheck>` method.
        """
        raise NotImplementedError(
            "%s doesn't support checking elements." % self.driver_name,
        )

    def uncheck(self, name: str) -> None:
        """Uncheck a checkbox by its name.

        Arguments:
            name (str): name of the element to uncheck.

        Example:

            >>> browser.uncheck("send-me-emails")

        If you call ``brower.uncheck`` n times, the checkbox keeps unchecked, it never get checked.

        To check a checkbox, take a look in the :meth:`check <DriverAPI.check>` method.
        """
        raise NotImplementedError(
            "%s doesn't support unchecking elements." % self.driver_name,
        )

    def select(self, name: str, value: str) -> None:
        """
        Select an ``<option>`` element in an ``<select>`` element using the ``name`` of the ``<select>`` and
        the ``value`` of the ``<option>``.

        Arguments:
            name (str): name of the option element.
            value (str): Value to select.

        Example:

            >>> browser.select("state", "NY")
        """
        raise NotImplementedError(
            "%s doesn't support selecting options in 'select' element." % self.driver_name,
        )

    def quit(self) -> None:  # NOQA: A003
        """Quit the browser, closing its windows (if it has one)."""
        raise NotImplementedError("%s doesn't support quit" % self.driver_name)

    def is_element_present_by_css(
        self,
        css_selector: str,
        wait_time: Optional[int] = None,
    ) -> bool:
        """Verify if an element is present in the current page.

        Arguments:
            css (str): css selector for the element.
            wait_time (int): Number of seconds to search.

        Returns:
            bool: True if the element is present and False if is not present.
        """
        raise NotImplementedError(
            "%s doesn't support verifying if element is present by css" % self.driver_name,
        )

    def is_element_not_present_by_css(
        self,
        css_selector: str,
        wait_time: Optional[int] = None,
    ) -> bool:
        """Verify if an element is not present in the current page.

        Arguments:
            css (str): css selector for the element.
            wait_time (int): Number of seconds to search.

        Returns:
            bool: True if the element is not present and False if is present.
        """
        raise NotImplementedError(
            "%s doesn't support verifying if element is not present by css" % self.driver_name,
        )

    def is_element_present_by_xpath(
        self,
        xpath: str,
        wait_time: Optional[int] = None,
    ) -> bool:
        """Verify if an element is present in the current page.

        Arguments:
            xpath (str): xpath of the element.
            wait_time (int): Number of seconds to search.

        Returns:
            bool: True if the element is present and False if is not present.
        """
        raise NotImplementedError(
            "%s doesn't support verifying if element is present by xpath" % self.driver_name,
        )

    def is_element_not_present_by_xpath(
        self,
        xpath: str,
        wait_time: Optional[int] = None,
    ) -> bool:
        """Verify if an element is not present in the current page.

        Arguments:
            xpath (str): xpath of the element.
            wait_time (int): Number of seconds to search.

        Returns:
            bool: True if the element is not present and False if is present.
        """
        raise NotImplementedError(
            "%s doesn't support verifying if element is not present by xpath" % self.driver_name,
        )

    def is_element_present_by_tag(
        self,
        tag: str,
        wait_time: Optional[int] = None,
    ) -> bool:
        """Verify if an element is present in the current page.

        Arguments:
            tag (str): tag of the element.
            wait_time (int): Number of seconds to search.

        Returns:
            bool: True if the element is present and False if is not present.
        """
        raise NotImplementedError(
            "%s doesn't support verifying if element is present by tag" % self.driver_name,
        )

    def is_element_not_present_by_tag(
        self,
        tag: str,
        wait_time: Optional[int] = None,
    ) -> bool:
        """Verify if an element is not present in the current page.

        Arguments:
            tag (str): tag of the element.
            wait_time (int): Number of seconds to search.

        Returns:
            bool: True if the element is not present and False if is present.
        """
        raise NotImplementedError(
            "%s doesn't support verifying if element is not present by tag" % self.driver_name,
        )

    def is_element_present_by_name(
        self,
        name: str,
        wait_time: Optional[int] = None,
    ) -> bool:
        """Verify if an element is present in the current page.

        Arguments:
            name (str): name of the element.
            wait_time (int): Number of seconds to search.

        Returns:
            bool: True if the element is present and False if is not present.
        """
        raise NotImplementedError(
            "%s doesn't support verifying if element is present by name" % self.driver_name,
        )

    def is_element_not_present_by_name(
        self,
        name: str,
        wait_time: Optional[int] = None,
    ) -> bool:
        """Verify if an element is not present in the current page.

        Arguments:
            name (str): name of the element.
            wait_time (int): Number of seconds to search.

        Returns:
            bool: True if the element is not present and False if is present.
        """
        raise NotImplementedError(
            "%s doesn't support verifying if element is not present by name" % self.driver_name,
        )

    def is_element_present_by_value(
        self,
        value: str,
        wait_time: Optional[int] = None,
    ) -> bool:
        """Verify if an element is present in the current page.

        Arguments:
            value (str): value in the element.
            wait_time (int): Number of seconds to search.

        Returns:
            bool: True if the element is present and False if is not present.
        """
        raise NotImplementedError(
            "%s doesn't support verifying if element is present by value" % self.driver_name,
        )

    def is_element_not_present_by_value(
        self,
        value: str,
        wait_time: Optional[int] = None,
    ) -> bool:
        """Verify if an element is not present in the current page.

        Arguments:
            value (str): value in the element.
            wait_time (int): Number of seconds to search.

        Returns:
            bool: True if the element is not present and False if is present.
        """
        raise NotImplementedError(
            "%s doesn't support verifying if element is not present by value" % self.driver_name,
        )

    def is_element_present_by_text(
        self,
        text: str,
        wait_time: Optional[int] = None,
    ) -> bool:
        """Verify if an element is present in the current page.

        Arguments:
            text (str): text in the element.
            wait_time (int): Number of seconds to search.

        Returns:
            bool: True if the element is present and False if is not present.
        """
        raise NotImplementedError(
            "%s doesn't support verifying if element is present by text" % self.driver_name,
        )

    def is_element_not_present_by_text(
        self,
        text: str,
        wait_time: Optional[int] = None,
    ) -> bool:
        """Verify if an element is not present in the current page.

        Arguments:
            text (str): text in the element.
            wait_time (int): Number of seconds to search.

        Returns:
            bool: True if the element is not present and False if is present.
        """
        raise NotImplementedError(
            "%s doesn't support verifying if element is not present by text" % self.driver_name,
        )

    def is_element_present_by_id(
        self,
        id: str,  # NOQA: A002
        wait_time: Optional[int] = None,
    ) -> bool:
        """Verify if an element is present in the current page.

        Arguments:
            id (str): id for the element.
            wait_time (int): Number of seconds to search.

        Returns:
            bool: True if the element is present and False if is not present.
        """
        raise NotImplementedError(
            "%s doesn't support verifying if element is present by id" % self.driver_name,
        )

    def is_element_not_present_by_id(
        self,
        id: str,  # NOQA: A002
        wait_time: Optional[int] = None,
    ) -> bool:
        """Verify if an element is not present in the current page.

        Arguments:
            id (str): id for the element.
            wait_time (int): Number of seconds to search.

        Returns:
            bool: True if the element is not present and False if is present.
        """
        raise NotImplementedError(
            "%s doesn't support verifying if element is not present by id" % self.driver_name,
        )

    def screenshot(
        self,
        name: Optional[str] = None,
        suffix: Optional[str] = None,
        full: bool = False,
        unique_file: bool = True,
    ) -> str:
        """Take a screenshot of the current page and save it locally.

        Arguments:
            name (str): File name for the screenshot.
            suffix (str): File extension for the screenshot.
            full (bool): If the screenshot should be full screen or not.
            unique_file (bool): If true, the filename will include a path to
                the system temp directory and extra characters at the end to
                ensure the file is unique.

        Returns:
            str: Full file name of the created screenshot.
        """
        raise NotImplementedError(
            "%s doesn't support taking screenshots." % self.driver_name,
        )

    def html_snapshot(
        self,
        name: str = "",
        suffix: str = ".html",
        encoding: str = "utf-8",
        unique_file: bool = True,
    ) -> str:
        """Write the current html to a file.

        Arguments:
            name (str): File name.
            suffix (str): File extension.
            encoding (str): File encoding.
            unique_file (str): If true, the filename will include a path to
                the system temp directory and extra characters at the end to
                ensure the file is unique.

        Returns:
            str: Full file name of the created html snapshot.
        """

        raise NotImplementedError(
            f"{self.driver_name} doesn't support taking screenshots.",
        )

    @property
    def cookies(self) -> Type[CookieManagerAPI]:
        """
        A :class:`CookieManager <splinter.cookie_manager.CookieManagerAPI>` instance.

        For more details, check the :doc:`cookies manipulation section </cookies>`.
        """
        raise NotImplementedError(
            "%s doesn't support cookies manipulation" % self.driver_name,
        )
