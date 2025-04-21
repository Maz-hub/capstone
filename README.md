# capstone

CS50W Capstone: Riviera Routes: A web application to explore hiking trails around the Swiss Riviera.

# Riviera Routes

## Overview

Riviera Routes is a web application designed to help tourists and casual hikers discover beautiful hiking trails in the Swiss Riviera. Users can view detailed information about each trail, including maps, photos, and current weather conditions.

## Technologies Used

- Django
- Python
- Pillow (for image handling)
- Google Maps API (for interactive maps)
- MeteoSwiss API (for weather information)

## Setup Instructions

1. Clone the repository.
2. Set up a virtual environment and activate it.
3. Install dependencies: `pip install -r requirements.txt`
4. Run migrations: `python3 manage.py migrate`
5. Start the server: `python3 manage.py runserver`

## Progress Updates

- [Date] Added Trail model with fields for name, description, start location, and difficulty.
- [Date] Integrated Pillow for handling image uploads to trail descriptions.

## Challenges and Solutions

- Faced issues with Pillow installation; resolved by ensuring virtual environment was active before installing the library.

## Future Features

- User authentication for saving favorite trails.
- Advanced filtering options based on weather conditions and difficulty.
