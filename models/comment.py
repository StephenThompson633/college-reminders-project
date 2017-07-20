from google.appengine.ext import ndb

class Comment(ndb.Model):
    author = ndb.StringProperty()
    contents = ndb.StringProperty()
    time= ndb.DateTimeProperty(auto_now_add=True)

    