# Iranian-Scraper

This repository contains scrape scripts for Iranian websites.

## Updates

### New Feature: Digikala Scraper

The repository now includes a scraper for Digikala, designed to extract product details based on category and brand. The scraper:

- Collects `product_id`, `description`, and `attributes`.
- Avoids duplicate entries by storing data in a SQLite database.

### Usage Instructions for Digikala Scraper

1. Navigate to the `Digikala/` folder.
2. Update the `scraper.py` file with your desired category and brand.
3. Run the scraper using:
   ```bash
   python scraper.py
   ```

For more details, refer to the `Digikala Scraper` README in the `Digikala/` folder.
