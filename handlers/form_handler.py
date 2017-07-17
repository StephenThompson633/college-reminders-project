
import jinja_env
import logging
import webapp2
from models import comment
from google.appengine.api import users

class FormHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("SecondHandler")
        
        # do stuff with books...
       
       


        user_comment_query= comment.Comment.query()
        comment_list= user_comment_query.fetch()
        comment_str= ""
        for user_comment in comment_list:
            comment_str +="<div>"
            comment_str+= "<h3>"+user_comment.author + "</h3>"
            comment_str += "<p>"+ (user_comment.contents) + "</p>"
            comment_str += "<div>"


        html_params = {
            "html_comments":(comment_str)
        }
        template = jinja_env.env.get_template('templates/form.html')
       
        self.response.out.write(template.render(html_params))



        # logging.info(users.get_current_user())
        # logging.info(users.create_login_url("/Q&A"))

        # current_user= users.get_current_user()
        # user_comment_query= comment.Comment.query()
        # user_comment= user_comment_query.fetch()
        # logging.info(len(user_comments))
        # comments = Comment.query().fetch()

        # comment_str= ""
        # for comment in comments:
        #     comment_str +="<div>"
        #     comment_str+= "<h3>"+comment.author + "</h3>"
        #     comment_str += "<p>"+ (comment.contents) + "</p>"
        #     comment_str += "<div>"
        # template=jinja_env.get_template("templates/form.html")

        # henry = {
        # "html_comments": comment_str,
        # "html_login_url": users.create_login_url("/Q&A"),
        # "html_get_current_user": users.get_current_user()
        # }
        # if current_user != None:
        #  henry["html_user"] = current_user.email()




    def post(self):
        r_author= self.request.get("form_author")
        r_comment=self.request.get("form_comment")

        new_author= comment.Comment(
            author=r_author,
            contents=r_comment,
            )
        new_author.put()
        self.redirect("/QA")
        # author= users.get_current_user()
        # if author != None:
        #     r_contents= self.request.get("form_comment")
        #     logging.info("contents was " + r_comment)
        #     new_comment=Comment(author=author.email(), contents=r_comment)
        #     new_comment.put()
        # self.redirect("/Q&A")
        # r_comment= self.request.get("form_comment")
        # logging.info(r_comment)
        # new_comment=Comment(author="place holder", contents=r_comment)
        # new_comment.put()
        # logging