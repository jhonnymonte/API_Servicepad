from config.settings import ma

class PublicationSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "title", "description","priority","status","user_id","created_at","updated_at")