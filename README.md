# Finance-UI REST API

This API app provides backend support for the Finance UI application. It uses SQLAlchemy as the Object-Relational Mapping (ORM) tool to interact with a PostgreSQL database and Alembic for database migrations. Additionally, the application is containerized using Docker for easy deployment and scalability.

## Table of Contents

- [Getting Started](https://gitlab.com/justas-finance-app/finance-app-api/#getting-started)
  - [Prerequisites](https://gitlab.com/justas-finance-app/finance-app-api/#prerequisites)
  - [Installation](https://gitlab.com/justas-finance-app/finance-app-api/#installation)
- [Usage](https://gitlab.com/justas-finance-app/finance-app-api/#usage)
  - [Running the API](https://gitlab.com/justas-finance-app/finance-app-api/#running-the-api)
  - [API Documentation](https://gitlab.com/justas-finance-app/finance-app-api/#api-documentation)
  - [Database Migrations](https://gitlab.com/justas-finance-app/finance-app-api/#database-migrations)

## Getting Started

### Prerequisites

- Python 3.6 or higher installed.
- Docker

### Installation

1. Clone this repository
2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Build and start Docker containers:
   ```bash
   docker compose build
   docker compose up
   ```
5. Perform the initial database setup and migrations:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

## Configuration (ENV variables)

Make sure to configure environment variables:

```bash
cp .env.dist .env
```

## Usage

### Running the API

To run the Finance-UI REST API, use the following command (in virtual environment):

```bash
flask run
```

This will start the API server, and it will be accessible at `http://localhost:5000/api/v1`.

### API Documentation

Once the flask server is running you can access the documentation at `http://localhost:5000/swagger-ui`

### Database Migrations

We use Alembic for database migrations. To generate a new migration, run:

```bash
flask db migrate -m "Your migration message"
```

To apply the migrations, use:

```bash
flask db upgrade
```
