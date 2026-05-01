def filter_input(user_input):
    if "<script>" in user_input.lower():
        return "BLOCKED"
    return "ALLOWED"

print(filter_input("&#60;script&#62;"))  # ALLOWED
