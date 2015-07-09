from setuptools import setup, find_packages
setup(
    name='gwlib-strap',
    version='0.2.0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    package_data={
        'gwlib-strap': ['gwlib-resources/img/*.png', '/gwlib-resources/img/*.gif', 'gwlib-resources/css/*.css'],
        },
    author='gwlibraries')
