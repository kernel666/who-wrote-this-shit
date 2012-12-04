# Who Wrote This Shit

Simple demonstration program to find out who wrote something.


## Usage

	$ python wwts.py -h
	usage: wwts.py [-h] -F FILE [-T TAG] [-t] [-g]

	Who wrote this shit?

	optional arguments:
	  -h, --help            show this help message and exit
	  -F FILE, --file FILE  Input file
	  -T TAG, --tag TAG     Tag, e.g. 'Thaddeus T. Grugq' or '@thegrugq'
	  -t, --train           Training mode
	  -g, --guess           Guessing mode


## Training

	$ python wwts.py --file examples/d99/tweet.txt --train --tag '@d99'
	$ python wwts.py --file examples/bc/tweet.txt --train --tag '@bennychandra'
	$ python wwts.py --file examples/gq/tweet.txt --train --tag '@thegrugq'

## Guessing

	$ python wwts.py --file examples/unknown/test.txt --guess
	[('@bennychandra', 0.8954002478493908), ('@thegrugq', 0.7109256426967558)]

