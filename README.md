# LangGraph Proyecto Learning

Proyecto de aprendizaje sobre **LangGraph** — un framework para construir aplicaciones con agentes de IA usando grafos de estado.

## Stack

- **LangGraph** — orquestación de agentes basada en grafos
- **LangChain** — integración con LLMs
- **OpenAI GPT-4o** — modelo de lenguaje
- **Tavily** — búsqueda web para los agentes

## Setup

```bash
# Crear entorno virtual
uv venv

# Activar entorno
source .venv/bin/activate

# Instalar dependencias
uv sync
```

## Variables de entorno

Crea un archivo `.env` en la raíz del proyecto:

```env
OPENAI_API_KEY=sk-proj-tu-clave
TAVILY_API_KEY=tvly-dev-tu-clave
```

## Estructura

```
├── config.py      # Configuración del LLM, herramientas y memoria
├── graph.py       # Definición del grafo de LangGraph
├── main.py        # Punto de entrada
├── state.py       # Estado del grafo
├── .env           # Variables de entorno (no se sube a Git)
└── pyproject.toml # Dependencias y metadata
```

## Uso

```bash
python main.py
```
