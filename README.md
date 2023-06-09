## Project Description

This project is a template FastAPI application that provides a starting point for building web applications using the FastAPI framework. It follows a structured organization with modular components to promote scalability, maintainability, and code reusability.

The application's backend is implemented using Python and consists of various modules and directories. The `backend` directory contains the main codebase, including modules for users, API routes, core components, models, securities, services, and utilities. The `user` module handles user-related functionality, such as user account management and authentication.

The project leverages Docker for containerization, allowing for easy deployment and scalability. The Dockerfile provided in the project facilitates the creation of a Docker image for the application.

The project also includes a configuration directory (`config`) with configuration files for different environments (development, production, staging). This enables easy management of application settings based on the deployment environment.

Database migrations are supported using Alembic, a database migration tool. The `migrations` directory contains the migration files, enabling easy versioning and management of the database schema.

The project provides a comprehensive test suite, with the `tests` directory containing modules for testing different components of the application. This ensures the reliability and correctness of the implemented functionality.

Overall, this FastAPI template application serves as a foundation for developing robust web applications, following best practices and promoting efficient development workflows. It offers a structured organization, containerization support, configuration management, database migration capabilities, and a test suite, facilitating the development process and ensuring the quality of the resulting application.

Note: This description is a general overview of the project's purpose and structure, tailored specifically for a GitHub repository.


## Project Structure

- `.dockerignore`: A file that contains a list of files and directories to be ignored during Docker image building.
- `.env`: A file that holds environment variables.
- `.env.example`: An example file for environment variables.
- `.gitignore`: A file that specifies files and directories to be ignored by Git when tracking changes.
- `Dockerfile`: A file used to build the Docker image of the application.
- `README.md`: A file that provides a description of the project.
- `alembic.ini`: The Alembic configuration file, used for managing database migrations.
- `backend/`: The directory containing the main backend code and components.
  - `__init__.py`: An initialization file for the `backend` module.
  - `user/`: The module directory for user-related functionality.
    - `__init__.py`: An initialization file for the `user` module.
    - `api/`: The API module directory for users.
      - `__init__.py`: An initialization file for the `api` module.
      - `routes/`: The routes module directory for the user API.
        - `__init__.py`: An initialization file for the `routes` module.
        - `account.py`: A module containing request handlers related to user accounts.
        - `authentication.py`: A module containing request handlers related to user authentication.
    - `core/`: The core components directory for the user module.
      - `__init__.py`: An initialization file for the `core` module.
      - `account.py`: A module containing the logic for working with user accounts.
      - `session.py`: A module containing the logic for working with user sessions.
    - `main.py`: The main application module.
    - `models/`: The directory for user-related database models.
      - `__init__.py`: An initialization file for the `models` module.
      - `db/`: The directory for database models.
        - `__init__.py`: An initialization file for the `db` module.
        - `account.py`: A module containing the database model for user accounts.
      - `schemas/`: The directory for user data schemas.
        - `__init__.py`: An initialization file for the `schemas` module.
        - `account.py`: A module containing the data schema for user accounts.
    - `securities/`: The directory for user security components.
      - `__init__.py`: An initialization file for the `securities` module.
      - `hashing.py`: A module containing hashing functions.
      - `security.py`: A module containing security components.
    - `services/`: The directory for user services.
      - `__init__.py`: An initialization file for the `services` module.
      - `account.py`: A module containing services for working with user accounts.
    - `utils/`: The directory for user utilities.
      - `__init__.py`: An initialization file for the `utils` module.
- `common/`: The directory for common components and utilities.
  - `__init__.py`: An initialization file for the `common` module.
- `config/`: The directory for project configuration files.
  - `__init__.py`: An initialization file for the `config` module.
  - `base.py`: The base configuration file.
  - `development.py`: The configuration file for development.
  - `environment.py`: The file defining the project environment.
  - `manager.py`: The configuration manager.
  - `production.py`: The configuration file for production environment.
  - `staging.py`: The configuration file for staging environment.
- `docker-compose.yml`: The Docker Compose configuration file used for deploying containerized services.
- `migrations/`: The directory for database migration files.
  - `README`: A file containing a description of the migrations.
  - `env.py`: The migration environment configuration file.
  - `script.py.mako`: The migration script template.
  - `versions/`: The directory for migration versions.
    - `35a5685cbd77_new.py`: A migration file for creating the user table.
- `requirements.txt`: The file containing project dependencies.
- `scripts/`: The directory for project scripts.
  - `__init__.py`: An initialization file for the `scripts` module.
- `tests/`: The directory for test modules.
  - `__init__.py`: An initialization file for the `tests` module  
## Project Installation

Follow these instructions to install and configure the project.

### Prerequisites

Make sure you have the following tools installed:

- Python 3
- Docker

### Installation Steps

1. Clone the project repository:

   ```bash
   git clone https://github.com/gecsagen/good_fastapi_template.git
   cd good_fastapi_template
   ```

2. Create a virtual environment and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure the `.env` file. Open the `.env` file and set the following environment variables:

   ```
   POSTGRES_USERNAME=<db_user>
   POSTGRES_PASSWORD=<db_password>
   POSTGRES_HOST=<db_server>
   POSTGRES_PORT=<db_port>
   POSTGRES_DB=<db_name>
   POSTGRES_SCHEMA=<db_schema>
   ```

   Replace `<db_user>`, `<db_password>`, `<db_server>`, `<db_port>`, `<db_name>`, and `<db_schema>` with the appropriate values.

5. Start the Docker containers using the command:

   ```bash
   docker-compose -f docker-compose-local.yaml up -d
   ```

6. Create migrations using the command:

   ```bash
   alembic revision --autogenerate -m "comment"
   ```

   Replace `"comment"` with a comment describing the migration.

7. Apply the migrations using the command:

   ```bash
   alembic upgrade heads
   ```

8. Run the project using the command:

   ```bash
   python3 -m uvicorn backend.user.main:app --port 8000 --reload
   ```

   Your project is now running and accessible at `http://localhost:8000`.

---

Please note that these instructions assume the use of a Unix-like operating system such as Linux or macOS. If you are using Windows, some commands or steps may differ.

**Contributing**

Contributions to this FastAPI template application are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

Before contributing, please review the [contributing guidelines](CONTRIBUTING.md) for more information.

**License**

This project is licensed under the MIT License.

**Acknowledgements**

- The FastAPI framework: [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)
- Docker: [https://www.docker.com/](https://www.docker.com/)
- Alembic: [https://alembic.sqlalchemy.org/](https://alembic.sqlalchemy.org/)

**Contact**

For any questions or inquiries, please contact [geksbomba@gmail.com]

Feel free to explore the codebase and customize it to suit your project requirements. Happy coding!

**Note:**
This project is based on the code and concepts from the following repositories:

- [FastAPI Backend Template](https://github.com/Aeternalis-Ingenium/FastAPI-Backend-Template)
- [luchanos_oxford_university](https://github.com/luchanos/luchanos_oxford_university)

I have used their code as a reference and inspiration to implement my own FastAPI template. I would like to acknowledge and express my gratitude to the authors and contributors of these projects for their valuable work.
