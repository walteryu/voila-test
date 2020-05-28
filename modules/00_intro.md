<h1><center>Jupyter Dashboard with Voila</center></h1>

<center><i>Dashboard to visualize open data, based on tutorial by <a href="https://github.com/voila-dashboards/voila-heroku">Martin Renou</a> with <a href="https://github.com/voila-dashboards/voila">Voila</a>, <a href="https://pandas.pydata.org/">Pandas</a> and <a href="https://seaborn.pydata.org/">Seaborn</a>.</i></center>

<center><i>Source Code on <a href="https://github.com/walteryu/voila-test">Github</a></i></center>

## Introduction

This notebook is a dashboard publication tool via Jupyter-Voila. It is developed based on this [tutorial](https://github.com/voila-dashboards/voila-heroku) by Martin Renou.

This notebook is organized into modules to complete the following tasks:

1. Data Analysis
2. Data Visualization
3. Dashboard Publication

## VTA Open Data

This dashboard visualizes cumulative monthly ridership from the VTA Open Data [Portal](http://data.vta.org/). The Portal is described as "central location for access to VTA's open data, including transit, active transportation, congestion management and more."

The [monthly ridership data](http://data.vta.org/datasets/ridership-by-route-cumulative-monthly) includes fields for train route, line type, ridership and cumulative monthly period. It consists of data from 2013 to 2018.
