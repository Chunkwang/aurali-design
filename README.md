# Aurali.design ⚡️

> **Category-defining AI for mobile teams.** Automatically generate high-converting onboarding flows, competitor-informed layouts, and wrapped App Store screenshots in seconds.

---

## 🚀 The Vision

Aurali reverses the traditional mobile design bottleneck. Instead of wasting hours wireframing, researching competitor design patterns, and manually wrapping screenshot layers, founders and product teams describe their app or paste details to instantly generate:
1. **Interactive Onboarding Flows:** High-conversion welcome, preference, and pricing screen sequences.
2. **Production-Ready Code:** React and Tailwind CSS exports matching custom layouts.
3. **Wrapped App Store Screens:** Multi-device, panoramic wrapped screenshots ready for upload.

---

## 🛠 Tech Stack

Aurali is built to be ultra-lightweight, high-performance, and conversion-optimized:
* **Frontend:** Static Vanilla HTML5, Custom CSS, and Modern JavaScript. (Optimized to deliver lightning-fast initial loads and zero-layout shifts).
* **Database & Waitlist Backend:** [Supabase](https://supabase.com) (Serverless REST API integration using custom anonymized row insertion and secure RPC counters).
* **Hosting & Deployments:** [Vercel](https://vercel.com).
* **Monitoring & Analytics:** 
  * Vercel Web Analytics (Traffic and visitor tracking).
  * Vercel Speed Insights (Real-time Core Web Vitals and load performance analysis).

---

## 📁 Repository Structure

```
├── index.html               # Main Landing Page & waitlist portal
├── feedback.html            # User feedback collection form
├── payment.html             # Premium Lifetime License payment gateway
├── dashboard.html           # Main user workspace portal (prototype)
├── my_projects.html         # User project selection view (prototype)
├── project_step1.html       # Step 1: Niche & Competitor Research UI
├── project_step2.html       # Step 2: Onboarding Flow Editor UI
├── project_step3.html       # Step 3: Screenshot Customization UI
├── project_step4.html       # Step 4: Export Options UI
├── assets/                  # Images, design assets, and walkthrough webps
└── src/components/
    └── index.css            # Base stylesheet rules
```

---

## 🔒 Supabase Database Configuration

The waitlist capture system connects to a Supabase PostgreSQL instance.

### 1. Waitlist Table Schema
Create a table named `waitlist` in your Supabase schema editor:
```sql
create table public.waitlist (
  id uuid default gen_random_uuid() primary key,
  email text not null unique,
  created_at timestamp with time zone default timezone('utc'::text, now()) not null
);
```

### 2. Row Level Security (RLS)
To prevent public users from harvesting waitlist emails, configure the following RLS policies:
* **Enable RLS** on the `waitlist` table.
* **Insert Policy:** Allow anonymous inserts (`public` role) so anyone can join the waitlist.
  ```sql
  create policy "Enable insert for anonymous users" 
  on public.waitlist 
  for insert 
  with check (true);
  ```
* **Select Policy:** Restrict SELECT queries to the `service_role` or authenticated admins (returns an empty list for anonymous public users).

### 3. Public Waitlist Counter (RPC)
To safely display the total count of waitlist signups on the landing page without exposing email addresses, run this SQL in your Supabase SQL Editor:
```sql
create or replace function get_waitlist_count()
returns bigint
security definer
as $$
  select count(*) from waitlist;
$$ language sql;
```

---

## 📈 Monitoring & Analytics Setup

Web Analytics and Speed Insights script blocks are injected in the `<head>` of our HTML documents:

```html
<!-- Vercel Web Analytics -->
<script>
  window.va = window.va || function () {
    (window.vaq = window.vaq || []).push(arguments);
  };
</script>
<script defer src="/_vercel/insights/script.js"></script>

<!-- Vercel Speed Insights -->
<script>
  window.si = window.si || function () {
    (window.siq = window.siq || []).push(arguments);
  };
</script>
<script defer src="/_vercel/speed-insights/script.js"></script>
```

When deploying to Vercel, simply toggle **Enable Web Analytics** and **Speed Insights** in your project dashboard settings to begin collecting metrics.

---

## 💻 Local Development

1. Clone this repository.
2. Serve the directory using any local development server (e.g., Live Server in VS Code, or python simple server):
   ```bash
   python3 -m http.server 8000
   ```
3. Open `http://localhost:8000` in your browser.
