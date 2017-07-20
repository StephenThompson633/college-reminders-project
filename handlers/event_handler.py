import jinja_env
import logging
import webapp2
from google.appengine.api import users
from models import event

class EventHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user == None:
            self.redirect("/")
            return
        
        logging.info("EventHandler")
        html_params = {
            "title": "My Events",
            "content": "Hello",
            }

        

        user_event_query= event.EventModel.query()
        event_list= user_event_query.fetch()
        event_str= ""
        for user_event in event_list:
            event_str += "<div>"+(user_event.date)
            event_str += "<h3>"+(user_event.event)+"</h3>"
            event_str += "<p>"+(user_event.describe)+"</p>"
            event_str += "<div>"+(user_event.invite)
        html_params = {
             "html_events": event_str,
             "html_get_current_user":(users.get_current_user().email()),
             "html_login_url": users.create_login_url("/"),


        }
        template = jinja_env.env.get_template('templates/event.html')
        self.response.out.write(template.render(html_params))

    def post(self):
        logging.info("PostHandler")
        r_date=self.request.get("date")
        logging.info (r_date)
        r_event=self.request.get("event")
        logging.info(r_event)
        r_describe=self.request.get("describe")
        logging.info(r_describe)
        r_invite=self.request.get("invite")
        logging.info(r_invite)
        
        new_event= event.EventModel(
             date=r_date,
             event=r_event,
             describe=r_describe, 
             invite=r_invite,   
              )
        new_event.put()
        self.redirect("/event")
