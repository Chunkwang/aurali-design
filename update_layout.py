import os
import re

files = ["dashboard.html", "project_step1.html", "project_step2.html", "project_step3.html", "my_projects.html"]
base = "/Users/chunkwangwangjen/Screenshot Platform Idea"

for f in files:
    filepath = os.path.join(base, f)
    with open(filepath, "r") as file:
        content = file.read()
    
    # 1. Update w-64 to w-56 for sidebars
    content = re.sub(r'w-64', r'w-56', content)
    
    # 2. Nav padding: py-6 px-4 -> py-4 px-3 (and py-6 px-2 for step3)
    content = re.sub(r'py-6 px-4', r'py-4 px-3', content)
    content = re.sub(r'py-6 px-2', r'py-4 px-2', content)
    
    # 3. Logo text size: text-xl -> text-lg
    content = re.sub(r'text-xl(.*?>\s*Aurali)', r'text-lg\1', content)
    
    # 4. Logo subtitle size: text-[10px] -> text-[9px] (in the sidebar context usually near SaaS Dashboard)
    content = re.sub(r'text-\[10px\](.*?>\s*SaaS Dashboard)', r'text-[9px]\1', content)
    
    # 5 & 6. Nav Links update
    # The links are typically inside the nav, and have 'text-xs' and 'py-2 px-3' or 'py-2.5 px-3'
    # We can do a broader replace for sidebar links. Let's find the nav block and replace inside it.
    
    def process_nav(match):
        nav_content = match.group(0)
        # padding
        nav_content = re.sub(r'py-2 px-3', r'py-1.5 px-2.5', nav_content)
        nav_content = re.sub(r'py-2\.5 px-3', r'py-1.5 px-2.5', nav_content)
        # text size
        nav_content = re.sub(r'text-xs', r'text-[11px]', nav_content)
        return nav_content
        
    content = re.sub(r"(<(nav|aside)[^>]*>.*?)</(nav|aside)>", process_nav, content, flags=re.DOTALL)
    
    # 7. Header height and padding
    content = re.sub(r'h-14 px-8', r'h-12 px-6', content)
    
    # 8. Main padding
    content = re.sub(r'px-8 py-6', r'px-6 py-4', content)
    
    # 9. Main max-width
    content = re.sub(r'max-w-\[1200px\]', r'max-w-[1100px]', content)
    
    with open(filepath, "w") as file:
        file.write(content)
        
print("Updated layouts")
