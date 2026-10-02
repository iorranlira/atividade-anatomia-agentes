import json
from pathlib import Path
from typing import Any


TRACE_FILE = Path("trace.txt")


def clear_trace():
    TRACE_FILE.write_text("", encoding="utf-8")


def write_interaction(interaction_id: int, user_input: str):
    with open(TRACE_FILE, "a", encoding="utf-8") as f:
        f.write("=" * 80 + "\n")
        f.write(f"INTERACTION {interaction_id}\n")
        f.write("=" * 80 + "\n")
        f.write("User:\n")
        f.write(user_input + "\n\n")


def write_iteration(
    iteration: int,
    thought: str,
    action: str = None,
    args: dict[str, Any] = None,
    observation: Any = None,
):
    with open(TRACE_FILE, "a", encoding="utf-8") as f:
        f.write(f"ITERATION {iteration}\n")
        f.write("-" * 80 + "\n")

        f.write("Thought:\n")
        f.write(thought.strip() + "\n")

        if action is not None:
            f.write("\nAction:\n")
            f.write(f"Tool: {action}\n")
            f.write(
                f"Args: {json.dumps(args, ensure_ascii=False)}\n"
            )

            f.write("\nObservation:\n")
            f.write(
                json.dumps(
                    observation,
                    ensure_ascii=False,
                    indent=2
                )
                + "\n"
            )

        f.write("\n")