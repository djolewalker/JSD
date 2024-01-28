from src.parser import parser
import logging


def main():
    resume_path = '../resume_examples/person_one.resume'

    try:
        resume_model = parser.parse_resume(resume_path)
        print(resume_model)
    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    main()