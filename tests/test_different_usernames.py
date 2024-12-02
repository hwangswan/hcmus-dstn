from dotenv import load_dotenv
import subprocess
import os

load_dotenv()

def test_using_student_id():
    result = subprocess.run(["python", os.getenv("EXECUTABLE", None), "single", "--config",
                            "configs/config.yaml", "--student_id", os.getenv("STUDENT_ID", None), "--degree_id", os.getenv("DEGREE_ID", None)], capture_output=True, text=True)

    assert "HttpException" not in result.stdout

    assert "NotFoundException" not in result.stdout
    
def test_using_no_diacritics_name():
    result = subprocess.run(["python", os.getenv("EXECUTABLE", None), "single", "--config",
                            "configs/config.yaml", "--student_id", os.getenv("NAME", None), "--degree_id", os.getenv("DEGREE_ID", None)], capture_output=True, text=True)

    assert "HttpException" not in result.stdout

    assert "NotFoundException" not in result.stdout
    
def test_using_diacritics_name():
    result = subprocess.run(["python", os.getenv("EXECUTABLE", None), "single", "--config",
                            "configs/config.yaml", "--student_id", os.getenv("NAME_VN", None), "--degree_id", os.getenv("DEGREE_ID", None)], capture_output=True, text=True)

    assert "HttpException" not in result.stdout

    assert "NotFoundException" not in result.stdout