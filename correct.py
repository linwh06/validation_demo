import urllib.parse
import unicodedata


def secure_filter(user_input):
    # 1. decode
    user_input = urllib.parse.unquote(user_input)

    # 2. normalize
    user_input = unicodedata.normalize("NFC", user_input)

    # 3. whitelist
    if not user_input.isalnum():
        return "BLOCKED"

    return "ALLOWED"
