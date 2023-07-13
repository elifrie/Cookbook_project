import {useState} from 'react'

function NewRecipeForm({addRecipe, updatePostFormData, categories, addCategoryRecipe, updatePostCategoryFormData}){

    const [formSubmitted, setFormSubmitted] = useState(false)

    return (
        <div className="recipe-add-form">
            <h2>Add New Recipe Form</h2>
            {formSubmitted ? <h1>Thanks for adding a new recipe!</h1> :
            <form onSubmit={event => {
                    addRecipe(event)
                    addCategoryRecipe(event)
                setFormSubmitted(formSubmitted => !formSubmitted)
            }}>
                <div className= 'recipe-form-container'>
                    <input onChange={updatePostFormData} type="text" className = "title_new_recipe" name="title" placeholder="Recipe name" required/>
                    <select onChange={updatePostCategoryFormData} type="text" className = "category_new_recipe" name="category" placeholder="Category" required>
                        {categories.map(category => {
                            return <option key = {category.id} value = {category.id}>{category.category}</option>
                        })}
                    </select>
                    <textarea onChange={updatePostFormData} type="text" name="ingredients" className = "ingredients_new_recipe" placeholder="Ingredients" required/>
                    <textarea onChange={updatePostFormData} type="text" name="preparation" className = "preparation_new_recipe"placeholder="Preparation" required/>                
                    <textarea onChange={updatePostFormData} type="text" name="tips" className = "tips_new_recipe" placeholder="Tips" />
                    <input type="submit" className = 'add-recipe' value="Add Recipe"/>
                </div>
            </form>}
        </div>
    )
}

export default NewRecipeForm