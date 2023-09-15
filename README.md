# Inventory Project
The 'Inventory' project is a Python-based web application built with Django. It is designed to help software companies keep track of their technologies, their allocation to workers, and related information such as amortization, quantity, and year.

## Features
- Create, update, and delete technologies in the inventory.
- Assign technologies to workers and track their allocation.
- Manage amortization, quantity, and year information for each technology.
- Search and filter technologies based on various criteria.
- User authentication and access control.
- 
## Installation
Follow these steps to set up and run the 'Inventory' project:
1. Clone the repository: `git clone <repository-url>`
2. Navigate to the project directory: `cd inventory`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Set up the database by running migrations: `python manage.py migrate`
5. Create a superuser account: `python manage.py createsuperuser`
6. Start the development server: `python manage.py runserver`
Make sure you have Python and Django installed on your system before proceeding with the installation.

## Usage
1. Access the application by visiting `http://localhost:8000` in your web browser.
2. Log in with your superuser account credentials.
3. Use the provided interface to manage technologies, worker assignments, and related information.
4. Utilize the search and filter functionality to find specific technologies or worker allocations.
   
## Contributing
Contributions to the 'Inventory' project are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request on GitHub.

## License
This project is licensed under the [Mozilla Public License Version 2.0].
