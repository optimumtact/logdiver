from collections import namedtuple
import re
handlers = list()
preprocessors = list()
skipped_handlers = list()
#Datatype class
class Message(namedtuple('Message', 'msgtype, submsgtype, time, restofline, orig_line')):
    pass

#Function decorator, will add function to the skipped_handlers list
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
def handles(msgtype, regex='', submsgtype=None):
        def wrap(func):
            pattern = re.compile(regex)
            def process(message):
                if not msgtype == message.msgtype:
                    return False

                if not submsgtype == message.submsgtype:
                    return False

                m = None
                if pattern:
                    m = pattern.match(message.restofline)
                    if not m:
                        return False
                        func(m, message)

                else:
                    func(message)

                return True
            handlers.append(process)
            return process
        return wrap

#Given 4 vars, call all handlers
def handle_action(msgtype, time, restofline, orig_line):
    message = Message(msgtype, None, time, restofline, orig_line)
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

