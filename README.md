# Pitch Prediction
Matthew Carrington-Fair, Matthew Epstein, Ben Francis  
March 2019

## Setup
To run the program, it is necessary to have a CSV file with pitch-by-pitch information for a number of games that a single pitcher appeared in.  In order to obtain this data, we can use the `pull_data.py` program, which will collect data for every pitch thrown by a specified pitcher during a full season and save the information in a CSV file.  Data is pulled from http://www.brooksbaseball.net/.  
In order to import pitcher data, you will need to first install the following libraries:
```
pip3 install pandas html5lib lxml
```
Then run
```
python3 pull_data.py "[bbref_game_log_page]" [pitcher_id]
```
* `bbref_game_log_page` should be a URL to a Baseball Reference page containing pitching game log information.  The link for Masahiro Tanaka's 2018 game logs, for example, is https://www.baseball-reference.com/players/gl.fcgi?id=tanakma01&t=p&year=2018.
* `pitcher_id` is a six-digit number which can be used to identify a player.  Each major league player has an identification number, which can be found by looking up that player's profile on mlb.com.  The player's profile page will have the URL format `https://www.mlb.com/player/[first_name]-[last_name]-[ID]`.  Tanaka's profile page, for example, can be found at https://www.mlb.com/player/masahiro-tanaka-547888, meaning his ID number is 547888.
The progam does very little error checking.  In fact, other than checking that two command line arguments are present and that the Baseball reference game log page is not from before 2011 (the site from which the statistics are pulled has data beginning in 2011), no error checking is performed at all.  If the command line arguments are incorrect in some way, behavior is undefined.  If input is correct, the program will pull statistics for every pitch the specified pitcher threw during the year referenced by the Baseball Reference page and save the information in a file called titled `[pitcher_id].csv` in the working directory.


## Run the Program
To run the program, simply execute
```
python3 main.py data/[filename].csv
```
