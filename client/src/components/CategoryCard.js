import {useState} from 'react'
import RecipeCard from './RecipeCard'


function CategoryCard({category, recipes, clicked, setClicked}) {

   

    function handleClick() {
        setClicked((clicked) = category.category)
        console.log(clicked)

    }


        return (
            <div className = 'category-container'>
            <div className = 'category' onClick = {handleClick}>
                {category.category}
            </div>
            </div>
            )
}


export default CategoryCard