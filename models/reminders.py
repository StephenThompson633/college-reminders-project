from google.appengine.ext import ndb

class RemindersModel(ndb.Model):
   
    content = ndb.StringProperty()
    date = ndb.StringProperty()
    
