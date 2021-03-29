# plshelp
created with <3 by zlataovce


plshelp is an API (and a [website](https://plshelp.mkdev.ml)) for parsing Minecraft server logs which extracts useful information, e.g plugins list, plugin/server errors, server version / software, and more! It even has the ability to share your parsed logs with people too! 

## Usage

```
Copy your latest.log file in your minecraft server files / or / upload them to paste.gg

Click [Parse] to parse!

With a simple UI, you can view all of your info easily and share it too!
```

## Installation / Self Hosting

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required dependencies.

```bash
pip install -r requirements.txt
```
Modify the domain in the `config.ini` file to your own domain.
```
[FLASK]
Domain: https://plshelp.mkdev.ml #Your domain here
```
Make sure you are running Python 3.
```
python ––version
```
Create a `.env` file that includes:
```
PASTEBIN_API_KEY=apikeyfrompastebin
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[GPL 3.0](https://choosealicense.com/licenses/gpl-3.0/)

(readme by Mad <3 uwu)
