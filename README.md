animelooppy
===========
A simple Python API wrapper for animeloop.org.

## Installing
Clone this repo:
```
git clone https://github.com/Brawl345/animelooppy.git
```

And `cd` into it and install it:
```
python setup.py install
```

Make sure that the [requests](http://docs.python-requests.org/en/master/) library is installed!

## Examples
Get random loops from the Anime [Flip Flappers](https://animeloop.org/series/5926654be2a21602cf277c75):
```python
import animelooppy

results = animelooppy.get_random_loops(seriesid="5926654be2a21602cf277c75")
# "results" now holds a list of all found loops

print(results[0].mp4_1080p)
# https://animeloop.org/files/mp4_1080p/598cb353faa55762ad219584.mp4
```

Get random loops from the Anime [Kinmoza!](https://animeloop.org/series/593470022ddf080af35514d9), episode [07](https://animeloop.org/episode/593494be2ddf080af355157b):
```python
import animelooppy

results = animelooppy.get_random_loops(seriesid="593470022ddf080af35514d9", episodeid="593494be2ddf080af355157b")
# "results" now holds a list of all found loops

print(results[0].mp4_1080p)
# https://animeloop.org/files/mp4_1080p/593494bf2ddf080af3551580.mp4
```

Search series:
````python
import animelooppy

results = animelooppy.search_series("Flip Flappers")
# "results" now holds a list of all found series

print(results[0].title_english)
# 'Flip Flappers'
print(results[0].genres)
# ['Action', 'Adventure', 'Sci-Fi', 'Comedy']

# See series.py for more values
````

Look into `__init__.py` for more functions.

## Notes
* Dates and times are converted to datetime objects for easier access
* Episodes are NOT ordered by number
* Empty genre strings are ignored
* Tags are kinda confusing, better to ignore this feature
* Empty results throw a `LookupError`

### Missing features
* Authentication
* Collections

## Credits
* Thanks to "spaceisstrange" for [itunespy](https://github.com/spaceisstrange/itunespy), gave me a nice starting point!
