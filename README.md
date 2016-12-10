.. image:: https://secure.travis-ci.org/minhhoit/yacms.png?branch=master
   :target: http://travis-ci.org/minhhoit/yacms

Created by `Andrew <http://twitter.com/minhhoit>`_

========
Overview
========

YaCms is a powerful, consistent, and flexible content management
platform. Built using the `Django`_ framework, YaCms provides a
simple yet highly extensible architecture that encourages diving in
and hacking on the code. YaCms is `BSD licensed`_ and supported by
a diverse and active community.

In some ways, YaCms resembles tools such as `Wordpress`_,
providing an intuitive interface for managing pages, blog posts, form
data, store products, and other types of content. But YaCms is
also different. Unlike many other platforms that make extensive use of
modules or reusable applications, YaCms provides most of its
functionality by default. This approach yields a more integrated and
efficient platform.

Visit the `YaCms project page`_ to see some of the `great sites
people have built using YaCms`_.

Features
========

In addition to the usual features provided by Django such as MVC
architecture, ORM, templating, caching and an automatic admin
interface, YaCms provides the following:

* Hierarchical page navigation
* Save as draft and preview on site
* Scheduled publishing
* Drag-and-drop page ordering
* WYSIWYG editing
* `In-line page editing`_
* Drag-and-drop HTML5 forms builder with CSV export
* SEO friendly URLs and meta data
* Ecommerce / Shopping cart module (`Cartridge`_)
* Configurable `dashboard`_ widgets
* Blog engine
* Tagging
* `Free Themes`_, and a `Premium Themes`_ Marketplace
* User accounts and profiles with email verification
* Translated to over 35 languages
* Sharing via Facebook or Twitter
* `Multi-lingual sites`_
* `Custom templates`_ per page or blog post
* `Twitter Bootstrap`_ integration
* API for `custom content types`_
* `Search engine and API`_
* Seamless integration with third-party Django apps
* Multi-device detection and template handling
* One step migration from other blogging engines
* Automated production provisioning and deployments
* `Disqus`_ integration, or built-in threaded comments
* `Gravatar`_ integration
* `Google Analytics`_ integration
* `Twitter`_ feed integration
* `bit.ly`_ integration
* `Akismet`_ spam filtering
* Built-in `test suite`_
* `JVM`_ compatible (via `Jython`_)

The YaCms admin dashboard:

.. image:: http://yacms.vn/docs/_images/dashboard.png


Support
=======

To **report a security issue**, please send an email privately to
`core-team@yacms.vn`_. This gives us a chance to fix the issue
and create an official release prior to the issue being made public.

For **all other YaCms support**, the primary channel is the
`YaCms-users`_ mailing list. Questions, comments, issues, feature
requests, and all other related discussions should take place here.

If you're **certain** you've come across a bug, then please use the
`GitHub issue tracker`_, however it's crucial that enough information
is provided to reproduce the bug, ideally with a small code sample repo
we can simply fork, run, and see the issue with. Other useful
information includes things such as the Python stack trace generated by
error pages, as well as other aspects of the development environment
used, such as operating system, database, and Python version. If
**you're not sure you've found a reproducible bug**, then please try
the mailing list first.

Finally, feel free to drop by the `#YaCms IRC channel`_ on
`Freenode`_, for a chat! Lastly, communications in all YaCms spaces
are expected to conform to the `Django Code of Conduct`_.


Contributing
============

YaCms is an open source project managed using both the Git and
Mercurial version control systems. These repositories are hosted on
both `GitHub`_ and `Bitbucket`_ respectively, so contributing is as
easy as forking the project on either of these sites and committing
back your enhancements.

Please note the following guidelines for contributing:

* If you're fairly confident you've identified a bug or have already written a
  patch, feel free to open an issue or pull request. Otherwise, please discuss
  on the `YaCms-users`_ mailing list first.
* Contributed code must be written in the existing style. For Python
  (and to a decent extent, JavaScript as well), this is as simple as
  following the `Django coding style`_ and (most importantly)
  `PEP 8`_. Front-end CSS should adhere to the
  `Bootstrap CSS guidelines`_.
* Contributions must be available on a separately named branch
  based on the latest version of the main branch.
* Run the tests before committing your changes. If your changes
  cause the tests to break, they won't be accepted.
* If you are adding new functionality, you must include basic tests
  and documentation.


Donating
========

If you would like to make a donation to continue development of
YaCms, you can do so via the `YaCms Project`_ website.


Quotes
======