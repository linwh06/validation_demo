def filter_input(user_input):
    if "<script>" in user_input.lower():
        return "BLOCKED"
    return "ALLOWED"

s1 = "example"
s2 = "ｅxample"

print(s1 == s2)  # False
print(filter_input(s2))  # ALLOWED
