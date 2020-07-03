import os
import connexion
from flask_cors import CORS


app = connexion.FlaskApp(__name__, specification_dir='openapi/')
app.add_api('swagger.yaml')

# add CORS support
CORS(app.app)

port = int(os.getenv("PORT", "8080"))

app.run(port=8080)
