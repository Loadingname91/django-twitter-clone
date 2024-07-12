# Twitter Clone API

This is a backend API for a Twitter clone built with Django and Django REST Framework.

## Setup

1. Clone the repository
2. Create a virtual environment and activate it
3. Install dependencies: `pip install -r requirements.txt`
4. Run migrations: `python manage.py migrate`
5. Create a superuser: `python manage.py createsuperuser`
6. Run the server: `python manage.py runserver`

## API Endpoints

- User Registration: POST /api/user/register/
- User Login: POST /api/user/login/
- User Logout: POST /api/user/logout/
- Create Tweet: POST /api/tweet/create/
- List Tweets: GET /api/tweet/list/
- Like Tweet: POST /api/tweet/like/<tweet_id>/

## Admin

Access the admin interface at /admin/ using your superuser credentials.