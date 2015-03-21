Spino
========

Spino is a python library allows to spin text using a bracket syntax. For example if we have the text:

::

    Kevin Bacon is {awesome|epic|a great actor}. He worked in an amazing number of {movies like {Apollo 13|Sleepers|Footlose}|tv series like {The following|Robot Chicken|Bored to Death}}.


Now if you put spino to work, you can have an output like:

::

    >> spino_spin -p mytext.txt -n 3
    Kevin Bacon is a great actor. He worked in an amazing number of tv series like     Robot Chicken.
    Kevin Bacon is awesome. He worked in an amazing number of movies like Footlose.
    Kevin Bacon is epic. He worked in an amazing number of tv series like Robot Chicken.


Installation
------------

Just install spino via github
::

    pip install -e git+https://github.com/carrerasrodrigo/spino.git#egg=spino

Spino will install a global command called spino_spin that will allow you to
spin the texts that you need.

spino_spin have 2 parameters
::

    spino_spin -p file_to_spin -n number_of_spins
    -n = number of spins
    -p = the path of the file that we want to spin


Spino from your python script?
------------------------------

If you need to use it in your python script you only have to import it
::

    from spino import spin_text
    spin_text('{hello|hola|oi}')


Tested
------

Spino was tested on python2.7+ and python3.4+
