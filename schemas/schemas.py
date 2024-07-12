from marshmallow import Schema, fields

class ItemSchema(Schema):
    id = fields.Str(dump_only=True)
    address_name = fields.Str(required=True)
    email = fields.Str(required=True)
    zip_code = fields.Str(required=True)
    street_name = fields.Str(required=True)
    additional_address_data = fields.Str(required=True)
    city = fields.Str(required=True)
    state = fields.Str(required=True)

class ItemUpdateSchema(Schema):
    address_name = fields.Str()
    email = fields.Str()
    zip_code = fields.Str()
    street_name = fields.Str()
    additional_address_data = fields.Str()
    city = fields.Str()
    state = fields.Str()


