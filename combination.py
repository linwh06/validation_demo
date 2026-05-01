def filter_input(user_input):
    if "<script>" in user_input.lower():
        return "BLOCKED"
    return "ALLOWED"

payload = "%3Cscrіpt%3E"
print(filter_input(payload))  # ALLOWED
