from collections import namedtuple
import re
handlers = list()


#Datatype class
class Message(namedtuple('Message', 'msgtype data')):
    pass

#Parse file, TODO: add file as arg
def parse_file():
    with open('05-Monday.txt') as f:
        for line in f:
            line = line.strip('\r\n')#remove line ending info
            endtime = line.find(']')
            if endtime > 0:
                time = line[:endtime]#Get time info
                line = line[endtime+1:]#Get rest of line
                time = time.strip('][')#strip remaining [ or ]
            else:
                time = 'null'

            line = line.split(':', 2)
            length = len(line)
            if length == 2:
                msgtype = line[0].strip(' ')
                action = line[1].strip(' ')
                user = ''
                handle_action(msgtype, user, action, time)
            elif length == 3:
                msgtype = line[0].strip(' ')
                user = line[1].strip(' ')
                action = line[2].strip(' ')
                handle_action(msgtype, user, action, time)
            else:
                msgtype = 'UNKNOWN'
                user = ''
                action = ':'.join(line)
                handle_action(msgtype, user, action, time)


#Given 4 vars, call all handlers
def handle_action(msgtype, user, action, time):
    message = Message(msgtype, (user, action, time))
    for handler in handlers:
            handler(message)

#Function decorator, will add function to handlers list
#func decorated will only be called when messagetype = passed in type
def handles(event_id):
        def wrap(func):
            def process(message):
                if not event_id == message.msgtype:
                    return False
                func(*message.data)
                return True
            handlers.append(process)
            return process
        return wrap

#Basic example handler
#@handles('SAY')
#def dummy(name, action, time):
#    print('SAY: {}, {}, {}'.format(name, action, time))

def reconstruct_line(msgtype, name, action, time):
    return '[{}]{}: {}: {}'.format(time, msgtype, name, action)

def try_parse_name(name):
    #strip out ip/ckey censoring
    name = re.sub(r'-censored.*-', '', name)
    name = name.split('/')
    if len(name) == 2:
        ckey = name[0]
        name = name[1]
        return ckey, name
    else:
        return None, None

@handles('ACCESS')
def login_logout(name,action,time):
    if name == 'Logout' or name == 'Login':
        #ckey + realname actually in the action field
        ckey, realname = try_parse_name(action)
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
        print(action)
        ckey, realname = try_parse_name(action[0])
        print(ckey,realname)
        ckey, realname = try_parse_name(action[1])
        print(ckey,realname)
    else:
        return
        #TODO error logging framework

parse_file()
