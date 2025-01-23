# Digikala Scraper

A simple scraper designed to extract product details from Digikala and store them in a SQLite database. The scraper collects the following information for each product:

- `product_id`
- `description`
- `attributes`

The scraper ensures that duplicate entities are avoided.
The scraper only stores product with description and attributes. (Data in معرفی section)

## Setup Instructions

### Step 1: Set Up Environment

1. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment:**

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Clone the repository:**
   ```bash
   git clone https://github.com/theHesari/iranian-scraper.git
   ```

### Step 2: Install Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

4. **Navigate to the project folder:**
   ```bash
   cd iranian-scraper/Digikala
   ```

## Usage Instructions

1. **Update Scraper Configuration:**
   Open the `scraper.py` file and insert your desired category and brand values:

   ```python
   category = "notebook-netbook-ultrabook"
   brand = "lenovo"
   ```

2. **Run the Scraper:**
   Execute the scraper script:
   ```bash
   python scraper.py
   ```

## Output

The scraper will:

- Create a SQLite database.
- Store the product details (`product_id`, `description`, and `attributes`) while avoiding duplicates.
