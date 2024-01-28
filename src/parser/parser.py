from textx import metamodel_from_file
import os

resume_metamodel_path = 'meta_model/resume.tx'


def parse_resume(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The resume file was not found at location {file_path}.")

    metamodel = metamodel_from_file(resume_metamodel_path)

    resume_model = metamodel.model_from_file(file_path)

    return resume_model
