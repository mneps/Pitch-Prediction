
import html5lib
import pandas as pd
import urllib.parse as urlparse
import sys
from calendar import month_abbr
from pandas import read_html


def handle_date(date, abbr_to_num):
    url = ""

    date = date.split("\xa0")
    month = abbr_to_num[date[0]]
    if month < 10:
        url += "0"
    url += str(month) + "_"
    if len(date[1]) == 1:
        url += "0"
    url += date[1] + "_"

    return url


# BbRef and BB (unfortunately) use different abbreviations for some teams
def create_dict():
    team_abbr = dict()
    team_abbr["NYY"] = "nya"
    team_abbr["TBR"] = "tba"
    team_abbr["CHW"] = "cha"
    team_abbr["KCR"] = "kca"
    team_abbr["LAA"] = "ana"
    team_abbr["FLA"] = "flo"
    team_abbr["WSN"] = "wsh"
    team_abbr["NYM"] = "nyn"
    team_abbr["STL"] = "sln"
    team_abbr["CHC"] = "chn"
    team_abbr["SDP"] = "sdn"
    team_abbr["SFG"] = "sfn"
    team_abbr["LAD"] = "lan"

    return team_abbr


def check_abbr(team, team_abbr, url):
    if team not in team_abbr:
        url += (team.lower() + "mlb_")
    else:
        url += (team_abbr[team] + "mlb_")

    return url

def handle_teams(away, home, team_abbr):
    url = check_abbr(away, team_abbr, "")
    return check_abbr(home, team_abbr, url)


def create_csv_file(urls, pitcher_id, year):
    filename = pitcher_id + "-" + year + ".csv"

    for i in range(len(urls)):
        single_game = pd.io.html.read_html(urls[i])[0]
        with open(filename, 'a') as f:
            if i == 0:
                single_game.to_csv(f, index=False)
            else:                
                single_game.to_csv(f, index=False, header=False)


def main(bbref_url, pitcher_id):
    game_log = pd.io.html.read_html(bbref_url)[0]
    game_log.rename(columns={'Unnamed: 5':'H_A'}, inplace=True)

    url_base = "http://www.brooksbaseball.net/pfxVB/tabdel_expanded.php?pitchSel=" + \
        str(pitcher_id) + "&game=gid_"
    abbr_to_num = {name: num for num, name in enumerate(month_abbr) if num}
    team_abbr = create_dict()


    urls = []
    for i in range(game_log.shape[0]):
        # BbRef has a title row for each month that we want to avoid looking at
        try:
            int(game_log.Rk[i])
        except:
            continue

        queries = urlparse.parse_qs((urlparse.urlparse(bbref_url)).query)
        if 'year' in queries:
            assert(int(queries['year'][0]) > 2010)
            year = str(queries['year'][0])
        else:
            year = str(game_log.Year[i])
        url = url_base + year + "_"

        url += handle_date(game_log.Date[i], abbr_to_num)
        if game_log.H_A[i] == "@":
            url += handle_teams(game_log.Tm[i], game_log.Opp[i], team_abbr)
        else:
            url += handle_teams(game_log.Opp[i], game_log.Tm[i], team_abbr)
        url += "1%2F&s_type=&h_size=700&v_size=500"

        urls.append(url)


    create_csv_file(urls, pitcher_id, year)




if __name__ == '__main__':
    assert (len(sys.argv) == 3)
    main(sys.argv[1], sys.argv[2])

