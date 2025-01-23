import request
import json
import sqlite3


def get_products(category, brand, page=1):
  url = f"https://api.digikala.com/v1/categories/{category}/brands/{brand}/search/?page={page}"
  
  payload = {}
  headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cookie': 'ab_test_experiments=%5B%22229ea1a233356b114984cf9fa2ecd3ff%22%2C%22db7b11075496e04f0a6ef0d3a02d5264%22%2C%22f0fd80107233fa604679779d7e121710%22%2C%2237136fdc21e0b782211ccac8c2d7be63%22%5D; tracker_glob_new=amfmPwm; _ga=GA1.1.1132595767.1734931114; _ym_uid=1735464919629174537; _ym_d=1735464919; Digikala:User:Token:new=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozNzk1NTU3LCJzdWIiOjM3OTU1NTcsImV4cGlyZV90aW1lIjoxNzM4ODI2NDcyLCJleHAiOjE3Mzg4MjY0NzIsInBheWxvYWQiOltdLCJwYXNzd29yZF92ZXJzaW9uIjoyLCJ0eXBlIjoidG9rZW4ifQ.QPuP3kLe-C84QYZmztf1uvOkg4QvFwPY18kTsLrMcCs; PHPSESSID=6i6htlg3mve4alddm4odl0i6v3; TS011434b1=0102310591e765cd092df1e80f78b0e550f8acec986e3f33d5099bca20c8c61fd6966019199df35b74c79e6e0d6670a34f65fb9bbfce753148b8933467e72b0432092eeeffc79ee04e8b49bac606af3b377915d9cc; TS01b6ea4d=01023105919eaf64521b8be813cc0256b84de970bbe5136c72e1c750b1521908425c7c8ee21c21614beeb0824b9b346cce4d65ee13b21c5b2ff92c60ac092323f9efbb66a9e3604eddbb393b73e7151bcaab525aff; _sp_ses.13cb=*; Digikala:General:Location=UGN6eDhPdnBFNndnVkNxWkJvZ3JjUT09%26djNoUThYVisxOHdGWFNITTZXR3NUbkYxYjFUUk5ES3U2M3ZSWk5iV3orYmluZDZGU3lXZHZYM1RCOVFjalhsSHYrSjBNOStueXRiblNXMFNBWkxlbUE9PQ~~; tracker_session=dqOngk4; _clck=yb2bet%7C2%7Cfss%7C0%7C1848; _clsk=icfsmv%7C1737547022909%7C1%7C1%7Cp.clarity.ms%2Fcollect; TS01c77ebf=01023105911e5fb9964c67480f2b9b3c669f32887a5161b3ba4df42719680e32deaaf7c914a8db8c9ba3bd14ebd9ad4431f0a6bc50dcfd300ace35f2fa4fa354f61b79b3cfa9194b98966507679ac84e3f3c4c61ff; TS010e7d7f=0102310591f90c3d7c968d0d75a6a4d5c852ddfc8ef125eaed84464cad32b9c6d2f9edcf68c68b8216aa21f8186bae1ad7563feab8f4f16712c3c2e39a419597989afedca073bbd556246a855588e480234a2a87382f1a7083eee34dc01a1f3aca2b077135; _sp_id.13cb=91ba178a-cdb9-48d6-8fd4-f709dedfc5b2.1734931108.8.1737547882.1737539411.b855197d-705e-4a3c-92d1-d32333714752.01e4c998-50de-4828-b340-4548d0c5acd5.879877f2-77ff-4fa6-a666-4080b7165d68.1737547018822.10; _ga_QQKVTD5TG8=GS1.1.1737547014.13.1.1737547883.0.0.0; TS011434b1=0102310591e765cd092df1e80f78b0e550f8acec986e3f33d5099bca20c8c61fd6966019199df35b74c79e6e0d6670a34f65fb9bbfce753148b8933467e72b0432092eeeffc79ee04e8b49bac606af3b377915d9cc; tracker_glob_new=amfmPwm; TS010e7d7f=01023105911041f3f0f822fc31693ce9a66d3acab2bd7bee574314cd534b2baaa4001c638d11625ddb41d0b80b3cd083a2a7839a462a97c4f3931a6c2c896c14f7a2a525a177b6656d5d137e998895120242a4bd88e6d3ee7025922c8843f0b5a39cd1cebb; tracker_session=dqOngk4',
    'origin': 'https://www.digikala.com',
    'priority': 'u=1, i',
    'referer': 'https://www.digikala.com/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'x-web-client': 'desktop',
    'x-web-optimize-response': '1'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  return json.loads(response.text)['data']['products']


