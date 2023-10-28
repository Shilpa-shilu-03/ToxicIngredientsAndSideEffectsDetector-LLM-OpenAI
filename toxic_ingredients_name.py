import openai
product_name=input("Enter Product Name : ")

openai.api_key='Enter your API key'
prompt=f"what are the toxic ingredients of '{product_name}' and its side effects"
response=openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.1,
        )
side_effects=response.choices[0].text.strip()
print(side_effects)