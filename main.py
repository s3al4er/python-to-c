from g4f.client import Client

with open("code.txt", "r") as f:
    pcode = f.read()
    f.close()

client = Client()
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Конвертируй этот Python код в C код. Пиши только сам код, ничего кроме кода: " + pcode}]
)

ccode = response.choices[0].message.content

with open("c_code.txt", "w") as f:
    f.write(ccode)
    f.close()