def get_product_details(productid):
  url = f"https://api.digikala.com/v2/product/{productid}/"

  payload = {}
  headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cookie': 'ab_test_experiments=%5B%22229ea1a233356b114984cf9fa2ecd3ff%22%2C%22db7b11075496e04f0a6ef0d3a02d5264%22%2C%22f0fd80107233fa604679779d7e121710%22%2C%2237136fdc21e0b782211ccac8c2d7be63%22%5D; tracker_glob_new=amfmPwm; _ga=GA1.1.1132595767.1734931114; _ym_uid=1735464919629174537; _ym_d=1735464919; Digikala:User:Token:new=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozNzk1NTU3LCJzdWIiOjM3OTU1NTcsImV4cGlyZV90aW1lIjoxNzM4ODI2NDcyLCJleHAiOjE3Mzg4MjY0NzIsInBheWxvYWQiOltdLCJwYXNzd29yZF92ZXJzaW9uIjoyLCJ0eXBlIjoidG9rZW4ifQ.QPuP3kLe-C84QYZmztf1uvOkg4QvFwPY18kTsLrMcCs; PHPSESSID=6i6htlg3mve4alddm4odl0i6v3; TS011434b1=0102310591e765cd092df1e80f78b0e550f8acec986e3f33d5099bca20c8c61fd6966019199df35b74c79e6e0d6670a34f65fb9bbfce753148b8933467e72b0432092eeeffc79ee04e8b49bac606af3b377915d9cc; TS01b6ea4d=01023105919eaf64521b8be813cc0256b84de970bbe5136c72e1c750b1521908425c7c8ee21c21614beeb0824b9b346cce4d65ee13b21c5b2ff92c60ac092323f9efbb66a9e3604eddbb393b73e7151bcaab525aff; _sp_ses.13cb=*; tracker_session=dqOngk4; _clck=yb2bet%7C2%7Cfss%7C0%7C1848; _clsk=icfsmv%7C1737547940362%7C3%7C1%7Cp.clarity.ms%2Fcollect; Digikala:General:Location=RVZsQ1d4NmR3VXZvaklieVFKRzlEUT09%26SjMycjB5bERJYUYrSjlqdWlxUlYvditzWFdkY3VybTRUbTJiNTFnVUtZQ3Q2cGExUldZWU1BOGJrRW1PU3h3UlQxeXpIam9BaFQyV0tJZ2NyQlkyNnc9PQ~~; TS01c77ebf=01023105911f649e94553de50f04fe1dc58793b18b0b1226e810f6096e502208b8d23105fe9580339e1089c1a5804d5d494ec3c78abbb5f391be6eb6479ee65c842500779c33d26a62dacf6aa22516efd56eafc6c9; TS010e7d7f=0102310591d1c963172c5e586a08780043fd9eacb1a345ed7684a8a823a7e4bd63683382c3d71345dbcce5285a69f7f333d1f6a16123c807a964cf2fc0fd8b04e52146318dd7a9b9d3ea63e27e4c848f29858b3215a3d30a8f7d67e03d15d8ff8053c1cf81; _ga_QQKVTD5TG8=GS1.1.1737547014.13.1.1737549596.0.0.0; _sp_id.13cb=91ba178a-cdb9-48d6-8fd4-f709dedfc5b2.1734931108.8.1737549599.1737539411.b855197d-705e-4a3c-92d1-d32333714752.01e4c998-50de-4828-b340-4548d0c5acd5.879877f2-77ff-4fa6-a666-4080b7165d68.1737547018822.21; TS011434b1=0102310591e765cd092df1e80f78b0e550f8acec986e3f33d5099bca20c8c61fd6966019199df35b74c79e6e0d6670a34f65fb9bbfce753148b8933467e72b0432092eeeffc79ee04e8b49bac606af3b377915d9cc; tracker_glob_new=amfmPwm; TS010e7d7f=01023105911041f3f0f822fc31693ce9a66d3acab2bd7bee574314cd534b2baaa4001c638d11625ddb41d0b80b3cd083a2a7839a462a97c4f3931a6c2c896c14f7a2a525a177b6656d5d137e998895120242a4bd88e6d3ee7025922c8843f0b5a39cd1cebb; tracker_session=dqOngk4',
    'origin': 'https://www.digikala.com',
    'priority': 'u=1, i',
    'referer': 'https://www.digikala.com/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'x-web-client': 'desktop',
    'x-web-optimize-response': '1'
  }

  response = requests.request("GET", url, headers=headers, data=payload)
  return json.loads(response.text)


  def get_product_review(jsonfile):
    # Safely extract the reviews
    reviews = jsonfile['data']['product'].get('review', {})
    
    # Handle missing description
    description = reviews.get('description', '').strip()
    
    # Handle missing attributes
    attributes = ""
    if 'attributes' in reviews:
        for attr in reviews['attributes']:
            attributes += attr['title'] + ': ' + ' '.join(attr['values']) + '\n'
    
    return description, attributes




# Function to store details in the database
def store_to_db(product_id, product_name, description, attributes):
    # Connect to SQLite database
    conn = sqlite3.connect('products_reviews.db')
    cursor = conn.cursor()

    # Create tables if not exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        product_id INTEGER PRIMARY KEY,
        product_name TEXT,
        description TEXT,
        attributes TEXT
    )
    ''')

    # Insert product
    cursor.execute('INSERT OR IGNORE INTO Products (product_id, product_name, description, attributes) VALUES (?, ?, ?, ?)',
                   (product_id, product_name, description, attributes))


    # Commit changes and close connection
    conn.commit()
    conn.close()
    print(f"Stored product {product_id} details successfully!")


# Function to fetch and store product details
def store_product_details(product):
    product_id = product['id']
    product_name = product['title_fa']
    
    # Fetch product details including description and attributes
    product_details = get_product_details(product_id)
    description, attributes = get_product_review(product_details)

    if description and attributes:
        # Store to database
        store_to_db(product_id, product_name, description, attributes)
    else:
        print(f"Skipped saving product {product_id} due to missing description or attributes.")



# Main function to orchestrate the workflow
def main():
    # Fetch all products
    category = "notebook-netbook-ultrabook" # Replace with the desired category
    brand = "lenovo" # Replace with the desired brand
    products = get_products(category=category, brand=brand)
    
    # Loop through each product and store details
    for product in products:
        store_product_details(product)

if name == "main":
    main()