import jinja_env
import logging
import webapp2
from google.appengine.api import users




class RemindHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("RemindHandler")
        html_params = {
            "title": "My Reminders",
            "content": "Hello",
            }
    
        template = jinja_env.env.get_template('templates/remind.html')
        self.response.out.write(template.render(html_params))



    def post(self):
        logging.info("USER SAID POST")
        r_re = self.request.get("form_re")

