import CategoryCard from './CategoryCard.js'

function CategoryList({categories}){
    const recipeCategories = categories.map(category => {
        return <CategoryCard key = {category.id} category = {category}/>
    })
    return (
        <p className="category-list">{recipeCategories}</p>
    )
    }


export default CategoryList