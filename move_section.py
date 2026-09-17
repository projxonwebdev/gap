import re

# 1. Extract the section from Home.jsx
with open('src/pages/Home.jsx', 'r') as f:
    home_content = f.read()

# Pattern to extract the Why Choose GAP section (5.5)
# Using DOTALL to capture everything between 5.5 and 5.6
pattern = r'(\{\/\* 5\.5 Why Be In GAP \*\/\}\n<section.*?)\{\/\* 5\.6 Tech Stack \*\/\}'
match = re.search(pattern, home_content, re.DOTALL)

if not match:
    print("Could not find Why Choose GAP section in Home.jsx")
    exit(1)

why_gap_section = match.group(1)

# Remove the section from Home.jsx
new_home_content = home_content.replace(why_gap_section, '')

with open('src/pages/Home.jsx', 'w') as f:
    f.write(new_home_content)

# 2. Add the section to MIP.jsx and rename title
with open('src/pages/MIP.jsx', 'r') as f:
    mip_content = f.read()

# Change "Why Choose GAP?" to "Why Join GAP?"
why_gap_section = why_gap_section.replace('Why Choose GAP?', 'Why Join GAP?')
why_gap_section = why_gap_section.replace('Why Choose GAP', 'Why Join GAP')
# Rename comment
why_gap_section = why_gap_section.replace('{/* 5.5 Why Be In GAP */}', '{/* Why Join GAP */}')

# Insert it before the closing </div> of MIP.jsx
# We will just replace the last </div>\n  );\n} with the section and then the closing tags
mip_tail = '\n    </div>\n  );\n}'

if mip_content.endswith(mip_tail) or mip_content.endswith('\n    </div>\n  );\n}\n'):
    # Remove the tail
    base_mip = mip_content.rsplit('\n    </div>', 1)[0]
    new_mip_content = base_mip + '\n\n      ' + why_gap_section.strip() + '\n    </div>\n  );\n}\n'
    
    with open('src/pages/MIP.jsx', 'w') as f:
        f.write(new_mip_content)
    print("Successfully moved section to MIP.jsx")
else:
    print("Could not cleanly insert into MIP.jsx")

