from flask_resty import FixedSorting, GenericModelView

from . import auth
from . import models
from . import schemas

# -----------------------------------------------------------------------------


class View(GenericModelView):
    authentication = auth.Authentication()
    authorization = auth.Authorization()


# -----------------------------------------------------------------------------


class WidgetViewBase(View):
    model = models.Widget
    schema = schemas.WidgetSchema()

    sorting = FixedSorting('created_at')


class WidgetListView(WidgetViewBase):
    def get(self):
        return self.list()

    def post(self):
        return self.create()


class WidgetView(WidgetViewBase):
    def get(self, id):
        return self.retrieve(id)

    def patch(self, id):
        return self.update(id, partial=True)

    def delete(self, id):
        return self.destroy(id)
