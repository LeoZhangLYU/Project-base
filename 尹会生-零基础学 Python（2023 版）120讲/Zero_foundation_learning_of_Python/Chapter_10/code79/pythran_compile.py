import os
import sys
import subprocess

# 强制设置标准输出和标准错误流为 UTF-8 编码
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')


def compile_with_pythran(file_path):
    # 使用绝对路径并确保路径中的所有字符被正确处理
    abs_file_path = os.path.abspath(file_path)

    # 检查文件是否存在
    if os.path.exists(abs_file_path):
        print(f"Compiling {abs_file_path} with Pythran...")

        # 使用 Pythran 的绝对路径
        pythran_path = r"C:\CodeEnvironment\Python\Python312\Scripts\pythran.exe"  # 替换为实际路径

        # 调用 Pythran 编译，确保 UTF-8 处理
        try:
            result = subprocess.run([pythran_path, abs_file_path], capture_output=True, text=True, encoding='utf-8')

            # 输出结果
            if result.returncode == 0:
                print("Compilation successful.")
            else:
                print("Compilation failed.")
                print(result.stderr.encode('utf-8').decode('utf-8'))
        except FileNotFoundError as e:
            print(f"Error: {e}")
    else:
        print(f"Error: File '{abs_file_path}' does not exist.")


if __name__ == "__main__":
    # 从命令行参数中获取文件路径
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        compile_with_pythran(file_path)
    else:
        print("No file path provided.")
