from django.contrib import messages

ERROR_MESSAGE = f"Sorry, we were unable to process that! Please make sure all " \
                f"your information is entered correctly."


def handle_validation_error(request):
    """
    Creates an error message to display in the browser when an error occurs on
    form submission
    """
    messages.error(request, ERROR_MESSAGE)
