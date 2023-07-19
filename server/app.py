#!/usr/bin/env python3

import ipdb

from flask import Flask, make_response, jsonify, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from datetime import datetime
from models import db, Recipe, User, Category

app = Flask(__name__)
app.secret_key = b'maylover'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotels.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

bcrypt = Bcrypt(app)

def get_current_user():
    return User.query.where( User.id == session.get("user_id") ).first()

def logged_in():
    return bool( get_current_user() )

# CORS(app)

api = Api(app)

@app.post('/users')
def create_user():
    json = request.json
    pw_hash = bcrypt.generate_password_hash(json['password']).decode('utf-8')
    new_user = User(username=json['username'], password=pw_hash)
    db.session.add(new_user)
    db.session.commit()
    session['user_id'] = new_user.id
    return new_user.to_dict(), 201

@app.post('/login')
def login():
    json = request.json
    user = User.query.where(User.username == json["username"]).first()
    if user and bcrypt.check_password_hash(user.password, json['password']):
        session['user_id'] = user.id
        return user.to_dict(), 201
    else:
        return {'message': 'Invalid username or password'}, 401

@app.get('/current_session')
def check_session():
    if logged_in():
        return get_current_user().to_dict(), 200
    else:
        return {}, 401

@app.delete('/logout')
def logout():
    session['user_id'] = None
    return {}, 204

class Users(Resource):

    def get(self):
        users = User.query.all()
        response_body = []
        for user in users:
            response_body.append(user.to_dict())
        return make_response(response_body,200)

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


api.add_resource(Users, '/users')

class UserById(Resource):

    def get(self,id):
        user = User.query.filter_by(id = id).first()
        response_body = user.to_dict()
        return make_response(jsonify(response_body), 200)
    
    def delete(self,id):
        user = User.query.filter_by(id = id).first()
        db.session.delete(user)
        db.session.commit()
        return make_response(jsonify({'message': 'User deleted!'}), 204)
    
api.add_resource(UserById, '/users/<int:id>')

class Recipes(Resource):

    def get(self):
        recipes = Recipe.query.all()
        response_body = [recipe.to_dict() for recipe in recipes]
        return make_response(jsonify(response_body), 200)
    
    def post(self):
        data = request.get_json()
        # category = Category.query.filter_by(category = categoryname).first()
        # categoryname = data['categoryname']
        new_recipe = Recipe(
            user_id = 1,
            title = data['title'],
            category = data['category'],
            # picture = data['picture'],
            ingredients = data['ingredients'],
            preparation = data['preparation'],
            tips = data['tips']
            # reviews = data['reviews']
        )
        db.session.add(new_recipe)
        db.session.commit()
        response_body = new_recipe.to_dict()
        return make_response(jsonify(response_body), 201)
    
api.add_resource(Recipes, '/recipes')

class RecipeById(Resource):
    def get(self,id):
        recipe = Recipe.query.filter_by(id = id).first()
        response_body = recipe.to_dict()
        return make_response(jsonify(response_body), 200)
    
    def patch(self, id):
        recipe = Recipe.query.filter_by(id = id).first()
        if recipe:
            data = request.get_json()
            for attr in data:
                setattr(recipe, attr, data[attr])
            db.session.commit()
            response_body = recipe.to_dict()
            return make_response(jsonify(response_body), 202)
        else:
            response_body = {
                'error': 'Recipe not found!'
            } 
            return make_response(jsonify(response_body), 404)

    
    def delete(self, id):
        recipe = Recipe.query.filter_by(id = id).first()
        db.session.delete(recipe)
        db.session.commit()
        return make_response(jsonify({'message': 'Recipe deleted!'}), 204)

api.add_resource(RecipeById, '/recipes/<int:id>')

class Categories(Resource):
    def get(self):
        categories = Category.query.all()
        response_body = [category.to_dict() for category in categories]
        return make_response(jsonify(response_body), 200)

api.add_resource(Categories, '/categories')

class CategoryById(Resource):
    def get(self, id):
        category = Category.query.filter_by(id = id).first()
        response_body = category.to_dict()
        return make_response(jsonify(response_body), 200)
    
api.add_resource(CategoryById, '/categories/<int:id>')

# class RecipesByCategory(Resource):
#     def get(self):
#         category_recipes = Category_recipe.query.all()
#         response_body = [category_recipe.to_dict() for category_recipe in category_recipes]
#         return make_response(jsonify(response_body), 200)

#     def post(self):
#         recipe = Recipe.query.filter_by(id = request.json.get('recipe_id')).first()
#         category = Category.query.filter_by(id = request.json.get('category_id')).first()
        
#         new_recipe_category = Category_recipe(
#             # recipe_id = recipe.id,
#             category_id = category.id
#         )
#         db.session.add(new_recipe_category)
#         db.session.commit()
#         response_body = new_recipe_category.to_dict()
#         return make_response(jsonify(response_body), 201)
    
# api.add_resource(RecipesByCategory, '/recipesbycategory')

if __name__ == '__main__':
    app.run(port=7555, debug=True)