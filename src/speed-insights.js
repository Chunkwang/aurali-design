/**
 * Vercel Speed Insights Integration for Static HTML
 * This script initializes Speed Insights tracking when the page loads.
 * 
 * Speed Insights must be enabled in your Vercel dashboard for this to work.
 * Once enabled, Vercel will automatically serve the tracking script.
 */

(function() {
  // Initialize the Speed Insights queue
  window.si = window.si || function () { 
    (window.siq = window.siq || []).push(arguments); 
  };
  
  // Create and inject the Speed Insights script
  // The script path will be automatically configured by Vercel when Speed Insights is enabled
  var script = document.createElement('script');
  script.defer = true;
  script.src = '/_vercel/speed-insights/script.js';
  
  // Add error handling
  script.onerror = function() {
    console.warn('Vercel Speed Insights: Could not load tracking script. Make sure Speed Insights is enabled in your Vercel dashboard.');
  };
  
  // Inject the script into the document
  if (document.head) {
    document.head.appendChild(script);
  } else {
    // If head is not available yet, wait for DOM to be ready
    document.addEventListener('DOMContentLoaded', function() {
      document.head.appendChild(script);
    });
  }
})();
