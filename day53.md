### day52

#### 1.HTTP 

www.cnblogs.com/clschao/articles/10391859.html

##### 1.1 HTTP工作原理

```
HTTP协议定义Web客户端如何从Web服务器请求Web页面，以及服务器如何把Web页面传送给客户端。HTTP协议采用了请求/响应模型。客户端向服务器发送一个请求报文，请求报文包含请求的方法、URL、协议版本、请求头部和请求数据。服务器以一个状态行作为响应，响应的内容包括协议的版本、成功或者错误代码、服务器信息、响应头部和响应数据。

以下是 HTTP 请求/响应的步骤：

1. 客户端连接到Web服务器
一个HTTP客户端，通常是浏览器，与Web服务器的HTTP端口（默认为80）建立一个TCP套接字连接。例如，http://www.luffycity.com。

2. 发送HTTP请求
通过TCP套接字，客户端向Web服务器发送一个文本的请求报文，一个请求报文由请求行、请求头部、空行和请求数据4部分组成。

3. 服务器接受请求并返回HTTP响应
Web服务器解析请求，定位请求资源。服务器将资源复本写到TCP套接字，由客户端读取。一个响应由状态行、响应头部、空行和响应数据4部分组成。

4. 释放连接TCP连接
若connection 模式为close，则服务器主动关闭TCP连接，客户端被动关闭连接，释放TCP连接;若connection 模式为keepalive，则该连接会保持一段时间，在该时间内可以继续接收请求;

5. 客户端浏览器解析HTML内容
客户端浏览器首先解析状态行，查看表明请求是否成功的状态代码。然后解析每一个响应头，响应头告知以下为若干字节的HTML文档和文档的字符集。客户端浏览器读取响应数据HTML，根据HTML的语法对其进行格式化，并在浏览器窗口中显示。
```

##### 1.2 HTTP状态码

```
所有HTTP响应的第一行都是状态行，依次是当前HTTP版本号，3位数字组成的状态代码，以及描述状态的短语，彼此由空格分隔。

状态代码的第一个数字代表当前响应的类型：

1xx消息——请求已被服务器接收，继续处理
2xx成功——请求已成功被服务器接收、理解、并接受
3xx重定向——需要后续操作才能完成这一请求
4xx请求错误——请求含有词法错误或者无法被执行
5xx服务器错误——服务器在处理某个正确请求时发生错误
虽然 RFC 2616 中已经推荐了描述状态的短语，例如"200 OK"，"404 Not Found"，但是WEB开发者仍然能够自行决定采用何种短语，用以显示本地化的状态描述或者自定义信息。
```

![image-20200303104026809](C:\Users\davidlu\AppData\Roaming\Typora\typora-user-images\image-20200303104026809.png)

```
GET / HTTP/1.1	#请求方法+空格+路径（/）+空格+协议版本
/*#请求头部信息
Host: 127.0.0.1 
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
DNT: 1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Sec-Fetch-Site: none
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
*/ #请求头部信息
```

##### 1.3 请求方法

get post

```
	GET 提交的数据会放在URL之后，也就是请求行里面，以？分割URL和传输数据，参数之间以&相连，如EditBook?name=test&id=12345.POST方法是把提交的数据放在HTTP包的请求数据部分中。
	GET提交的数据大小限制（因为浏览器对URL的长度有限制），而POST方法提交的数据没有限制。
	GET与POST请求在服务端获取请求数据方式不同，就是我们自己在服务端取请求数据的时候方式不同了。
	
	常用的get请求方式：浏览器输入网址，a标签，form标签 method='get'
	post请求方法，一般都用来提交数据，比如用户名密码登录
```

##### 1.4 HTTP协议特点

​	1.基于 请求-响应 的模式

​	2.无状态保存

​	3.无连接

#### 2.