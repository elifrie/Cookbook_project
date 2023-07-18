import {useState} from 'react'
import RecipeCard from './RecipeCard'

function RecipeList({recipes}){
   
    const recipeComponents = recipes.map(recipe => {
        return <RecipeCard key={recipe.id} recipe={recipe} title = {recipe.title} preparation = {recipe.preparation} />
           })
    return (
        <p className="recipe-list">{recipeComponents}</p>
        )
}

export default RecipeList