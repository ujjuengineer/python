# creating our custom error

class CustomError(Exception):
    def __init__(self, message, code):
        super().__init__(f"Error code {code}: {message}")

# err = CustomError('An error happende.', 500)

raise CustomError('An error happend!.', 500)