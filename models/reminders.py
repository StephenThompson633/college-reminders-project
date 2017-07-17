from google.appengine.ext import ndb

class RemindersModel(ndb.Model):
    author = ndb.StringProperty()
    title = ndb.StringProperty()
    description = ndb.StringProperty()
