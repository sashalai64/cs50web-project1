# CS50's Web Programming with Python and JavaScript

# Project 1 - Wiki
Website: https://cs50.harvard.edu/web/2020/projects/1/wiki/

## Description
Welcome to the Wiki Encyclopedia! This is a web application where you can create, edit, and browse encyclopedia entries.

## Features
- **Home**
    - Displays a list of all encyclopedia entries on the home page.
    - Each entry is listed with a clickable title that navigates the user to the respective entry page.
    - Provides an overview of available entries for easy navigation and exploration of the encyclopedia content.

- **Entry Page**
    - Renders a page displaying the contents of a specific encyclopedia entry when visiting **/wiki/TITLE**.
    - Provides error handling for non-existent entries.
   
- **Search**
    - Enables users to search for encyclopedia entries by typing a query into the **Search Box** in the sidebar.
    - Redirects users to the entry page if the query matches an entry name.
    - Displays a list of search results for queries that don't match entry names, allowing users to navigate to relevant entries.

- **New Pages**
    - Allows users to create new encyclopedia entries by clicking **"Create New Page"** in the sidebar.
    - Provides input fields for users to enter a title and Markdown content for the new page.
    - Validates input to prevent duplicate entry titles and provides appropriate error messages.
      
- **Edit Existing Pages**
    - Enables users to edit the Markdown content of existing encyclopedia entries.
    - Presents an **"Edit"** button on each entry page for users to navigate to an edit page with pre-populated Markdown content.
    - Allows users to save changes made to the entry content and redirects them back to the entry page.

- **Random Page**
    - Provides a **"Random Page"** link in the sidebar for users to navigate to a randomly selected encyclopedia entry.
      
## Requirements
- Python 3.x
- Django
  
## How to Run
1. **Clone the Repository**
      ```
      git clone https://github.com/sashalai64/cs50web-project1.git
      ```
   
2. **Run the Server**
      ```
      python manage.py runserver
      ```
      
3. **Access the Application**
   
    Visit `http://127.0.0.1:8000/` in your browser.