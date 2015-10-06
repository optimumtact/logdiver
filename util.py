from collections import namedtuple
handlers = list()

#Datatype class
class Message(namedtuple('Message', 'msgtype data')):
    pass

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

