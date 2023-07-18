import {useState} from 'react'

function Search({searchByRecipe, searchRecipe}){
    return (
        <div className='container'>
            <div className = 'search-background'>
                <input className = 'search-bar' onChange = {searchByRecipe} value = {searchRecipe} placeholder='Search'/>
            </div>
        </div>

    )
}

export default Search