from setuptools import setup, find_packages

setup(name='scraper',
        version='1.0',
        packages=find_packages(),
        install_requires=[
            'selenium',
            'webdriver_manager',
            ])