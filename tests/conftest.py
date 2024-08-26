import pytest
import os
import importlib.util


def pytest_addoption(parser):
    parser.addoption("--developer", action="store", default="default_value")


@pytest.fixture
def developer(request):
    return request.config.getoption("--developer")


def import_solution_module(developer):
    solution_path = os.path.join(
        "submissions", f"developer-{developer}", "results", "solution.py"
    )
    assert os.path.exists(
        solution_path
    ), f"Solution file {solution_path} does not exist."

    spec = importlib.util.spec_from_file_location("solution", solution_path)
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    return solution


@pytest.fixture(scope="session")
def solution(request):
    developer = request.config.getoption("--developer")
    solution = import_solution_module(developer)
    return solution


# run pytest tests/autoamtic_task_verification.py --developer=<number>
