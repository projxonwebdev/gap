import re

with open('src/pages/coaching_gen.html', 'r') as f:
    content = f.read()

# Extract main tag
match = re.search(r'<main.*?>(.*?)</main>', content, re.DOTALL)
if not match:
    print("Could not find main tag")
    exit(1)

html_content = match.group(1)

# Fix class to className
html_content = html_content.replace('class="', 'className="')
# Fix self-closing tags if any (img, input, hr) but here we might not have any.
# In React, things like <br> must be <br />
html_content = html_content.replace('<br>', '<br />')
html_content = html_content.replace('M&amp;A', 'M&amp;A') # it's already encoded, React is fine with &amp; if it's not inside {}

# Remove the hero section because the prompt requested the GAP navigation.
# I'll just find Section 1 and Section 2.
s1 = re.search(r'<!-- Section 1: The GAP Methodology -->(.*?)<!-- Section 2: Development Tracks -->', html_content, re.DOTALL)
s2 = re.search(r'<!-- Section 2: Development Tracks -->(.*?)$', html_content, re.DOTALL)

if s1 and s2:
    # Just render Section 1 and Section 2
    jsx_body = s1.group(0) + "\n" + s2.group(1)
else:
    # fallback to whole main
    jsx_body = html_content

jsx = f"""import React from 'react';

export default function Coaching() {{
  return (
    <div className="space-y-section-gap pt-12 pb-24">
      {jsx_body}
    </div>
  );
}}
"""

with open('src/pages/Coaching.jsx', 'w') as f:
    f.write(jsx)

print("Coaching.jsx rebuilt with Stitch HTML.")
