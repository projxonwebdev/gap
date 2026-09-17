import re

with open('src/pages/Home.jsx', 'r') as f:
    text = f.read()

# Remove space-y-section-gap from the root div
text = text.replace('<div className="space-y-section-gap">', '<div className="flex flex-col">')

# We only want to modify sections AFTER the hero section.
hero_end = text.find('</section>') + 10
hero = text[:hero_end]
rest = text[hero_end:]

# In the rest, change bg-charcoal to bg-obsidian
rest = rest.replace('bg-charcoal', 'bg-obsidian')

# In the rest, reduce py-section-gap to py-16 md:py-24
rest = rest.replace('py-section-gap', 'py-16 md:py-24')

with open('src/pages/Home.jsx', 'w') as f:
    f.write(hero + rest)

print("Updates applied.")
