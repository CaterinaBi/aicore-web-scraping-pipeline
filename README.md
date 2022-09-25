# Web scraping pipeline (AiCore training)

Web scraping pipeline I'm working on as part of my 'AI and data engineering' training at [AiCore](https://www.theaicore.com/?utm_source=google&utm_medium=cpc&utm_campaign=new-broad&utm_term=classification&utm_source=google&utm_medium=ppc&utm_campaign=UK-Brand&utm_term=ai%20core&utm_content=621263672281&hsa_acc=7296592433&hsa_cam=13050226730&hsa_grp=146850559851&hsa_ad=621263672281&hsa_src=g&hsa_tgt=kwd-453580118074&hsa_kw=ai%20core&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gclid=Cj0KCQjwj7CZBhDHARIsAPPWv3cRHYGa6UYh2t0kFM_4r7C6QAXdB4IMha25Y77p7wcgt712S5vymj4aAq8xEALw_wcB). Despite me being quite confident coding in Python, this is my first ever webscraping experience, therefore all technologies and tools mentioned throughout are being learned from scratch, one at a time 🤯

![Image from the AiCore portal](images/portal.png)

## 🏅 Goals of the project 🏅

The requirements for this data collection pipeline are to:

- develop a module that scrapes data from various sources using Selenium and Requests;

- curate a database with information about the chosen website and store it on an AWS RDS database using SQLAlchemy and PostgreSQL;

- perform unit testing and integration testing on the application to ensure that the package published to Pypi works as expected;

- use Docker to containerise the application and deploy it to an EC2 instance;

- set up a CI/CD pipeline using GitHub Actions to push a new Docker image;

- monitor the container using Prometheus and create dashboards to visualise those metrics using Grafana.

## Language and tools

<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://www.selenium.dev" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/detain/svg-logos/780f25886640cef088af994181646db2f6b1a3f8/svg/selenium-logo.svg" alt="selenium" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> </p>

## Milestones 1-2: Environment setup and choice of website to scrape

The project is being completed using [VS Code](https://code.visualstudio.com/) as a code editor, plus Git and GitHub for version control. The environment setup was done by creating a new environment, `web-scraping`, in conda. Once every required package had been installed, a `requirements.txt` file was generated.

The choice of website to scrape was based on two main criteria: personal interest, and learning opportunities. Being a real estate enthusiast, my choice fell rather naturally on [RightMove](https://www.rightmove.co.uk/). Quite luckily, the website is challenging to scrape and offers plenty of opportunities to learn HTML tricks. Additionally, it stores data in rigorous fashion, thus making it a pleasure to scrape and create a database out of.

Given that the website includes thousands of properties for sale and rent located throughout the United Kingdom, I decided to reduce the scope of my project to only include properties for sale in a 10-mile radius from Cambridge, as shown in the image below.

![Image from the RightMove website](images/website.png)

## Milestone 3: Find links to the pages from which we wish to scrape data

The project is written in Python and utilises OOP concepts throughout. In this milestone, I created a `Scraper()` class within a `scraper.py` file and started to populate it with methods intended to create a list of the properties featured on the first page of my research, and then extract the links of each one of these and store them in a dedicated list. The `main.py` file, which runs the code, includes what follows:

```python
if __name__ == '__main__':
    bot = Scraper()
    bot.bypass_cookies()
    while True:
        bot.get_all_properties_in_the_page()
        bot.get_all_property_links()
        bot.create_global_list()
        bot.scroll_to_bottom()
        bot.move_to_the_next_page()
```

`if __name__ == '__main__':` assigns the scraper to the `bot` variable. First, the scraper bypasses cookies - `try-except` is used in the `bypass_cookies` to make sure the programme doesn't crash in the absence of cookies to accept. The scraper then performs all actions from the methods in `scraper.py`, until all properties in all web pages into consideration have been found. This is done using a while-loop.

The scraper includes a crawler. The first action performed by the scraper after accepting the cookies is indeed that of finding all properties on the page, and then all the links to said properties. These are stored in dedicated lists, and then added to a `global_list` which is extended little with all extracted elements (properties and their links) from all pages. 

Once a page has been scraped, the scraper moves to the bottom of it and clicks on the 'next page' botton. `try-except` syntax is used to ensure that the programme doesn't crash when there is no more 'next page' button.

## Milestone 4: Retreive data from details page

Meaningful messages are printed throughout to make the user experience more pleasurable.