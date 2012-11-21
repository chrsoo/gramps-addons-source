register(QUICKREPORT,
         id = 'Descendant Count Quickview',
         name = _("Descendant Count"),
         category = CATEGORY_QR_MISC,
         runfunc = "run",
         status = STABLE, # not yet tested with python 3
         description= _("Display descendant counts for each person."),
         fname="DescendantCount.py",
         authors=["Douglas S. Blank"],
         authors_email=["doug.blank@gmail.com"],
         version = '1.0.9',
         gramps_target_version = "4.0",
         )

register(GRAMPLET, 
         id="Descendant Count Gramplet", 
         name=_("Descendant Count Gramplet"), 
         description = _("Gramplet for showing people and descendant counts"),
         status=STABLE, # not yet tested with python 3
         fname="DescendantCount.py",
         height=300,
         expand=True,
         gramplet = "DescendantCountGramplet",
         gramplet_title=_("Descendant Count"),
         detached_width = 600,
         detached_height = 400,
         version = '1.0.10',
         gramps_target_version = "4.0",
         )

