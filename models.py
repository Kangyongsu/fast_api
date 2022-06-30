from mongoengine import Document, StringField, IntField, ListField, BooleanField

class auto_complete(Document):
    category= StringField()
    keyword=StringField()
    weight=IntField()
    shard=IntField()
    searchCount=IntField()
    satisfactionCount=IntField()
    force= BooleanField()