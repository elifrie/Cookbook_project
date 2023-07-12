import {useState} from 'react'

function Search({searchByRecipe, searchRecipe}){
    return (
        <div className = 'search-background'>
            <input className = 'search-bar' onChange = {searchByRecipe} value = {searchRecipe} placeholder='Search'/>
        </div>
    )
}

export default Search