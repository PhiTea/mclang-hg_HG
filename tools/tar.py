import os, zipfile, re, fire # Fire install: pip install fire

def compress(srcpath: str, savepath: str = "./", ignore: tuple = ()):
    if not os.path.exists(srcpath) or not os.path.exists(savepath):
        raise ValueError("Invaild srcpath or savepath.")
    f = zipfile.ZipFile(savepath + ".zip", 'w',zipfile.ZIP_DEFLATED)
    for file in os.listdir(srcpath):
        if file in ignore:
            print("! 文件在ignore列表里，跳过")
        else:
            if os.path.isdir(file):
                    while True
            print("- 成功添加 {} 文件到压缩文件中".format(file))
    f.close()
    print("- 成功压缩文件。")

fire.Fire()
