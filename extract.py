import re
with open('stitch_home_update.html', 'r') as f:
    html = f.read()

sections = html.split('<section')
if len(sections) > 2:
    new_content = '<section' + '<section'.join(sections[2:])
    new_content = new_content.split('</main>')[0]
    with open('extracted_sections.html', 'w') as f:
        f.write(new_content)
    print("Extracted", len(sections)-2, "sections")
