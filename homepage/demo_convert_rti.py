import os
import subprocess
import shutil
import zipfile


"""
A demo of convert the rti file(.ptm,.hsh)
to a zip, each of the files is saved 
locally on my computer, it is just a pipeline
"""
def convert_and_compress(input_file, exe_path, output_folder, zip_file):
    # 调用 .exe 文件进行转换
    try:
        subprocess.run([exe_path, input_file, output_folder], check=True)
        print(f"Conversion successful: {input_file} -> {output_folder}")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")
        return

    # 压缩生成的文件夹为 ZIP 文件
    zipf = zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(output_folder):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, start=output_folder)
            zipf.write(file_path, arcname)
    zipf.close()
    print(f"Folder compressed to ZIP file: {zip_file}")

# 示例用法
input_file = r'D:\UOA\project\Izbet_Sarteh.ptm'
exe_path = r'C:\Users\luo\Downloads\RelightLab2024.01-windows (1)\relight-cli.exe'
output_folder = r'D:\UOA\project\output'
zip_file = r'D:\UOA\project\output\output.zip'

convert_and_compress(input_file, exe_path, output_folder, zip_file)