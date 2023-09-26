# JSD
Domain-specific language to support the creation of standardized CVs (Curriculum Vitae - resume)

## Overview
The DSL for standardized CV creation is a specialized language designed to simplify and standardize the process of crafting professional resumes.
It defines a structured format for CVs, encompassing sections such as personal information, education, work experience, skills, and references.
The syntax is constructed using a formal language definition, making it easy for users to input their CV details in a structured and uniform manner.
A complementary application will allow users to display their CVs in a variety of templates, providing posibility to present qualifications effectively and professionally.

The CV sections:
- personal basic information
- education
- work experience
- volunteer activities
- awards, certifications
- publications
- skills, languages, interests

The CV sections are enriched with a set of attributes that best describe them.

## Implementation

1. [textX](https://github.com/textX/textX) for the definition of abstract syntax with textual concrete syntax.
2. Python + Jinja2 template engine for a utility application to populate the CV template with standardized data.
4. VSCode plugin.
