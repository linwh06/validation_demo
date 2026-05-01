import urllib.parse

def filter_input(user_input):
    if "script" in user_input.lower():
        return "BLOCKED"
    return "ALLOWED"

print(filter_input("<script>"))   # BLOCKED
print(filter_input("<sсrіpt>"))   # ALLOWED

print("scrіpt" == "script")
