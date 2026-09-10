from __future__ import annotations

import argparse
from collections.abc import Sequence


def build_parser() -> argparse.ArgumentParser:
    raise NotImplementedError


def parse_arguments(argv: Sequence[str] | None = None) -> argparse.Namespace:
    raise NotImplementedError


def render_greeting(arguments: argparse.Namespace) -> str:
    raise NotImplementedError


def main(argv: Sequence[str] | None = None) -> int:
    raise NotImplementedError
