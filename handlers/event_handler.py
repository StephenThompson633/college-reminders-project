import jinja_env
import logging
import webapp2
from google.appengine.api import users
from models import event

class EventHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("EventHandler")
        html_params = {
            "title": "My Reminders",
            "content": "Hello",
            }

        template = jinja_env.env.get_template('templates/event.html')
        self.response.out.write(template.render(html_params))


        # user_event_query= event.Event.query()
        # comment_list= user_event_query.fetch()
        # comment_str= ""
        # for user_event in comment_list:
        #     comment_str +=""
        #     comment_str+= 
        #     comment_str += 
        #     comment_str += 


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
