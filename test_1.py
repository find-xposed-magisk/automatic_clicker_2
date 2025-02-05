import time


def get_current_date_time():
    # 获取当前时间
    local_time = time.localtime(time.time())
    # 格式化日期和时间
    formatted_date_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    return formatted_date_time


# 调用函数并打印结果
print(f"当前日期和时间: {get_current_date_time()}")
