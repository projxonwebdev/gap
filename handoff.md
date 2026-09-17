# PROJXON GAP Website Handoff

Welcome to the PROJXON Growth Advisory Program (GAP) website project. This document provides the essential context, branding guidelines, and architecture details needed to continue development seamlessly.

## Project Overview
PROJXON GAP is an elite, veteran-owned professional development and advisory program. The website is designed to reflect a premium, exclusive, and high-end executive coaching environment.

**Tech Stack:** React, Vite, Tailwind CSS, React Router (`dist` is deployed via Netlify).

## What We've Built
The site is a React Single Page Application (SPA) with the following core routes:
- **Home (`/`)**: Hero section, value propositions, Tech Stack, and CEO vision.
- **Portfolio (`/portfolio`)**: Showcases client work (e.g., Celyfos Shopify migration).
- **Team (`/team`)**: Displays leadership and advisors.
- **MIP (`/mip`)**: Momentum Internship Program details and "The Nexus of Growth" Venn diagram.
- **Coaching (`/coaching`)**: Details the 3-step GAP Methodology and the two Development Tracks (1:1 Advisory & Growth Labs).
- **Contact/Work (`/contact`, `/work`)**: FAQ and the "Work with GAP" lead intake form.

## Branding Guidelines
- **Theme:** Luxury dark mode, minimalist, and executive. Use glassmorphism (`backdrop-blur`, semi-transparent borders) and subtle glows/shadows.
- **Typography:** 
  - Headings: **Manrope** (`font-headline`, `font-display`)
  - Body/Labels: **Inter** (`font-body`, `font-label`, `font-caption`)
- **Core Colors:**
  - `obsidian` (`#0A0A0A`) & `surface` (`#131313`) for backgrounds
  - `momentum-gold` (`#FFC800`) & `momentum-gold-bright` (`#FFD700`) for accents and buttons
  - `slate-gray` (`#888888`) for secondary text
- **Icons:** We use Google Material Symbols. Avoid "generic AI" icons (like `psychology` or `hub`). Use premium/specific icons (e.g., `strategy`, `architecture`, `handshake`).

## Basic Guidelines & Quirks
- **Routing:** We use `react-router-dom`. We have a `<ScrollToTop />` component in `App.jsx` to ensure pages snap to the top on navigation.
- **Copywriting:** Keep text sharp, confident, and free of fluff. The client dislikes em dashes ("—") in project descriptions—use commas or standard punctuation instead.
- **Images:** The `public/` directory contains all static assets (logos, headshots, `venn-new.png`).
- **Forms:** The `WorkWithGap.jsx` form currently has an `e.preventDefault()` that stops default Netlify form submission to show a success UI. If Netlify data capture is needed, an AJAX `fetch` POST needs to be wired up in the `handleSubmit` function.
- **Builds:** Always run `npm run build && zip -r dist.zip dist` after making structural changes so the client can upload the zip to Netlify.
