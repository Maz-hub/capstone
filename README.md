# Swiss Romande Hikes

## Overview

**Swiss Romande Hikes** is a personal hiking guide and trail explorer for the French-speaking region of Switzerland. It offers real, practical trail suggestions based on my own hiking experiences, with original photos, detailed trail descriptions, and an interactive map. Built as my CS50W Capstone Project, this web app is designed to help casual hikers and tourists discover scenic and safe routes across the Swiss Romande.

All hikes featured on the site are ones I’ve personally completed, and are presented in a helpful, down-to-earth style — from me to you.

## Distinctiveness and Complexity

**Swiss Romande Hikes** is a personal guide-based web app with a geospatial component. It features a map-based interface, dynamic trail data, trail-specific weather integration, and a user-centric design inspired by real-world tourism needs.

The application uses:

- **Mapbox GL JS** to render an interactive map with custom markers
- **JavaScript** to enhance the dynamic behavior of the site (e.g., filter trails, refresh comments)
- **SCSS custom design**, for full control over layout and responsive behavior
- **Django models** to manage dynamic trail data, images, and user-submitted comments
- **Open-Meteo API** to fetch and display live weather information for each trail page

This project also stands out because it is **based on my personal hiking experience** and includes original content and photos. It combines real-world storytelling with technical implementation — including responsive design, external APIs, dynamic user-generated content, and scalable structure.

Together, these elements demonstrate both creative originality and the technical complexity expected of a CS50W Capstone.

---

## Features

### Core Functionality (Completed)

- 📍 **Interactive Map:**

  - Uses Mapbox GL JS to display trails across the Swiss Romande region
  - Custom boot-shaped markers for each trail
  - Fully responsive and mobile-friendly map

- 🥾 **Trail Cards:**

  - 6 real trails dynamically loaded from Django models
  - Display trail name, canton, and thumbnail image
  - Clicking a trail card opens a dynamic trail detail page

- 🗺️ **Trail Detail Pages:**

  - Dedicated pages for each hike
  - Includes photo galleries, structured trail data, real-time weather, full trail description, and Swisstopo map embeds
  - Organized responsive layout for desktop and mobile

- 🌦️ **Weather Integration:**

  - Real-time temperature and wind speed pulled from Open-Meteo API
  - Weather shown directly on each trail page based on trail coordinates

- 💬 **Trail-Specific Comments:**

  - Visitors can leave a comment about a specific hike
  - Comments are saved in the database and paginated (5 per page)
  - New comments dynamically refresh without a full page reload (handled by `comments.js`)

- 🎨 **Custom UI:**

  - Full SCSS-based styling (no Bootstrap)
  - Google Fonts + theme color palette
  - Modern, mobile-first layout using CSS Grid and Flexbox

- 🔎 **Trail Filter:**
  - Users can filter hikes by difficulty level ("Easy", "Intermediate", "Moderate")
  - Filter is handled with a simple `<select>` input without reloading the whole page

---

### Optional Future Features

- 👤 User accounts to save favorites or add personal reviews
- 📸 Scrollable full-screen photo galleries for each trail
- 🧭 Advanced trail search filters (distance, season, elevation)

---

## How to Run Locally

To run Swiss Romande Hikes locally, follow these steps:

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/capstone.git
cd capstone
```

### 2. Set up a virtual environment

```bash
python3 -m venv myvenv
source myvenv/bin/activate
```

### 3. Install required Python packages

```bash
pip install -r requirements.txt
```

### 4. Install and compile SCSS (requires Node.js)

```bash
npm install
npm run scss
```

### 5. Apply Django migrations

```bash
python3 manage.py migrate
```

### 6. Run the development server

```bash
python3 manage.py runserver
```

## Project Structure

capstone/
├── rivieraroutes/ # Main Django project folder (settings, URLs)
├── trails/ # Core app: views, models, templates
│ ├── templates/trails/ # HTML templates (layout, homepage, trail pages, 404 page)
│ ├── static/css/ # Compiled CSS
│ ├── static/scss/ # Main SCSS files and partials
│ ├── static/img/ # Trail and homepage images
│ ├── static/js/ # JavaScript (map.js, filter.js, comments.js)
│ ├── models.py # Trail, TrailImage, and Comment models
│ ├── views.py # Views for homepage, trail detail, comments
│ ├── forms.py # Comment form logic
├── media/trail_images/ # Uploaded images (trail galleries)
├── db.sqlite3 # Default Django database
├── package.json # Node/NPM config for SCSS build
├── package-lock.json # NPM lock file
├── README.md # This file
├── requirements.txt # Python dependencies
├── runtime.txt # Runtime version (for deployment)
├── manage.py

Trail data is fully dynamic. Each hike's page, weather information, images, and comments are loaded from the database in real-time.
