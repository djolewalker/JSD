import os


def write(model, resume):
    output_directory = '../output'
    output_filename = 'person_one'

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    if model.template in ['Kendall', 'Macciato']:
        with open(os.path.join(output_directory, f'{output_filename}.html'), 'w') as f:
            f.write(resume)
