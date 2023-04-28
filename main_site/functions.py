from django.contrib import messages

ERROR_MESSAGE = f"Sorry, we were unable to process that! Please make sure all " \
                f"your information is entered correctly."


def handle_validation_error(request):
    messages.error(request, ERROR_MESSAGE)
