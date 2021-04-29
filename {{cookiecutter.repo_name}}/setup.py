from setuptools import setup

requirements = [
    # package requirements go here
]

setup(
    name='{{ cookiecutter.repo_name }}',
    version='0.1.0',
    description="{{ cookiecutter.project_short_description }}",
    license="{{ cookiecutter.open_source_license }}",
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    packages=['{{ cookiecutter.package_name }}'],
    {% if cookiecutter.include_cli == "y" -%}
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.package_name }}={{ cookiecutter.package_name }}.cli:cli'
        ]
    },
    {%- endif %}
    install_requires=requirements,
    keywords='{{ cookiecutter.repo_name }}',
    classifiers=[
        'Programming Language :: Python :: 3.8',
    ]
)
