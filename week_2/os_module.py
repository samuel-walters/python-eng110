import os
import math, datetime, sys

working_directory = os.getcwd()
print(working_directory)


print(os.cpu_count())

# always yyyy-mm-dd (same for sql)
print(datetime.date.today())

print(sys.path)