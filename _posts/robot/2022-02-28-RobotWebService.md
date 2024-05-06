---
layout: post
title: "Robot Web Service"
date: 2022-02-28 09:48:00 +0800
author: Michael
categories: robot
---

# Port
C:\Users\CNMIZHU7\AppData\Local\ABB\RobotWare\RobotWare_6.13.0176\system\appweb.conf  

	Listen 46131

![日志文件夹](/assets/robot/RWS/RWSListenPort.png)   

# rapid symbol data
	username = "Default User"
	password = "robotics"
	web_service_connection = WebServiceConnection("localhost", 6155, username, password)

	url = f"http://{WebServiceConnection.get_host()}:{WebServiceConnection.get_port()}/rw/rapid/symbol/data/RAPID/T_ROB1/user/reg1?json=1"
	resp = WebServiceConnection.get_session().get(url, cookies=WebServiceConnection.get_cookies())
	obj = json.loads(resp.text)
	reg1 = obj["_embedded"]["_state"][0]["value"]
	print(reg1)

# Get or Update IO Signal Value
	username = "Default User"
	password = "robotics"
	web_service_connection = WebServiceConnection("localhost", 6155, username, password)

	url = f"http://{WebServiceConnection.get_host()}:{WebServiceConnection.get_port()}/rw/iosystem/signals/EtherNetIP/PPABOARD/doTrigVis1?json=1"
	resp = WebServiceConnection.get_session().get(url, cookies=WebServiceConnection.get_cookies())
	obj = json.loads(resp.text)
	doTrigVis1 = obj["_embedded"]["_state"][0]["lvalue"]
	print(doTrigVis1)

	url = f"http://{WebServiceConnection.get_host()}:{WebServiceConnection.get_port()}/rw/iosystem/signals/EtherNetIP/PPABOARD/doTrigVis1?action=set"
	payload = {"lvalue": 0 if doTrigVis1 == "1" else 1}
	resp = WebServiceConnection.get_session().post(url, cookies=WebServiceConnection.get_cookies(), data=payload)
	print(resp)

# Pulase Signal
可以设置脉冲一次或多次，如果多次，需要设置正周期和负周期

	url = f"http://{WebServiceConnection.get_host()}:{WebServiceConnection.get_port()}/rw/iosystem/signals/EtherNetIP/PPABOARD/doTrigVis1?action=set"
	payload = {"lvalue": 1, "mode": "pulse", "Pulses":1}
	# payload = {"lvalue": 1, "mode": "pulse", "Pulses":10, "ActivePulse":200, "PassivePulse":200, "userlog": "true"}
	resp = WebServiceConnection.get_session().post(url, cookies=WebServiceConnection.get_cookies(), data=payload)
	print(resp)