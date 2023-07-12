function CategoryCard({category}) {

    function handleClick() {
        console.log('clicked')
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