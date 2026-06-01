# 🤖 AI Agent con LangGraph + Groq + Tavily

Agente conversacional con capacidad de búsqueda web en tiempo real, construido con **LangGraph** para orquestar el flujo de estados del agente.

## ¿Qué hace?

- Mantiene conversaciones con memoria de contexto persistente (SQLite)
- Realiza búsquedas web automáticamente cuando necesita información actualizada (via Tavily)
- Usa **Llama 3.3 70B** (Groq) como modelo de lenguaje — respuestas rápidas y gratuitas
- Arquitectura basada en grafos de estado con LangGraph

## Stack

| Tecnología | Uso |
|---|---|
| LangGraph | Orquestación del agente (grafo de estados) |
| Groq API (Llama 3.3 70B) | Modelo de lenguaje |
| Tavily | Búsqueda web en tiempo real |
| SQLite | Memoria persistente entre sesiones |
| Python 3.12 + uv | Lenguaje y gestor de dependencias |

## Arquitectura

```
state.py     →  Define el estado del grafo (mensajes, contexto)
config.py    →  Configura LLM, herramientas y memoria
graph.py     →  Define el grafo de LangGraph (nodos + aristas)
chat.py      →  Loop interactivo de conversación
main.py      →  Punto de entrada
```

## Instalación

```bash
# Clonar el repo
git clone https://github.com/Fcktor/langgraph-proyecto-learning
cd langgraph-proyecto-learning

# Instalar dependencias con uv
uv sync

# Activar entorno
source .venv/bin/activate

# Configurar variables de entorno
cp .env.example .env
# Editar .env con tus API keys
```

## Variables de entorno

```env
GROQ_API_KEY=tu_api_key_de_groq
TAVILY_API_KEY=tu_api_key_de_tavily
```

Ambas APIs tienen **tier gratuito**:
- Groq: https://console.groq.com
- Tavily: https://app.tavily.com

## Uso

```bash
python main.py
```

Escribe tu mensaje y presiona Enter. Para salir: `exit`, `quit` o `q`.

El historial de conversaciones se guarda automáticamente en `conversations.db`.

## Próximos pasos

- [ ] Agregar más herramientas: calculadora, ejecutor de código
- [ ] Interfaz web con Streamlit o Gradio
- [ ] Soporte multi-conversación con thread_id dinámico
- [ ] Tests unitarios para nodos del grafo
