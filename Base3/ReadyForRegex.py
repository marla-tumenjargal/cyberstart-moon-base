import re

html = """
<html>
<head>
    <title>Regex Demo</title>
</head>
<body>
    <div class='firstDiv'>Hello</div>
    <div class='secondDiv'>Hello</div>
</body>
</html>
"""

class_array = re.findall(r"<div\s+class='([^']+)'", html)
print('\n'.join(class_array))
