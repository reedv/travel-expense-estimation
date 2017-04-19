
Now we might be able to get away with putting our templates directly in polls/templates
(rather than creating another polls subdirectory), but it would actually be a bad idea.
Django will choose the first template it finds whose name matches, and if you had a template
with the same name in a different application, Django would be unable to distinguish between them.