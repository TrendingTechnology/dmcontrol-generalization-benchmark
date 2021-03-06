from algorithms.sac import SAC
from algorithms.rad import RAD
from algorithms.curl import CURL
from algorithms.pad import PAD
from algorithms.soda import SODA

algorithm = {
	'sac': SAC,
	'rad': RAD,
	'curl': CURL,
	'pad': PAD,
	'soda': SODA
}


def make_agent(obs_shape, action_shape, args):
	return algorithm[args.algorithm](obs_shape, action_shape, args)
