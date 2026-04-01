# ahut-ele-astrbot

安徽工业大学电费查询 AstrBot 插件

> [!NOTE]
> 这是一个 [AstrBot](https://github.com/AstrBotDevs/AstrBot) 插件，用于查询安徽工业大学宿舍电费。
>
> [AstrBot](https://github.com/AstrBotDevs/AstrBot) 是一个支持多平台的智能对话机器人框架。

## 功能特性

- **管理员登录设置**: 管理员可以配置缴费系统登录信息
- **用户宿舍设置**: 群内用户可以设置自己的宿舍信息
- **电费查询**: 查询所有已配置宿舍的电费余额

## 安装依赖

本插件需要 RSA 加密库：

```bash
pip install cryptography
```

## 使用方法

### 管理员命令

| 命令 | 说明 |
|------|------|
| `/ele_login` | 设置缴费系统登录（学号和密码） |
| `/ele_logout` | 清除登录信息 |

### 用户命令

| 命令 | 说明 |
|------|------|
| `/ele_set` | 设置宿舍信息 |
| `/ele_my` | 查看我的宿舍设置 |
| `/ele_del` | 删除我的宿舍设置 |

### 查询命令

| 命令 | 说明 |
|------|------|
| `/ele` | 查询所有已设置宿舍的电费 |
| `/ele_one <房间号>` | 查询指定房间电费 |
| `/ele_status` | 查看插件状态 |
| `/ele_help` | 查看帮助信息 |

## 设置宿舍信息格式

设置宿舍时，请按以下格式输入：

```
校区 楼栋ID 栋名称 房间号
```

例如：
```
翡翠湖 1 1栋 101
```

注意：楼栋ID需要从缴费系统查询获取。

## 配置项

在 AstrBot 管理面板中可以配置：

- `admin_users`: 管理员用户ID列表（QQ号），留空则所有人都可以管理

## 相关链接

- [AstrBot Repo](https://github.com/AstrBotDevs/AstrBot)
- [AstrBot Plugin Development Docs (Chinese)](https://docs.astrbot.app/dev/star/plugin-new.html)
- [AstrBot Plugin Development Docs (English)](https://docs.astrbot.app/en/dev/star/plugin-new.html)
