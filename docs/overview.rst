.. include:: ../README.rst


Installation
============

The easiest method is to install directly from pypi using `pip`_ by
running the command below, which will also install the required
dependencies mentioned above::

    $ pip install Yacms

If you prefer, you can download Yacms and install it directly from
source::

    $ python setup.py install

Once installed, the command ``Yacms-project`` can be used to
create a new Yacms project in similar fashion to
``django-admin.py``::

    $ Yacms-project project_name
    $ cd project_name
    $ python manage.py createdb --noinput
    $ python manage.py runserver

.. note::

    The ``createdb`` command is a shortcut for using Django's
    ``migrate`` command, which will also install some demo content,
    such as a contact form, image gallery, and more. If you'd like to
    omit this step, use the ``--nodata`` option with ``createdb``.

You should then be able to browse to http://127.0.0.1:8000/admin/ and
log in using the default account (``username: admin, password:
default``). If you'd like to specify a different username and password
during set up, simply exclude the ``--noinput`` option included above
when running ``createdb``.

For information on how to add Yacms to an existing Django project,
see the FAQ section of the documentation.

Yacms makes use of as few libraries as possible (apart from a
standard Django environment), with the following dependencies, which
unless noted as optional, should be installed automatically following
the above instructions:

* `Python`_ 2.7 to 3.5
* `Django`_ 1.8 to 1.9
* `django-contrib-comments`_ - for built-in threaded comments
* `Pillow`_ - for image resizing (`Python Imaging Library`_ fork)
* `grappelli-safe`_ - admin skin (`Grappelli`_ fork)
* `filebrowser-safe`_ - for managing file uploads (`FileBrowser`_ fork)
* `bleach`_ and `BeautifulSoup`_ - for sanitizing markup in content
* `pytz`_ and `tzlocal`_ - for timezone support
* `chardet`_ - for supporting arbitrary encoding in file uploads
* `django-modeltranslation`_ - for multi-lingual content (optional)
* `django-compressor`_ - for merging JS/CSS assets (optional)
* `requests`_ and `requests_oauthlib`_ - for interacting with external APIs
* `pyflakes`_ and `pep8`_ - for running the test suite (optional)

Users on Debian or Ubuntu will require some system packages to support
the imaging library::

    $ apt-get install libjpeg8 libjpeg8-dev
    $ apt-get build-dep python-imaging

OSX users can do the same via `Homebrew`_::

    $ brew install libjpeg


Themes
======

A handful of attractive `Free Themes`_ are available thanks to
`@abhinavsohani`_, while there is also a marketplace for buying and
selling `Premium Themes`_ thanks to `@joshcartme`_.


Browser Support
===============

Yacms's admin interface works with all modern browsers.
Internet Explorer 7 and earlier are generally unsupported.


Third-Party Plug-Ins
====================

The following plug-ins have been developed outside of Yacms. If you
have developed a plug-in to integrate with Yacms and would like to
list it here, send an email to the `Yacms-users`_ mailing list, or
better yet, fork the project and create a pull request with your
plug-in added to the list below. We also ask that you add it to the
`Yacms Grid on djangopackages.com`_.

* `Cartridge`_ - ecommerce for Yacms.
* `Drum`_ - A `Hacker News`_ / `Reddit`_ clone powered by Yacms.
* `Yacms-html5boilerplate`_ - Integrates the
  `html5boilerplate project`_  into Yacms.
* `Yacms-mdown`_ - Adds `Markdown`_ support to Yacms's rich
  text editor.
* `Yacms-openshift`_ - Setup for running Yacms on
  `Redhat's OpenShift`_ cloud platform.
* `Yacms-stackato`_ - Setup for running Yacms on
  `ActiveState's Stackato`_ cloud platform.
* `Yacms-blocks`_ - A Yacms flavored fork of
  django-flatblocks.
* `Yacms-widgets`_ - Widget system for Yacms.
* `Yacms-themes`_ - A collection of Django/Yacms templates.
* `Yacms-twittertopic`_ - Manage multiple Twitter topic feeds
  from the Yacms admin interface.
* `Yacms-captcha`_ - Adds CAPTCHA field types to Yacms's
  forms builder app.
