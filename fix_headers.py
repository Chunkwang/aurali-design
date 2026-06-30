import os
import re

base = "/Users/chunkwangwangjen/Screenshot Platform Idea"

# Step 1: Remove TopAppBar from project_step1.html and my_projects.html
for fname in ["project_step1.html", "my_projects.html"]:
    with open(os.path.join(base, fname), "r") as f:
        content = f.read()
    
    # Matches <header ...>...</header> where it has TopAppBar or flex justify-end
    content = re.sub(r'<!-- TopAppBar -->\s*<header[^>]*>.*?</header>', '', content, flags=re.DOTALL)
    
    with open(os.path.join(base, fname), "w") as f:
        f.write(content)

# Step 2: Replace project_step1.html inner header
step1_path = os.path.join(base, "project_step1.html")
with open(step1_path, "r") as f:
    content = f.read()

new_step1_header = """      <!-- Header Area -->
      <header class="flex flex-col gap-1 shrink-0 mb-4">
        <div class="flex items-center gap-1.5 text-secondary font-label-caps text-label-caps uppercase tracking-wider text-[10px] mb-1">
          <span class="w-1.5 h-1.5 rounded-full bg-primary"></span>
          <span class="w-1.5 h-1.5 rounded-full bg-outline-variant"></span>
          <span class="w-1.5 h-1.5 rounded-full bg-outline-variant"></span>
          <span class="ml-1.5">Step 1 of 3</span>
        </div>
        <h1 class="text-3xl font-extrabold text-on-surface">Define the essence.</h1>
        <p class="text-xs text-secondary max-w-2xl mt-1">Provide the foundational details and core assets for your application. This shapes the creative direction of your generated screenshots.</p>
      </header>"""

content = re.sub(r'<!-- Header -->\s*<section[^>]*>.*?</section>', new_step1_header, content, flags=re.DOTALL)

with open(step1_path, "w") as f:
    f.write(content)

# Step 3: Replace project_step3.html inner header
step3_path = os.path.join(base, "project_step3.html")
with open(step3_path, "r") as f:
    content = f.read()

new_step3_header = """      <!-- Header Area -->
      <header class="flex flex-col gap-1 shrink-0 mb-4 text-left w-full">
        <div class="flex items-center gap-1.5 text-secondary font-label-caps text-label-caps uppercase tracking-wider text-[10px] mb-1">
          <span class="w-1.5 h-1.5 rounded-full bg-primary/40"></span>
          <span class="w-1.5 h-1.5 rounded-full bg-primary/40"></span>
          <span class="w-1.5 h-1.5 rounded-full bg-primary"></span>
          <span class="ml-1.5">Step 3 of 3</span>
        </div>
        <h1 class="text-3xl font-extrabold text-on-surface">Perfecting spatial rhythm</h1>
        <p class="text-xs text-secondary max-w-2xl mt-1 mb-6">Calculating margins, applying constraints, and rendering the final editorial layout.</p>
      </header>"""

content = re.sub(r'<span class="font-label-caps text-label-caps text-secondary tracking-widest uppercase mb-1.5 block text-\[10px\]">Step 3 of 3</span>\s*<h1[^>]*>Perfecting spatial rhythm</h1>\s*<p[^>]*>Calculating margins, applying constraints, and rendering the final editorial layout.</p>', new_step3_header, content, flags=re.DOTALL)
# The div container around it had class "text-center", change to "text-left"
content = re.sub(r'<div class="text-center z-10 max-w-md w-full px-4 shrink-0">', r'<div class="text-left z-10 max-w-xl w-full px-4 shrink-0">', content)

with open(step3_path, "w") as f:
    f.write(content)

print("Updated headers")
