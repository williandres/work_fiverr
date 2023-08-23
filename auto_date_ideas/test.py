import openai

openai.api_key = ""
with open("ideas.txt", mode="r", encoding="utf-8") as archivo_ideas:
    ideas = archivo_ideas.read().splitlines()

nuevas_ideas = []
for _ in range(88):
    prompt = "Create a unique idea for a date"
    respuesta = openai.Completion.create(
        prompt=prompt,
        max_tokens=100,
        model="text-davinci-003",
        temperature=0.9,
        top_p=1,
        frequency_penalty=1,
        presence_penalty=1
    )
    print(respuesta.choices[0].text.strip())
    nuevas_ideas.append(respuesta.choices[0].text.strip())

ideas.extend(nuevas_ideas)
with open("ideas.txt", mode="w", encoding="utf-8") as archivo_txt:
    for idea in ideas:
        archivo_txt.write(idea + "\n")