* `Yacms-bookmarks`_ - A multi-user bookmark app for Yacms.
* `Yacms-events`_ - Events plugin for Yacms, with geocoding
  via Google Maps, iCalendar files, webcal URLs and directions via
  Google Calendar/Maps.
* `Yacms-polls`_ - Polls application for Yacms.
* `Yacms-pagedown`_ - Adds the `Pagedown`_ WYSIWYG editor to
  Yacms.
* `Yacms-careers`_ - Job posting application for Yacms.
* `Yacms-recipes`_ - Recipes plugin with built-in REST API.
* `Yacms-slides`_ - Responsive banner slides app for Yacms.
* `mezzyblocks`_ - Another app for adding blocks/modules to Yacms.
* `Yacms-flexipage`_ - Allows designers to manage content areas
  in templates.
* `Yacms-instagram`_ - A simple Instagram app for Yacms.
* `Yacms-wiki`_ - Wiki app for Yacms.
* `Yacms-calendar`_ - Calendar pages in Yacms
* `Yacms-facebook`_ - Simple Facebook integration for Yacms.
* `Yacms-instagram-gallery`_ - Create Yacms galleries using
  Instagram images.
* `Yacms-cli`_ - Command-line interface for Yacms.
* `Yacms-categorylink`_ - Integrates Yacms's Link pages with
  its blog categories.
* `Yacms-podcast`_ - A simple podcast streamer and manager for
  Yacms.
* `Yacms-linkcollection`_ - Collect links. Feature them. Share
  them over RSS.
* `cash-generator`_ - Generate `GnuCash`_ invoices with Yacms.
* `Yacms-foundation`_ - `Zurb Foundation`_ theme for Yacms.
* `Yacms-file-collections`_ - Simple file collection page type
  for Yacms.
* `Yacms-wymeditor`_ - `WYMeditor`_ adapted as the rich text
  editor for Yacms.
* `Yacms-meze`_ - Adds support for `reStructuredText`_,
  `Pygments`_ and more, to Yacms's rich text editing.
* `Yacms-pageimages`_ - Add background and banner images per page
  in Yacms.
* `Yacms-protected-pages`_ - Restrict access to pages by group
  membership.
* `Yacms-page-auth`_ - A Yacms module for add group-level
  permission to pages.
* `django-widgy`_ - Widget-oriented content editing. Includes an
  adapter for Yacms and a powerful form builder.
* `Yacms-admin-backup`_ - Export your Yacms database and assets
  directly from the admin.
* `Yacms-mailchimp`_ - Integrate Yacms forms with a MailChimp
  subscription list.
* `Yacms-grappelli`_ - Integrates latest upstream
  grappelli/filebrowser with Yacms.
* `Yacms-workout`_ - Store and display FIT data in Yacms.
* `Yacms-agenda`_ - Event functionality for your Yacms sites.
* `Yacms-dpaste`_ - Integrate `dpaste`_, a Django pastebin, into
  your Yacms site.
* `Yacms-linkdump`_ - Create, display and track links in Yacms.
* `Yacms-people`_ - Categorize and list people in Yacms.
* `Yacms-webf`_ - Fabfile for deploying Yacms to Webfaction.
* `Yacmsopenshift`_ Another setup for `Redhat's OpenShift`_ cloud
  platform.
* `Yacms-bsbanners`_ - Add `Twitter Bootstrap`_ Carousels and
  Jumbotrons to Yacms.
* `Yacms-business-theme`_ - Starter business theme for Yacms.
* `open-helpdesk`_ - A helpdesk app built with Yacms.
* `Yacms-invites`_ - Allow site registration via alphanumeric
  invite codes.
* `ansible-Yacms`_ - Full pipeline (dev, staging, production)
  deployment of Yacms using `Ansible`_.
* `Yacms-modal-announcements`_ - Popup announcements for Yacms
  websites via Bootstrap modals.
* `Yacms-buffer`_ - `Buffer`_ integration for Yacms.
* `Yacms-slideshows`_ - Allows placement of Yacms galleries
  within other Yacms pages as slideshows.
* `Yacms-onepage`_ - Design helper for single-page Yacms sites.
* `Yacms-api`_ - RESTful web API for Yacms.
* `Yacms-smartling`_ - Integrates Yacms content with
  `Smartling Translations`_.
* `Yacms-shortcodes`_ - `Wordpress shortcodes`_ for Yacms.


