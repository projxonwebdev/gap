import re

with open('src/pages/Projects.jsx', 'r') as f:
    content = f.read()

# Remove Internal Projects
content = re.sub(r'      \{/\* Internal Projects \*/\}.*?      </section>\n\n', '', content, flags=re.DOTALL)

# Remove External Projects
content = re.sub(r'      \{/\* External Projects \*/\}.*?      </section>\n\n', '', content, flags=re.DOTALL)

with open('src/pages/Projects.jsx', 'w') as f:
    f.write(content)

print("Removed internal and external projects.")
