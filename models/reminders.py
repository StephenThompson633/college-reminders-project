from google.appengine.ext import ndb

class RemindersModel(ndb.Model):
    email = ndb.StringProperty()
    content = ndb.StringProperty()
    date = ndb.StringProperty()
    time = ndb.StringProperty()
