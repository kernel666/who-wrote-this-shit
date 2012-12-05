# Who Wrote This Shit

Simple demonstration forensic linguistics program analysing a document based on linguistic style to attribute the authorship to anonymous or disputed documents.

**Note**: This program is considered primitive and might be rewritten later.

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


### Training

	$ python wwts.py --file examples/d99/article.txt --train --tag '@d99'
	$ python wwts.py --file examples/bc/article.txt --train --tag '@bennychandra'

### Guessing

	$ python wwts.py --file examples/unknown/article.txt --guess
	[('@d99', 0.7474532128163579), ('@bennychandra', 0.6844689616042425)]
	$ python wwts.py --file examples/unknown/article2.txt --guess
	[('@bennychandra', 0.8276354287373211), ('@d99', 0.4619067492669147)]

## Similar approaches:

* Dave Aitel's [Umask](http://www.immunitysec.com/downloads/unmask1.0.tar.gz), released in 2002. 
* [The Signature Stylometric System](http://www.philocomp.net/?pageref=humanities&page=signature)
* [JGAAP](http://evllabs.com/jgaap/w/index.php/Main_Page) (Java Graphical Authorship Attribution Program)

## Further reading

* [Stylometry](http://en.wikipedia.org/wiki/Stylometry)
* [Writeprint](http://en.wikipedia.org/wiki/Writeprint)

