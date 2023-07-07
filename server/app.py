#!/usr/bin/env python3

import ipdb

from flask import Flask, make_response, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS

from models import db, Recipe, User, Category_recipe, Category

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotels.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

# CORS(app)

api = Api(app)

class User(Resource):

    def get(self):
        users = User.query.all()

        response_body = []

        for user in users:
            response_body.append(user.to_dict())

        return make_response(jsonify(response_body), 200)

    def post(self):
        try:
            new_user = User(username=request.get_json().get('username'), password=request.get_json().get('password'))
            db.session.add(new_user)
            db.session.commit()

            response_body = new_user.to_dict()
            
            return make_response(jsonify(response_body), 201)
        except ValueError as error:
            response_body = {
                "error": error.args
            }
            return make_response(jsonify(response_body), 422)


api.add_resource(User, '/users')

class Recipe(Resource):

    def get(self):
        recipes = Recipe.query.all()
        response_body = [recipe.to_dict() for recipe in recipes]
        return make_response(jsonify(response_body), 200)
    
    def post(self):
        data = request.get_json()
        new_recipe = Recipe(
            title = data['title'],
            picture = data['picture'],
            ingredients = data['ingredients'],
            preparation = data['preparation'],
            tips = data['tips'],
            reviews = data['reviews']
        )
        db.session.add(new_recipe)
        db.session.commmit()
        response_body = new_recipe.to_dict()
        return make_response(jsonify(response_body), 201)
    
api.add_resource(Recipe, '/recipes')

class RecipeById(Resource):
    def get(self,id):
        recipe = Recipe.query.filter_by(id = id).first()
        response_body = recipe.to_dict()
        return make_response(jsonify(response_body), 200)
    
    def patch(self, id):
        recipe = Recipe.query.filter_by(id = id).first()
        data = request.get_json()
        for attr in data:
            setattr(recipe, data[attr])
        db.session.commit()
        response_body = recipe.to_dict()
        return make_response(jsonify(response_body), 202)
    
    def delete(self, id):
        recipe = Recipe.query.filter_by(id = id).first()
        db.session.delete(recipe)
        return make_response(jsonify({'message': 'Recipe deleted!'}), 204)

api.add_resource(RecipeById, '/recipes/<int:id>')

class Category(Resource):
    def get(self):
        category = Category.query.all()
        response_body = category.to_dict()
        return make_response(jsonify(response_body), 200)

api.add_resource(Category, '/category')

class CategoryById(Resource):
    def get(self, id):
        category = Category.query.filter_by(id = id).first()
        response_body = category.to_dict()
        return make_response(jsonify(response_body), 200)
    
api.add_resource(CategoryById, '/category/<int:id>')

class Category_recipe(Resource):
    def get(self):
        category_recipe = Category_recipe.query.all()
        response_body = category_recipe.to_dict()
        return make_response(jsonify(response_body), 200)
    
api.add_resource(Category_recipe, '/category_recipe')