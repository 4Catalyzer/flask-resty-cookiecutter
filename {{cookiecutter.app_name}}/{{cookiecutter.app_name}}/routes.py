from flask_resty import Api

from . import app
from . import views

# -----------------------------------------------------------------------------

api = Api(app, '/api/v1')

# -----------------------------------------------------------------------------

api.add_resource(
    '/widgets',
    views.WidgetListView, views.WidgetView,
    id_rule='<uuid:id>',
)

# -----------------------------------------------------------------------------

api.add_ping('/ping')