Sites Using Yacms
=====================

Got a site built with Yacms? You can add it to the gallery on
the `Yacms project page`_ by adding it to the list below - just
fork the project and create a pull request. Please omit the trailing
slash in the URL, as we manually add that ourselves to feature
certain sites.

* `Citrus Agency <http://citrus.com.au/>`_
* `Yacms Project <http://Yacms.jupo.org>`_
* `Nick Hagianis <http://hagianis.com>`_
* `Thomas Johnson <http://tomfmason.net>`_
* `Central Mosque Wembley <http://wembley-mosque.co.uk>`_
* `Ovarian Cancer Research Foundation <http://ocrf.com.au/>`_
* `The Source Procurement <http://thesource.com.au/>`_
* `Imageinary <http://imageinary.com>`_
* `Brad Montgomery <http://blog.bradmontgomery.net>`_
* `Jashua Cloutier <http://www.senexcanis.com>`_
* `Alpha & Omega Contractors <http://alphaomegacontractors.com>`_
* `Equity Advance <http://equityadvance.com.au/>`_
* `Head3 Interactive <http://head3.com>`_
* `PyLadies <http://www.pyladies.com>`_
* `Ripe Maternity <http://www.ripematernity.com/>`_
* `Cotton On <http://shop.cottonon.com/>`_
* `List G Barristers <http://www.listgbarristers.com.au>`_
* `Tri-Cities Flower Farm <http://www.tricitiesflowerfarm.com>`_
* `daon.ru <http://daon.ru/>`_
* `autoindeks.ru <http://autoindeks.ru/>`_
* `immiau.ru <http://immiau.ru/>`_
* `ARA Consultants <http://www.araconsultants.com.au/>`_
* `Boîte à Z'images <http://boiteazimages.com/>`_
* `The Melbourne Cup <http://www.melbournecup.com/>`_
* `Diablo News <http://www.diablo-news.com>`_
* `Goldman Travel <http://www.goldmantravel.com.au/>`_
* `IJC Digital <http://ijcdigital.com/>`_
* `Coopers <http://store.coopers.com.au/>`_
* `Joe Julian <http://joejulian.name>`_
* `Sheer Ethic <http://sheerethic.com/>`_
* `Salt Lake Magazine <http://saltlakemagazine.com/>`_
* `Boca Raton Magazine <http://bocamag.com/>`_
* `Photog.me <http://www.photog.me>`_
* `Elephant Juice Soup <http://www.elephantjuicesoup.com>`_
* `National Positions <http://www.nationalpositions.co.uk/>`_
* `Like Humans Do <http://www.likehumansdo.com>`_
* `Connecting Countries <http://connectingcountries.net>`_
* `tindie.com <http://tindie.com>`_
* `Environmental World Products <http://ewp-sa.com/>`_
* `Ross A. Laird <http://rosslaird.com>`_
* `Etienne B. Roesch <http://etienneroes.ch>`_
* `Recruiterbox <http://recruiterbox.com/>`_
* `Mod Productions <http://modprods.com/>`_
* `Appsembler <http://appsembler.com/>`_
* `Pink Twig <http://www.pinktwig.ca>`_
* `Parfume Planet <http://parfumeplanet.com>`_
* `Trading 4 Us <http://www.trading4.us>`_
* `Chris Fleisch <http://chrisfleisch.com>`_
* `Theneum <http://theneum.com/>`_
* `My Story Chest <http://www.mystorychest.com>`_
* `Philip Sahli <http://www.fatrix.ch>`_
* `Raymond Chandler <http://www.codearchaeologist.org>`_
* `Nashsb <http://nashpp.com>`_
* `AciBASE <http://acinetobacter.bham.ac.uk>`_
* `Matthe Wahn <http://www.matthewahn.com>`_
* `Bit of Pixels <http://bitofpixels.com>`_
* `European Crystallographic Meeting <http://ecm29.ecanews.org>`_
* `Dreamperium <http://dreamperium.com>`_
* `UT Dallas <http://utdallasiia.com>`_
* `Go Yama <http://goyamamusic.com>`_
* `Yeti LLC <http://www.yetihq.com/>`_
* `Li Xiong <http://idhoc.com>`_
* `Pageworthy <http://pageworthy.com>`_
* `Prince Jets <http://princejets.com>`_
* `30 sites in 30 days <http://1inday.com>`_
* `St Barnabas' Theological College <http://www.sbtc.org.au/>`_
* `Helios 3D <http://helios3d.nl/>`_
* `Life is Good <http://lifeisgoodforall.co.uk/>`_
* `Building 92 <http://bldg92.org/>`_
* `Pie Monster <http://piemonster.me>`_
* `Cotton On Asia <http://asia.cottonon.com/>`_
* `Ivan Diao <http://www.adieu.me>`_
* `Super Top Secret <http://www.wearetopsecret.com/>`_
* `Jaybird Sport <http://www.jaybirdgear.com/>`_
* `Manai Glitter <https://manai.co.uk>`_
* `Sri Emas International School <http://www.sriemas.edu.my>`_
* `Boom Perun <http://perunspace.ru>`_
* `Tactical Bags <http://tacticalbags.ru>`_
* `apps.de <http://apps.de>`_
* `Sunfluence <http://sunfluence.com>`_
* `ggzpreventie.nl <http://ggzpreventie.nl>`_
* `dakuaiba.com <http://www.dakuaiba.com>`_
* `Wdiaz <http://www.wdiaz.org>`_
* `Hunted Hive <http://huntedhive.com/>`_
* `mjollnir.org <http://mjollnir.org>`_
* `The Beancat Network <http://www.beancatnet.org>`_
* `Raquel Marón <http://raquelmaron.com/>`_
* `EatLove <http://eatlove.com.au/>`_
* `Hospitality Quotient <http://hospitalityq.com/>`_
* `The Andrew Story <http://theandrewstory.com/>`_
* `Charles Koll Jewelry <http://charleskoll.com/>`_
* `Creuna (com/dk/fi/no/se) <http://www.creuna.com/>`_
* `Coronado School of the Arts <http://www.cosasandiego.com/>`_
* `SiteComb <http://www.sitecomb.com>`_
* `Dashing Collective <http://dashing.tv/>`_
* `Puraforce Remedies <http://puraforceremedies.com/>`_
* `Google's VetNet <http://www.vetnethq.com/>`_
* `1800RESPECT <http://www.1800respect.org.au/>`_
* `Evenhouse Consulting <http://evenhouseconsulting.com/>`_
* `Humboldt Community Christian School <http://humboldtccs.org>`_
* `Atlanta's Living Legacy <http://gradyhistory.com>`_
* `Shipgistix <http://shipgistix.com>`_
* `Yuberactive <http://www.yuberactive.asia>`_
* `Medical Myth Busters <http://pogromcymitowmedycznych.pl>`_
* `4player Network <http://4playernetwork.com/>`_
* `Top500 Supercomputers <http://top500.org>`_
* `Die Betroffenen <http://www.zeichnemit.de>`_
* `uvena.de <http://uvena.de>`_
* `ezless.com <http://ezless.com>`_
* `Dominican Python <http://python.do>`_
* `Stackful.io <http://stackful.io/>`_
* `Adrenaline <http://www.adrln.com/>`_
* `ACE EdVenture Programme <http://aceedventure.com/>`_
* `Butchershop Creative <http://www.butchershopcreative.com/>`_
* `Sam Kingston <http://www.sjkingston.com>`_
* `Ludwig von Mises Institute <http://mises.fi>`_
* `Incendio <http://incendio.no/>`_
* `Alexander Lillevik <http://lillevikdesign.no/>`_
* `Walk In Tromsø <http://www.turitromso.no>`_
* `Mandrivia Linux <http://www.mandriva.com/>`_
* `Crown Preschool <http://crownpreschool.com>`_
* `Coronado Pathways Charter School <http://coronadopathways.com>`_
* `Raindrop Marketing <http://www.raindropads.com>`_
* `Web4py <http://www.web4py.com>`_
* `The Peculiar Store <http://thepeculiarstore.com>`_
* `GrinDin <http://www.grindin.ru>`_
* `4Gume <http://www.4gume.com>`_
* `Skydivo <http://skydivo.com>`_
* `Noshly <http://noshly.com>`_
* `Kabu Creative <http://kabucreative.com.au/>`_
* `KisanHub <http://www.kisanhub.com/>`_
* `Your Song Your Story <http://yoursongyourstory.org/>`_
* `Kegbot <http://kegbot.org>`_
* `Fiz <http://fiz.com/>`_
* `Willborn <http://willbornco.com>`_
* `Copilot Co <http://copilotco.com>`_
* `Amblitec <http://www.amblitec.com>`_
* `Gold's Gym Utah <http://www.bestgymever.com/>`_
* `Appsin - Blog to Native app <http://apps.in/>`_
* `Take Me East <http://takemeeast.net>`_
* `Code Raising <http://www.coderaising.org>`_
* `ZigZag Bags <http://www.zigzagbags.com.au>`_
* `VerifIP <http://verifip.com/>`_
* `Clic TV <http://www.clictv.tv/>`_
* `JE Rivas <http://www.jerivas.com/>`_
* `Heather Gregory Nutrition <http://heathergregorynutrition.com>`_
* `Coronado Island Realty <http://coronado-realty.com>`_
* `Loans to Homes <http://loanstohomes.com>`_
* `Gensler Group <http://genslergroup.com>`_
* `SaniCo <https://sanimedicaltourism.com>`_
* `Grupo Invista <http://grupoinvista.com>`_
* `Brooklyn Navy Yard <http://brooklynnavyyard.org/>`_
* `MEZZaTHEME <http://mezzathe.me/>`_
* `Nektra Advanced Computing <http://www.nektra.com/>`_
* `Bootstrap ASAP <https://bootstrapasap.com/>`_
* `California Center for Jobs <http://www.centerforjobs.org/>`_
* `Sam Kingston <http://www.sjkingston.com>`_
* `Code Juggle DJ <http://www.codejuggle.dj>`_
* `Food News <http://food.hypertexthero.com>`_
* `Australian Discworld Conventions <http://ausdwcon.org>`_
* `Distilled <http://www.distilled.net/>`_
* `OpenMRP <http://www.openmrp.es>`_
* `Arkade Snowboarding <http://www.arkadesnowboarding.com/>`_
* `Linktective The Link Checker <http://www.linktective.com>`_
* `Zetalab <http://www.zetalab.de>`_
* `Make-Up Artists & Hair Stylists Guild <http://www.local706.org>`_
* `Anywhereism <http://www.anywhereism.net>`_
* `Assistive Listening Device Locator <http://aldlocator.com>`_
* `Frank & Connie Spitzer <http://sdhome4you.com>`_
* `Coronado Unified School District <http://coronadousd.net>`_
* `Coronado Inn <http://coronadoinn.com>`_
* `Coronado Schools Foundation <http://csfkids.org>`_
* `Light and Life Christian School <http://www.lightandlifechristianschool.com>`_
* `The Morabito Group <http://themorabitogroup.com>`_
* `Law Offices of Nancy Gardner <http://nancygardnerlaw.com>`_
* `Soden & Steinberger APLC <http://legalmattersllp.com>`_
* `Stalwart Communications <http://stalwartcom.com>`_
* `Ubuntu Consultants <http://ubuntuconsultants.com>`_
* `Wine a Bit Coronado <http://wineabitcoronado.com>`_
* `Mercury Mastering <http://mercurymastering.com>`_
* `Flowgrammable <http://flowgrammable.org>`_
* `Shibe Mart <http://shibemart.com>`_
* `Carlos Isaac Balderas <http://caisbalderas.com/>`_
* `Enrico Tröger <http://www.pending.io>`_
* `Perugini <http://peruginicase.it/>`_
* `YouPatch <https://www.youpatch.com>`_
* `Batista Peniel <http://batistapeniel.org>`_
* `Perceptyx <http://www.perceptyx.com/>`_
* `Guddina Coffee <http://guddina.com>`_
* `Atami Escape Resort <http://www.atami.com.sv>`_
* `Philip Southwell <http://www.philipsouthwell.com>`_
* `Justine & Katie's Bowtique <http://www.jnkbows.com>`_
* `The Grantwell LLC <https://www.thegrantwell.com>`_
* `PyCon Asia-Pacific <https://tw.pycon.org/>`_
* `Nerdot <http://nerdot.com.do>`_
* `Coworking.do <http://coworking.do>`_
* `Arlette Pichardo <http://arlettepichardo.com>`_
* `Sani Dental Group <http://sanidentalgroup.com>`_
* `Biocap 06 <http://www.biocap06.fr>`_
* `Python Baja California <http://pythonbc.co/>`_
* `The Art Rebellion <http://www.theartrebellion.com/>`_
* `Engineered Arts <https://www.engineeredarts.co.uk>`_
* `Paul Whipp Consulting <http://www.paulwhippconsulting.com>`_
* `Lipman Art <https://lipmanart.com/>`_
* `MODCo Group <http://modcogroup.com/>`_
* `Terminal Labs <http://www.terminallabs.com>`_
* `Resource Management Companies <http://rmcrecycle.com>`_
* `DollFires <http://dollfires.com>`_
* `Quantifind <http://quantifind.com/>`_
* `ZHackers <https://www.zhackers.com>`_
* `Open ERP Arabia <http://openerparabia.org/>`_
* `DataKind <http://www.datakind.org/>`_
* `New Zealand Institute of Economic Research <http://nzier.org.nz/>`_
* `CodingHouse <http://thecodinghouse.in>`_
* `Triple J Products <http://triplejcoilproducts.com>`_
* `Aaron E. Balderas <http://abalderas.com>`_
* `DVD.nl <http://dvd.nl/>`_
* `Constantia Fabrics <http://www.constantiafabrics.co.za/>`_
* `Potrillo al Pie <http://potrilloalpie.com/>`_
* `Skyfalk Web Studio <http://skyfalk.ru>`_
* `Firefox OS Partners <https://mobilepartners.mozilla.org/>`_
* `You Name It <http://you-name-it.net>`_
* `Atlas of Human Infectious Diseases <https://infectionatlas.org>`_
* `The Entrepreneurial School <http://theentrepreneurialschool.com/>`_
* `Wednesday Martin <http://wednesdaymartin.com/>`_
* `Avaris to Avanim <https://avaristoavanim.com>`_
* `Cognitions Coaching and Consulting <http://www.cognitionscoachingandconsulting.com>`_
* `Foundation Engineering Group <http://fegroup.net.au>`_
* `Hivelocity <https://www.hivelocity.net>`_
* `Zooply <http://zoop.ly>`_
* `Oceana Technologies <http://oceanatech.com>`_
* `TerraHub <http://terrahub.org/>`_
* `djangoproject.jp <http://djangoproject.jp/>`_
* `Joshua Ginsberg <http://starboard.flowtheory.net>`_
* `Savant Digital <http://www.savantdigital.net>`_
* `weBounty <https://webounty.com>`_
* `Oxfam America <http://www.oxfamamerica.org/>`_
* `Artivest <https://artivest.co/>`_
* `Dark Matter Sheep <http://darkmattersheep.net>`_
* `Mission Healthcare <http://homewithmission.com>`_
* `Two Forty Fives <http://twofortyfives.com/>`_
* `Rodeo Austin <http://rodeoaustin.com/>`_
* `Krisers <http://krisers.com/>`_
* `Intentional Creation <http://intentionalcreation.com/>`_
* `BytesArea <http://www.bytesarea.com>`_
* `Debra Solomon <http://www.debrasolomon.com>`_
* `Pampanga Food Company <http://pampangafood.com>`_
* `Aman Sinaya <http://amansinaya.com>`_
* `Deschamps osteo <http://www.deschamps-osteopathe.fr>`_
* `Deschamps kine <http://www.deschamps-kinesitherapeute.fr>`_
* `Creactu <http://creactu.fr>`_
* `scrunch <https://scrunch.com>`_
* `App Dynamics <http://www.appdynamics.com/>`_
* `Homespun Music Instruction <https://www.homespun.com>`_
* `Fusionbox <https://www.fusionbox.com/>`_
* `The Street University <http://www.streetuni.net>`_
* `Glebe <http://glebe.com.au>`_
* `CeoDental Seminars <https://www.ceodental.com.au>`_
* `Pay By Super <https://www.paybysuper.com.au>`_
* `Noffs <https://www.noffs.org.au>`_
* `Spokade <http://spokade.com>`_
* `Brisbane Prosthodontics <http://www.brisbaneprosthodontics.com.au>`_
* `Carbonised <http://carbonised.com.au>`_
* `Derry Donnell <http://www.derrydonnell.com.au>`_
* `Dr Kenneth Cutbush <http://kennethcutbush.com>`_
* `American Institute for Foreign Study <http://www.aifs.com.au>`_
* `Camp America <http://campamerica.com.au>`_
* `Code Source <http://codesource.com.au/>`_
* `The Federation of Egalitarian Communities <http://thefec.org>`_

