import pathlib
import os
import os.path as osp

import appdirs


def init_config(app):
    app.config.update(build_config(app))


def build_config(app):
    config = default_config(app)

    config = load_fpath_configs(app, config, app_config_fpaths(app), app.env)
    config.update(environ_config(app.name))

    return config


def load_fpath_configs(app, config, fpaths, config_prefix):
    for fpath in map(pathlib.Path, fpaths):
        if not fpath.exists():
            continue
        config = load_fpath_config(app, config, fpath, config_prefix)

    return config


def load_fpath_config(app, config, fpath, config_prefix):
    pymod_vars = {}
    exec(fpath.read_bytes(), pymod_vars)

    # TODO: not sure we need 'default'?  config files could call common function to assign defaults
    # Unless all the defaults get ran first, then the environ configs
    config = call_env_config(app, config, pymod_vars, 'default')
    config = call_env_config(app, config, pymod_vars, config_prefix)

    return config


def call_env_config(app, config, pymod_vars, config_prefix):
    callable_name = f'{config_prefix}_config'
    if callable_name in pymod_vars:
        return pymod_vars[callable_name](app, config)

    return config


def app_config_fpaths(app):
    return [
        # todo: should work on Windows too
        f'/etc/{app.name}/config.py',
        osp.join(appdirs.user_config_dir(app.name), 'config.py'),
        osp.join(app.root_path.parent.resolve(), f'{app.name}-config.py'),
    ]


def default_config(app):
    return {
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    }


def environ_config(prefix):
    retval = {}
    app_prefix = f'{prefix.upper()}_'
    for key, val in os.environ.items():
        if key.startswith(app_prefix):
            config_key = key.replace(app_prefix, '', 1)
            retval[config_key] = val

    return retval
