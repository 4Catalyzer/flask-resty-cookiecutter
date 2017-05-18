from marshmallow import fields, Schema

# -----------------------------------------------------------------------------


class WidgetSchema(Schema):
    id = fields.UUID()

    message = fields.String()
    created_at = fields.DateTime()
