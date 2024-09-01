# Recipe App (Command Line Version)
## Project Brief
Project created for careerFoundry's Python for Web Developers specialization course. Main goal is to complete a command line version of a Recipe App which is able to create, read, and modify recipes, as well as searching for recipes based on ingredients available.

## Key Features
- easy-to-use interface
- user's recipes are stored and managed on a locally hosted MySQL database
- recipes can be searched for based on a set of ingredients specified by the user
- automatic difficulty rating for each recipe
- more details available for each recipe if the user prompts for it


## Technical Requirements

- Python 3.6+ installation
- Locally hosted MySQL database
- ipython installation

## Structure Choices
1) Each recipe is stored as a dictionary object. It works as a structure because of the key:value pairs it offers. This will help both users and developers further down the line, as it will make each dictionary object(each recipe) easily search-able. Using Python one can get information on ingredients, cooking time, etc, just by pulling the corresponding key. This sets up some of the base functionality of the app, since the users need to be able to search for all of the keys described above.

2) The outer structure (all_recipes) is a list object. The intention here was to have a container for all of the recipe data that will allow the developer to organize recipes, add, or modify them as necessary. A tuple would have worked to keep the recipes together, but is too rigid of a structure and would make updating & organizing recipes too cumbersome to be practical. 