.. _`Yacms Grid on djangopackages.com`: http://www.djangopackages.com/grids/g/Yacms/
.. _`Cartridge`: http://cartridge.jupo.org/
.. _`Drum`: https://github.com/stephenmcd/drum
.. _`Hacker News`: https://news.ycombinator.com
.. _`Reddit`: http://www.reddit.com
.. _`Yacms-html5boilerplate`: https://github.com/tvon/Yacms-html5boilerplate
.. _`Yacms-html5boilerplate`: https://github.com/tvon/Yacms-html5boilerplate
.. _`html5boilerplate project`: http://html5boilerplate.com/
.. _`Yacms-mdown`: https://bitbucket.org/onelson/Yacms-mdown
.. _`Markdown`: http://en.wikipedia.org/wiki/Markdown
.. _`Yacms-openshift`: https://github.com/overshard/Yacms-openshift
.. _`Redhat's OpenShift`: https://openshift.redhat.com/
.. _`Ansible`: http://www.ansible.com/
.. _`Yacms-stackato`: https://github.com/Stackato-Apps/Yacms
.. _`ActiveState's Stackato`: http://www.activestate.com/stackato
.. _`Yacms-blocks`: https://github.com/renyi/Yacms-blocks
.. _`Yacms-widgets`: https://github.com/osiloke/Yacms_widgets
.. _`Yacms-themes`: https://github.com/renyi/Yacms-themes
.. _`Yacms-twittertopic`: https://github.com/lockhart/Yacms-twittertopic
.. _`Yacms-captcha`: https://github.com/mjtorn/Yacms-captcha
.. _`Yacms-bookmarks`: https://github.com/adieu/Yacms-bookmarks
.. _`Yacms-events`: https://github.com/stbarnabas/Yacms-events
.. _`Yacms-polls`: https://github.com/sebasmagri/Yacms_polls
.. _`Yacms-pagedown`: https://bitbucket.org/akhayyat/Yacms-pagedown
.. _`PageDown`: https://code.google.com/p/pagedown/
.. _`Yacms-careers`: https://github.com/mogga/Yacms-careers
.. _`Yacms-recipes`: https://github.com/tjetzinger/Yacms-recipes
.. _`Yacms-slides`: https://github.com/overshard/Yacms-slides
.. _`mezzyblocks`: https://github.com/jardaroh/mezzyblocks
.. _`Yacms-flexipage`: https://github.com/mrmagooey/Yacms-flexipage
.. _`Yacms-wiki`: https://github.com/dfalk/Yacms-wiki
.. _`Yacms-instagram`: https://github.com/shurik/Yacms_Instagram
.. _`Yacms-calendar`: https://github.com/shurik/Yacms.calendar
.. _`Yacms-facebook`: https://github.com/shurik/Yacms_Facebook
.. _`Yacms-instagram-gallery`: https://github.com/georgeyk/Yacms-instagram-gallery
.. _`Yacms-cli`: https://github.com/adieu/Yacms-cli
.. _`Yacms-categorylink`: https://github.com/mjtorn/Yacms-categorylink
.. _`Yacms-podcast`: https://github.com/carpie/Yacms-podcast
.. _`Yacms-linkcollection`: https://github.com/mjtorn/Yacms-linkcollection
.. _`cash-generator`: https://github.com/ambientsound/cash-generator
.. _`GnuCash`: http://www.gnucash.org/
.. _`Yacms-foundation`: https://github.com/zgohr/Yacms-foundation
.. _`Zurb Foundation`: http://foundation.zurb.com/
.. _`Yacms-file-collections`: https://github.com/thibault/Yacms-file-collections
.. _`Yacms-wymeditor`: https://github.com/excieve/Yacms-wymeditor
.. _`WYMeditor`: http://wymeditor.github.io/wymeditor/
.. _`Yacms-meze`: https://github.com/abakan/Yacms-meze
.. _`reStructuredText`: http://docutils.sourceforge.net/rst.html
.. _`Pygments`: http://pygments.org/
.. _`Yacms-pageimages`: https://github.com/bcs-de/Yacms-pageimages
.. _`Yacms-protected-pages`: https://github.com/evilchili/Yacms-protected-pages
.. _`Yacms-page-auth`: https://github.com/simodalla/Yacms_page_auth
.. _`django-widgy`: http://django-widgy.readthedocs.org/en/latest/
.. _`Yacms-admin-backup`: https://bitbucket.org/joshcartme/Yacms-admin-backup
.. _`Yacms-mailchimp`: https://bitbucket.org/naritas/Yacms-mailchimp
.. _`Yacms-grappelli`: https://github.com/sephii/Yacms-grappelli
.. _`Yacms-workout`: https://github.com/kampfschlaefer/Yacms-workout
.. _`Yacms-agenda`: https://github.com/jpells/Yacms-agenda
.. _`Yacms-dpaste`: https://github.com/prikhi/Yacms-dpaste
.. _`Yacms-linkdump`: https://github.com/prikhi/Yacms-linkdump
.. _`Yacms-people`: https://github.com/eci/Yacms-people
.. _`Yacms-webf`: https://github.com/jerivas/Yacms-webf
.. _`Yacmsopenshift`: https://bitbucket.org/radeksvarz/Yacmsopenshift
.. _`Yacms-bsbanners`: https://pypi.python.org/pypi/Yacms-bsbanners
.. _`Yacms-business-theme`: https://github.com/dfalk/Yacms-business-theme
.. _`open-helpdesk`: https://github.com/simodalla/open-helpdesk
.. _`Yacms-invites`: https://github.com/averagehuman/Yacms-invites
.. _`ansible-Yacms`: https://github.com/keithadavidson/ansible-Yacms
.. _`Yacms-modal-announcements`: https://github.com/joshcartme/Yacms-modal-announcements
.. _`Yacms-buffer`: https://github.com/caffodian/Yacms-buffer
.. _`Buffer`: http://buffer.com
.. _`Yacms-slideshows`: https://github.com/philipsouthwell/Yacms-slideshows
.. _`Yacms-onepage`: https://github.com/lucmilland/Yacms-onepage
.. _`Yacms-api`: https://github.com/gcushen/Yacms-api
.. _`Yacms-smartling`: https://github.com/Appdynamics/Yacms-smartling
.. _`Yacms-shortcodes`: https://github.com/ryneeverett/Yacms-shortcodes

