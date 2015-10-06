import util as u
import re
pattern = re.compile(r'(?P<action>.*): (?P<restofline>.*)')

#Calculate sub message types for the ACCESS line
@u.preprocesses('ACCESS')
def preprocess_access(message):
    m = pattern.match(message.restofline)
    if(m):
        msgtype = m.group('action')
        restofline = m.group('restofline')
        return u.Message(message.msgtype, msgtype, message.time, restofline, message.orig_line)
    return None

@u.handles('ACCESS', r'(?P<name>.*) has the same IP \(-censored\(ip\)-\) as (?P<name2>.*)\.', 'Notice')
def handle_shared_ip(match, message):
    pass

@u.handles('ACCESS', r'(?P<name>.*) has the same IP \(-censored\(ip\)-\) and ID \(.*\) as (?P<name2>.*)\.', 'Notice')
def handle_shared_ip_id(match, message):
    pass

@u.handles('ACCESS', r'(?P<name>.*) from -censored\(ip/cid\)- || (?P<byondver>.*)', 'Login')
def handle_login(match, message):
    pass

@u.handles('ACCESS', r'(?P<name>.*)', 'Logout')
def handle_logout(match, message):
    pass

@u.handles_skipped('ACCESS')
def log_skipped_access(message):
    print('{} was not parsed'.format(message.orig_line))
