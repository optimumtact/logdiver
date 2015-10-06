import util as u
import re

@handles('ACCESS')
def login_logout(name,action,time):
    if name == 'Logout' or name == 'Login':
        #ckey + realname actually in the action field
        ckey, realname = u.try_parse_name(action)
        if not ckey or not realname:
            #TODO build error framework
            return
    elif name == 'Notice':
        handle_notice(name, action, time)

    else:
        print('Unknown type {}'.format(name))

def handle_notice(name, action, time):
    action = re.split(r'has the same IP \(-censored\(ip\)-\) as', action)
    if len(action) == 2:
        ckey, realname = u.try_parse_name(action[0])
        print(ckey,realname)
        ckey, realname = u.try_parse_name(action[1])
        print(ckey,realname)
    else:
        return
        #TODO error logging framework
