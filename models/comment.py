from google.appengine.ext import ndb

class Comment(ndb.Model):
    author = ndb.StringProperty()
    contents = ndb.StringProperty()
   