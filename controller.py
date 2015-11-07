import os
from time import sleep
from sys import argv, exit

IDENTITY_FILE = os.path.join(os.getenv('PATH_TO_INSTALLATION_UTILS'), "metropictures")
PI = [
	{
		'homedir' : 'SplendidIsolation',
		'module' : "splendid_isolation",
		'addr' : 200
	},
	{
		'homedir' : 'IsHeCheating',
		'module' : "is_he_cheating",
		'addr' : 204
	},
	{
		'homedir' : 'Skypesnail',
		'module' : "skypesnail",
		'addr' : 202
	},
	{
		'homedir' : 'EnoughIsEnough',
		'module' : "enough_is_enough",
		'addr' : 201
	},
	{
		'homedir' : 'GuiltTripping',
		'module' : "guilt_tripping",
		'addr' : 205
	},
	{
		'homedir' : 'MasoMeetMaso',
		'module' : "maso_meet_maso",
		'addr' : 206
	},
	{
		'homedir' : 'BadDadAndBeyond',
		'module' : "bad_dad_and_beyond",
		'addr' : 207
	},
	{
		'homedir' : 'DawgShaming',
		'module' : "dawg_shaming",
		'addr' : 208
	},
	{
		'homedir' : 'DedMoroz',
		'module' : "ded_moroz",
		'addr' : 209
	}
]

def get_pi_by_name(name):
	for p in PI:
		if p['homedir'].lower() == name:
			return p

	return None

def restart(p):
	return run_cmd("restart", p)

def startup(p):
	return run_cmd("start", p)

def shutdown(p):
	return run_cmd("stop", p)

def run_cmd(cmd, pi=None):
	if pi is None:
		pi = PI
	
	if type(pi) in [str, unicode]:
		pi = [get_pi_by_name(pi)]
		
		if pi is None:
			return False

	for p in pi:
		c = "ssh -f -i %s -o PubkeyAuthentication=yes -o IdentitiesOnly=yes pi@%s.%d 'cd ~/%s && python %s.py --%s'" \
			% (IDENTITY_FILE, os.getenv('METROPICTURES_SUBNET'), p['addr'], p['homedir'], p['module'], cmd)

		os.system(c)
		sleep(3)

	return True

if __name__ == "__main__":
	usage = "python controller.py startup|shutdown|restart [name]"
	
	res = False
	p = None if len(argv) != 3 else argv[2]

	if argv[1] == "startup":
		res = startup(p)
	elif argv[1] == "shutdown":
		res = shutdown(p)
	elif argv[1] == "restart":
		res = restart(p)
	else:
		print usage

	exit(0 if res else -1)