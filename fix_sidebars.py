import os
import re

files = {
    'dashboard.html': 'Home',
    'project_step1.html': 'New Project',
    'project_step2.html': 'New Project',
    'project_step3.html': 'New Project',
    'my_projects.html': 'My Projects'
}
base = "/Users/chunkwangwangjen/Screenshot Platform Idea"

# Step 1: Extract sidebar from step2
with open(os.path.join(base, "project_step2.html"), "r") as f:
    step2_content = f.read()
    
# Extract the aside block
aside_match = re.search(r'(<aside[^>]*>.*?</aside>)', step2_content, re.DOTALL)
if not aside_match:
    print("Could not find aside in step2")
    exit(1)
base_aside = aside_match.group(1)

# Step 2: Remove "SaaS Dashboard" from the base aside
# Find: <span class="text-secondary ...">SaaS Dashboard</span>
base_aside = re.sub(r'<span[^>]*SaaS Dashboard</span>\n?', '', base_aside)

# Function to set active link
def set_active_link(aside_html, active_label):
    # Reset all links to default inactive state
    # First, let's find the active one in step2 and make it inactive
    # In step2, "New Project" is active: text-primary, border-r-4, bg-surface-container-high, style FILL 1
    # Actually, it's easier to just reset all to a standard template and then apply active state.
    
    # Let's simplify: replace active classes with inactive for all
    aside_html = re.sub(r'text-primary dark:text-primary-fixed-dim font-bold border-r-4 border-primary bg-surface-container-high dark:bg-secondary-container active:scale-95 transition-transform group text-\[11px\]',
                        r'text-secondary dark:text-secondary-fixed-dim hover:bg-surface-container-high dark:hover:bg-secondary-container transition-colors duration-200 active:scale-95 transition-transform group text-[11px] font-semibold',
                        aside_html)
    aside_html = re.sub(r"style=\"font-variation-settings: 'FILL' 1;\"", r"group-hover:text-primary transition-colors", aside_html)
    
    # Now set the desired one to active
    # We look for the <a> containing the active_label
    pattern = r'(<a[^>]*text-secondary[^>]*>)\s*(<span class="material-symbols-outlined text-sm )group-hover:text-primary transition-colors(">[^<]+</span>)\s*(<span>' + active_label + r'</span>)\s*</a>'
    replacement = r'\1\n        \2style="font-variation-settings: \'FILL\' 1;"\3\n        \4\n      </a>'
    
    # The \1 contains the a tag with inactive classes. We need to replace them.
    # Let's do it manually by finding the a tag block
    parts = aside_html.split('</a>')
    for i, part in enumerate(parts):
        if active_label in part and '<a ' in part:
            # Found the block, make it active
            part = re.sub(r'text-secondary dark:text-secondary-fixed-dim hover:bg-surface-container-high dark:hover:bg-secondary-container transition-colors duration-200 active:scale-95 transition-transform group text-\[11px\] font-semibold',
                          r'text-primary dark:text-primary-fixed-dim font-bold border-r-4 border-primary bg-surface-container-high dark:bg-secondary-container active:scale-95 transition-transform group text-[11px]', part)
            part = re.sub(r'group-hover:text-primary transition-colors', r'style="font-variation-settings: \'FILL\' 1;"', part)
            parts[i] = part
    
    return '</a>'.join(parts)

# Process all files
for f, active_label in files.items():
    filepath = os.path.join(base, f)
    with open(filepath, "r") as file:
        content = file.read()
        
    # Replace existing <nav> or <aside> sidebar
    new_aside = set_active_link(base_aside, active_label)
    content = re.sub(r'<(nav|aside)\s+class="[^>]*w-(64|16|56)[^>]*>.*?</\1>', new_aside, content, flags=re.DOTALL)
    
    # Write back
    with open(filepath, "w") as file:
        file.write(content)
        
print("Updated sidebars")
