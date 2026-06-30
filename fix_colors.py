import os
import re

base = "/Users/chunkwangwangjen/Screenshot Platform Idea"

files = ["dashboard.html", "project_step1.html", "project_step2.html", "project_step3.html", "my_projects.html"]

surface_card_css = """
    .surface-card {
        background-color: #F5F2EC;
        box-shadow: 0 4px 20px rgba(96, 94, 91, 0.08);
    }
"""

for fname in files:
    filepath = os.path.join(base, fname)
    with open(filepath, "r") as f:
        content = f.read()

    # 1. Force body background color to match step 2
    if 'body { background-color:' in content:
        content = re.sub(r'body \{ background-color: #[a-fA-F0-9]+; \}', 'body { background-color: #FBF9F6 !important; }', content)
    else:
        # Add it to the top of <style>
        content = re.sub(r'<style>', '<style>\n    body { background-color: #FBF9F6 !important; }', content)

    # 2. Add .surface-card to style if not present
    if '.surface-card {' not in content:
        content = re.sub(r'</style>', surface_card_css + '</style>', content)

    # 3. Replace bg-surface-container-lowest with surface-card (for step1, my_projects)
    content = content.replace('bg-surface-container-lowest', 'surface-card')
    
    # 4. Replace card-surface with surface-card (for dashboard)
    content = content.replace('card-surface', 'surface-card')

    # Note: step2 already uses surface-card and FBF9F6. Step 3 uses paper-texture which also uses FBF9F6.

    with open(filepath, "w") as f:
        f.write(content)

print("Colors standardized across all files.")
