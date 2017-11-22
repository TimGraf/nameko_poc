""" Nameko POC """
import os

from nameko.events import EventDispatcher, event_handler
from nameko.web.handlers import http

class Publisher:
    """ Event dispatching service. """
    name = "publisher"
    dispatch = EventDispatcher()

    @http('POST', '/stuff')
    def do_post(self, request):
        payload = request.get_data(as_text=True)
        self.dispatch("stuff_happened", payload)
        return u"received: {}".format(payload)


class Consumer:
    """ Event listening service. """
    name = "consumer"

    @event_handler("publisher", "stuff_happened")
    def handle_event(self, payload):
        print("Consumer (Instance: %s) received: %s" % (os.getpid(), payload))



class ExtraSpecialConsumer:
    """ Event listening service. """
    name = "extra-special-consumer"

    @event_handler("publisher", "stuff_happened")
    def handle_event(self, payload):
        print("Extra Special Consumer (Instance: %s) received: %s" % (os.getpid(), payload))
