# Swiss Romande Hikes

## Overview

**Swiss Romande Hikes** is a personal hiking guide and trail explorer for the French-speaking region of Switzerland. It offers real, practical trail suggestions based on my own hiking experiences, with original photos, detailed trail descriptions, and an interactive map. Built as my CS50W Capstone Project, this web app is designed to help casual hikers and tourists discover scenic and safe routes across the Swiss Romande.

All hikes featured on the site are ones I’ve personally completed, and are presented in a helpful, down-to-earth style — from me to you.

## Distinctiveness and Complexity

**Swiss Romande Hikes** is a personal guide-based web app with a geospatial component. It features a map-based interface, dynamic trail data, and a user-centric design inspired by real-world tourism needs.

The application uses:

- **Mapbox GL JS** to render an interactive map with custom markers
- **JavaScript and the DOM** to connect map markers with trail cards, allowing for a dynamic and engaging experience
- A **custom SCSS-based design**, for full control over layout and responsive behavior
- **Django models** to manage trail data and prepare for future extensibility, such as user accounts, reviews, or real-time trail updates

This project also stands out because it is **based on my personal hiking experience** and includes original content and photos. It combines real-world storytelling with technical implementation — including responsive design, external APIs, and scalable structure.

Together, these elements demonstrate both creative originality and the technical complexity expected of a CS50W Capstone.

## Features

### Core Functionality (Completed)

- 📍 Interactive Map:

  - Uses Mapbox GL JS to display the Swiss Romande region
  - Custom boot-shaped markers for each trail
  - Clicking a trail card scrolls and zooms the map to the corresponding location

- 🥾 Trail Cards:

  - Display 6 real trails with original photos and location info
  - Responsive grid layout for desktop, tablet, and mobile
  - Each card includes trail name, location, and canton

- 🗺️ Mobile-First Layout:

  - Fully responsive design using CSS Grid and SCSS
  - Trail cards and map reflow intuitively on smaller screens

- 🎨 Custom UI:
  - Styled entirely with SCSS (no Bootstrap)
  - Google Fonts + theme colors for a personal, clean look

### Optional Future Features

- 🧾 Trail Detail Pages (with full description, weather, difficulty, etc.)
- 👤 User accounts to save favorites or add comments
- 🌦️ Weather integration using MeteoSwiss API
- 📸 Photo gallery per trail with scrollable carousel
- 🔍 Trail filter by distance, season, or difficulty

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
├── rivieraroutes/ # Main Django project folder (settings, URLs) ├── trails/ # Core app: views, models, templates │
├── templates/trails/ # HTML templates (layout, homepage, etc.) │ ├── static/css/ # Compiled CSS from SCSS │
├── static/scss/ # Main SCSS files and partials │
├── static/img/ # Images used in homepage/cards/map markers │
├── static/js/ # JavaScript (e.g. map.js for Mapbox interaction) ├── db.sqlite3 # Default Django development database
├── requirements.txt # Python dependencies
├── package.json # Node/NPM config for SCSS build
├── README.md # This file

```markdown
Trail data is currently hardcoded for launch (6 hikes), but the structure supports future integration with Django models and dynamic content.
```
