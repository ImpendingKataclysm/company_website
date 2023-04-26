from django.contrib import messages


def handle_validation_error(request):
    error_message = f"Sorry, we were unable to process that! Please make" \
                    f" sure all your information is entered correctly."
    messages.error(request, error_message)
