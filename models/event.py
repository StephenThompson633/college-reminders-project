from google.appengine.ext import ndb

class EventModel(ndb.Model):
    describe = ndb.StringProperty()
    event = ndb.StringProperty()
    date = ndb.StringProperty()
    invite = ndb.StringProperty()