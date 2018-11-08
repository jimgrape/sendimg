# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 by ksy <910661511@qq.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

#
# (this script requires WeeChat 0.3 or newer)
#
# History:
# 2018-11-05, ksy <910661511@qq.com>
#  version 0.1: initial release

from os import popen
from os.path import expanduser, exists
import weechat as w

SCRIPT_NAME    = "sendimg"
SCRIPT_AUTHOR  = "ksy <910661511@qq.com>"
SCRIPT_VERSION = "0.1"
SCRIPT_LICENSE = "GPL3"
SCRIPT_DESC    = "send your image to the chanel via the picture bed"
SCRIPT_COMMAND  = SCRIPT_NAME

settings = {
    'picbed': 'https://img.vim-cn.com/',  
}

if w.register(SCRIPT_NAME, SCRIPT_AUTHOR, SCRIPT_VERSION, SCRIPT_LICENSE,SCRIPT_DESC, "", ""):
    for option, default_value in settings.items():
        if not w.config_is_set_plugin(option):
            w.config_set_plugin(option, default_value)

    w.hook_command(SCRIPT_COMMAND,
        "send image via the picture bed",
        "[filename]",
        "  filename: target file \n",
        "%f",
        "sendimg_cmd",
        '')

def sendimg_cmd(data, buffer, args):
    ''' Callback for /sendimg command '''

    filename = args

    if not filename:
        w.command('', '/help %s' %SCRIPT_COMMAND)
        return w.WEECHAT_RC_OK

    filename = filename.strip("'")
    ''' use for '/home/ksy/xxx.png' '''

    filename = filename.replace('file://','')
    ''' filename may have a head if you copy from desktop '''

    w.prnt(buffer, 'sending\t'+filename)
    ''' show the picture you sent '''

    filename = filename.replace('~', expanduser('~'))
    ''' curl can't use '~' '''

    if not exists(filename):
        w.prnt('', 'Error: target file does not exist!')
        return w.WEECHAT_RC_OK

    picbed = w.config_get_plugin('picbed')
    cmd = "curl -s -F 'name=@" + filename + "' " + picbed 

    w.command(buffer, popen(cmd).read())
    # w.command(buffer, '/window refresh')
    return w.WEECHAT_RC_OK
