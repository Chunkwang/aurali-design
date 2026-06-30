import os
import re

base = "/Users/chunkwangwangjen/Screenshot Platform Idea"
files = ["dashboard.html", "project_step1.html", "my_projects.html", "project_step3.html"]

for fname in files:
    filepath = os.path.join(base, fname)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, "r") as f:
        content = f.read()

    # Find the main tag and replace max-w-[...] or max-w-xx with max-w-7xl
    # We want to replace any max-w-[1100px] or max-w-[1200px] or similar
    # For project_step3 and my_projects, they might not have a max-w on main, let's check
    
    # Let's target exactly what we saw earlier:
    content = re.sub(r'max-w-\[1100px\]', 'max-w-7xl', content)
    content = re.sub(r'max-w-\[1200px\]', 'max-w-7xl', content)
    
    with open(filepath, "w") as f:
        f.write(content)

print("Updated max-widths")
