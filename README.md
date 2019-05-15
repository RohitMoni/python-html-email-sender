# HTML Email Sender

Simple script to allow for easy e-mail sending.
Includes html email support with html templates + data passed in to replace data in the template.

## Requirements

Python 3 standard lib

## Usage

Set up the config file. Can either edit the `DEFAULT` section or add a section of your own.

Run the python script:

```
python main.py --options  
```

### Options

`-c` `--config` :- Specify the config section to use. Note that `DEFAULT` will still be used for any keys that aren't specified

### Examples

`python main.py --config TEST`