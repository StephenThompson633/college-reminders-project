import jinja_env
import logging
import webapp2
from google.appengine.api import users

class RemindHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("MapHandler")
        html_params = {
            "title": "My Reminders",
            "content": "Hello",
            }

        template = jinja_env.env.get_template('templates/map.html')
        self.response.out.write(template.render(html_params))