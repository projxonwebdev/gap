import re

with open('src/pages/Coaching.jsx', 'r') as f:
    content = f.read()

# I will extract the Methodology Timeline section and the Development Tracks section
# and swap their order.

# Find the Development Tracks section
tracks_match = re.search(r'(<section className="space-y-12">\s*<div className="space-y-4">\s*<h2 className="font-headline-xl text-headline-xl text-on-surface border-b border-glass pb-4">Development Tracks</h2>.*?)</section>\s*{/\* Methodology Timeline \*/}', content, re.DOTALL)
tracks_html = tracks_match.group(1) + "</section>\n"

# Find the Methodology Timeline section
meth_match = re.search(r'({/\* Methodology Timeline \*/}\s*<section className="space-y-12 bg-charcoal/30 border border-glass rounded-xl p-8 md:p-12">.*?</section>)', content, re.DOTALL)
meth_html = meth_match.group(1) + "\n"


# Replace them in the full content
new_content = content.replace(tracks_match.group(0), meth_html + "\n      " + tracks_html.replace('</section>\n', '</section>'))
new_content = new_content.replace(meth_match.group(0), "")

with open('src/pages/Coaching.jsx', 'w') as f:
    f.write(new_content)

print("Coaching.jsx updated.")
