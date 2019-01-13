from setuptools import setup, find_packages
try: # for pip >= 10
        from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
        from pip.req import parse_requirements

setup(
    name = 'signature_extraction',
    version = '1.0.0',
    url = 'https://github.com/harmening/signature_extraction.git',
    packages = find_packages(),    
    install_reqs = parse_requirements('requirements.txt', session='hack')
)
