# Strategic Pricing, Unit Economics & Usage Limits for Aurali

This document outlines the architectural pricing strategy, unit economics modeling, feature matrix, and lifetime deal (LTD) structures for **Aurali**.

---

## 1. Unit Economics & Cost Assumptions
To calculate sustainable pricing, we assume a premium generation engine (e.g., FLUX.1 via Fal.ai or Replicate) capable of rendering crisp text, high-fidelity mockups, and cohesive backgrounds:

*   **Premium Generation Cost:** **$0.04** per render (FLUX.1 [dev] at 1024px or equivalent).
*   **Draft/Low-Res Cost (Standard):** **$0.005** per render (SDXL or FLUX.1 [schnell] for rapid edits).
*   **Average Package Requirement:** App store submissions require a 5-screen panoramic wrap. 
*   **User Multiplier (Trial & Error):** An average user generates/regenerates **3.5x** more screens than their final download package.
    *   *Result:* One 5-screen package requires ~18 generations.

---

## 2. Proposed Monthly Tier Allocation & Gross Margin Analysis

We target a **>80% gross margin** on infrastructure costs to account for hosting, customer acquisition, Stripe fees, and failed renders.

| Tier | Monthly Price | Included Generations | Max API Cost | Gross Margin | Use Case |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Starter** | **$9** | **35 generations** | $1.40 | **84%** | Indie Hacker launching 1-2 apps. |
| **Growth** | **$25** | **120 generations** | $4.80 | **81%** | Active founder managing 5-6 apps. |
| **Agency** | **$50** | **300 generations** | $12.00 | **76%** | Design studios & serial app builders. |

---

## 3. Feature Allocation Matrix

To incentivize upgrades, we gate by features and styling choices rather than raw generation credits alone.

### Tier 1: Starter ($9/mo)
*   **Access:** Standard templates (App Store & Play Store).
*   **Devices:** iOS only (iPhone 15 Pro, standard dark/light).
*   **Export formats:** PNG/JPG standard resolution.
*   **AI generation:** Standard speed pipeline.
*   **Backgrounds:** 10 curated color presets (no custom creative prompts).

### Tier 2: Growth ($25/mo)
*   **Access:** All premium & panoramic templates.
*   **Devices:** iOS & Android (iPhone, iPad, Google Pixel, Samsung Galaxy).
*   **Export formats:** High-Res PNG + Figma file link exports.
*   **AI generation:** Fast-track generation queue.
*   **Backgrounds:** Custom AI prompt generator (Flux) for unique backgrounds.
*   **Features:** Custom logo uploads & custom brand fonts.

### Tier 3: Agency ($50/mo)
*   **Access:** Team seats (up to 3 members).
*   **White-labeling:** Save custom brand palettes and templates.
*   **Features:** Unlimited concurrent rendering, API access (future), premium support.

---

## 4. The Lifetime Access (One-Time Fee) Model
Selling unlimited lifetime access for an AI generation product is a **liquidity trap**—it generates high cash flow at launch but leaves the business bankrupt when early users continue consuming expensive API resources indefinitely.

### Recommended LTD Structure: **The Recurring Credit Cap**
*   **Price Option:** **$149 one-time**
*   **Limit:** **60 generations per month** (resets every month).
*   *Why?* The user gets the feeling of "lifetime value" without generating uncapped, compounding API liabilities. If they need to build three apps in one week, they purchase an Add-on Pack.

---

## 5. Add-On Pack Pricing
Add-ons should be pure profit drivers, designed for users who exceed their limits but do not want to jump to the next monthly tier.

*   **Mini Pack:** 30 Generations for **$8** ($0.26 / gen)
*   **Pro Pack:** 100 Generations for **$19** ($0.19 / gen)
*   *Gross Margin:* **>90%**

---

## 6. Challenging Your Assumptions (CTO Feedback)

### Challenge 1: The "Failed Render" Penalty
*   **Your Assumption:** Regenerating a screen costs 1 credit.
*   **My Critique:** If the AI generates distorted text or ignores a prompt, charging users a credit for a broken output leads to direct customer churn.
*   **Better Approach:** Provide a **"Low-Res Draft Mode"** using a super fast, cheap model (FLUX schnell - $0.003/gen) inside the editor. The user iterates on layout/text for free. Once they are happy with the layout, they hit **"Render High-Resolution Wrap"** which costs **1 Premium Credit** (using FLUX dev).

### Challenge 2: Launcher Limits (Conservative vs. Generous)
*   **My Recommendation:** **Be conservative at launch.**
    *   It is mathematically and relationally easy to say: *"We upgraded our starter plan to include 10 more generations for free!"* (wins customer loyalty).
    *   It is near-impossible to say: *"We are decreasing your limits by 50% because we are losing money."* (leads to public complaints).
