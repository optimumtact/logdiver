import util as u
import notice
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
    message = u.Message(msgtype, (user, action, time))
    for handler in u.handlers:
            handler(message)


#Basic example handler
#@handles('SAY')
#def dummy(name, action, time):
#    print('SAY: {}, {}, {}'.format(name, action, time))
parse_file()
