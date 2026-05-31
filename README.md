# LangGraph Proyecto Learning

Proyecto de aprendizaje sobre **LangGraph** — un framework para construir aplicaciones con agentes de IA usando grafos de estado.

## Stack

- **LangGraph** — orquestación de agentes basada en grafos
- **Groq (Llama 3.3 70B)** — modelo de lenguaje
- **Tavily** — búsqueda web para los agentes
- **Python 3.12**

## Setup

```bash
# Crear entorno virtual e instalar dependencias
uv sync

# Activar entorno
source .venv/bin/activate
```

## Variables de entorno

Crea un archivo `.env` en la raíz del proyecto:

```env
GROQ_API_KEY=gsk_tu-clave
TAVILY_API_KEY=tvly-dev-tu-clave
```

## Estructura

```
├── chat.py         # Bucle interactivo del chat
├── config.py       # Configuración del LLM, herramientas y memoria
├── graph.py        # Definición del grafo de LangGraph
├── main.py         # Punto de entrada
├── state.py        # Estado del grafo
├── .env            # Variables de entorno (no se sube a Git)
└── pyproject.toml  # Dependencias y metadata
```

## Uso

```bash
python main.py
```

Escribe `exit`, `quit` o `q` para salir.
