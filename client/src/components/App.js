import '../App.css';
import {useState, useEffect} from 'react'
import { Route, Switch } from "react-router-dom"

import NavBar from './NavBar'
import Header from './Header'
import RecipeList from './RecipeList'
import NewRecipeForm from './NewRecipeForm'
import UpdateRecipeForm from './UpdateRecipeForm'
import About from './About'
import CategoryCard from './CategoryCard.js'
import CategoryList from './CategoryList'
import Search from './Search'

function App() {

  const [recipes, setRecipes] = useState([])
  const [categories, setCategories] = useState([])
  const [postFormData, setPostFormData] = useState({})
  const [idToUpdate, setIdToUpdate] = useState(0)
  const [patchFormData, setPatchFormData] = useState({})
  const [searchRecipe, setRecipeSearch] = useState('')
  const [searchCategory, setCategorySearch] = useState('')

function searchByRecipe(e) {
  setRecipeSearch(e.target.value)
}

const filterRecipe = recipes.filter(recipe => {
  if (searchRecipe === '') {
    return true
  }
  return recipe.title.toLowerCase().includes(searchRecipe.toLowerCase())
})

// function searchByCategory(e) {
//   setCategorySearch(e.target.value)
// }

// const filterCategory = categories.filter(category => {
//   if (searchCategory === '') {
//     return true
//   }
//   return category.category.toLowerCase().includes(searchCategory.toLowerCase())
// })

  useEffect(() => {
    fetch('/recipes')
    .then(response => response.json())
    .then(recipeData => setRecipes(recipeData))
  }, [])

  useEffect(() => {
    fetch('/categories')
    .then(response => response.json())
    .then(categoryData => setCategories(categoryData))
  }, [])

  // useEffect(() => {
  //   if(hotels.length > 0 && hotels[0].id){
  //     setIdToUpdate(hotels[0].id)
  //   }
  // }, [hotels])

  function addRecipe(event){
    event.preventDefault()

    fetch('/recipes', {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json"
      },
      body: JSON.stringify(postFormData)
    })
    .then(response => response.json())
    .then(newRecipe => {
      console.log(newRecipe)
        setRecipes(recipes => [...recipes, newRecipe])
      })
  }

  function updatePostFormData(event){
    setPostFormData({...postFormData, [event.target.name]: event.target.value})
  }

  function updateRecipe(event){
    event.preventDefault()
    fetch(`/recipes/${idToUpdate}`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json"
      },
      body: JSON.stringify(patchFormData)
    })
    .then(response => response.json())
    .then(updatedRecipe => {
      setRecipes(recipes => {
        return recipes.map(recipe => {
          if(recipe.id === updatedRecipe.id){
            return updatedRecipe
          }
          else{
            return recipe
          }
        })
      })
    })
  }

  // function deleteHotel(id){
  //   fetch(`/hotels/${id}`, {
  //     method: "DELETE"
  //   })
  //   .then(() => setHotels(hotels => {
  //     return hotels.filter(hotel => {
  //       return hotel.id !== id
  //     })
  //   }))
  // }


  function updatePatchFormData(event){
    setPatchFormData({...patchFormData, [event.target.name]: event.target.value})
  }

  return (
    <div className="app">
      <NavBar/>
      <Header />
      <Switch>
        <Route exact path="/">
          <About />
        </Route>
        <Route exact path = "/recipesbycategory">
          <CategoryList categories = {categories} />
          {/* <RecipeList recipes={recipes} /> */}
        </Route>
        <Route exact path = "/search">
          <Search searchByRecipe = {searchByRecipe} searchRecipe = {searchRecipe}/> 
        </Route>
        <Route path="/add_recipe">
          <NewRecipeForm addRecipe ={addRecipe} updatePostFormData={updatePostFormData} categories = {categories} searchByRecipe = {searchByRecipe}/>
        </Route>
        <Route path="/update_recipe">
          <UpdateRecipeForm updateRecipe={updateRecipe} setIdToUpdate={setIdToUpdate} updatePatchFormData={updatePatchFormData} recipes={filterRecipe} categories = {categories}/>
        </Route>
      </Switch>
    </div>
  );
}

export default App;
