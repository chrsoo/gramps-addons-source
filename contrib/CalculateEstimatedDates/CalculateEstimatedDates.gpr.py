#------------------------------------------------------------------------
#
# Calculate Estimated Dates
#
#------------------------------------------------------------------------

register(TOOL, 
id    = 'calculateestimateddates',
name  = _("Calculate Estimated Dates"),
description =  _("Calculates estimated dates for birth and death."),
version = '0.90.10',
gramps_target_version = '4.0',
status = UNSTABLE, # not yet tested with python 3
fname = 'CalculateEstimatedDates.py',
authors = ["Douglas S. Blank"],
authors_email = ["dblank@cs.brynmawr.edu"],
category = TOOL_DBPROC,
toolclass = 'CalcToolManagedWindow',
optionclass = 'CalcEstDateOptions',
tool_modes = [TOOL_MODE_GUI]
  )

