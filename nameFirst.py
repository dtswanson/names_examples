from platform import system as system_name  # Returns the system/OS name
from subprocess import call as system_call  # Execute a shell command

import time

firstName = input("What is your first name?")
print(firstName, "\n", firstName)

time.sleep(3)