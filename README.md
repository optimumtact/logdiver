This is an attempt at making a log parser and viewer for the tgstation 13 byond game logs, I've pulled ideas out of an earlier IRC bot to provide a really simple and clean way to handle the parsing of each type of line

##Flow of execution
parse_log.py reads each line in and dispatches it based on the lines MSGTYPE, first to the any defined preprocessors, then to the rest of the line handlers for that MSGTYPE

###Line handlers
A line handler can one of two types

Preprocessor - these are denoted with the @preprocessor(MSGTYPE) decorator and should return None or a new instance of the Message class, they're used to take a given MSGTYPE and break it down further as needed - an example of this is in the access.py, it has a preprocessor that takes in ACCESS log lines and breaks them into Login/Logout and Notice lines

Handler - these are denoted with the @handles(MSGTYPE, REGEX_PATTERN) decorator, and do not need to return anything. They're used to actually pull data from a given line and do something with, for example there is a handle_notice function in the access.py file that handles Notice msgtypes and looks for those telling you when a user logs in with the same ip as another user

Skipped message - these are denoted with the @handles_skipped(MSGTYPE) decorator, they should be used to print/log/store or otherwise work with messages that were not found to be handled by any of the handler functions (useful when looking for lines that are not being parsed)

###Message class
The message class is just a simple named tuple for moving the data around between the handler functions

It has four attributes

msgtype = msgtype code

time = time message receieved

restofline = rest of the line being parsed

orig_line = full original line

Good pratice is for your preprocessor method to ALWAYS maintain the originaline attribute from the previous message when producing a new version of the Message object to be consumed. End users are expected to use this to quickly print/eyeball the original full line that was being parsed

i.e

    return Message(newtype, orig_message.time, newrestofline, orig_message.orig_line)


##End goal
The end goal is for methods to do basic preprocessing and then throw the file into a sqlite3 db, SCHEMA to be decided at this stage

That means any number of users can write their own frontend backing onto the sqlite3 db and just use appropriate SQL to generate the lookups of interest

Logic for the handling of events lives in util.py, with the handles/preprocesses decorators, so check this out for a understanding of how that logic works - the key point is that the driving parse_file file calls u.handle_action and passes it the appropriate info

##util functions from util.py 
try_parse_name  takes string in form ckey/(name) and pulls out ckey and name

returns None, None if it couldn't parse the string

    ckey, name = try_parse_name(string)

