from dependency_injector.containers import copy

from src.dependency.uow_container import UowContainer


@copy(UowContainer)
class UseCaseContainer(UowContainer): ...
