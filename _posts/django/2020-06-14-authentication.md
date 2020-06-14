---
layout: post
title: "Authentication"
date: 2020-06-14 09:28:00 +0800
author: Michael
categories: Django
---

# Default permissions
- Access to view objects is limited to users with the “**view**” or “**change**” permission for that type of object.
- Access to view the “add” form and add an object is limited to users with the “**add**” permission for that type of object.
- Access to view the change list, view the “change” form and change an object is limited to users with the “**change**” permission for that type of object.
- Access to delete an object is limited to users with the “**delete**” permission for that type of object.

# Authorization
	user = authenticate(username='john', password='secret')
	u = User.objects.get(username='john')
	has_view_permission()
	has_add_permission()
	has_change_permission()
	has_delete_permission()
	myuser.groups.set([group_list])
	myuser.groups.add(group, group, ...)
	myuser.groups.remove(group, group, ...)
	myuser.groups.clear()
	myuser.user_permissions.set([permission_list])
	myuser.user_permissions.add(permission, permission, ...)
	myuser.user_permissions.remove(permission, permission, ...)
	myuser.user_permissions.clear()
	add: user.has_perm('foo.add_bar')
	change: user.has_perm('foo.change_bar')
	delete: user.has_perm('foo.delete_bar')
	view: user.has_perm('foo.view_bar')

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...

	logout(request)