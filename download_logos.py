import urllib.request
import os

logos = {
    'github-logo.svg': 'https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg',
    'vercel-logo.svg': 'https://upload.wikimedia.org/wikipedia/commons/5/5e/Vercel_logo_black.svg',
    'aws-logo.svg': 'https://upload.wikimedia.org/wikipedia/commons/9/93/Amazon_Web_Services_Logo.svg'
}

for name, url in logos.items():
    try:
        urllib.request.urlretrieve(url, os.path.join('public', name))
        print(f"Downloaded {name}")
    except Exception as e:
        print(f"Failed to download {name}: {e}")
