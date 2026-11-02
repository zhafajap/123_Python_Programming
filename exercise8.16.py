# 1. Import seluruh module
import message_functions
message_functions.display_message()

# 2. Import fungsi tertentu
from message_functions import display_message
display_message()

# 3. Import fungsi dengan alias
from message_functions import display_message as dm
dm()

# 4. Import module dengan alias
import message_functions as mf
mf.display_message()

# 5. Import semua fungsi dari module
from message_functions import *
display_message()