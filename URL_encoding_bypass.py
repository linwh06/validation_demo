import urllib.parse

def filter_input(user_input):
    if "<script>" in user_input.lower():
        return "BLOCKED"
    return "ALLOWED"

print(filter_input("%3Cscript%3E"))  # ALLOWED

decoded = urllib.parse.unquote("%3Cscript%3E")
print(decoded)  # <script>
