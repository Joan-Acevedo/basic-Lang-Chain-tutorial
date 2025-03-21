import os
import getpass
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate

# Cargar variables desde .env
load_dotenv()



# Verificar si OPENAI_API_KEY está configurada

if not os.environ.get("OPENAI_API_KEY"):
    print("No se encontró la API Key en el entorno. Verifica tu archivo .env")
    exit(1)

# Inicializar el modelo de chat
model = init_chat_model("gpt-4o-mini", model_provider="openai")

# Crear la plantilla de prompt
system_template = "Translate the following from English into {language}"
prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_template),
    ("user", "{text}")
])

# Definir el idioma y el texto a traducir
input_data = {"language": "Italian", "text": "hi!"}
prompt = prompt_template.invoke(input_data)

# Invocar el modelo con el prompt formateado
response = model.invoke(prompt)

# Mostrar la respuesta
print(response.content)
