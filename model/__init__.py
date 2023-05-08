from flask import Flask
from flask_cors import CORS
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://f7bf6da58d384c7cacf967b90540b879@o358880.ingest.sentry.io/5480579",
    integrations=[FlaskIntegration()],
    traces_sample_rate=10.0
)

app = Flask(__name__)
CORS(app)

from model import routes
from model import utils
