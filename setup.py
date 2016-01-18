try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project, used to create new project setup.',
    'author': 'Rob',
    'url': 'URL to get it at.',
    'download_url': 'www.Where to download it.',
    'author_email': 'My@email',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47', 'ex48'],
    # 'packages': find_packages(),
    'scripts': [],
    'name': 'project name'
}

setup(**config)
