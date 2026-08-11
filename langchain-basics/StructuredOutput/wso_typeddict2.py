from langchain_ollama import ChatOllama
from typing import TypedDict, Annotated

prompt = """Every morning, thousands of containers leave Indian ports carrying products for customers around the world. But behind every container is a story of a farmer, engineer, manufacturer, software developer, or entrepreneur.

Rajesh was one such entrepreneur.

He owned a small textile business in India. For years, he sold cotton clothes in the domestic market. His dream was to see his products in shops outside India.

One day, he received an inquiry from a buyer in Germany.

Rajesh prepared his products, arranged international packaging, completed the export documentation, and sent his first shipment. When the shipment successfully reached Germany, the buyer was impressed and placed another, larger order.

That small order changed Rajesh's business.

He started exporting to Germany, the United States, the United Kingdom, the UAE and other countries. He hired more workers and began purchasing raw materials from local suppliers.

India’s Export Numbers

Rajesh was only one small part of a much larger story.

India's exports have reached enormous levels. In FY 2025–26, India's total exports of goods and services were estimated at about US$860.09 billion, compared with US$825.26 billion in FY 2024–25 — an increase of about 4.22%.

Merchandise exports increased from US$437.70 billion in FY 2024–25 to US$441.78 billion in FY 2025–26. Non-petroleum exports also reached about US$387.88 billion.

India does not export only clothes and agricultural products. Its export basket includes engineering goods, petroleum products, pharmaceuticals, electronics, chemicals, automobiles, textiles, gems and jewellery, rice and other agricultural products.

The growth of electronics is particularly interesting. In April 2026, India's electronic-goods exports were estimated at US$5.18 billion, up 40.31% from US$3.69 billion in April 2025. Engineering-goods exports reached about US$10.35 billion in that month.

India's services sector is equally important. Software and other professional services allow an Indian company to serve customers in another country without physically shipping a product.
"""

class Review(TypedDict):
    key_points: Annotated[list[str], "Write down all the important key points"]
    summmary: Annotated[str, "Write a brief summarty in 300 words"]
    facts: Annotated[str, "Write the facts and figures avaialable in the prompts"]
    improvement: Annotated[str, "Keypoint to improve the exports"]

model = ChatOllama(model="qwen3:0.6b")

structured_model = model.with_structured_output(Review)

result = structured_model.invoke(prompt)

print(result)
