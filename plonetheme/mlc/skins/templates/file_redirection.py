## Script (Python) "File Redirection"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
"""
Will open file automatically for non-editors.
"""
request = context.REQUEST
response = request.response

from Products.CMFCore.utils import getToolByName

properties = getToolByName(context, 'portal_properties')
membership = getToolByName(context, 'portal_membership')

download = properties.site_properties.getProperty('redirect_links', False)
can_modify = membership.checkPermission('Modify portal content', context)

if download and not can_modify:
    return response.redirect(context.absolute_url())
else:
    return context.file_view()