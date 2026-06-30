# Project Context: Aurali Screenshot Wrap Platform

This document outlines the product description, technical architecture, frontend implementation standards, and development roadmap for **Aurali**, an AI-powered App Store and Play Store screenshot marketing generator.

---

## 1. Product Overview
Aurali is designed for indie hackers, startup founders, and solo developers to instantly transform raw, unedited screenshots into premium App Store and Play Store promotional graphics. 

By automating background generation, device framing, dynamic visual pacing, and panoramic layout styling, the platform eliminates the need for expensive design resources or complex design software (like Figma or Photoshop).

---

## 2. Technical Stack
Aurali is architected as a lightweight, performant, static-first client application, avoiding the overhead of heavy framework bundles while maintaining a high degree of interactivity:

*   **Markup:** Standard Semantic HTML5 with dynamic component templates.
*   **Styling:** Utility-first CSS using Tailwind CSS (loaded via CDN) combined with Vanilla CSS variables and custom classes for premium visual touches (e.g. glassmorphism, floating shadows).
*   **Fonts:** Inter and Instrument Serif (loaded via Google Fonts API) to establish a premium warm-beige typography system.
*   **Icons:** Material Symbols Outlined (Google Material Icons).
*   **State & Transitions:** Pure Vanilla JavaScript (ES6+) managing browser DOM states, multi-page data flows, URL-based transitions, and local styling animations.

---

## 3. Architecture & File Structure
The project is built around a progressive multi-step wizard architecture. The flow is partitioned logically across specialized single-purpose HTML pages:

```
├── index.html            # Product Landing Page & Interactive Walkthrough
├── dashboard.html        # Main Client Workspace Dashboard (Home)
├── my_projects.html      # User Projects Manager (Grid view of draft screenshot wraps)
├── project_step1.html    # Step 1: Creative Context, App Identity, & Raw Uploads
├── project_step2.html    # Step 2: Visual Narrative Direction & Palette Presets
├── project_step3.html    # Step 3: Loading Engine / Generating State Transitions
├── project_step4.html    # Step 4: Live Preview Editor (Dynamic Zoom & Parameter Dock)
└── assets/               # Core Static Assets
    ├── ShutEye/          # Sample raw screens used for client mockups
    └── loop_video/       # Product walkthrough animations and WebP loops
```

### Key Architectural Patterns:
*   **Sidebar Layout:** A global navigation sidebar standardizes user placement across all states.
*   **URL-Driven State Transfer:** Context parameters (like coordinate scaling or demo-mode flags) are propagated between page boundaries using URL query strings (e.g., `?demo=true&zoomX=...`).
*   **Self-Contained Interactions:** Each page houses its own inline style overrides and JavaScript logic at the bottom of the body to remain modular and fast-loading.

---

## 4. Coding & Design Conventions
To maintain technical quality and visual consistency, all code modifications must respect the following standards:

1.  **Layout Width Constraint:** All main dashboard and project workspace content wrappers (`<main>`) must adhere to the standardized width constraint:
    ```html
    <main class="max-w-7xl w-full mr-auto flex flex-col overflow-hidden">
    ```
    Never hardcode arbitrary constraints like `max-w-[1100px]` unless explicitly requested.
2.  **Color System Coordination:** Utilize the core palette definitions loaded inside the Tailwind configuration:
    *   `primary`: Terracotta Orange/Brown (`#8a4f32`)
    *   `surface`: Warm Ivory/Cream (`#F5F2EC` or `#FBF9F6`)
    *   `on-surface`: Charcoal Dark (`#201a18`)
    *   `secondary`: Muted Gray (`#605e5b`)
3.  **Scoped Interaction States:** Gating specific transition rules (like click scale zooms) behind checking URL parameter values (e.g., `const isDemo = params.get('demo') === 'true'`) ensures automated walkthrough recordings look phenomenal without cluttering standard client navigation.

---

## 5. Development Roadmap
The roadmap outlines upcoming phases to transition the static preview platform into a scalable production application:

*   **Phase 1: Dynamic Canvas Rendering (Canvas API / SVG)**
    *   Integrate frontend canvas library (like Fabric.js or HTML2Canvas) in Step 4 to dynamically overlay user-submitted text and screenshots on top of visual themes.
*   **Phase 2: Backend Generation Pipeline**
    *   Architect backend endpoints (Node.js/FastAPI) connected to Stable Diffusion/Flux to programmatically render visual matching backgrounds based on the Step 1 Creative Prompt.
*   **Phase 3: Multi-Format Export Package**
    *   Build exporting workflows to generate ZIP files containing screenshots pre-sized for all Apple App Store requirements (iPhone 6.7", 6.5", iPad Pro) and Google Play Store formats.
