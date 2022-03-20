from setuptools import setup, find_packages
 
VERSION = '0.0.3'
DESCRIPTION = "Simple stats for fastapi api"

setup(
    name='fast-api-stats',
    version=VERSION,
    author='Siddhesh Zantye',
    author_email='siddheshadsv@icloud.com',
    url='https://github.com/FusionSid/API-Stats',
    description=DESCRIPTION,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages()
)

# python3 setup.py bdist_wheel
# twine upload dist/*
# sudo rm -rf ./build ./dist ./*egg-info