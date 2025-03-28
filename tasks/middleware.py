# middleware.py
import logging  # Import logging module for logging error messages
from django.http import JsonResponse  # Import JsonResponse to return JSON responses for errors

# Create a logger for this module
logger = logging.getLogger(__name__)

class CustomExceptionMiddleware:
    """
    Middleware to catch exceptions globally and return a JSON response.
    Logs the error details and returns a 500 status code for internal errors.
    """

    def __init__(self, get_response):
        """
        Initialize the middleware with the next layer of middleware or view.

        Parameters:
        get_response: The next middleware or view to be called.
        """
        self.get_response = get_response  # Store the reference to the next layer

    def __call__(self, request):
        """
        Process the request and handle exceptions.

        Parameters:
        request: The incoming HTTP request.

        Returns:
        The HTTP response from the next layer.
        """
        try:
            response = self.get_response(request)  # Call the next middleware or view
            return response  # Return the response from the next layer
        except Exception as e:
            # Log the exception details
            logger.error(f"An error occurred: {str(e)}")
            # Return a JSON response with a 500 status code
            return JsonResponse({"detail": "An internal error occurred."}, status=500)