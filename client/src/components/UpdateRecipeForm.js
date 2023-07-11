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
                    <input onChange={updatePatchFormData} type="text" className = "title_new_recipe" name="title" placeholder="Recipe name" required/>
                    <select onChange={updatePatchFormData} type="text" className = "category_new_recipe" name="category" placeholder="Category" required>
                        {categories.map(category => {
                            return <option key = {category.id} value = {category.id}>{category.category}</option>
                        })}
                    </select>
                    <textarea onChange={updatePatchFormData} type="text" name="ingredients" className = "ingredients_new_recipe" placeholder="Ingredients" required/>
                    <textarea onChange={updatePatchFormData} type="text" name="preparation" className = "preparation_new_recipe"placeholder="Preparation" required/>                
                    <textarea onChange={updatePatchFormData} type="text" name="tips" className = "tips_new_recipe" placeholder="Tips" />
                    <input className = "update-recipe" type="submit" value= "Update Recipe"/>
                </div>
            </form>}
        </div>
    )
}

export default UpdateRecipeForm