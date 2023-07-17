import {useState} from 'react'
import FileInput from './FileInput';


// let listCounter = 1;
let submitted = 1;


function NewRecipeForm({addRecipe, updatePostFormData, categories}){


    const [formSubmitted, setFormSubmitted] = useState(false)

    let previousLength = 0;

    const handleInput = (event) => {
        const bullet = "\u25A0";
        const newLength = event.target.value.length;
        const characterCode = event.target.value.substr(-1).charCodeAt(0);

        if (newLength > previousLength) {
            if (characterCode === 10) {
                event.target.value = `${event.target.value}${bullet} `;
            } else if (newLength === 1) {
                event.target.value = `${bullet} ${event.target.value}`;
            }
        }

    previousLength = newLength;
}


    // const handleInputNum = (event) => {
    //     const newLength= event.target.value.length;
    //     const characterCode = event.target.value.substr(-1).charCodeAt(0);

    //     if (newLength > previousLength) {
    //         if (characterCode === 10) {
    //             event.preventDefault();
    //             event.target.value = `${event.target.value}\n${listCounter}. `;
    //             listCounter++;
    //         } else if (newLength === 1) {
    //             event.target.value = `${listCounter}. ${event.target.value}`;
    //             listCounter++;
    //         }
    //     }

    //     previousLength = newLength;
    // };

    // const handleSubmit = (event) => {
    //     if (!submitted) {
    //         listCounter = 1;
    //         submitted = true;
    //       }
    //     };

    // const form = document.querySelector('form');
    // form.addEventListener('submit', handleSubmit);

    // const inputField = document.querySelector('input');
    // inputField.addEventListener('input', handleInput);

    return (
        <div className="recipe-add-form">
            <h2>Add New Recipe Form</h2>
            {formSubmitted ? <h1>Thanks for adding a new recipe!</h1> :
            <form onSubmit={event => {
                    addRecipe(event)
                    // addCategoryRecipe(event)
                setFormSubmitted(formSubmitted => !formSubmitted)
            }}>
                <div className= 'recipe-form-container'>
                    <input onChange={updatePostFormData} type="text" className = "title_new_recipe" name="title" placeholder="Recipe name" required/>
                    {/* <FileInput></FileInput> */}
                    {/* <input className = 'upload-button' type ='file' accept = "image/*" placeholder='Upload Image' name = 'picture' id = 'select-image'/>
                        <label htmlFor = 'select-image'/>
                        <Button/> */}
                    <select onChange={updatePostFormData} type="text" className = "category_new_recipe" name="category" placeholder="Category" required>
                        {categories.map(category => {
                            return <option key = {category.id} value = {category.category}>{category.category}</option>
                        })}
                    </select>
                    <textarea onInput = {handleInput} onChange={updatePostFormData} type="text" name="ingredients" className = "ingredients_new_recipe" placeholder="Ingredients" required/>
                    <textarea onInput = {handleInput} onChange={updatePostFormData} type="text" name="preparation" className = "preparation_new_recipe"placeholder="Preparation" required/>                
                    <textarea onChange={updatePostFormData} type="text" name="tips" className = "tips_new_recipe" placeholder="Tips" />
                    <input type="submit" className = 'add-recipe' value="Add Recipe"/>
                </div>
            </form>}
        </div>
    )
}

export default NewRecipeForm