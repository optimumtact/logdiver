This is an attempt at making a log parser and viewer for the tgstation 13 byond game logs, I've pulled ideas out of an earlier IRC bot to provide a really simple and clean way to handle the parsing of each line and msgtype (I Hope)

Structure - parse_log reads each line in and despatches it to the appropriate handler - these live in their own files i.e say parsing in say.py, and are included in the parser by simply importing the file (logic for how this is done lives in a decorator in util.py)

The idea is to maintain for each ACTION type a list of regexes and a method to call if that regex matches, so call chain is

parse_log reads line

despatch to appropriate handler based on msgtype

handler calls method if it finds a regex that matches the line

method does work

note that this isn't implented yet as the current notice.py is a quick and dirty test case to validate concepts

The end goal is for methods to do basic preprocessing and then throw the file into a sqlite3 db, SCHEMA to be decided at this stage

That means any number of users can write their own frontend backing onto the sqlite3 db and just use appropriate SQL to generate the lookups of interest


The hardest thing here will be nailing the correct sql scheme for the sqlite table - I'm still thinking about this right now
