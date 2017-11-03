"""
Basic Observable class for observer to observe

Heavily based off of www.giantflyingsaucer.com/blog/?p=5117
'10 minute guide to the observer pattern'
"""


class Observable(object):

    def __init__(self):
        self.observers = []

    def sub(self, observer):
        """
        Make observer subscribe to this observer service
        :param observer: Observer to become subscribed
        """
        if observer not in self.observers:
            self.observers.append(observer)

    def unsub(self, observer):
        """
        Make observer unsubscribe from this observer service
        :param observer: Observer to become unsubcribed
        """
        if observer in self.observers:
            self.observers.remove(observer)

    def unsub_all(self):
        """
        Removes all subscribers from this service
        """
        if self.observers:
            del self.observers[:]

    def update_observers(self, *args, **kwargs):
        """
        Notifies all subscribers in the service
        :param args: list of arguments to pass to observers of this service
        :param kwargs: dictionary of arguments to pass to observers of this service
        """
        for observer in self.observers:
            observer.update(*args, **kwargs)
