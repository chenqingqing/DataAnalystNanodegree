# Explore US Bikeshare DataAnalysis
## Overview
In this project, you will make use of Python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. You will write code to import the data and answer interesting questions about it by computing descriptive statistics. You will also write a script that takes in raw input to create an interactive experience in the terminal to present these statistics.

## Bike Share Data
Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

In this project, you will use data provided by [Motivate](https://www.motivateco.com/), a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. You will compare the system usage between three large cities: Chicago, New York City, and Washington, DC.

## The Datasets
Data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:
  - Start Time (e.g., 2017-01-01 00:07:57)
  - End Time (e.g., 2017-01-01 00:20:53)
  - Trip Duration (in seconds - e.g., 776)
  - Start Station (e.g., Broadway & Barry Ave)
  - End Station (e.g. Sedgwick St & North Ave)
  - User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:
  - Gender
  - Birth Year

The original files, which can be accessed here ([Chicago](https://www.divvybikes.com/system-data), [New York](https://www.citibikenyc.com/system-data) City, [Washington](https://www.capitalbikeshare.com/system-data)), had more columns and they differed in format in many cases. Some [data wrangling](https://en.wikipedia.org/wiki/Data_wrangling) has been performed to condense these files to the above core six columns to make your analysis and the evaluation of your Python skills more straightforward. In the Data Wrangling course that follows this course in the Data Analyst Nanodegree program, students learn how to wrangle the dirtiest, messiest datasets so don't fret if you worried about missing out.

## The Questions
You will write code to answer the following questions about the bike share data:
  - What is the most popular month for start time?
  - What is the most popular day of week (Monday, Tuesday, etc.) for start time? Hint: datetime.weekday() (documentation [here](https://docs.python.org/3/library/datetime.html#datetime.date.weekday)) may be helpful!
  - What is the most popular hour of day for start time?
  - What is the total trip duration and average trip duration?
  - What is the most popular start station and most popular end station?
  - What is the most popular trip?
  - What are the counts of each user type?
  - What are the counts of gender?
  - What are the earliest (i.e. oldest person), most recent (i.e. youngest person), and most popular birth years?

## TODOs
All of the code you must fill out in bikeshare.py is marked in comments that start with "TODO". Take a detailed read through that file to get a gauge for how the script flows and the additions you will have to make to complete this project.

## An Interactive Experience
The bikeshare.py file is set up as a script that takes in raw input to create an interactive experience in the terminal that answers questions about the dataset. The experience is interactive because depending on a user's input, the answers to the questions on the previous page will change! There are four questions that will change the answers:
  - Would you like to see data for Chicago, New York, or Washington?
  - Would you like to filter the data by month, day, or not at all?
  - Which month? January, February, March, April, May, or June?
  - Which day?

The four questions above are already provided for you as input() statements in bikeshare.py. You will write the conditional code to guide this interactive experience.

A sample end product would look something like this:
  - Prompt: Hello! Let's explore some US bikeshare data! Would you like to see data for Chicago, New York, or Washington?
  - User input: Chicago
  - Prompt: Would you like to filter the data by month, day, or not at all? Type "none" for no time filter.
  - User input: month
  - Prompt: Which month? January, February, March, April, May, or June?
  - User input: March
  - Statistics for Chicago in March are printed out
  - Prompt: Would you like to restart? Type 'yes' or 'no.'
  - User input: no

For printing out statistics, keep in mind one goal of the script is to present the statistics (e.g., "What is the most popular hour of day?") in a way that is pleasurable to read.

Note that this bikeshare.py file is simply a template you can use, but you don't need to use it. You can change the functions however you like as long as you have an ending product that works like the above sample interactive experience. Changes to the structure of bikeshare.py (e.g., adding and/or deleting helper functions) that you think make the code more efficient or have a better style are encouraged!

## The csv Module
The csv module is core to completing this project. Its DictReader class will allow you to interact with the bikeshare data CSV files as if they were Python dictionaries. DictReader returns an iterator that produces each row as needed. Check out [this documentation page](https://docs.python.org/3/library/csv.html#csv.DictReader) for a short usage example.

One thing to be careful about—these bikeshare CSV files are quite large so iterating through them will be costly in terms of compute time. Two strategies to mitigate this:
  - Load each CSV file into a data structure once at the beginning of the script rather than at the beginning of every function. Hint: converting the DictReader iterator into a list of dictionaries (as described in this [Stack Overflow](https://stackoverflow.com/questions/21572175/convert-csv-file-to-list-of-dictionaries/21572244) post) could be handy!
  - Be sure to bite off bits of code that you can chew and regularly test your code as you develop it. Print statements are your friend.

If you are familiar with NumPy and/or pandas, you may realize that using the csv module is much less efficient than these libraries tailored for data analysis. The csv module is used in this project so foundational programming skills can be tested, as well as to gain an appreciation for the speed at which NumPy and pandas (which are taught later in the Data Analyst Nanodegree program) can do their calculations on large files. If you already possess NumPy and/or pandas skills, you are welcome to use them in this project. If you don't, do not worry—these libraries are taught in the next course in the Data Analyst Nanodegree program.
