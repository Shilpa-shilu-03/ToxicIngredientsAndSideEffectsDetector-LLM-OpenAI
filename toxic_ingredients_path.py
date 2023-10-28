import easyocr
from PIL import Image
import openai

reader = easyocr.Reader(['en'], gpu=False)
image_path = r'C:\Users\shilp\OneDrive\Documents\Luminar\Internship\Toxicity\Minimalist-Sunscreen.jpg'
image = Image.open(image_path)

results = reader.readtext(image)
name=''
for detection in results:
    text = detection[1]
    name=name+" "+text
print(name)
openai.api_key='Enter your API key'
prompt=f"what are the toxic ingredients in '{name}' and its side effects"
response=openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.1,
        )
side_effects=response.choices[0].text.strip()
print(side_effects)