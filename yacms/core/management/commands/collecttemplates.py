from __future__ import unicode_literals
from future.builtins import int
from future.builtins import input

import os
import shutil

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from yacms.utils.importing import path_for_import


class Command(BaseCommand):
    """
    Copies templates from app templates directories, into the
    project's templates directory. Specify 1 or more app names
    listed in INSTALLED_APPS to copy only the templates for those
    apps. Specifying no apps will copy templates for all apps.
    """

    can_import_settings = True

    def add_arguments(self, parser):
        parser.add_argument(
            '--noinput', action='store_false', dest='interactive',
            help="Do NOT prompt for input of any kind. "
                 "Existing templates will be overwritten.")
        parser.add_argument(
            '-t', '--template', dest='template',
            help="The template name and relative path of a single template "
                 "to copy, eg: blog/blog_post_list.html")
        parser.add_argument(
            '-a', '--admin', action='store_true', dest='admin',
            help="Include admin templates.")

    usage = lambda foo, bar: ("usage: %prog [appname1] [appname2] [options] "
                              "\n" + Command.__doc__.rstrip())

    def handle(self, *apps, **options):

        admin = options.get("admin")
        single_template = options.get("template")
        verbosity = int(options.get('verbosity', 1))
        to_dir = settings.TEMPLATES[0]["DIRS"][0]
        templates = []

        # Build a list of apps to copy templates from.
        if apps:
            # Ensure specified apps are installed.
            not_installed = set(apps) - set(settings.INSTALLED_APPS)
            if not_installed:
                raise CommandError("Apps are not in INSTALLED_APPS: " +
                                    ", ".join(not_installed))
        else:
            # No apps specified - default to all in yacms/Cartridge.
            apps = [a for a in settings.INSTALLED_APPS
                    if a.split(".")[0] in ("yacms", "cartridge")]

        # Build a list of name/path pairs of all templates to copy.
        for app in apps:
            from_dir = os.path.join(path_for_import(app), "templates")
            if os.path.exists(from_dir):
                for (dirpath, dirnames, filenames) in os.walk(from_dir):
                    for f in filenames:
                        path = os.path.join(dirpath, f)
                        name = path[len(from_dir) + 1:]
                        # Bail if template isn't single template requested,
                        # or an admin template without the admin option
                        # specified.
                        if single_template and name != single_template:
                            continue
                        if not admin and name.startswith("admin" + os.sep):
                            continue
                        templates.append((name, path, app))

        # Copy templates.
        count = 0
        template_src = {}
        for name, path, app in templates:
            dest = os.path.join(to_dir, name)
            # Prompt user to overwrite template if interactive and
            # template exists.
            if verbosity >= 2:
                self.stdout.write("\nCopying: %s"
                                  "\nFrom:    %s"
                                  "\nTo:      %s"
                                  "\n" % (name, path, dest))
            copy = True
            if options.get("interactive") and os.path.exists(dest):
                if name in template_src:
                    prev = ' [copied from %s]' % template_src[name]
                else:
                    prev = ''
                self.stdout.write("While copying %s [from %s]:\n" %
                                  (name, app))
                self.stdout.write("Template exists%s.\n" % prev)
                confirm = input("Overwrite?  (yes/no/abort): ")
                while confirm not in ("yes", "no", "abort"):
                    confirm = input(
                        "Please enter either 'yes', 'no' or 'abort': ")
                if confirm == "abort":
                    self.stdout.write("Aborted\n")
                    break  # exit templates copying loop
                elif confirm == "no":
                    self.stdout.write("[Skipped]\n")
                    copy = False
            if copy:
                try:
                    os.makedirs(os.path.dirname(dest))
                except OSError:
                    pass
                shutil.copy2(path, dest)
                template_src[name] = app
                count += 1
        if verbosity >= 1:
            s = "s" if count != 1 else ""
            self.stdout.write("\nCopied %s template%s\n" % (count, s))
