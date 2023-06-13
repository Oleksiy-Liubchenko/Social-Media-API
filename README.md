# DRF Social Media API

## Project Description

This project aims to build a powerful RESTful API for a social media platform. The API provides users with a wide range of features,
including profile creation, following other users, post creation and retrieval, 
and various social media actions. The implementation utilizes Django REST framework, with token-based authentication for secure user access.

## Key Features

### User Registration and Authentication

- Users can easily register by providing their email and password to create an account.
- Token-based authentication is implemented, allowing users to log in and receive a token for subsequent API requests.
- Users can log out, which invalidates their token and ensures account security.

### User Profile

- Users have the ability to create and update their profiles, including profile pictures, bios, and additional details.
- Profiles can be retrieved by the respective user or by other users who are interested.
- Users can search for other users based on their usernames or other specified criteria.

### Follow/Unfollow

- Users can effortlessly follow and unfollow other users, building their own network of connections.
- The API provides endpoints to view the list of users they are following and the list of users who are following them.

### Post Creation and Retrieval

- Users can create engaging posts, sharing their thoughts and experiences through text content.
- Retrieving posts is made simple, allowing users to access their own posts as well as posts from users they are following.
- The API also enables post retrieval based on hashtags or other specified criteria, enhancing content discovery.

### API Permissions

- Certain actions, such as creating posts and following/unfollowing users, require authentication to ensure data security.
- Users can only update and delete their own posts ensuring content ownership and privacy.
- Profile updates and deletions are also limited to the respective user, providing control over personal information.

### API Documentation

- The API is meticulously documented, providing clear instructions on how to utilize each endpoint effectively.
- The documentation includes sample API requests and responses, helping developers integrate the API seamlessly.

## Installation

Python must be installed before the next steps:

```shell
git clone https://github.com/Oleksiy-Liubchenko/Social-Media-API.git
cd Social-Media-API
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```
