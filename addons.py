#encoding=utf-8
from addon.filter_url import FilterUrl

addons = [
    FilterUrl()
    # ...
]

# mitmdump  -s addons.py "~u xiaohongshu ~s"
# ~q ~s response