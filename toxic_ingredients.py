import easyocr
from PIL import Image
import openai



product=input("Enter Product Name or image path: ")


if product.endswith('.jpg') or product.endswith('.png') or product.endswith('.jpeg'):
    reader = easyocr.Reader(['en'], gpu=True)
    # image_path = r'C:\Users\shilp\OneDrive\Documents\Luminar\Internship\61qvMq1Pd0L.jpg'
    image = Image.open(product)
    results = reader.readtext(product)
    name=''
    for detection in results:
        text = detection[1]
        name=name+" "+text
    print(name)

    openai.api_key='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'
    prompt=f"what are the toxic ingredients in '{name}' and its side effects"
    response=openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=300,
        temperature=0.1,
        )
    side_effects=response.choices[0].text.strip()
    print(side_effects)

else:
    openai.api_key='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'
    prompt=f"what are the toxic ingredients of '{product}' and its side effects"
    response=openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=300,
        temperature=0.1,
        )
    side_effects=response.choices[0].text.strip()
    print(side_effects)