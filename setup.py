from setuptools import setup, find_packages


setup(
    name='spino',
    version='0.0',
    url='https://github.com/carrerasrodrigo/spino',
    license='mit',
    author='Rodrigo N. Carreras',
    author_email='carrerasrodrigo@gmail.com',
    description='Text spiner library for python',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    classifiers=[],
    entry_points={
        'console_scripts': [
            'spino_spin=spino.spin:main',
            ],
        },
)
