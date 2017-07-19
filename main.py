import os
import webapp2
import logging

from handlers import jinja_env
from handlers import main_handler
from handlers import form_handler
from handlers import remind_handler
from handlers import map_handler
from handlers import event_handler

jinja_env.init(os.path.dirname(__file__))





app = webapp2.WSGIApplication([
    ('/', main_handler.MainHandler),
    ('/QA', form_handler.FormHandler),
    ('/remind', remind_handler.RemindHandler),
    ('/map', map_handler.MapHandler),
    ('/event', event_handler.EventHandler),

], debug=True)
