from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models import ItemModel
from sqlalchemy.exc import SQLAlchemyError


from models.db import db
from schemas.schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint("Items", "items", description="Operações nos itens")


@blp.route("/item/<int:item_id>")
class Item(MethodView):
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        """Faz a busca de um item a partir do ID informado."""
        item = ItemModel.query.get_or_404(item_id)
        return item

    def delete(self, item_id):
        """Deleta um item a partir do ID informado."""
        item = ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Item deleted."}

    @blp.response(200, ItemSchema)
    @blp.arguments(ItemUpdateSchema)
    def put(self, item_data, item_id):
        """Edita um item a partir de seu ID informado."""
        item = ItemModel.query.get_or_404(item_id)
        if item:
            if "address_name" in item_data:
                item.address_name = item_data["address_name"]
            if "email" in item_data:
                item.email = item_data["email"]
            if "street_name" in item_data:
                item.street_name = item_data["street_name"]
            if "zip_code" in item_data:
                item.zip_code = item_data["zip_code"]
            if "additional_address_data" in item_data:
                item.additional_address_data = item_data["additional_address_data"]
            if "city" in item_data:
                item.city = item_data["city"]
            if "state" in item_data:
                item.city = item_data["state"]
        else:
            item = ItemModel(id=item_id, **item_data)

        db.session.add(item)
        db.session.commit()

        return item


@blp.route("/item")
class ItemList(MethodView):
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        """Faz a busca de todos os items cadastrados"""
        return ItemModel.query.all()

    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):
        """Adiciona um novo item à base de dados"""
        item = ItemModel(**item_data)

        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error ocurred while inserting the item.")
        return item
