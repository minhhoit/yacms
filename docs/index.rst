=========
Yacms
=========

Welcome to the Yacms project. To learn more about Yacms please
read the :doc:`overview` which contains a feature list, installation
guide and other general information. To get an idea of the types of
sites possible with Yacms, have a look at the `gallery of sites
powered by Yacms <http://Yacms.jupo.org/sites/>`_.

.. note::
    A working knowledge of `Django <https://www.djangoproject.com/>`_
    is required to work with Yacms and the documentation assumes as
    much. If you're new to Django, you'll need to work through the
    `Django tutorial
    <https://docs.djangoproject.com/en/dev/intro/tutorial01/>`_
    before being able to understand the concepts used throughout the
    Yacms documentation. *A mantra for working with Yacms:
    Yacms Is Just Django* - `Ken Bolton <http://bscientific.org/>`_,
    Yacms core team member.

**Front-end developers** can read about how to set up templates for
specific :doc:`device-handling` such as phones and tablets. Yacms
also comes with the ability for content authors to edit content directly
within a page while viewing it on the website. You can read about this
and how to implement this feature within templates under
:doc:`inline-editing`.

**Back-end developers** can get a better technical overview of how
content is managed and how to customize Yacms in general by
reading about Yacms's :doc:`content-architecture` which describes
the main components and how to extend them with your own custom
content types, or by reading about :doc:`model-customization` for
implementing more low-level customizations as required. There is also
a section on the :doc:`admin-customization` provided by Yacms, as
well as a :doc:`model-graph` depicting the relationships between all
the models.

**System administrators** can find out about some of the production
requirements and operations in the :doc:`deployment` and
:doc:`caching-strategy` sections.

**Further reading** includes :doc:`frequently-asked-questions`,
:doc:`utilities`, a section on :doc:`user-accounts`, support for
:doc:`multi-lingual-sites`, information about Yacms's
:doc:`search-engine`, and a section on Yacms's
:doc:`configuration` which outlines the various settings for
configuring Yacms. Lastly, you can learn about
:doc:`blog-importing` into Yacms, :doc:`twitter-integration`, or
just browse the auto-generated docs for each of Yacms's
:doc:`packages`.

Table Of Contents
=================

.. toctree::
    :maxdepth: 2

    overview
    content-architecture
    model-customization
    admin-customization
    multi-lingual-sites
    utilities
    model-graph
    device-handling
    inline-editing
    caching-strategy
    multi-tenancy
    deployment
    frequently-asked-questions
    user-accounts
    search-engine
    configuration
    blog-importing
    twitter-integration
    packages
    colophon
