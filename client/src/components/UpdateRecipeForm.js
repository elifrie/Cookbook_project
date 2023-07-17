import {useState} from 'react'

function UpdateRecipeForm({updateRecipe, setIdToUpdate, updatePatchFormData, recipes, categories}){

    const [updateFormSubmitted, setUpdateFormSubmitted] = useState(false)


    return (
        <div className="recipe-update-form">
            <h2>Need to update a recipe?</h2>
            {updateFormSubmitted ? <h1>Recipe Updated!</h1> :
            <form onSubmit={event => {
                    updateRecipe(event)
                setUpdateFormSubmitted(updateFormSubmitted => !updateFormSubmitted)
            }}>
                <div className= 'recipe-form-container'>
                    <select onChange={updatePatchFormData} type="text" placeholder="Search for a recipe" required>
                        {recipes.map(recipe => {
                            return <option key = {recipe.id} value = {recipe.id}>{recipe.title}</option>
                        })}
                    </select>
                    <input onChange = {updatePatchFormData} className = "title_new_recipe" placeholder= "Recipe Title" name ='title' type="text"/>
                    <select onChange={updatePatchFormData} type="text" className = "category_new_recipe" name="category" placeholder="Category" >
                        {categories.map(category => {
                            return <option key = {category.id} value = {category.category}>{category.category}</option>
                        })}
                    </select>
                    <textarea onChange={updatePatchFormData} type="text" name="ingredients" className = "ingredients_new_recipe" placeholder="Ingredients" />
                    <textarea onChange={updatePatchFormData} type="text" name="preparation" className = "preparation_new_recipe"placeholder="Preparation" />                
                    <textarea onChange={updatePatchFormData} type="text" name="tips" className = "tips_new_recipe" placeholder="Tips" />
                    <input className = "update-recipe" type="submit" value= "Update Recipe"/>
                </div>
            </form>}
        </div>
    )
}

export default UpdateRecipeForm