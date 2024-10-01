# Project Management API

This is a simple Project Management API built with FastAPI. It allows you to manage projects, including creating, reading, updating, and deleting projects.

## HTTP Methods

- GET, POST, PUT, PATCH, DELETE

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn

## API Endpoints

### Retrieve All Projects

- **URL:** `/projects`
- **Method:** `GET`
- **Response:** List of all projects

### Create a New Project

- **URL:** `/projects`
- **Method:** `POST`
- **Request Body:** JSON object representing the new project
- **Response:** The created project

### Retrieve a Specific Project by ID

- **URL:** `/projects/{project_id}`
- **Method:** `GET`
- **Response:** The project with the specified ID

### Retrieve Projects by Name

- **URL:** `/projects/name/{name}`
- **Method:** `GET`
- **Response:** List of projects that match the specified name

### Retrieve Projects by Status

- **URL:** `/projects/status/{status}`
- **Method:** `GET`
- **Response:** List of projects that match the specified status

### Retrieve Projects by Team Member

- **URL:** `/projects/team/{team_member}`
- **Method:** `GET`
- **Response:** List of projects that include the specified team member

### Retrieve Projects by Start Date

- **URL:** `/projects/start_date/{start_date}`
- **Method:** `GET`
- **Response:** List of projects that match the specified start date

### Retrieve Projects by End Date

- **URL:** `/projects/end_date/{end_date}`
- **Method:** `GET`
- **Response:** List of projects that match the specified end date

### Update a Specific Project by ID

- **URL:** `/projects/{project_id}`
- **Method:** `PUT`
- **Request Body:** JSON object representing the updated project
- **Response:** The updated project

### Partially Update a Specific Project by ID

- **URL:** `/projects/{project_id}`
- **Method:** `PATCH`
- **Request Body:** JSON object representing the partial updates
- **Response:** The updated project

### Delete a Specific Project by ID

- **URL:** `/projects/{project_id}`
- **Method:** `DELETE`
- **Response:** The deleted project

## License

This project is licensed under the MIT License.