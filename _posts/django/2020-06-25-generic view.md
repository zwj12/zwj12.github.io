---
layout: post
title: "generic view"
date: 2020-06-25 11:07:00 +0800
author: Michael
categories: Django
---

ListView:

	model = Publisher
	template_name: books/publisher_list.html
	context_object_name = object_list
    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, name=self.kwargs['publisher'])
        return Book.objects.filter(publisher=self.publisher)
		self.request.user

DetailView:

	get_context_data
	queryset
	get_object

FormView: