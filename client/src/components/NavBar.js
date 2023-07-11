import {NavLink} from "react-router-dom"

function NavBar(){
    return (
        <nav>
            <div>
                <NavLink to="/">Home</NavLink>
                <NavLink to="/recipesbycategory">Recipes by Category</NavLink>
                <NavLink to="/search">Search Recipe</NavLink>
            </div>
            <div>
                <NavLink to="/add_recipe">Add Recipe</NavLink>
                <NavLink to="/update_recipe">Update Recipe</NavLink>
            </div>
        </nav>
    )
}

export default NavBar;