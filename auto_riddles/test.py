import openai
import csv


openai.api_key = ""

riddles = []
for _ in range(5):
    prompt = "Create a unique riddle, separating the riddle and its answer with '|'. Remember to be creative and distinct from previous prompts:"
    respuesta = openai.Completion.create(
        prompt=prompt,
        max_tokens=70,
        model="text-davinci-003",
        temperature=0.3,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0.5
    )
    print(respuesta.choices[0].text.strip())
    row = respuesta.choices[0].text.strip().split("|")
    row = [elemento.strip() for elemento in row]

    riddles.append(row)

with open("riddles.csv", mode="w", newline="", encoding="utf-8") as archivo_csv:
    writer = csv.writer(archivo_csv)
    writer.writerow(["Riddles", "Answers"])
    for row in riddles:
        writer.writerow(row)
