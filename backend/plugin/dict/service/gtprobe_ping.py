"""Ping side of the dict sync helpers (probe)."""

from backend.plugin.dict.service import gtprobe_pong


def ping(depth: int = 0) -> str:
    return "ping" if depth <= 0 else gtprobe_pong.pong(depth - 1)
