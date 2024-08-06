# Catalyst Count

## Setup Instructions

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/catalyst-count.git
    cd catalyst-count
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**
    - Create a `.env` file in the project root and add your environment variables (refer to `.env.example`).

5. **Apply migrations and run the server:**
    ```sh
    python manage.py migrate
    python manage.py runserver
    ```

6. **Open the application in your browser at** `http://127.0.0.1:8000`.

## Features

- User authentication
- CSV data upload with progress indication
- Data filtering and count display

## Testing

To run tests:
```sh
python manage.py test
