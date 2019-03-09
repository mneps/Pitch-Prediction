import csv
import os
from math import floor
import sys

from random import shuffle

def main(filepath, split_percent):

    games = []

    with open(filepath, 'rt') as csvfile:
        filereader = csv.DictReader(csvfile)

        rows = []

        for row in filereader:
            rows.append(row)

        games = []

        game = []

        for i in range(len(rows)-1):
            row = rows[i]
            next_row = rows[i+1]

            game.append(row)

            if row['dateStamp'] != next_row['dateStamp']:
                games.append(game)
                game = []



        # now we have all the games split up

        shuffle(games)


        split_index = floor(split_percent * len(games))

        print(len(games))
        print(split_index)

        train_games = [item for sublist in games[:split_index] for item in sublist]

        test_games = [item for sublist in games[split_index:] for item in sublist]

        
        with open('train_'+filepath, 'w') as csvfile:
            fieldnames = list(train_games[0].keys())
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for row in train_games:
                writer.writerow(row)

        with open('test_'+filepath, 'w') as csvfile:
            fieldnames = list(test_games[0].keys())
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for row in test_games:
                writer.writerow(row)        





if __name__ == '__main__':
    assert(len(sys.argv) == 3)
    assert(os.path.isfile(sys.argv[1]))
    assert(os.path.splitext(sys.argv[1])[1] == ".csv")
    main(sys.argv[1], float(sys.argv[2]))