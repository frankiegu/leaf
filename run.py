"""框架运行示例文件"""

import logging
import flask

import leaf
import config

print("Initialing leaf modules...")
init = leaf.Init()
init.kernel()
init.logging(config.logging)
init.server()
init.database(config.database)
init.plugins(config.plugins)
init.weixin(config.weixin)
init.wxpay(config.wxpay)

# 获取服务模块
server: flask.Flask = leaf.modules.server
plugins: leaf.plugins.Manager = leaf.modules.plugins
logger: logging.Logger = leaf.modules.logging.logger
events: leaf.core.events.Manager = leaf.modules.events
wxpay: leaf.core.algorithm.AttrDict = leaf.payments.wxpay
weixin: leaf.core.algorithm.AttrDict = leaf.modules.weixin
schedules: leaf.core.schedule.Manager = leaf.modules.schedules

print("All modules has been imported...")
