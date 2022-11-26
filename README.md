
# Song Stat Graph Project

───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───  
───█▒▒░░░░░░░░░▒▒█───  
────█░░█░░░░░█░░█────  
─▄▄──█░░░▀█▀░░░█──▄▄─  
█░░█─▀▄░░░░░░░▄▀─█░░█  
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█  
█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█  
█░░║║║╠─║─║─║║║║║╠─░░█  
█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█  



Project for 12th Boards in Python (MatPlotLib, NumPy, Pandas) and MySQL by SAKSHHAM BHAGAT &amp; VASUNDHRA SHARMA




## Run Locally

First, clone this repo in your machine by
```sh
git clone https://github.com/SakshhamTheCoder/school-project.git
```


You need to make a MySQL Database having atleast these 4 columns

```Danceability```
```Energy```
```Tempo```
```Time_signature```

___

Then, make sure you have these dependencies installed on your machine

- [matplotlib](https://pypi.org/project/matplotlib/)
- [pandas](https://pypi.org/project/pandas/)
- [numpy](https://pypi.org/project/numpy/)
- [mysql-connector-python](https://pypi.org/project/mysql-connector-python/)

___

Now, change the **username**, **password**, and **database name** in the file to your SQL credentials

```python
# line 33
conn = mysql.connector.connect(user="your username", password="your password", database="your db name")
```

Finally, you can run the code on your machine by

```bash
cd school-project
python main.py
```


## Authors

- [@SakshhamTheCoder](https://www.github.com/SakshhamTheCoder) (Sakshham Bhagat)
- [@kitty788v](https://www.github.com/kitty788v) (Vasundhra Sharma)


*Thanks for Reading ^^*