# coding: utf-8
import datetime
import hashlib
import sys

import ntplib


def get_webserver_time() -> datetime.date | None:
    """获取网络时间，如果网络异常则返回None"""
    ntp_servers = [
        "ntp.aliyun.com",
        "time.windows.com",
        "pool.ntp.org",
        "time.nist.gov",
    ]
    for server in ntp_servers:
        for retry in range(3):
            try:
                client = ntplib.NTPClient()
                response = client.request(server, version=3, timeout=3)
                ntp_time = datetime.datetime.fromtimestamp(response.tx_time)
                print(f"成功从 {server} 获取NTP时间: {ntp_time.date()}")
                return ntp_time.date()
            except Exception as exc:
                print(f"第{retry + 1}次从 {server} 获取NTP时间失败: {exc}")
                if retry == 2:
                    print(f"从 {server} 获取时间的所有重试都失败")
    print("所有NTP服务器都无法获取时间")
    return None


def get_month_start_str(web_date: datetime.date) -> str:
    """返回当前月份第一天的标准字符串。"""
    return web_date.replace(day=1).strftime("%Y-%m-%d")


def generate_activation_code(secret_key: str, web_date: datetime.date) -> str:
    """根据网络时间和密匙生成当月激活码。"""
    month_start = get_month_start_str(web_date)
    raw = f"{month_start}|{secret_key}"
    return hashlib.sha256(raw.encode("utf-8")).hexdigest().upper()[:16]


def main() -> int:
    secret_key = input("请输入密匙: ").strip()
    if not secret_key:
        print("错误：密匙不能为空。")
        return 1

    web_date = get_webserver_time()
    if web_date is None:
        print("错误：无法获取网络时间，未生成激活码。")
        return 1

    activation_code = generate_activation_code(secret_key, web_date)
    print(f"网络日期: {web_date.strftime('%Y-%m-%d')}")
    print(f"月初基准: {get_month_start_str(web_date)}")
    print(f"当月激活码: {activation_code}")
    x = input("按回车键退出...")
    return 0


if __name__ == "__main__":
    sys.exit(main())
