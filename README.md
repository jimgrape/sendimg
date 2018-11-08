# sendimg：weechat图床插件
一个[weechat](https://weechat.org/download/) 插件，用于通过图床发送图片


## Install

```
	$ it clone git@github.com:jimgrape/sendimg.git ~/.weechat/python/
	$ cd ~/.weechat/python/autoload
	$ ln -s ../script.py
```

## Usage

```
	[python/sendimg] /sendimg [filename]

	filename可以是：
		/home/XXX/Desktop/XXX.jpg
		~/Desktop/XXX.png
		'/home/XXX/Desktop/XXX.jpg'

	建议复制文件后，直接Ctrl+Shift+P粘贴
```
	
### Examples
```
  	在weechat聊天窗口中输入：
  	/sendimg ~/Desktop/test.png

```

### About Picture Bed

```
	默认图床
	https://img.vim-cn.com/

	修改图床地址
	/set plugins.var.python.sendimg.picbed "xxxx"
```

## License

GPL3 © 
