---
layout: post
title: "Message Queue"
date: 2020-08-31 12:57:00 +0800
author: Michael
categories: Halcon
---

	create_message_queue (QueueHandle)
	create_message (MessageHandle)
	set_message_tuple (MessageHandle,'first' , ['hello','world'])
	enqueue_message (QueueHandle, MessageHandle,[] , [])
	
	set_message_tuple (MessageHandle,'first2' , ['hello2','world2'])
	enqueue_message (QueueHandle, MessageHandle,[] , [])
	
	dequeue_message (QueueHandle, 'timeout', 'infinite', MessageHandleOut)
	get_message_tuple (MessageHandleOut,'first' , TupleData)
	dequeue_message (QueueHandle, 'timeout', 'infinite', MessageHandleOut2)
	get_message_tuple (MessageHandleOut2,'first2' , TupleData2)