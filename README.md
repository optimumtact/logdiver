This is an attempt at making a log parser and viewer for the tgstation 13 byond game logs, I've pulled ideas out of an earlier IRC bot to provide a really simple and clean way to handle the parsing of each line and msgtype (I Hope)

TODO: add parsers for each type of action, try to pull out useful information like ckey/name

TODO: generalise to allow you to feed it any type of lines

TODO: idea is to slurp logs into a sqlite db, for the actual search/displaying of results, as then all we do is write sql, + SQLITe has fulltext search for keyword searching

TODO:Fields of interest, action, time, date, ckey, name


TODO: attack logs???
