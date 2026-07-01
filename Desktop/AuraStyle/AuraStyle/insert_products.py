from database import products

# Clear old data
products.delete_many({})

sample_products = [

    {
        "name": "Black Hoodie",
        "brand": "Nike",
        "category": "Hoodie",
        "price": 1499,
        "image_url": "https://images.pexels.com/photos/6311392/pexels-photo-6311392.jpeg"
    },

    {
        "name": "White T-Shirt",
        "brand": "Adidas",
        "category": "T-Shirt",
        "price": 799,
        "image_url": "https://images.pexels.com/photos/9558770/pexels-photo-9558770.jpeg"
    },

    {
        "name": "Blue Jeans",
        "brand": "Levis",
        "category": "Jeans",
        "price": 1999,
        "image_url": "https://images.pexels.com/photos/1598505/pexels-photo-1598505.jpeg"
    },

    {
        "name": "Running Shoes",
        "brand": "Puma",
        "category": "Shoes",
        "price": 2499,
        "image_url": "https://images.pexels.com/photos/2529148/pexels-photo-2529148.jpeg"
    },

    {
        "name": "Luxury Watch",
        "brand": "Fossil",
        "category": "Watch",
        "price": 3999,
        "image_url": "https://images.pexels.com/photos/190819/pexels-photo-190819.jpeg"
    },

    {
        "name": "Red Dress",
        "brand": "Zara",
        "category": "Dress",
        "price": 2899,
        "image_url": "https://images.pexels.com/photos/985635/pexels-photo-985635.jpeg"
    }

]

products.insert_many(sample_products)

print("✅ Products Inserted Successfully!")