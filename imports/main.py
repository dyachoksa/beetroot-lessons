import logic
import sys

sys.path.append("..\\extra-modules")

# print("Paths:", sys.path)

import auth_config
import security_config
# from auth_config import TIMEOUT as AUTH_TIMEOUT
# from security_config import SECRET_KEY, TIMEOUT

print("Name:", logic.name)
print("Secret key:", security_config.SECRET_KEY)
print("Security Timeout:", security_config.TIMEOUT)
print("Auth Timeout:", auth_config.TIMEOUT)
