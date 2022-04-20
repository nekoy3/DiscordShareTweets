import asyncio
import time

from concurrent.futures import ProcessPoolExecutor

def func(sec: int):
    print("非同期の処理")
    time.sleep(sec)
    print("非同期の処理おわり")

def func_not(sec):
    print("すし")
    time.sleep(sec)
    print("たべたい")

def main():
    executor = ProcessPoolExecutor(max_workers=3)

    for i in range(10):
        print(i)
        if i == 3:
            asyncio.new_event_loop().run_in_executor(None, func, 3)
        if i == 5:
            asyncio.new_event_loop().run_in_executor(None, func_not(3), None)
        if i == 7:
            asyncio.new_event_loop().run_in_executor(executor, func, 3)
        time.sleep(1)

#run_in_executerは非同期処理を実行するためのメソッドだが、ロックがかかってしまえば処理はブロックされ同期処理的な動作になってしまう。
#IOバウンドというより、CPUバウンドな処理であったり、GIL(グローバルインタプリタロック、スレッドセーフ（安全にスレッドを両立させる書き方)が出来ていない場合に
#他のスレッドと共有してしまうことを防ぐための排他ロック）がかかるようなコードの場合にロックがかけられてしまう。

#run_in_executerではThreadPoolExecutorを使っているが、ProcessPoolExecutorを使うことでスレッドでは無くプロセスで処理を行うことができる。
#プロセスで処理すれば、別プロセスで動作するためGILがかからない。他に影響を与えないため、非同期的に処理することが出来る、らしい。

if __name__ == "__main__":
    main()