import jinja_env
import logging
import webapp2
from google.appengine.api import users

class EventHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("EventHandler")
        html_params = {
            "title": "My Reminders",
            "content": "Hello",
            }

        template = jinja_env.env.get_template('templates/event.html')
        self.response.out.write(template.render(html_params))