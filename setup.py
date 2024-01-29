from setuptools import find_packages, setup


setup(
    name='resume_domain_builder',
    version='0.1.0',
    description='Resume builder tool with built in resume domain specific language',
    url='https://github.com/djolewalker/JSD',
    author='Dimitrije Zarkovic (djolewalker)',
    author_email='dimitrije24000@gmail.com',
    keywords='textX dsl resume',
    license='MIT',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    package_data={'': ['*.j2', '**/partials/*.j2', '*.css'], 'meta_model': ['meta_model/resume.tx']},
    install_requires=['textx', 'Jinja2'],
    entry_points={
        'textx_languages': [
            'resume_lang = parser.parser:resume_parser',
        ],
        'textx_generators': [
            'resume_gen = generator.generator:resume_generator',
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development :: Code Generators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.10',
    ],
)