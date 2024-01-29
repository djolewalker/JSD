import logging

from src.parser import parser
from src.generator import generator
from src.writter import writter


def main():
    resume_path = '../resume_examples/person_one.resume'

    try:
        resume_model = parser.parse_resume(resume_path)
        resume = generator.generate(resume_model)
        writter.write(resume_model, resume)
    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    main()
