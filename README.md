# JSD

Domain-specific language to support the creation of standardized CVs (Curriculum Vitae - resume)

## Overview

The DSL for standardized CV creation is a specialized language designed to simplify and standardize the process of
crafting professional resumes.
It defines a structured format for CVs, encompassing sections such as personal information, education, work experience,
skills, and references.
The syntax is constructed using a formal language definition, making it easy for users to input their CV details in a
structured and uniform manner.
A complementary application will allow users to display their CVs in a variety of templates, providing posibility to
present qualifications effectively and professionally.

The CV sections:

- personal basic information
- education
- work experience
- volunteer activities
- awards, certifications
- publications
- skills, languages, interests
- project contributions

The CV sections are enriched with a set of attributes that best describe them.

## Implementation

1. [textX](https://github.com/textX/textX) for the definition of abstract syntax with textual concrete syntax.
2. Python + Jinja2 template engine for a utility application to populate the CV template with standardized data.
3. VSCode plugin.

## Usage

Project can be run locally or as a package with pip package provider and textX cli.

### Local run

To prepare venv follow instructions:

```bash
git clone https://github.com/djolewalker/JSD
cd JSD
python3 -m venv venv
source venv/bin/activate
(venv): pip3 install -r requirements.txt
```

When virtual environment is ready we can use our tool. `main.py` file contains path to the example .resume file.
Change it to point your file and everything is ready to be run.

```bash
(venv): python3 main.py
```

### Use with textX cli

To keep global environment clean it is recommended to use venv:

```bash
python3 -m venv venv
source venv/bin/activate
# Optional if you miss textX cli
(venv): pip3 install textx[cli]
```

In the virtual environment install `resume_domain_builder` package:

```bash
(venv): pip isntall git+https://github.com/djolewalker/JSD@develop
```

To check if language and generator are available in the text:

```bash
textx list-languages
# output: 
# ...
# resume (*.resume)             resume-domain-builder[0.1.1] 
# ...

textx list-generators
# output: 
# ...
# resume -> HTML                resume-domain-builder[0.1.1] 
# ...
```

To generate resume use next textX command:

```bash
textx generate resume_examples/example_resume.resume --target HTML -o .
```

## Example
Resume example written in resume dsl
```
Personal info:
    Name: "John Doe"
    Label: "Programmer"
    Image: https://www.hsph.harvard.edu/diversity/wp-content/uploads/sites/2597/2020/11/Barbosa-1-500x500-1.jpg
    Email: john@gmail.com
    Phone: (912) 555-4321
    URL: https://johndoe.com/
    Summary: "A summary of John Doe…"
    Location: 
        Address: "2712 Broadway St"
        City: "San Francisco"
        Country Code: US
        Postal Code: "CA 94115"
        Region: "California"
    Profiles:
        Network: "Twitter"
        URL: https://twitter.com/john/
        Username: "john"

        Network: "Linkedin"
        URL: https://linkedin.com/johnDoe/
        Username: "John Doe"

        Network: "Instagram"
        URL: https://instagram.com/john_the_programmer/
        Username: "john_the_programmer"


Works:
    Name: "Company 1"
    Position: "President"
    URL: https://company.com
    Duration: 
        Start date: 02-2019
    Summary: "The best director in the company 1"
    Highlights: "Started the company", "God of programming"

    Name: "Company 2"
    Position: "Programmer"
    URL: https://max-company.com
    Duration: 
        Start date: 06-2015
        End date: 02-2019
    Summary: "The best programmer in the company"
    Highlights: "C#, Development leader, Good employee"


Volunteer:
    Organization: "Organization"
    Position: "Volunteer"
    URL: https://organization.com/
    Duration: 
        Start date: 01-01-2020
        End date: 01-01-2021
    Summary: "Description…"
    Highlights: "Awarded 'Volunteer of the Month'"


Education:
    Institution: "University"
    URL: https://institution.com/
    Area: "Software Development"
    Study type: Bachelor
    Duration: 
        Start date: 09-2011
        End date: 09-2015
    Score: 10.0
    Courses: "DB1101 - Basic SQL", "CC2105 - Software engineering"


Certificates:
    Name: "Certificate"
    Date: 07-11-2021
    Issuer: "Issuer Company"
    URL: https://certificate.com


Awards:
    Title: "Award"
    Date: 12-2019
    Issuer: "Company"
    Summary: "Best employee of the year"


Publications:
    Name: "Publication"
    Publisher: "Company"
    Release date: 01-10-2019
    URL: https://publication.com
    Summary: "Description…"


Skills:
    Name: "Web Development"
    Level: "Master"
    Keywords: "HTML", "CSS", "JavaScript"

    Name: "Data Base modeling"
    Level: "Average"
    Keywords: "SQL", "SSMS", "SQL Server"


Languages:
    Language: "English"
    Fluency: "Native speaker"

    Language: "French"
    Fluency: "B2"


Interests:
    Name: "Wildlife"
    Keywords: "Ferrets", "Unicorns"


Projects:
    Name: "Project"
    Duration:
        Start date: 01-01-2019
        End date: 05-11-2021
    Description: "Description..."
    Highlights: "Won award at AIHacks 2020"
    URL: https://project.com/

Template: Macciato
```

## Output generated with Macciato template
![example resume image](https://raw.githubusercontent.com/djolewalker/JSD/develop/.github/example_resume.png)