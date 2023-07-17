from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Category(db.Model, SerializerMixin):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key = True)
    category = db.Column(db.String, unique = True, nullable = False)
    # title = db.Column(db.String, unique = True, nullable = False)

    # category_recipes = db.relationship('Category_recipe', backref = 'category')

    serialize_rules = ('-recipes',)

# class Category_recipe(db.Model, SerializerMixin):
#     __tablename__ = 'category_recipes'

#     id = db.Column(db.Integer, primary_key = True)

#     recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'))
#     category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable = False)

#     serialize_rules = ('-categories', '-recipes',)

class Recipe(db.Model, SerializerMixin):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key = True)

    title = db.Column(db.String, nullable = False)
    category = db.Column(db.String, nullable = False, default = 'Appetizers')
    picture = db.Column(db.String)
    ingredients = db.Column(db.String)
    preparation = db.Column(db.String)
    tips = db.Column(db.String)
    reviews = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # category_recipes = db.relationship('Category_recipe', backref = 'recipe')

    serialize_rules = ('-users',)


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique = True, nullable = False)
    password = db.Column(db.String, unique = True, nullable = False)
    reviews = db.Column(db.String, unique = True)

    recipes = db.relationship('Recipe', backref = 'user')

    serialize_rules = ('-recipes',)

# Models go here!
