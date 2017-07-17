import jinja_env
import logging
import webapp2
from google.appengine.api import users

template = jinja_env.env.get_template('templates/remind.html')
self.response.out.write(template.render(html_params))



class RemindHandler(webapp2.RequestHandler):
	def get(self):
		logging.info("RemindHandler")
		html_params = {
			"title": "My Reminders",
			"content": "Hello",
			}


	def post(self):
		logging.info("USER SAID POST")
		r_email = self.request.get("form_email")
		r_contet= self.requeest.get("form_content")
		r_date= self.request.get("form_date")
		r_time= self.request.get("form_time")


		new_reminders= reminders.RemindersModel(
			email= r_email,
			content= r_contet,
			date= r_date,
			time= r_time,

			)
		new_reminders.put()
		self.redirect('/remind')
