from textx import metamodel_from_file, language
from importlib.resources import files
import os

resume_metamodel_path = files('meta_model').joinpath('resume.tx')


def get_meta_model():
    return metamodel_from_file(str(resume_metamodel_path))


def parse_resume(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The resume file was not found at location {file_path}.")

    return get_meta_model().model_from_file(file_path)


@language('resume', '*.resume')
def resume_parser():
    return get_meta_model()
