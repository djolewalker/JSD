import logging

from parser.parser import parse_resume
from generator.generator import generate


def main():
    resume_path = '../resume_examples/person_one.resume'

    try:
        resume_model = parse_resume(resume_path)
        resume = generate(resume_model)
    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    main()
