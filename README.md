

---

# Task Management API Documentation

Welcome to the **Task Management API**. This API is designed to help users manage tasks, categories, and user accounts efficiently. It allows you to perform operations such as creating, updating, retrieving, and deleting tasks and categories, with secure authentication. This README provides an overview of the API endpoints and how to interact with the system.

## Table of Contents
1. [Introduction](#introduction)
2. [Base URL](#base-url)
3. [Authentication](#authentication)
4. [User Endpoints](#user-endpoints)
   - [Login](#login)
   - [Register](#register)
   - [Logout](#logout)
   - [Password Reset](#password-reset)
5. [Task Management Endpoints](#task-management-endpoints)
   - [List All Tasks](#list-all-tasks)
   - [Create a New Task](#create-a-new-task)
   - [Retrieve a Specific Task](#retrieve-a-specific-task)
   - [Update a Specific Task](#update-a-specific-task)
   - [Delete a Specific Task](#delete-a-specific-task)
6. [Category Management Endpoints](#category-management-endpoints)
   - [List All Categories](#list-all-categories)
   - [Create a New Category](#create-a-new-category)
   - [Retrieve a Specific Category](#retrieve-a-specific-category)
   - [Update a Specific Category](#update-a-specific-category)
7. [Contributing](#contributing)
8. [License](#license)

## Introduction
The Task Management API enables users to manage their tasks and categories in a simple, efficient way. It is ideal for managing daily activities and personal projects, providing easy access to track and update tasks.

This documentation provides detailed information on how to interact with the API. Each section includes the relevant endpoints, HTTP methods, request bodies, and example responses.

## Base URL
The base URL for accessing the API is:
```
http://127.0.0.1:8000/api/
```

All API requests must start with this base URL, followed by the appropriate endpoint.

## Authentication
This API uses **token-based authentication**. Users must log in to obtain a token, which should be included in the `Authorization` header of all subsequent requests.

### Login
To log in, send a `POST` request with your `username` and `password`:

**Endpoint**: `/accounts/login/`  
**Method**: `POST`  
**Request Body**:
```json
{
    "username": "new_user",
    "password": "asdasdasd"
}
```
**Response**:
```json
{
    "token": "your_token_here"
}
```

This will return a token that must be included in the `Authorization` header of future requests. For example:
```
Authorization: Token your_token_here
```

### Register
To create a new user, send a `POST` request with the required fields:

**Endpoint**: `/accounts/register/`  
**Method**: `POST`  
**Request Body**:
```json
{
    "username": "new_user",
    "email": "user@example.com",
    "password": "your_password"
}
```
**Response**:
```json
{
    "id": 1,
    "username": "new_user",
    "email": "user@example.com"
}
```

### Logout
To log out, send a `POST` request with the token in the header:

**Endpoint**: `/accounts/logout/`  
**Method**: `POST`  
**Headers**:
```
Authorization: Token your_token_here
```
**Response**: `204 No Content`

### Password Reset
To request a password reset, send a `POST` request with your email:

**Endpoint**: `/accounts/password-reset/`  
**Method**: `POST`  
**Request Body**:
```json
{
    "email": "user@example.com"
}
```
**Response**:
```json
{
    "message": "If an account with that email exists, a password reset link has been sent."
}
```

### Password Reset Confirmation
To confirm the password reset, send a `POST` request with the necessary parameters:

**Endpoint**: `/accounts/password-reset-confirm/`  
**Method**: `POST`  
**Request Body**:
```json
{
    "Uidb64": "NQ",
    "Token": "a9cb04b669f5d9025ba5e33db56c6516cb177964",
    "new_password": "87654321"
}
```
**Response**:
```json
{
    "message": "Password has been reset."
}
```

## Task Management Endpoints

### List All Tasks
To retrieve all tasks associated with the logged-in user, send a `GET` request:

**Endpoint**: `/tasks/list/`  
**Method**: `GET`  
**Headers**:
```
Authorization: Token your_token_here
```
**Response**:
```json
[
    {
        "id": 12,
        "title": "Complete project",
        "description": "Finalize and submit the project.",
        "due_date": "2025-01-15T12:00:00Z",
        "priority": "High",
        "status": "Pending",
        "completed_at": null,
        "user": 14,
        "category": null
    }
]
```

### Create a New Task
To create a new task, send a `POST` request with the necessary details:

**Endpoint**: `/tasks/create/`  
**Method**: `POST`  
**Headers**:
```
Authorization: Token your_token_here
```
**Request Body**:
```json
{
    "user": 2,
    "title": "Complete project",
    "description": "Finalize and submit the project.",
    "due_date": "2025-01-15T12:00:00Z",
    "priority": "High",
    "status": "Pending"
}
```
**Response**:
```json
{
    "id": 11,
    "title": "Complete project",
    "description": "Finalize and submit the project.",
    "due_date": "2025-01-15T12:00:00Z",
    "priority": "High",
    "status": "Pending",
    "completed_at": null,
    "user": 5,
    "category": null
}
```

### Retrieve a Specific Task
To retrieve a specific task, send a `GET` request with the task's ID:

**Endpoint**: `/tasks/{id}/`  
**Method**: `GET`  
**Headers**:
```
Authorization: Token your_token_here
```
**Response**:
```json
{
    "id": 11,
    "title": "Complete project",
    "description": "Finalize and submit the project.",
    "due_date": "2025-01-15T12:00:00Z",
    "priority": "High",
    "status": "Pending",
    "completed_at": null,
    "user": 5,
    "category": null
}
```

### Update a Specific Task
To update an existing task, send a `PUT` request with the updated details:

**Endpoint**: `/tasks/{id}/`  
**Method**: `PUT`  
**Headers**:
```
Authorization: Token your_token_here
```
**Request Body**:
```json
{
    "title": "Updated Task",
    "description": "Updated description",
    "due_date": "2025-10-11T00:00:00Z",
    "priority": "Low",
    "status": "Pending",
    "category": null,
    "recurrence": "None"
}
```
**Response**:
```json
{
    "id": 1,
    "title": "Updated Task",
    "description": "Updated description",
    "due_date": "2024-10-01T00:00:00Z",
    "priority": "Low",
    "status": "Pending",
    "category": null,
    "recurrence": "None"
}
```

### Delete a Specific Task
To delete a specific task, send a `DELETE` request:

**Endpoint**: `/tasks/{id}/`  
**Method**: `DELETE`  
**Headers**:
```
Authorization: Token your_token_here
```
**Response**: `204 No Content`

## Category Management Endpoints

### List All Categories
To retrieve all categories, send a `GET` request:

**Endpoint**: `/categories/list/`  
**Method**: `GET`  
**Headers**:
```
Authorization: Token your_token_here
```
**Response**:
```json
[
    {
        "id": 5,
        "name": "Electronics"
    }
]
```

### Create a New Category
To create a new category, send a `POST` request:

**Endpoint**: `/categories/create/`  
**Method**: `POST`  
**Headers**:
```
Authorization: Token your_token_here
```
**Request Body**:
```json
{
    "name": "Electronics"
}
```
**Response**:
```json
{
    "id": 5,
    "name": "Electronics"
}
```

### Retrieve a Specific Category
To retrieve a specific category, send a `GET` request with the category's ID:

**Endpoint**: `/categories/{id}/`  
**Method**: `GET`

## Conclusion
This API provides an efficient way to manage tasks and categories, supporting a variety of operations for users and administrators. It uses token-based authentication to secure access and provide a seamless user experience.

---
