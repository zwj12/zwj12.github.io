---
layout: post
title: "Appweb Http API"
date: 2022-06-29 14:50:00 +0800
author: Michael
categories: CPP
---

# HttpRx
## HttpRx.method (cchar *)
Request method: GET, HEAD, POST, DELETE, OPTIONS, PUT, TRACE.

##  HttpRx.uri (cchar *)
Current URI (not decoded, may be rewritten). 不包含IP地址和端口

	/pick/michael/index.html

## HttpRx.parsedUri (HttpUri *)
Parsed request uri.

## HttpRx.length
Content length header value (ENV: CONTENT_LENGTH).http报文头里面的数据长度。

# HttpUri.query (cchar *)
查询字符串

	a=b&c=d

# HttpStream
## HttpStream.username
basic或digest模式登录时的用户名。

## HttpStream.data
Custom data for request - must be a managed reference.

# HttpStage
## HttpStage.incoming
每次接收到数据包会被调用，该函数至少会被调用两次，最后一次是HttpPacket.flags=HTTP_PACKET_END的数据包，代表数据包结尾。如果客户端发送的数据包很大，会出发多次incoming函数，此时就会被调用不仅仅两次了。  
The end of the input stream is signified by a packet with flags set to HTTP_PACKET_END. The handler may choose to aggregate body data on its read service queue until the entire body is received.

# httpSetStatus
此函数用于设置http返回的状态码。

	PUBLIC void httpSetStatus(HttpStream *stream, int status)
	{
	    stream->tx->status = status;
	    stream->tx->responded = 1;
	}

# httpFinalize & httpFinalizeInput & httpFinalizeOutput
You can call httpFinalize if you have generated all the response output and completed all processing. This implies httpFinalizeOutput and may then discard any remaining input. Alternatively, call httpFinalizeInput when you have processed all input and httpFinalizeOutput when you have generated all output.