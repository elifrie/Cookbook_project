function RecipeCard({recipe}){
    return (
        <li className="recipe">
            <h1>{recipe.title}</h1>
                <li>Ingredients: {recipe.ingredients}</li>
                <br></br>
                <li>Preparation</li>
            <img src={recipe.image} alt={recipe.name} />
        </li>
    )
}

export default RecipeCard