# Jupyter Dashboard - Voila

## Introduction
This notebook is a dashboard publication tool via Jupyter-Voila. It is developed based on this [tutorial](https://github.com/voila-dashboards/voila-heroku) by Martin Renou.

This notebook is organized into modules to complete the following tasks:

1. Data Analysis
2. Data Visualization
3. Dashboard Publication

## Notebook Modules

This repository is organized into the following folders:

1. Data - Contains CSV files used for analysis
2. Modules (Notebook) - Individual modules used for data analysis
3. Modules (Voila) - Individual modules used for data publication
4. Notebooks - Voila publishes from file named "bqplot.ipynb"

## VTA Open Data

This dashboard visualizes cumulative monthly ridership from the VTA Open Data [Portal](http://data.vta.org/). The Portal is described as "central location for access to VTA's open data, including transit, active transportation, congestion management and more."

The [monthly ridership data](http://data.vta.org/datasets/ridership-by-route-cumulative-monthly) includes fields for train route, line type, ridership and cumulative monthly period. It consists of data from 2013 to 2018; chart below shows monthly cumulative passenger boarding count by VTA train line type.

## Original README

## Voila application deployed on Heroku

This is an example of Voila deployed on Heroku, try it out: https://voila-heroku-demo.herokuapp.com

## How to deploy your own?

1. First, create an Heroku account (free account is fine for testing)

2. Install Heroku on your machine: https://devcenter.heroku.com/articles/getting-started-with-python#set-up

2. Clone this repository, or create your own repository that follows the same structure:

```bash
git clone https://github.com/voila-dashboards/voila-heroku
cd voila-heroku
```

3. Create your Notebook and put it in the `notebooks` directory

5. Add the dependencies needed for running your Notebook in the `requirements.txt` file

6. Edit the `Procfile` file by replacing `notebooks/bqplot.ipynb` by the path to your awesome Notebook

7. Commit everything

```bash
git commit -m "My awesome app on Heroku!"
```

8. Create the Heroku app:

```bash
heroku create
```

9. Now deploy your code:

```bash
git push heroku master
```

10. That's it! Easy right? Now you can open your app using:

```bash

heroku open
```

Note that this last command is only a handy shortcut for opening your browser following the right url, you can also do that manually.

## Extra steps

- You can rename your application on the Heroku website, in the applicaion settings. If you rename it, don't forget to update the remote repository doing `git remote remove heroku && git remote add heroku https://git.heroku.com/your-application-name.git`
- You can add/remove/update voila command line arguments in the `Procfile` file, _e.g._ you can use the dark theme by adding `--theme=dark`
