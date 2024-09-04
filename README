# Song Lyrics Analyzer

## Table of Contents
- [Song Lyrics Analyzer](#song-lyrics-analyzer)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Features](#features)
  - [Technologies Used](#technologies-used)
  - [Prerequisites](#prerequisites)
  - [Setup and Installation](#setup-and-installation)
  - [Usage Guide](#usage-guide)
  - [Development](#development)
    - [Making Changes](#making-changes)
    - [Running Tests](#running-tests)
    - [Debugging](#debugging)
  - [Project Structure](#project-structure)
  - [API Reference](#api-reference)
  - [Contributing](#contributing)
  - [License](#license)

## Overview
Song Lyrics Analyzer is a web application that provides insights into song lyrics. It allows users to input a song's artist and title, retrieve lyrics using the MusixMatch API, and receive a summary of the lyrics along with a list of countries mentioned using OpenAI's GPT model.

## Features
- Secure user authentication system (admin-only access)
- Song input functionality (artist and title)
- Automatic lyrics retrieval using MusixMatch API
- AI-powered lyric summarization using OpenAI GPT
- Country name extraction from lyrics
- Performance-optimized caching system
- Docker containerization for consistent development and deployment

## Technologies Used
- Python 3.12
- Django 5.0.1
- OpenAI GPT-3.5-turbo API
- MusixMatch API
- Docker and Docker Compose
- HTML/JavaScript (Frontend)
- SQLite (Development Database)

## Prerequisites
Before you begin, ensure you have the following installed on your system:
- [Docker](https://docs.docker.com/get-docker/) (version 20.10.0 or later)
- [Docker Compose](https://docs.docker.com/compose/install/) (version 1.29.0 or later)
- Git (for cloning the repository)

You will also need:
- An OpenAI API key (obtainable from [OpenAI's website](https://platform.openai.com/))
- A MusixMatch API key (obtainable from [MusixMatch's developer portal](https://developer.musixmatch.com/))

## Setup and Installation

Follow these steps to get the Song Lyrics Analyzer up and running on your local machine:

1. **Clone the Repository**
   Open a terminal and run:
   ```
   git clone https://github.com/akhossanX/lyrics_analyzer.git
   cd lyrics_analyzer
   ```

2. **Environment Configuration**
   Create a `.env` file in the project root directory and add the following environment variables:
   ```
   OPENAI_API_KEY=your_openai_api_key
   MUSIXMATCH_API_KEY=your_musix_match_api_key
   SECRET_KEY=your_secret_key
   DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 0.0.0.0
   DEBUG=1
   ```
   Note: The values provided here are examples. Please replace them with your actual API keys and preferred settings.

   - `OPENAI_API_KEY`: Your OpenAI API key
   - `MUSIXMATCH_API_KEY`: Your MusixMatch API key
   - `SECRET_KEY`: A secret key for Django. Choose a unique, unpredictable value
   - `DJANGO_ALLOWED_HOSTS`: Hosts/domain names that this Django site can serve
   - `DEBUG`: Set to 1 for development, 0 for production

3. **Build the Docker Container**
   Run the following command to build the Docker image:
   ```
   docker-compose build
   ```

4. **Database Migration**
   Before starting the application, you need to apply the database migrations:
   ```
   docker-compose run --rm web python manage.py migrate
   ```
   This command creates the necessary database tables.

5. **Create a Superuser**
   Create an admin account to access the application:
   ```
   docker-compose run --rm web python manage.py createsuperuser
   ```
   Follow the prompts to set up your admin username and password.

6. **Start the Application**
   Launch the application using:
   ```
   docker-compose up
   ```
   The application will be available at `http://localhost:8000`

## Usage Guide

1. **Accessing the Application**
   Open your web browser and go to `http://localhost:8000`

2. **Logging In**
   - Click on the login link or go to `http://localhost:8000/admin`
   - Enter the superuser credentials you created during setup

3. **Analyzing Song Lyrics**
   - On the main page, you'll see a form to input song details
   - Enter the artist name and song title
   - Click "Add Song" to submit the form
   - The application will fetch the lyrics using the MusixMatch API, generate a summary using OpenAI GPT, and list mentioned countries
   - View the results displayed on the page

   **Important Note: Only admin users have permission to add and create songs. Make sure you're logged in as an admin user to access this functionality.**

4. **Logging Out**
   - Use the logout option in the top right corner of the page when you're finished.

## Development

### Making Changes
1. Modify the code in your preferred editor
2. If you make changes to the Django models, create new migrations:
   ```
   docker-compose run --rm web python manage.py makemigrations
   ```
3. Apply the new migrations:
   ```
   docker-compose run --rm web python manage.py migrate
   ```
4. Rebuild and restart the container to reflect your changes:
   ```
   docker-compose up --build
   ```

### Running Tests
No tests are available for the moment.

### Debugging
- Check Docker logs: `docker-compose logs`
- Access Django shell: `docker-compose run --rm web python manage.py shell`

## Project Structure
```
song-lyrics-analyzer/
├── lyrics_analyzer/        # Main Django project directory
│   ├── settings.py         # Project settings
│   ├── urls.py             # Main URL configuration
│   └── wsgi.py             # WSGI configuration
├── songs/                  # Django app directory
│   ├── models.py           # Database models
│   ├── admin.py            # Admin interface
│   ├── views.py            # View functions
│   ├── apps.py             # App configuration
│   ├── tests.py            # Tests
│   ├── urls.py             # Url configuration
│   ├── utils.py            # Utility functions
│   ├── forms.py            # Form definitions
│   ├── services.py         # Business logic and API interactions
│   └── templates/          # HTML templates
│       └── songs/
│           └── index.html
│           └── login.html
├── Dockerfile              # Docker configuration
├── templates/ 
|   └── base.html          
├── docker-compose.yml      # Docker Compose configuration
├── requirements.txt        # Python dependencies
├── manage.py               # Django management script
└── README.md               # This file
```

## API Reference
This project utilizes the following APIs:
- OpenAI GPT-3.5-turbo model for lyric analysis. For detailed information, refer to the [OpenAI API documentation](https://platform.openai.com/docs/api-reference).
- MusixMatch API for lyrics retrieval. For more information, visit the [MusixMatch API documentation](https://developer.musixmatch.com/documentation).

## Contributing
We welcome contributions to the Song Lyrics Analyzer project. Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

For major changes, please open an issue first to discuss what you would like to change.

## License
This project is distributed under the MIT License. See the `LICENSE` file in the repository for full details.