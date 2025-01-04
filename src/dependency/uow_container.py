from dependency_injector.containers import copy

from src.core.containers import BaseContainer


@copy(BaseContainer)
class UowContainer(BaseContainer): ...
