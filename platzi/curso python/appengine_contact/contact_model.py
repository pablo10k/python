from google.appengine.ext import ndb

#clase contacto extiendo ndb.model
class Contact(ndb.Model):
    name = ndb.StringProperty()
    phone = ndb.StringProperty()
    email = ndb.StringProperty()
