import re

with open('src/pages/Coaching.jsx', 'r') as f:
    content = f.read()

# Replace HTML comments with JSX comments
content = re.sub(r'<!--(.*?)-->', r'{/*\1*/}', content)

with open('src/pages/Coaching.jsx', 'w') as f:
    f.write(content)

print("Coaching.jsx fixed comments.")
