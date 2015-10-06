import util as u


@u.handles('SAY', r'(?P<name>.*)/(?P<ckey>.*) :(?P<say>.*)')
def store_say(match, message):
    name = match.group('name')
    ckey = match.group('ckey')
    say = match.group('say')
    #print('{} said {} as {}'.format(ckey, say, name))

@u.handles('SAY', r'(?P<ckey>.*)/(?P<name>.*) has made a (?P<type>station|priority|Centcom|Syndicate) announcement: (?P<announce>.*)')
def store_announce(match, message):
    name = match.group('name')
    ckey = match.group('ckey')
    announce = match.group('announce')
    announcetype = match.group('type')
    #print('{} announced {} as {}'.format(ckey, announce, name))

@u.handles('SAY', r'(?P<ckey>.*)/(?P<name>.*) has requested the nuclear codes from Centcomm')
def store_nuke_request(match, message):
    name = match.group('name')
    ckey = match.group('ckey')
    #print('{} announced {} as {}'.format(ckey, announce, name))

@u.handles_skipped('SAY')
def log_skipped_say(message):
    print('{} was not picked up by prexisting parse function'.format(message.orig_line))
