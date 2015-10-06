import util as u

@u.handles('GAME', '(?P<name>.*) has primed a (?P<grenade_type>.*) for detonation at (?P<location>.*)')
def log_grenade_prime(match, message):
    pass

@u.handles('GAME', 'PA Control Computer (?P<change>increased|decreased) to (?P<output_power>\d) by (?P<name>.*) in (?P<location>.*)')
def log_pa_power_change(match, message):
    pass

@u.handles('GAME', 'PA Control Computer turned (?P<change>OFF|ON) by (?P<name>.*) in (?P<location>.*)')
def log_pa_power_switch(match, message):
    pass

@u.handles('GAME', 'Explosion with size \((?P<size>.*)\) in area (?P<area_name>.*) \((?P<location>.*)\)')
def log_explosion(match, message):
    pass

@u.handles('GAME', 'Antagonists at round end were...')
def skip_antag_line(match, message):
    pass

@u.handles('GAME', r'(?P<name>.*) has triggered a (?P<explosive_type>.*) at (?P<area_name>.*) \((?P<location>.*)\)')
def triggered_explosion(match, messsage):
    pass

@u.handles('GAME', r'(?P<name>.*) triggered a fueltank explosion.')
def triggered_fueltank_explosion(match, messsage):
    pass

@u.handles('GAME', r'(?P<relic_name>.*) relic used by (?P<name>.*) in \((?P<location>.*)\)')
def relic_used(match, message):
    pass

@u.handles('GAME', r'Random Event triggering: (?P<name>.*) \((?P<eventpath>.*)\)')
def random_event_triggered(match, message):
    pass

@u.handles('GAME', r'(?P<name>.*) has been selected as a (?P<antagtype>)')
def antag_selected(match, message):
    pass

@u.handles_skipped('GAME')
def log_skipped_game(message):
    print('{} was not parsed'.format(message.orig_line))
