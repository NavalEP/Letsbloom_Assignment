# Running the application
1. Clone the repository.
2. Creata and activate a new virtual environment in the repository's root directory. Refer the [docs](https://docs.python.org/3/tutorial/venv.html) for instructions on how to work with virtual environments.
3. Install the necessary dependencies by running `pip install -r requirements.txt`.
4. Run `python manage.py migrate` in the root directory to create a database.
5. Run `python manage.py runserver` to start the server. API requests can be sent to the server once it is started.

## Seeding with mock data
1. Run `python manage.py shell` from the terminal, while you are in the repository's root directory. Ensure that the correct virtual environment is activated.
2. Run the following lines of code in the interactive shell (`num` is the number of mock entries to be generated in the database) -

    ```
    from utils import mockData
    mockData(num)
    exit()
    ```

# API Documentation
## Retreive all Books
### Request
`GET /api/books`
### Response
JSON containing all entries in the database.


## Add a new book
### Request 
`POST /api/books`

The following JSON should be given in request body as form-data
```
{
"title": "Book Title",
"author": "Book Author"
}
```
The published_date field is optional and defaults to current date.


### Response
The following JSON response is obtained on a successful POST request
```
{
    "id": <Book ID>,
    "title": "<Book title>",
    "author": "<Book Author>",
    "published_date": "<Book publishing date>"
}
```
The server will return the response code 400 (Bad request) if some fields are missing in the POST data and/or the title of the book already exists in the database.

## Update book details
### Request
`PUT /api/books/{id}`

The following JSON should be given in request body as form-data
```
{
"title": "<Book Title>",
"author": "<Book Author>"
}
```
### Response
The following JSON response is obtained on a successful POST request
```
{
    "id": <Book ID>,
    "title": "<Book title>",
    "author": "<Book Author>",
    "published_date": "<Book publishing date>"
}
```
The server will return the response code 400 (Bad request) if some fields are missing in the POST data and/or the title of the book already exists in the database. 404 response is returned if the id is not found in the database.