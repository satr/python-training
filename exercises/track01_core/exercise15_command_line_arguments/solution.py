from __future__ import annotations

import argparse
from collections.abc import Sequence


def _bounded_count(value: str) -> int:
    try:
        count = int(value)
    except ValueError as error:
        raise argparse.ArgumentTypeError("count must be an integer") from error
    if not 1 <= count <= 1000:
        raise argparse.ArgumentTypeError("count must be between 1 and 1000")
    return count


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Create a greeting.")
    parser.add_argument("name", help="name to greet")
    parser.add_argument(
        "--count",
        type=_bounded_count,
        default=1,
        help="number of greetings to create (1-1000)",
    )
    parser.add_argument(
        "--shout", action="store_true", help="write the greeting in uppercase"
    )
    return parser


def parse_arguments(argv: Sequence[str] | None = None) -> argparse.Namespace:
    return build_parser().parse_args(argv)


def render_greeting(arguments: argparse.Namespace) -> str:
    greeting = f"Hello, {arguments.name}!"
    if arguments.shout:
        greeting = greeting.upper()
    return "\n".join(greeting for _ in range(arguments.count))


def main(argv: Sequence[str] | None = None) -> int:
    print(render_greeting(parse_arguments(argv)))
    return 0
