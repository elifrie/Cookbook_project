import {NavLink} from "react-router-dom"

function NavBar(){
    return (
        <nav>
            <div className="nav">
                <div className="nav-wrapper">
                    <NavLink className = 'custom-button' to="/">Home</NavLink>
                    <NavLink className = 'custom-button' to="/recipesbycategory">Recipes by Category</NavLink>
                    <NavLink className = 'custom-button' to="/search">Search Recipe</NavLink>
                    <NavLink className = 'custom-button' to="/add_recipe">Add Recipe</NavLink>
                    <NavLink className = 'custom-button' to="/update_recipe">Update Recipe</NavLink>
                </div>
            </div>
        </nav>
    )
}

export default NavBar;