# Explore Weather Trends
### Author: Chen Qingqing
#### Data: Oct 16, 2017

![](/Users/qingqing/udacity-course/exploring-weather-trends/data/weather.png)


In this project, I will analyze local and global temperature data and compare the temperature trends where you live to overall global temperature trends.

#### Instructions
I will create a visualization and prepare a write up describing the similarities and differences between global temperature trends and temperature trends in the closest big city to where I live. To do this, I’ll follow the steps below:

- **Extract the data** from the database. There's a workspace in the next section that is connected to a database. I’ll need to export the temperature data for the world as well as for the closest big city to where you live. I can find a list of cities and countries in the city_list table. To interact with the database, I'll need to write a SQL query.

    - Write a SQL query to extract the city level data. Export to CSV.
    - Write a SQL query to extract the global data. Export to CSV.

- **Open up the CSV** in whatever tool I feel most comfortable using.

- **Create a line chart** that compares my city’s temperatures with the global temperatures. Make sure to plot the moving average rather than the yearly averages in order to smooth out the lines, making trends more observable (the last concept in the previous lesson goes over how to do this in a spreadsheet).

- **Make observations** about the similarities and differences between the world averages and my city’s averages, as well as overall trends. Here are some questions to get started.

  - Is your city hotter or cooler on average compared to the global average? Has the difference been consistent over time?

  - “How do the changes in your city’s temperatures over time compare to the changes in the global average?”
  
  - What does the overall trend look like? Is the world getting hotter or cooler? Has the trend been consistent over the last few hundred years?



#### Extra data from a database using SQL
##### (1) Extra local temperature data
```SQL
SELECT *
FROM city_data
WHERE country LIKE ('Singapore') and avg_temp IS NOT NULL
ORDER BY year
```
##### (2) Extra my hometown temperature data
```SQL

SELECT *
FROM city_data
WHERE city LIKE ('Fuzhou') and avg_temp IS NOT NULL
ORDER BY year
```

##### (3) Extra global temperature data

```SQL

SELECT *
FROM global_data

```


#### Create a clear data visualization using Python

<center>
<img src="/Users/qingqing/udacity-course/exploring-weather-trends/data/py1.png"width="500"height="250"/>
</center>
<center>
<img src="/Users/qingqing/udacity-course/exploring-weather-trends/data/py2.png"width="500"height="400"/>
</center>


#### Interpret a data visualization
I use python to plot the data where I extracted using SQL. And the results are shown below:

</center>
<center>
<img src="/Users/qingqing/udacity-course/exploring-weather-trends/data/final.png"width="800"height="600"/>
</center>

In Figure1, it illustrates the change in Singapore temperature relative to 1825-2013 average temperatures. And the temperature range is around **25.5-27.5°C**, which is a bit higher than Fuzhou city where the temperature is around **17.5-20°C** in figure2, and it is much higher than the global average temperature if we look at the third figure where the range is only around **6-10°C**.

Since the temperature range of Singapore, Fuzhou city and global is different, and in order to better compare three of them easier. I do a normalization calculation. And the result is shown on figure4. We can see that they all show a waring trend neither in Singapore, Fuzhou city nor in global cities. The temperature keeps increasing, which point to the conclusion that **_our planet is warming_**.
