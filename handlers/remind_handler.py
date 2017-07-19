import jinja_env
import logging
import webapp2
from google.appengine.api import users
from models import reminders
from google.appengine.ext import ndb




class RemindHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("RemindHandler")
        html_params = {
            "title": "My Reminders",
            "content": "Hello",
            }
            #last spot
        user_reminder_query= reminders.RemindersModel.query()
        comments_list= user_reminder_query.fetch()
        comments_str= ""
        for user_reminder in comments_list:
            comments_str +="<div>"
            comments_str+= "<h3>"+user_reminder.date + "</h3>"
            comments_str += "<p>"+ (user_reminder.content) + "</p>"
            comments_str+="<input type= 'checkbox' name= 'delete' value= '"+str(user_reminder.key.urlsafe())+"'></input>"
            comments_str += "<div>"


        html_params = {
            "html_comments":comments_str,
        }

        template = jinja_env.env.get_template('templates/remind.html')
        self.response.out.write(template.render(html_params))

    def post(self):
        r_date= self.request.get("date")
        r_reminder=self.request.get("form_reminder")

        new_reminders= reminders.RemindersModel(
            date=r_date,
            content=r_reminder,
            )
        new_reminders.put()
        self.redirect("/remind")



    # def post(self):
    #     logging.info("USER SAID POST")
    #     r_email = self.request.get("form_email")
    #     r_contet= self.requeest.get("form_content")
    #     r_date= self.request.get("form_date")
    #     r_time= self.request.get("form_time")


    #     new_reminders= reminders.RemindersModel(
    #         email= r_email,
    #         content= r_contet,
    #         date= r_date,
    #         time= r_time,
    #         )
    def post(self):
        r_delete= self.request.get("delete")
        r_deletekey= ndb.Key(urlsafe=r_delete)
        r_deletekey.delete()





