from config.settings import ma

class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "public_id", "fullname","email")