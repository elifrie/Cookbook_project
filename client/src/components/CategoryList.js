import CategoryCard from './CategoryCard.js'
import {useState} from 'react'
import RecipeList from './RecipeList'

function CategoryList({categories, recipes}){

    let [clicked, setClicked] = useState(null)

    const filteredRecipesByCategory = recipes.filter(recipe => {
        return recipe.category === clicked 
    })

    const recipeCategories = categories.map(category => {
        return <CategoryCard key = {category.id} category = {category} recipes = {recipes} clicked = {clicked} setClicked = {setClicked}/>
    })
    return (
        <div>
        {!clicked ?
        <p className="category-list">{recipeCategories}</p> :
        <div>
            <button onClick= {() => setClicked(null)}>BACK</button>
            <RecipeList recipes = {filteredRecipesByCategory}/>
        </div>}
        
        </div>
    )
}

export default CategoryList