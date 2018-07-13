# Homework

I originally was going to just use pure python api/libs to do the group bys.
This would require a hashmap (dict) with keys containing the group by with a list
of each individual spot so that we could do a sum on the series of data then
the CPV calculation. Midway through this I found pandas lib that basically does this
so I went that direction. I haven't used pandas before and I am a bit rusty with my python, but this
homework was a good chance to try something new.


## Layout
* /data - csv files
* / - basic python packaging and installation files
* /homework - main package for doing homework
* /test - basic tests
* /output - two csvs with results



## Setup

This code was developed to use python 3.7+

```bash
dnf install python
python --version

```

```bash
python setup.py install
pip install -r requirements.txt

```

```bash
cd homework
python tatari.py

```


## Assumptions

* Timezone isn't specified, I assumed this does not matter for brevity of homework. IAB usually dictates Eastern as the r
default reporting timezone for analytics. This can vary for foreign entities.

* Spend does not have a value qualifier, I assume this also doesn't matter but this may become an issue later on as I 
currently deal with foreign currencies a lot at the publisher level.

* Assume date time was American format (mm/dd/yyyy), this is also an issue I've dealt with in the past
for foreign clients or data sources

* Views I am assuming are like imps, clicks, conversions etc... in ad tech so they are whole numbers, I typically treat them as longs

* There is overlap in Rotations, assumed that means they should be counted in both for that grouping

* Rotations since they overlap seems like it should be pro-rated in the last CPV by rotation by date. Didn't dive into this.


