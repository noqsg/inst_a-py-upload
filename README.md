# Instagram Photo Uploader Selenium (For Windows)
## Installation
* Download [Google Chrome](https://google.com/chrome) and install
+ After run these commands in the Windows Command Prompt
  + ```git clone https://github.com/imnotyours/instagram-uploader-selenium``` 
  + ```cd instagram-uploader-selenium```
  + ```pip install -r requirements.txt```
## Usage
```shell
ig-ul-sl.py -u username -p password -i /path/to/the/image.jpg -c 'Caption Here'
```
```
Usage: ig-ul-sl.py [OPTIONS]

Options:
  -u, --username TEXT    The username to your Instagram account.  [required]
  -p, --password TEXT    The password to your Instagram account.  [required]
  -i, --image-path TEXT  The path to the image you want to upload. Until now
                         unly work if its going from the path you run the
                         script from  [required]
  -c, --caption TEXT     The caption for underneath your image.
  --help                 Show this message and exit.
  ```
