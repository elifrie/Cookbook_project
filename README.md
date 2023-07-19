# Daphna & Chuchu's Family Recipes

This website is an ode to my wonderful parents. Food is a cornerstone of my family dynamic and meals are a time we come together. This is not unique to my family. Food breaks barriers; it reaches across socio-economic groups, cultural groups, etc.

My family has a shared email and drive that we share and I was inspired to create this website to give my parents the option to eventually publish that drive for public consumption. Whether or not they give me the okay is a separate story...

The recipes here span a variety of cuisines, but all are near and dear to the Friedlanders, please enjoy them as much as we do.

## Setup

1. Fork and then Clone this repository.

2. Make sure that you are in the correct directory (folder) that contains a `Pipfile`, then run `pipenv install` in your terminal to install the required Python libraries.

3. Now that your `pipenv` virtual environment is ready to use, enter `pipenv shell` to enter the virtual environment.

4. Run `npm install --prefix client` in your terminal to install the dependencies for the React app.

5. Enter the command `cd server` in the terminal to move into the server directory.

6. Enter the command `python app.py` in the terminal to run the Flask app (make sure that you are in the `server` directory before running this terminal command).

7. In a new terminal, run `npm start --prefix client` in your terminal to run the React app in the browser. If your browser does not automatically open the page for you, open [http://localhost:4000](http://localhost:4000) to view it in your browser.

## If you are using this lecture repository as a template

1. Make sure that you are in the root directory of this repository. You can enter the command `ls` in the terminal and if you see the `Pipfile`, `Pipfile.lock`, and `README.md` then you are in the correct directory.
2. Run `rm -rf .git` in the terminal to remove existing git configuration.
3. Run `git init` to initialize the project as a git repository.
