# Course Web Application

## Project Description
This is a Django web application that displays a list of courses with details and videos for each course. It uses two JSON files to load course data and video details.

## Features
- List of courses with titles, descriptions, and course details.
- Display of course videos with titles, descriptions, and video links.
- Responsive design using CSS.
- Uses Django template system for rendering HTML pages.

## Installation

### Prerequisites
- Python 3.x
- Django 5.1.1 or higher

### Steps to Run the Project:

1. Clone this repository (if using GitHub) or extract the ZIP file.
2. Navigate to the project directory:
    ```bash
    cd my_django_project
    ```
3. Install the dependencies from `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the Django development server:
    ```bash
    python manage.py runserver
    ```
5. Open your browser and navigate to:
    ```
    http://127.0.0.1:8000/
    ```

## Usage
- On the home page, you'll see a list of courses.
- Clicking on a course will show the course details and videos.

## Dependencies
The project uses the following major Python libraries:
- Django (5.1.1)
- Requests (for fetching external data, if applicable)

