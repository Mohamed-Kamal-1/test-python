# Import the `datetime` module
import datetime

# Import the `importlib` module
import importlib

# Reload the `datetime` module
importlib.reload(datetime)

# Get the current date and time
today = datetime.today()

# Print the current date and time
print(today)
