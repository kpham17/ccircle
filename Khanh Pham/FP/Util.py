import ccircle
cache_image = {}
def image(name):
    global cache_images
    x = cache_image.get(name, None)
    if x:
        return x
    x = ccircle.Image('%s' % name)
    cache_image[name] = x
    return x
