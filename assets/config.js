/**
 * Aurali — Shared App Configuration
 * Used by: payment.html, feedback.html
 *
 * Load this before the page-specific <script> block:
 *   <script src="assets/config.js"></script>
 */

// Supabase project credentials
const SUPABASE_URL = 'https://abhucczsxwrxtyuspgll.supabase.co';
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFiaHVjY3pzeHdyeHR5dXNwZ2xsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODI0NDc1MDAsImV4cCI6MjA5ODAyMzUwMH0.5IlZXBnUmBsCVjckS6GmbbA5_elqxa3Xz0ToevePM80';

// Dodo Payments hosted checkout link
const DODO_CHECKOUT_URL = "https://checkout.dodopayments.com/buy/pdt_0NiAFIEDApS8pCWx848Jn?quantity=1&redirect_url=https://aurali-design.vercel.app%2Fpayment.html%3Fplan%3Dlifetime";
