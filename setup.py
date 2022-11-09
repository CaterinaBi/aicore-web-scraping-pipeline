from setuptools import setup, find_packages

setup(name='scraper',
        version='1.0',
        description='Package allows you to scrape property data from RightMove',
        url='https://github.com/CaterinaBi/aicore-web-scraping-pipeline',
        author='Caterina Bonan',
        license='MIT',
        packages=find_packages(),
        install_requires=[
            'selenium',
            'webdriver_manager'
            ])