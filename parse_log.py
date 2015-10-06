import util as u
import access
import say
#Parse file, TODO: add file as arg
def parse_file():
    with open('05-Monday.txt') as f:
        for line in f:
            originalline = line
            line = line.strip('\r\n')#remove line ending info
            endtime = line.find(']')
            if endtime > 0:
                time = line[:endtime]#Get time info
                line = line[endtime+1:]#Get rest of line
                time = time.strip('][')#strip remaining [ or ]
            else:
                time = 'null'

            line = line.split(':', 1)
            length = len(line)
            if length == 2:
                msgtype = line[0].strip(' ')
                restofline = line[1].strip(' ')
            else:
                msgtype = 'UNKNOWN'
                restofline = ':'.join(line)
            u.handle_action(msgtype, time, restofline, originalline)



#Basic example handler
#@handles('SAY')
#def dummy(msgtype, time, restofline):
#    print('SAY: {}'.format(time, restofline))

parse_file()
