# Aurali AI Onboarding & Screenshot Generator: Product Architecture

As your CTO and Co-Founder, I fully align with your vision. If we want Aurali to be a premium, category-defining SaaS rather than a simple utility, we must build an **Agentic Product Designer**. 

Below is the comprehensive technical architecture, user flow, and backend design system we will build to deliver this high-tier experience.

---

## 1. System Architecture Diagram
This diagram shows how user prompts trigger web research, layout wireframing, brand visual asset synthesis, and final Figma/code compilation.

```mermaid
graph TD
    %% User Inputs
    User[User Prompt / App Link] -->|Submits| Portal[Aurali Web App]
    
    %% Backend Agentic Pipeline
    subgraph Agentic Backend Engine
        Portal -->|1. Dispatch| Agent[AI Lead Product Designer Agent]
        
        %% Research Phase
        Agent -->|2. Scrape & Search| Search[Web Scraper & Tavily Search API]
        Search -->|Niche Best Practices & Competitors| Research[Competitor UX Analysis Report]
        
        %% Layout & Strategy Phase
        Research -->|3. Wireframe Blueprint| Planner[UX Flow & Copywriting Planner]
        Planner -->|Generates Screen Schemas| FlowJSON[Screen-by-Screen JSON Schemas]
        
        %% Styling & Visual Asset Synthesis
        FlowJSON -->|4. Style Match| Visuals[Visual Asset & Color Palette Matcher]
        Visuals -->|Color Codes, Fonts, Layout Rules| CSSSystem[Aurali CSS Theme Engine]
        FlowJSON -->|5. Render Prompts| ImageAPI[GPT Image 2 / Asset API]
        ImageAPI -->|High-Res Visual Assets & Icons| MediaStorage[Cloud Storage CDN]
    end

    %% Compiler & Output Phase
    subgraph Compiler & Code Output
        FlowJSON -->|Compile Structures| Compiler[Design & Code Compiler]
        CSSSystem -->|Inject Themes| Compiler
        MediaStorage -->|Inject Images| Compiler
        
        Compiler -->|Figma File Format| Figma[Editable Figma File .fig / JSON]
        Compiler -->|React / Tailwind| Frontend[Interactive React Component ZIP]
        Compiler -->|Live Canvas Preview| Preview[Interactive Live Mockup Slider]
    end
    
    %% User Delivery
    Figma -->|Import Layers| User
    Frontend -->|Deploy Code| User
    Preview -->|Test Clicks| User
```

---

## 2. Onboarding Feature User Flow Diagram
This shows the step-by-step path a customer takes when interacting with Aurali's onboarding generator.

```mermaid
sequenceDiagram
    autonumber
    actor Founder as App Founder
    participant App as Aurali Canvas App
    participant Agent as AI Design Agent
    participant DB as Supabase DB

    Founder->>App: Inputs app link/niche (e.g. "Duolingo for math")
    App->>Agent: Send Generation Request
    Note over Agent: Phase 1: Research & UX Scrape<br/>Searches top math & learning apps<br/>Analyzes onboarding step counts & paywalls
    Agent-->>App: UI Update: "Analyzing competitor math onboarding flows..."
    Note over Agent: Phase 2: Flow Blueprinting<br/>Writes copy, determines input screens,<br/>sets paywall pricing structures
    Agent-->>App: UI Update: "Creating 6-screen onboarding wireframe..."
    Note over Agent: Phase 3: Visual Generation<br/>Extracts brand palette & renders custom illustrations
    Agent-->>App: UI Update: "Rendering custom brand illustrations..."
    Agent->>App: Return completed Interactive Flow & Code Files
    App->>Founder: Display Live interactive device mockup slider
    Founder->>App: Clicks through screens to test inputs & animations
    Founder->>App: Clicks "Export to Figma" / "Download React Code"
    App->>DB: Log generation metrics & credit deductions
    App->>Founder: Download ready-to-use production files
```

---

## 3. Product Sitemap (Information Architecture)
Here is how the user interface is structured to expose these premium features.

```
aurali.design (Landing & Conversion)
├── / (Homepage: Hero, Steps Card Carousel, Early Bird LTD Pricing)
├── /payment.html (Checkout Redirection & Post-Purchase License Activation Portal)
├── /feedback.html (Public Roadmap & Feature Backlog submissions)
│
└── /app (Private Workspace Dashboard - Requires Login/LTD Activation)
    ├── /my-projects (Manage App Screen Sets & Onboarding Flows)
    │
    └── /editor (Core Creative Workspace Canvas)
        ├── Left Control Sidebar:
        │   ├── Brand Settings (Upload logo, fonts, select primary/secondary/accent colors)
        │   ├── Screenshot Configurator (Device frames, layout modes, background flows)
        │   └── Onboarding Flow Builder (Screen manager: add, remove, rearrange steps)
        │
        ├── Central Interactive Canvas:
        │   ├── Device Mockup Slider (Double View: ASO App Store mockup + Onboarding simulation)
        │   └── Live preview container (Interactable form inputs and animations)
        │
        └── Right Export Panel:
            ├── ASO Package (Download multi-device package for App Store/Google Play)
            ├── React/Tailwind Source Code (Export production-ready components zip)
            └── Figma Integration (Download editable Figma vector layers)
```

---

## 4. How the "Code & Figma Compiler" Works Under the Hood
To ensure our users get **fully editable Figma layers** and not flat PNGs, our backend compiler performs a node-tree conversion:

1.  **Figma API Translation:** Figma's document format is represented as a structured JSON tree containing frame nodes, vector paths, text nodes, and fill styles. Our compiler reads our `FlowJSON` schema and translates it directly into Figma's layout schema. We package this as a `.fig` binary or a JSON file that users can paste into Figma using our companion plugin.
2.  **Tailwind Code Compilation:** The compiler translates our component JSON nodes into standardized, clean JSX. It outputs semantic HTML elements wrapped in Tailwind utility classes, keeping inline styles to absolute zero.

This architecture ensures Aurali is perceived as a highly premium, developer-centric tool that saves weeks of design and engineering resources.
