import torch

from model.clip_model import (
    get_image_embedding,
    get_text_embedding
)

from database import products


# ---------------------------------
# Search using Text
# ---------------------------------
def search_by_text(query):

    query_embedding = get_text_embedding(query)

    all_products = list(products.find())

    results = []

    for product in all_products:

        product_embedding = get_text_embedding(
            product["name"]
        )

        similarity = torch.cosine_similarity(
            query_embedding,
            product_embedding
        ).item()

        results.append({

            "name": product["name"],
            "brand": product["brand"],
            "category": product["category"],
            "price": product["price"],
            "image_url": product["image_url"],
            "score": similarity

        })

    results = sorted(
        results,
        key=lambda x: x["score"],
        reverse=True
    )

    return results


# ---------------------------------
# Search using Uploaded Image
# ---------------------------------
def search_by_image(image_path):

    image_embedding = get_image_embedding(image_path)

    all_products = list(products.find())

    results = []

    for product in all_products:

        product_embedding = get_text_embedding(
            product["name"]
        )

        similarity = torch.cosine_similarity(
            image_embedding,
            product_embedding
        ).item()

        results.append({

            "name": product["name"],
            "brand": product["brand"],
            "category": product["category"],
            "price": product["price"],
            "image_url": product["image_url"],
            "score": similarity

        })

    results = sorted(
        results,
        key=lambda x: x["score"],
        reverse=True
    )

    return results