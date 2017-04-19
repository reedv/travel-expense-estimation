
    We might be able to get away with putting our static files directly in polls/static (rather than creating another
polls subdirectory), but it would actually be a bad idea. Django will choose the first static file it finds whose
name matches, and if you had a static file with the same name in a different application, Django would be unable to
distinguish between them. We need to be able to point Django at the right one, and the easiest way to ensure this is
by namespacing them. That is, by putting those static files inside another directory named for the application itself.

    The {% static %} template tag is not available for use in static files like your stylesheet which aren’t generated
by Django. You should always use relative paths to link your static files between each other, because then you can
change STATIC_URL (used by the static template tag to generate its URLs) without having to modify a bunch of paths
in your static files as well.

    see https://docs.djangoproject.com/en/1.11/howto/static-files/