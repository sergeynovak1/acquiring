from dependency_injector.containers import WiringConfiguration, copy

from src.dependency.use_case_container import UseCaseContainer


@copy(UseCaseContainer)
class Container(UseCaseContainer):
    wiring_config = WiringConfiguration(
        modules=[],
    )
