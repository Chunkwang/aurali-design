/**
 * Aurali — Shared Tailwind CDN Theme Config
 * Used by: dashboard.html, project_step1-4.html, my_projects.html
 *
 * Load this BEFORE the Tailwind CDN <script> tag so the CDN
 * picks up the config via the global tailwind.config object.
 *
 *   <script src="assets/tailwind-theme.js"></script>
 *   <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
 */
tailwind = window.tailwind || {};
tailwind.config = {
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        "on-background": "#201a18",
        "secondary-container": "#e6e2de",
        "on-primary-fixed-variant": "#6e381d",
        "on-secondary-container": "#666461",
        "on-tertiary-fixed-variant": "#004f50",
        "on-error": "#ffffff",
        "primary": "#8a4f32",
        "on-primary": "#ffffff",
        "on-primary-container": "#58270d",
        "surface": "#fff8f6",
        "tertiary": "#136969",
        "secondary-fixed": "#e6e2de",
        "inverse-on-surface": "#fbeee9",
        "on-tertiary-fixed": "#002020",
        "primary-fixed-dim": "#ffb695",
        "error": "#ba1a1a",
        "on-tertiary-container": "#003b3c",
        "tertiary-fixed-dim": "#89d3d3",
        "outline": "#85736c",
        "on-surface-variant": "#53443d",
        "secondary-fixed-dim": "#cac6c2",
        "on-secondary": "#ffffff",
        "secondary": "#605e5b",
        "on-secondary-fixed": "#1c1b19",
        "surface-container-highest": "#ede0db",
        "surface-bright": "#fff8f6",
        "background": "#fff8f6",
        "surface-variant": "#ede0db",
        "inverse-primary": "#ffb695",
        "tertiary-fixed": "#a5f0ef",
        "surface-dim": "#e4d7d3",
        "on-primary-fixed": "#351000",
        "surface-container-lowest": "#ffffff",
        "inverse-surface": "#362f2c",
        "primary-container": "#d48c6b",
        "on-tertiary": "#ffffff",
        "on-error-container": "#93000a",
        "on-secondary-fixed-variant": "#484644",
        "surface-container-high": "#f3e5e1",
        "on-surface": "#201a18",
        "surface-container": "#f8ebe6",
        "error-container": "#ffdad6",
        "surface-tint": "#8a4f32",
        "outline-variant": "#d8c2ba",
        "surface-container-low": "#fef1ec",
        "tertiary-container": "#5fa9a9",
        "primary-fixed": "#ffdbcc"
      },
      borderRadius: {
        "DEFAULT": "0.25rem",
        "lg": "0.5rem",
        "xl": "0.75rem",
        "full": "9999px",
        "card": "20px",
        "btn": "12px"
      },
      spacing: {
        "container-padding": "24px",
        "grid-gutter": "24px",
        "element-gap": "16px",
        "section-gap": "56px",
        "base": "8px"
      },
      fontFamily: {
        "headline-md": ["Plus Jakarta Sans"],
        "display-lg": ["Plus Jakarta Sans"],
        "display-accent": ["Instrument Serif"],
        "title-sm": ["Plus Jakarta Sans"],
        "label-caps": ["Plus Jakarta Sans"],
        "body-md": ["Plus Jakarta Sans"],
        "headline-md-mobile": ["Plus Jakarta Sans"],
        "body-lg": ["Plus Jakarta Sans"]
      },
      fontSize: {
        "headline-md": ["32px", { "lineHeight": "1.2", "letterSpacing": "-0.01em", "fontWeight": "700" }],
        "display-lg": ["48px", { "lineHeight": "1.1", "letterSpacing": "-0.02em", "fontWeight": "800" }],
        "display-accent": ["48px", { "lineHeight": "1.1", "fontWeight": "400" }],
        "title-sm": ["18px", { "lineHeight": "1.5", "fontWeight": "600" }],
        "label-caps": ["12px", { "lineHeight": "1", "letterSpacing": "0.05em", "fontWeight": "700" }],
        "body-md": ["14px", { "lineHeight": "1.5", "fontWeight": "400" }],
        "headline-md-mobile": ["24px", { "lineHeight": "1.2", "fontWeight": "700" }],
        "body-lg": ["16px", { "lineHeight": "1.6", "fontWeight": "400" }]
      }
    }
  }
};
