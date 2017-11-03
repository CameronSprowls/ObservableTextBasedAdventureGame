"""
Basic observer class to observe an observable service.
Using python's Abstract Base Class to create an abstract class

Heavily based off of www.giantflyingsaucer.com/blog/?p=5117
'10 minute guide to the observer pattern'
"""

from abc import ABCMeta, abstractmethod


class Observer(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, *args, **kwargs):
        pass
