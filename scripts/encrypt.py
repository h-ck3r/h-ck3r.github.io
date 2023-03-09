from sys import argv
import os


# Nice one liner, it's so unclean, yet so fun.
password: str = argv[1] if len(argv) >= 2 else exit()

os.system("git clone https://github.com/h-ck3r/website_source.git")

for root, dirs, files in os.walk("./website_source/build"):
    for name in dirs:
        if "git" not in name:
            path: str = os.path.join(root, name)
            os.system(f"mkdir -p {path.replace('website_source/build', 'docs')}")
        
    for name in files:
        file_extension: str = name.split(".")[-1]

        if file_extension == "html" or file_extension == "css":
            path: str = os.path.join(root, name)
            os.system(f"npx pagecrypt {path} {path.replace('website_source/build', 'docs')} {password}")

os.system("rm -rf website_source")
