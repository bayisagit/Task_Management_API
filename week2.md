Task Management API - API Endpoints
User Endpoints:
HTTP Method
Endpoint
Description
Authentication
POST
/api/register/
User registration
No
POST
/api/login/
User login and token generation
No
GET
/api/users/{id}/
Retrieve user details
Yes
PUT
/api/users/{id}/
Update user profile
Yes
DELETE
/api/users/{id}/
Delete user account
Yes





Task Endpoints:
HTTP Method
Endpoint
Description
Authentication
POST
/api/tasks/
Create a new task
Yes
GET
/api/tasks/
Retrieve all tasks
Yes
GET
/api/tasks/{id}/
Retrieve a specific task
Yes
PUT
/api/tasks/{id}/
Update a task
Yes
DELETE
/api/tasks/{id}/
Delete a task
Yes
PATCH
/api/tasks/{id}/complete/
Mark task as complete
Yes
PATCH
/api/tasks/{id}/incomplete/
Mark task as incomplete
Yes

