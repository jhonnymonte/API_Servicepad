from api.auth.models import *
from config.settings import app
from routes.Publications import *
from routes.Users import *

if __name__ == "__main__":
    app.run(port=5000, debug=True)