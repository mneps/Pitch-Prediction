
import csv
import os

# Loads the csv files into a single two-dimensional list.  Each of the inner
# lists represents a single at-bat with the elements within those lists
# being the name of the pitch that was thrown.  For example, if there are two
# at-bats and the first one was three pitches (fastball, fastball, slider) and
# the second at bat was a single pitch (curveball) the resulting list will be
# [["FB", "FB", "SL"], ["CB"]]
def get_data(filepath):
	at_bats = []

	with open(filepath, 'rt') as csvfile:
		# next(csvfile) # skip header line
		filereader = csv.DictReader(csvfile)

		at_bat = []
		tot=0
		for row in filereader:
			at_bat += [row["mlbam_pitch_name"]]
			if row["ab_total"] == row["ab_count"]:
				at_bats += [at_bat]
				tot+=len(at_bat)
				at_bat = []

		print (at_bats, len(at_bats), tot)

	return at_bats



