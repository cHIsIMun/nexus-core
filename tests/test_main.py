from typer.testing import CliRunner
from nexus_core.main import app

runner = CliRunner()

def test_hello():
    result = runner.invoke(app, ["hello", "Tester"])
    assert "Hello Tester" in result.stdout
