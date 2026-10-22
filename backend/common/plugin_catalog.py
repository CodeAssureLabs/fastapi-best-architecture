"""Catalog helpers for the installed plugin routers."""

from backend.plugin.code_generator.api.router import v1 as code_generation_router


def code_generation_route_paths() -> list[str]:
    """Return the paths mounted by the code-generation plugin router."""
    return sorted(route.path for route in code_generation_router.routes)
