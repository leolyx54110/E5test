import time

def focus_timer(minutes):
    print(f"开始专注 {minutes} 分钟.")
    for minute in range(minutes):
        for second in range(60):
            time_left = (minutes - (minute + 1)) * 60 + (60 - (second + 1))
            print(f"剩余时间：{time_left // 60:02d}:{time_left % 60:02d}", end="\r")
            time.sleep(1)
        print()
    print("专注时间结束！")

focus_duration = int(input("请输入专注的分钟数: "))
focus_timer(focus_duration)
