from google import genai
from google.genai.errors import APIError
from dotenv import load_dotenv
import os

load_dotenv()
client = genai.Client()

class RespostaIA:
    def __init__(self, resposta, id=None):
        self.resposta = resposta
        self.id = id

    def interacao(self):
        try:
            interaction = client.interactions.create(
                model="gemini-3.5-flash",
                input=self.resposta,
                previous_interaction_id=self.id

            )

            print(interaction.output_text)
            return interaction.id

        except (APIError) as erro:
            print("\nHouve um erro de conexão e/ou rede. Verifique seu wi-fi!")
            print(f"Detalhes do erro: {erro}\n")

            return self.id

historico = None

while True:

    pergunta_usuario = input("Digite aqui xuxu: ")

    aux = RespostaIA(pergunta_usuario, historico)
    historico = aux.interacao()

    extra = input("Tem mais alguma dúvida?(s/n): ").lower()

    if extra == "s":
        os.system("clear")

    else:
        print("Obrigado pela conversa!")
        break