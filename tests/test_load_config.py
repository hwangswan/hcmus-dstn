from dotenv import load_dotenv
import subprocess
import os

load_dotenv()


def test_single_yaml_config():
    result = subprocess.run(["python", os.getenv("EXECUTABLE", None), "single", "--config",
                            "configs/config.yaml", "--student_id", os.getenv("NAME", None), "--degree_id", os.getenv("DEGREE_ID", None)], capture_output=True, text=True)

    assert "HttpException" not in result.stdout

    assert "NotFoundException" not in result.stdout


def test_single_json_config():
    result = subprocess.run(["python", os.getenv("EXECUTABLE", None), "single", "--config",
                            "configs/config.json", "--student_id", os.getenv("NAME", None), "--degree_id", os.getenv("DEGREE_ID", None)], capture_output=True, text=True)

    assert "HttpException" not in result.stdout

    assert "NotFoundException" not in result.stdout


def test_multiple_yaml_config():
    result = subprocess.run(["python", os.getenv("EXECUTABLE", None), "multiple", "--config",
                            "configs/config.yaml", "--file", os.getenv("CSV_FILE", None)], capture_output=True, text=True)

    assert "HttpException" not in result.stdout

    assert "NotFoundException" not in result.stdout


def test_multiple_json_config():
    result = subprocess.run(["python", os.getenv("EXECUTABLE", None), "multiple", "--config",
                            "configs/config.json", "--file", os.getenv("CSV_FILE", None)], capture_output=True, text=True)

    assert "HttpException" not in result.stdout

    assert "NotFoundException" not in result.stdout
