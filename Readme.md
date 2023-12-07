## Running the application
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