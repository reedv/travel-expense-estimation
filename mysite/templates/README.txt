
Templates can live anywhere on your filesystem that Django can access. (Django runs as whatever user your server runs.)
However, keeping your templates within the project is a good convention to follow.

If project grew more sophisticated and required modification of Django’s standard admin templates for some of its
functionality, it would be more sensible to modify the application’s templates, rather than those in the project.
That way, you could include the polls application in any new project and be assured that it would find the custom
templates it needed.