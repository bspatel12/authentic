from protean.conf import active_config

from .conf import AuthenticConfig

__version__ = '0.0.1'


# Update the config here so that loading the repo will load the config
active_config.update_defaults(AuthenticConfig)
