import jinja_env
import logging
import webapp2
from google.appengine.api import users
from models import reminders


class RemindHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("RemindHandler")
        html_params = {
            "title": "My Reminders",
            "content": "Hello",
            }
            #last spot
        users_comments_query= reminders.RemindersModel.query()
        comments_list= users_comments_query.fetch()
        comments_str= ""
        for users_comments in comments_list:
            comments_str +="<div>"
            comments_str+= "<h3>"+users_comments.date + "</h3>"
            comments_str += "<p>"+ (users_comments.content) + "</p>"
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





