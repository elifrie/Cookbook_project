import {useState, useEffect} from 'react'


function RecipeCard({recipe}){

   let [readMore, setReadMore] = useState(false)
    
    function handleClick(){
        setReadMore((readMore) = !readMore)
    }

    return (
        <div >
            <h1 onClick = {handleClick} className='card-title'> {recipe.title} </h1> 
                {readMore ?
                <div className='recipe-body'> 
                    <p>Ingredients:</p> 
                    <br></br> 
                    <p className='recipe-ingredients'>{recipe.ingredients}</p>
                        <br></br> 
                        <br></br>
                    <li>Preparation:</li>
                        <br></br>
                     <p>{recipe.preparation}</p>  
                        <br></br>
                    <p></p> 
                    <p>Tips:</p>
                        <br></br>
                    <p>{recipe.tips}</p>
                </div> : ''}
            <img src={recipe.image} alt={recipe.name} />
        </div>
    )
}

export default RecipeCard