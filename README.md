# Basic LangChain Tutorial  

## Descripción del Proyecto  
Este proyecto implementa una aplicación básica de traducción de texto utilizando LangChain. El objetivo es aprender a usar modelos de lenguaje (LLMs), plantillas de prompts y herramientas de depuración con LangSmith.  

## Arquitectura y Componentes  
El proyecto se basa en la siguiente estructura:  

```
PythonProject/
├── .venv/              # Entorno virtual (excluido del repo)
├── .gitignore          # Archivos ignorados por Git
├── .env                # Variables de entorno (no incluido en el repo)
├── llm_chain.py        # Código principal del proyecto
└── README.md           # Documentación del proyecto
```


- **LangChain**: Framework para construir aplicaciones con LLMs.  
- **OpenAI API**: Se utiliza como modelo de lenguaje para la traducción.  
- **ChatPromptTemplate**: Genera prompts estructurados para el modelo.  

## Instalación  

1. **Clonar el repositorio**:  
   ```
   git clone https://github.com/Joan-Acevedo/basic-Lang-Chain-tutorial.git  
   cd basic-Lang-Chain-tutorial  
    ```

---   
**Nota**

Si necesitas activar el entorno virtual, agrega el siguiente comando:

```
.\.venv\Scripts\activate
```

---

2. Para las dependencias ejecutamos en la terminal:

```
pip install langchain openai
```
```
pip install -qU "langchain[openai]"
```

3. Configurar variables de entorno: Creamos un archivo `.env` en la raiz del proyecto, en el cual agregamos el siguiente codigo:

```
OPENAI_API_KEY=llave_api #Por seguridad, no la subimos al repo 
```

## Uso

Ejcutar en la terminal:

```
python llm_chain.py  
```
### Ejemplo de salida:

![Image](https://github.com/user-attachments/assets/28b2a0d8-a9a9-44af-b4c4-4cac0b7a6079)

## Autor

Joan S. Acevedo Aguilar