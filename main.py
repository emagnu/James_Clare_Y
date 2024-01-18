import os

path_: str = "/home/manny/dev/py/os/James_Clare_Y"


# files_dirs = os.listdir(path_)
# print(files_dirs)

# for f in os.listdir(path_):
#     print(f)

# for f in os.listdir(path_):
#     if f.endswith(".txt"):
#         # print(f)
#         print(f" - {f} is a text file!")


# txt_files: list[str] = [f for f in os.listdir(path_) if f.endswith(".txt")]
# print(f"This are the text files: {txt_files}")


# t_string: str = "text_string"
# print(os.path.join(path_, t_string))

txt_files: list[str] = [
    os.path.join(path_, f) for f in os.listdir(path_) if f.endswith(".txt")
]
print(txt_files)
