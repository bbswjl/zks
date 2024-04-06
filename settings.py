# RANDOM WALLETS MODE 如果设置为True，脚本会随机选择一个可用的钱包账户执行操作；如果设置为False，则会按顺序使用配置文件中的每个账户
RANDOM_WALLET = True  # True or False

QUANTITY_RUN_ACCOUNTS = 2 #这个变量通常用于控制某个程序或脚本中的重复操作次数。

##睡眠模式，这两个配置项分别指定了睡眠时间的最短和最长时间（以秒为单位）
SLEEP_FROM = 500  # Second 最短睡眠时间（以秒为单位）
SLEEP_TO = 1000  # Second 最长睡眠时间（以秒为单位）

# PROXY MODE 是否启用代理模式。如果设置为True，脚本将使用代理服务器执行操作；如果设置为False，脚本将直接执行操作。
USE_PROXY = False

# GWEI CONTROL MODE 控制以太坊交易的GWEI（燃气价格）。如果设置为True，脚本将检查当前的GWEI价格，如果高于指定的MAX_GWEI，则可能会等待以获得更好的交易费用
CHECK_GWEI = True  # True or False
MAX_GWEI = 30

GAS_MULTIPLIER = 1.1 #设置交易费用的倍增器。例如，如果设置为1.3，交易费用将增加30%。

# RETRY MODE 如果设置为True，脚本会尝试多次执行交易，最多重试RETRY_COUNT次。
RETRY_COUNT = 3

# INCH API KEY 1inch API相关的API密钥
INCH_API_KEY = ""
