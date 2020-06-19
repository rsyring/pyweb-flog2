import pathlib
import os
from unittest import mock

import flog.app
from flog.libs import config

data_dpath = pathlib.Path(__file__).parent / 'data'


class TestConfig:
    def test_app_config_files(self, app):
        with mock.patch.dict(os.environ, {'HOME': '~'}):
            fpaths = config.app_config_fpaths(app)
            assert fpaths == [
                '/etc/flog/config.py',
                '~/.config/flog/config.py',
                str(app.root_path.parent.resolve() / 'flog-config.py')
            ]

    def test_load_fpath_config(self, app):
        config_fpath = data_dpath / 'config.py'
        assert config.load_fpath_config(app, {}, config_fpath, 'foo') == {
            'default': 1,
            'foo': 2,
        }

    def test_load_config_fpaths(self, app):
        fpaths = [data_dpath / 'config.py', data_dpath / 'config2.py', '/not/there']
        result = config.load_fpath_configs(app, {}, fpaths, 'foo')
        assert result == {
            'default': 3,
            'foo': 2,
            'foo2': 4,
        }

    def test_environ_config(self):
        with mock.patch.dict(os.environ, {'FOO_BAR': 'baz'}):
            assert config.environ_config('foo') == {
                'BAR': 'baz'
            }

    def test_config_applied(self):
        with mock.patch.dict(config.os.environ, {'FLOG_BAR': 'baz'}):
            app = flog.app.FlogApp.create(testing=True)
            assert app.config['BAR'] == 'baz'
