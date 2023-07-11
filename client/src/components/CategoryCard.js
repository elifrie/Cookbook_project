function CategoryCard({category}) {

    function handleClick() {

    }

    return (
        <div className = 'category-container'>
            <div className = 'category'>
            {category.category}
            </div>
        </div>
        )
}


export default CategoryCard