# Linkpad

## Description

Linkpad is a web application that provides a platform for students, alumni, and staff to connect and interact within the educational institution's community. The application allows users to create profiles based on their role (Student, Alumni, Staff), showcasing their achievements, interests, and professional backgrounds.

## Installation

1. **Clone the repository:**
    ```sh
    git clone <repository_url>
    ```
2. **Navigate to the project directory:**
    ```sh
    cd linkpad
    ```
3. **Create a virtual environment (optional but recommended):**
    ```sh
    python3 -m venv env
    ```
4. **Activate the virtual environment:**
    - On Windows:
        ```sh
        env\Scripts\activate
        ```
    - On macOS and Linux:
        ```sh
        source env/bin/activate
        ```
5. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

1. **Rename the `.env.example` file to `.env`.**
2. **Update the `.env` file with your configuration settings (database, secret key, etc.).**

## Database Setup

1. **Run database migrations:**
    ```sh
    python manage.py migrate
    ```

## Running the Server

1. **Start the development server:**
    ```sh
    python manage.py runserver
    ```
2. **Open your web browser and navigate to `http://127.0.0.1:8000/`.**

## Usage

1. **Access the login page at `/login/` and the signup page at `/signup/`.**
2. **Enter your credentials to log in or sign up for a new account.**
3. **After logging in, users will be redirected to their respective profile pages based on their roles.**

## Troubleshooting

- If you encounter any issues during installation or setup, make sure you have followed all the steps correctly.
- If you're facing database-related errors, ensure that your database settings are configured correctly in the `.env` file.
- For any other technical issues, consult the Django documentation or seek assistance from the project maintainers.

## Contributing

1. **Fork the repository.**
2. **Create a new branch:**
    ```sh
    git checkout -b feature_branch
    ```
3. **Make your changes and commit them:**
    ```sh
    git commit -m "Add new feature"
    ```
4. **Push to the branch:**
    ```sh
    git push origin feature_branch
    ```
5. **Submit a pull request.**
