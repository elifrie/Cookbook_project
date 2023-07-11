import RecipeCard from './RecipeCard'

function RecipeList({recipes}){
    const recipeComponents = recipes.map(recipe => {
        return <RecipeCard key={recipe.id} recipe={recipe} title = {recipe.title} preparation = {recipe.preparation} />
    })
    return (
        <ul className="recipe-list">{recipeComponents}</ul>
        )
}

export default RecipeList