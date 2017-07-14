
import jinja_env
import logging
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	logging.info("MainHandler")
    	logging.info(students.get_current_student())
        logging.info(students.create_login_url("/"))

        current_student= students.get_current_student()

        student= students.get_current_student()
        if student!= None:
            html_params["html_user"]= student.email()
        

        html_params = {
            "title": "Hampton HangOuts",
            "content": "Hello",
            "html_login_url": students.create_login_url("/"),
        }
        template = jinja_env.env.get_template('templates/tmpl.html')
        self.response.out.write(template.render(html_params))