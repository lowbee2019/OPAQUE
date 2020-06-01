# 算法过程：

## 0x00 描述过程：



## 0x01 初始化：

用户和服务器之间首先约定素数n阶群G，选择生成元g。

 

用户User：

| 参数 | 意义       | 解释                 |
| ---- | ---------- | -------------------- |
| x    | password   | 类似salt的功能       |
| IDU  | ID         | 用户的标志ID         |
| PubU | 用户的公钥 | PubU = $$g^{PrivU}$$ |

服务器Server：

| 参数 | 意义         | 解释                 |
| ---- | ------------ | -------------------- |
| y    | User Key     | 用户在服务器端的标志 |
| IDS  | ID           | 服务器的ID           |
| PubS | 服务器的公钥 | PubS = $$g^{PrivS}$$ |

 

## 0x02 交换信息：

User------> Server: $$g^x$$,IDU,PubU

User计算d = H($$g^x$$, IDS)

Server------->User:$$g^y$$,IDS,PubS

Server计算e = H($$g^y$$, IDU)

## 0x03 计算密钥：

User：UK = H[($$g^y$$$$PubS^e$$$$)^{(d*PrivU+x)}$$]

Server: SK = H[($$g^x$$$$PubU^d$$$$)^{(e*PrivS+y)}$$]

经验证可知UK=SK,实现了密钥交换