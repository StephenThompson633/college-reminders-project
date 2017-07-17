import os
import webapp2
import logging

from handlers import jinja_env
from handlers import main_handler
from handlers import form_handler

jinja_env.init(os.path.dirname(__file__))





app = webapp2.WSGIApplication([
    ('/', main_handler.MainHandler),
    ('/QA', form_handler.FormHandler),
], debug=True)
