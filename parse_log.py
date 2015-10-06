from collections import namedtuple
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
                msgtype = line[0]
                action = line[1]
                user = ''
                handle_action(msgtype, user, action, time)
            elif length == 3:
                msgtype = line[0]
                user = line[1]
                action = line[2]
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
        try:
            handler(message)
        except Exception as e:
            log.exception("Error in log parser plugin:{0}".format(plugin.name))

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
@handles('SAY')
def dummy(name, action, time):
    print('SAY: {}, {}, {}'.format(name, action, time))

parse_file()
