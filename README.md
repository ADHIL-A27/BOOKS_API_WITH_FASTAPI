Bookly - REST API for Book Reviews
Bookly is a REST API designed for a book review web service. It allows users to manage books, add reviews, and tag books for better organization. This API is built using FastAPI, a modern, fast (high-performance) web framework for building APIs with Python.





Features
Book Management:
Create, read, update, and delete books.
Add tags to books for better categorization.
Review Management:
Add reviews to books.
Retrieve reviews for specific books.
Authentication:
Secure endpoints with authentication.
Error Handling:
Custom error handling for better debugging.
Middleware:
Custom middleware for request/response processing.













celery commands

celery -A src.celery_tasks.c_app worker --loglevel=info --pool=solo
celery -A src.celery_tasks.c_app flower --address=127.0.0.1
