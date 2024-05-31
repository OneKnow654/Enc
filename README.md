this program is used to encrpyt  the files and  decrpyt files using key *(like password)* 
> note : if the wrong key is passed to decrpty then it will decrpty but unable to read the data in short unable to access the file contain



# Install
---

```bash
git clone https://github.com/OneKnow654/Enc.git
cd Enc
pip install -r requirements.txt
python  enc.py -h
```

### or

#### run the setup file to use directly by terminal
```bash
sudo chmod +x setup.sh
./setup.sh

```

---

---
# Usage
to use the script

#### Encrypt a single file with a direct key
```bash
python enc.py -e -k your_key test.txt
```
#### Encrypt a single file with a key file
```bash
python enc.py -e -K keyfile.txt test.txt
```


#### Encrypt multiple files with a direct key
```bash
python enc.py -e -k your_key test1.txt test2.txt
```

#### Encrypt multiple files with a key file
```bash
python enc.py -e -K keyfile.txt test1.txt test2.txt
```

#### Decrypt a single file with a direct key
```bash
python enc.py -d -k your_key test.txt.enc
```

#### Decrypt a single file with a key file
```bash
python enc.py -d -K keyfile.txt test.txt.enc
```

#### Generate and print a key
```bash
python enc.py -g
```

#### Generate and save a key
```bash
python enc.py -gs
``````
### using build version then 
you can find  - >  [ here ](https://github.com/OneKnow654/Enc/releases/download/Oneknown654/enc)


# Encrypt a single file with a direct key
```bash
enc.py -e -k your_key test.txt
```

#### Encrypt a single file with a key file
```bash
enc.py -e -K keyfile.txt test.txt
```

#### Encrypt multiple files with a direct key
```bash
enc.py -e -k your_key test1.txt test2.txt
```

#### Encrypt multiple files with a key file
```bash
enc.py -e -K keyfile.txt test1.txt test2.txt
```

#### Decrypt a single file with a direct key
```bash
enc.py -d -k your_key test.txt.enc
```

#### Decrypt a single file with a key file
```bash
enc.py -d -K keyfile.txt test.txt.enc
```

#### Generate and print a key
```bash
enc.py -g
```

#### Generate and save a key
```bash
python enc.py -gs
```
