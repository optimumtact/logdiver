from collections import namedtuple
import re
handlers = list()
preprocessors = list()
skipped_handlers = list()
#Datatype class
class Message(namedtuple('Message', 'msgtype, time, restofline, orig_line')):
    pass

def handles_skipped(event_id):
        def wrap(func):
            def process(message):
                if not event_id == message.msgtype:
                    return None
                return func(message)

            skipped_handlers.append(process)
            return process
        return wrap

#Function decorator, will add function to preprocessors list
def preprocesses(event_id):
        def wrap(func):
            def process(message):
                if not event_id == message.msgtype:
                    return None
                return func(message)

            preprocessors.append(process)
            return process
        return wrap

#Function decorator, will add function to handlers list
#func decorated will only be called when messagetype = passed in type
def handles(event_id, regex=''):
        def wrap(func):
            if regex:
                pattern = re.compile(regex)
                def process(message):
                    if not event_id == message.msgtype:
                        return False
                    m = pattern.match(message.restofline)
                    if not m:
                        return False
                    func(m, message)
                    return True
            else:
                pattern = None
                def process(message):
                    if not event_id == message.msgtype:
                        return False
                    func(message)
                    return True

            handlers.append(process)
            return process
        return wrap

#Given 4 vars, call all handlers
def handle_action(msgtype, time, restofline, orig_line):
    message = Message(msgtype, time, restofline, orig_line)
    for preprocessor in preprocessors:
        newm = preprocessor(message)
        if newm:
            message = newm

    not_handled = True
    for handler in handlers:
        if handler(message):
            not_handled = False

    if not_handled:
        for handler in skipped_handlers: 
            handler(message)

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

