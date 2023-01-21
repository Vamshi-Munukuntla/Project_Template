from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

SRC_REPO = 'src'
AUTHOR = 'Vamshi-Munukuntla'
AUTHOR_EMAIL = 'vamshi.kumar59@gmail.com'
REPO_NAME = 'Project_Template'
LIST_OF_REQUIREMENTS = []

setup(name=SRC_REPO,
      version='0.0.1',
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      description='This is our first release',
      long_description=long_description,
      url=f'https://github.com/{AUTHOR}/{REPO_NAME}',
      packages=[SRC_REPO],
      python_requires=">=3.6",
      install_requires=LIST_OF_REQUIREMENTS
      )

