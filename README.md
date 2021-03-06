# python-nozomi
[![Build Status](https://travis-ci.com/Alfa-Q/python-nozomi.svg?token=NAcpuTjLC6CrUpWrqz9p&branch=master)](https://travis-ci.com/Alfa-Q/python-nozomi)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f3bffdff70794c5cb569645b60699e0b)](https://www.codacy.com?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Alfa-Q/python-nozomi&amp;utm_campaign=Badge_Grade)
[![PyPI version](https://badge.fury.io/py/python-nozomi.svg)](https://badge.fury.io/py/python-nozomi)
[![Python version](https://img.shields.io/badge/python-%203.7%20%7C%203.8-green)](https://www.python.org/downloads/release/python-360/)

nozomi.la (**NSFW**) API in Python.

## Features
-   Retrieving image and video posts
-   Downloading posts

## Installation
```
$ pip install python-nozomi
```

## Example Usage
Retrieve and download all posts containing certain tags
```python
from pathlib import Path
from nozomi import api
    
# The tags that the posts retrieved must contain
positive_tags = ['kimetsu_no_yaiba', 'wallpaper']

# Gets all posts with the tags 'kimetsu_no_yaiba', 'wallpaper'
for post in api.get_posts(positive_tags):
    api.download_media(post, Path.cwd())
```

Retrieve all posts containing certain tags with blacklisted tags
```python
# The blacklisted tags
negative_tags = ['nudity']

# Gets all posts with the tags 'kimetsu_no_yaiba', 'wallpaper' but no 'nudity' tag.
for post in api.get_posts(positive_tags, negative_tags):
    api.download_media(post, Path.cwd())
```
