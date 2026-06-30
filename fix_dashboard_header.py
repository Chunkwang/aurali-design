import os
import re

base = "/Users/chunkwangwangjen/Screenshot Platform Idea"
filepath = os.path.join(base, "dashboard.html")

with open(filepath, "r") as file:
    content = file.read()

# Remove the TopAppBar header
content = re.sub(r'<!-- TopAppBar -->\s*<header[^>]*>.*?</header>', '', content, flags=re.DOTALL)

# Let's adjust the padding on main to make it look balanced if needed.
# Since we removed a 48px header, main might feel a bit tight at the top. Let's change py-4 to py-6 on the main tag for dashboard.
# Find: <main class="flex-grow flex flex-col px-6 py-4... or similar
content = re.sub(r'(<main[^>]*?py-)4', r'\g<1>8', content)

with open(filepath, "w") as file:
    file.write(content)

print("Dashboard header removed and padding adjusted.")
