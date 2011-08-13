# -*- coding: utf-8 -*-:
"""
This module contains the basic API for splinter drivers and elemnts.
"""

from splinter.element_list import ElementList
from splinter.request_handler.request_handler import RequestHandler


class DriverAPI(RequestHandler):
    """
    Basic driver API class.
    """

    @property
    def title(self):
        """
        Title of current page.
        """
        raise NotImplementedError

    @property
    def html(self):
        """
        Source of current page.
        """
        raise NotImplementedError

    @property
    def url(self):
        """
        URL of current page.
        """
        raise NotImplementedError

    def visit(self, url):
        """
        Visits a given URL.

        The ``url`` parameter is a string.
        """
        raise NotImplementedError

    def back(self):
        """
        Back to the last URL in the browsing history.

        If there is no URL to back, this method does nothing.
        """
        raise NotImplementedError

    def forward(self):
        """
        Forward to the next URL in the browsing history.

        If there is no URL to forward, this method does nothing.
        """
        raise NotImplementedError

    def reload(self):
        """
        Revisits the current URL
        """
        raise NotImplementedError

    def get_alert(self):
        raise NotImplementedError

    def get_iframe(self, id):
        raise NotImplementedError

    def execute_script(self, script):
        """
        Executes a given JavaScript in the browser.

        e.g.: ::
            >>> browser.execute_script('document.getElementById("body").innerHTML = "<p>Hello world!</p>"')
        """
        raise NotImplementedError

    def evaluate_script(self, script):
        """
        Similar to :meth:`DriverAPI.execute_script`.

        Executes javascript in the browser and returns the value of the expression.

        e.g.: ::
            >>> assert 4 == browser.evaluate_script('2 + 2')
        """
        raise NotImplementedError

    def find_by_css(self, css_selector):
        """
        Returns an instance of :class:`ElementList <splinter.element_list.ElementList>`, using a CSS selector to query the
        current page content.
        """
        raise NotImplementedError

    find_by_css_selector = find_by_css

    def find_by_xpath(self, xpath):
        """
        Returns an instance of :class:`ElementList <splinter.element_list.ElementList>`, using a xpath selector to query the
        current page content.
        """
        raise NotImplementedError

    def find_by_name(self, name):
        """
        Finds elements in current page by them name.

        Returns an instance of :class:`ElementList <splinter.element_list.ElementList>`.
        """
        raise NotImplementedError

    def find_by_id(self, id):
        """
        Finds an element in current page by its id.

        Even when only one element is find, this method returns an instance of :class:`ElementList <splinter.element_list.ElementList>`
        """
        raise NotImplementedError

    def find_by_value(self, value):
        """
        Finds elements in current page by them value.

        Returns an instance of :class:`ElementList <splinter.element_list.ElementList>`
        """
        raise NotImplementedError

    def find_by_tag(self, tag):
        """
        Find all elements of a given tag in current page.

        Returns an instance of :class:`ElementList <splinter.element_list.ElementList>`
        """
        raise NotImplementedError

    def find_link_by_href(self, href):
        """
        Find all elements of a given tag in current page.

        Returns an instance of :class:`ElementList <splinter.element_list.ElementList>`
        """
        raise NotImplementedError

    def find_link_by_partial_href(self, partial_href):
        """
        Find links by looking for a partial ``str`` in them href attribute.

        Returns an instance of :class:`ElementList <splinter.element_list.ElementList>`
        """
        raise NotImplementedError

    def find_link_by_text(self, text):
        """
        Find links querying for they text.

        Returns an instance of :class:`ElementList <splinter.element_list.ElementList>`
        """
        raise NotImplementedError

    def find_link_by_partial_text(self, partial_text):
        """
        Find links by looking for a partial ``str`` in them text.

        Returns an instance of :class:`ElementList <splinter.element_list.ElementList>`
        """
        raise NotImplementedError

    def find_option_by_value(self, value):
        """
        Finds ``<option>`` elements by them value.

        Returns an instance of :class:`ElementList <splinter.element_list.ElementList>`
        """
        raise NotImplementedError

    def find_option_by_text(self, text):
        """
        Finds ``<option>`` elements by them text.

        Returns an instance of :class:`ElementList <splinter.element_list.ElementList>`
        """
        raise NotImplementedError

    def wait_for_element(self, selector, timeout, interval):
        """
        Waits for an element to appear in the page.

        Receives the ``selector`` of the element, a ``timeout`` and an ``interval``.
        """
        raise NotImplementedError

    def type(self, name, value, slowly=False):
        """
        Types the ``value`` in the field identified by ``name``.

        It's useful to test javascript events like keyPress, keyUp, keyDown, etc.
        """
        raise NotImplementedError

    def fill(self, name, value):
        """
        Fill the field identified by ``name`` with the content specified by ``value``.
        """
        raise NotImplementedError

    fill_in = fill
    attach_file = fill

    def choose(self, name, value):
        raise NotImplementedError

    def check(self, name):
        raise NotImplementedError

    def uncheck(self, name):
        raise NotImplementedError

    def select(self, name, value):
        raise NotImplementedError

    def click_link_by_href(self, href):
        return self.find_link_by_href(href).first.click()

    def click_link_by_partial_href(self, partial_href):
        return self.find_link_by_partial_href(partial_href).first.click()

    def click_link_by_text(self, text):
        return self.find_link_by_text(text).first.click()

    def click_link_by_partial_text(self, partial_text):
        return self.find_link_by_partial_text(partial_text).first.click()

    def within(self, context):
        return ElementList([], context, self)

    def quit(self):
        raise NotImplementedError

    def is_element_present(self, finder, selector, wait_time=None):
        raise NotImplementedError

    @property
    def cookies(self):
        raise NotImplementedError


class ElementAPI(object):

    def _get_value(self):
        raise NotImplementedError

    def _set_value(self, value):
        raise NotImplementedError

    value = property(_get_value, _set_value)

    def click(self):
        raise NotImplementedError

    def check(self):
        raise NotImplementedError

    def uncheck(self):
        raise NotImplementedError

    def mouseover(self):
        raise NotImplementedError

    @property
    def checked(self):
        raise NotImplementedError

    @property
    def visible(self):
        raise NotImplementedError

    def __getitem__(self, attribute):
        raise NotImplementedError

