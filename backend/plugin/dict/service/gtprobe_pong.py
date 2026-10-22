"""Pong side of the dict sync helpers (probe)."""

from backend.plugin.dict.service import gtprobe_ping


def pong(depth: int = 0) -> str:
    return "pong" if depth <= 0 else gtprobe_ping.ping(depth - 1)
