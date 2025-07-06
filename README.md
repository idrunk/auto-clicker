# 自动点击工具

## 工具介绍

本工具是一个使用 Python 编写的自动点击工具。它可以模拟鼠标点击，并具有以下功能：

-   **可配置的点击速度：** 用户可以在 `config.toml` 文件中配置点击速度的范围。
-   **可配置的点击偏移量：** 用户可以在 `config.toml` 文件中配置点击位置的偏移量。
-   **可配置的快捷键：** 用户可以在 `config.toml` 文件中配置启动、暂停和停止工具的快捷键。
-   **点击位置选择：** 通过左击鼠标来选择需要连点的位置。

## 安装方式

1.  安装 Python 3.6 或更高版本。
2.  使用 pip 安装依赖项：

    ```bash
    pip install -r requirements.txt
    ```

    请确保安装 `requirements.txt` 文件中列出的所有依赖项。

## 使用方式

1.  修改 `config.toml` 文件以配置工具的参数，例如点击速度、偏移量和快捷键。
2.  运行 `tool.py` 文件：

    ```bash
    python tool.py
    ```

3.  使用快捷键启动、暂停和停止工具。默认快捷键如下：

    -   启动/停止：`Ctrl+Shift+Alt+W`
    -   暂停/恢复：`Ctrl+Shift+Alt+Q`
    -   退出：`Ctrl+Shift+Alt+E`

4.  左击鼠标来选择需要连点的位置。

## 配置文件说明 (config.toml)

```toml
speed = [0.7, 1.2]  # 点击速度范围 (秒)
offset = 4          # 点击位置偏移量 (像素)

[shortcut]
pause = "ctrl+shift+alt+q"  # 暂停/恢复 快捷键
swicth = "ctrl+shift+alt+w" # 启动/停止 快捷键
exit = "ctrl+shift+alt+e"   # 退出 快捷键
```

请根据您的需求修改配置文件。