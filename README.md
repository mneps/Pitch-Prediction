# Pitch Prediction
Matthew Carrington-Fair, Matthew Epstein, Ben Francis  
March 2019

## Setup
In order to import pitcher data, you will need to first install the following libraries:
```
pip3 install pandas html5lib lxml
```
Then run
```
python3 pull_data.py "[bbref_game_log_page]" [pitcher_id] [year]
```
* `bbref_game_log_page` should be a URL to a Baseball Reference page containing pitching game log information.  The link for Masahiro Tanaka's 2018 game logs, for example, is https://www.baseball-reference.com/players/gl.fcgi?id=tanakma01&t=p&year=2018.
* `pitcher_id` is a six-digit number which can be used to identify a player.  Each major league player has an identification number, which can be found by looking up that player's profile on mlb.com.  The player's profile page will have the URL format `https://www.mlb.com/player/[first_name]-[last_name]-[ID]`.  Tanaka's profile page, for example, can be found at https://www.mlb.com/player/masahiro-tanaka-547888, meaning his ID number is 547888.
* `year` is the year for which you wish to download statistics.  The year should be either a four digit number (eg. 2018) or simply read "postseason", in which case the program will find the data from the pitcher's entire postseason career.
Other than checking that three command line arguments exist, the progam does not do any error checking.  If the command line arguments are incorrect in some way, behavior is undefined.  If input is correct, the program will download statistics for every pitch the specified pitcher threw during the specified year and save the information in a file called titled `[pitcher_id].csv` in the working directory.


## Run the Program
To run the program, simply execute
```
python3 main.py data/[filename].csv
```
