from pypcalc import __main__


def test_smoke():
    __main__.main(['10.0.0.0/8'])
    __main__.main(['--color=always', '10.0.0.0/8'])
    __main__.main(['--color=always', '::1'])
    __main__.main(['--color=always', '::1/120'])
