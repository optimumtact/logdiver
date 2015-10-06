import util as u
import re
pattern = re.compile(r'(?P<action>.*): (?P<restofline>.*)')

@u.preprocesses('ACCESS')
def preprocess_access(message):
    m = pattern.match(message.restofline)
    if(m):
        msgtype = m.group('action')
        restofline = m.group('restofline')
        return u.Message(msgtype, message.time, restofline, message.orig_line)
    return None

@u.handles('Notice', r'(?P<name>.*) has the same IP \(-censored\(ip\)-\) as (?P<name2>.*)\.')
def handle_notice(match, message):
    name1 = match.group('name')
    name2 = match.group('name2')
    print(name1, name2, message.originaline)
