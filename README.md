# CONTROLFAN

Controlfan is a simple python script designed to control any fan wired to parallel port in your device such as thin clients or even desktop PCs.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies.

```bash
pip install pyparallel pathlib time
```

## Usage
There are few lines allowing You to play with the config:

`ON_THRESHOLD`  - Temperature at which the fan starts to spin.

`OFF_THRESHOLD` - Temperature at which the fan stops spinning.

`SLEEP_INTERVAL` - Time between updates.

The script can be started by issuing:
```bash
python3 controlfan.py
```
or
```bash
python3 controlfan.py &
```
to run it in background.

This command might need to use sudo in order to gain access to `/dev/parport*`.
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to check the code for any bugs or errors

## License
[MIT](https://choosealicense.com/licenses/mit/)
