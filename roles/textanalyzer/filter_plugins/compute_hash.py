# python3.9 compute_hash.py

from ansible.errors import AnsibleError
import zlib
import hashlib


def compute_hash(_text, _hash):
    if _hash == "CRC32":
        return hex(zlib.crc32(bytes(_text, encoding='utf-8')) & 0xffffffff)
    if _hash == "MD5":
        return hashlib.md5(bytes(_text, encoding='utf-8')).hexdigest()
    if _hash == "SHA512":
        return hashlib.sha512(bytes(_text, encoding='utf-8')).hexdigest()
       
class FilterModule(object):
    ''' Ansible jinja2 filters '''

    def filters(self):
        return {
            'compute_hash': compute_hash,
        }


if __name__== "__main__":
   print ("CRC32 example  : " + compute_hash("AAA BBB", "CRC32") )
   print ("MD5 example    : " + compute_hash("AAA BBB", "MD5") )
   print ("SHA512 example : " + compute_hash("AAA BBB", "SHA512") )
