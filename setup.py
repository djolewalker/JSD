from setuptools import find_packages, setup


setup(
    name='resume_domain_builder',
    version='0.1.1',
    description='Resume builder tool with built in resume domain specific language',
    url='https://github.com/djolewalker/JSD',
    author='Dimitrije Zarkovic (djolewalker)',
    author_email='dimitrije24000@gmail.com',
    keywords='textX dsl resume',
    license='MIT',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    package_data={'': ['*.j2', '**/partials/*.j2', '*.css'], 'meta_model': ['*.tx']},
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
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)