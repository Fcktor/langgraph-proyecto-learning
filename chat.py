from graph import build_graph
from config import graph_config

def stream_graph_updates(graph, user_input: str):
    for event in graph.stream(
        {"messages": [{"role": "user", "content": user_input}]},
        config=graph_config,
        stream_mode="values"
    ):
        event["messages"][-1].pretty_print()


def run_chat_loop():
    graph = build_graph()
    while True:
        try:
            user_input = input("user: ")
            if user_input.lower() in ["exit", "quit", "q"]:
                print("Goodbye")
                break
            stream_graph_updates(graph, user_input)
        except KeyboardInterrupt:
            print("\nGoodbye")
            break
        except Exception as e:
            print(f"Error: {e}")