.. _`Wordpress shortcodes`: https://codex.wordpress.org/Shortcode
.. _`Smartling Translations`: http://www.smartling.com/
.. _`dpaste`: https://github.com/bartTC/dpaste


.. _`Python`: http://python.org/
.. _`django-contrib-comments`: https://pypi.python.org/pypi/django-contrib-comments
.. _`bleach`: http://pypi.python.org/pypi/bleach
.. _`BeautifulSoup`: http://www.crummy.com/software/BeautifulSoup/
.. _`pytz`: http://pypi.python.org/pypi/pytz/
.. _`tzlocal`: http://pypi.python.org/pypi/tzlocal/
.. _`django-compressor`: https://pypi.python.org/pypi/django_compressor
.. _`Python Imaging Library`: http://www.pythonware.com/products/pil/
.. _`Pillow`: https://github.com/python-imaging/Pillow
.. _`grappelli-safe`: http://github.com/stephenmcd/grappelli-safe
.. _`filebrowser-safe`: http://github.com/stephenmcd/filebrowser-safe/
.. _`Grappelli`: http://code.google.com/p/django-grappelli/
.. _`FileBrowser`: http://code.google.com/p/django-filebrowser/
.. _`pip`: http://www.pip-installer.org/
.. _`requests`: http://docs.python-requests.org/en/latest/
.. _`requests_oauthlib`: http://requests-oauthlib.readthedocs.org/
.. _`pyflakes`: http://pypi.python.org/pypi/pyflakes
.. _`chardet`: https://chardet.readthedocs.org
.. _`pep8`: http://pypi.python.org/pypi/pep8
.. _`Homebrew`: http://mxcl.github.com/homebrew/
.. _`django-modeltranslation`: http://django-modeltranslation.readthedocs.org
