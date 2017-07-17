
import jinja_env
import logging
import webapp2



from google.appengine.api import users



class MainHandler(webapp2.RequestHandler):
    def get(self):

#how to get login from the user
        student = users.get_current_user()

        if student!= None:
            html_params["html_user"]= student.email()
        logging.info("MainHandler")
        logging.info(student)
    def get(self):
        

       
        html_params = {
            "title": "Hampton HangOuts",
            "content": "Hello",
            "html_login_url": users.create_login_url("/"),
        }
        template = jinja_env.env.get_template('templates/tmpl.html')
        self.response.out.write(template.render(html_params))