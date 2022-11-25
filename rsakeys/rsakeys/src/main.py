from Crypto.PublicKey import RSA

def is_valid_file(pemFile):
    file_lines = pemFile.split('\n')
    print(file_lines)
    if file_lines[0] == '-----BEGIN PUBLIC KEY-----' and file_lines[-1] == '-----END PUBLIC KEY-----':
        return True, 'public'
    elif file_lines[0] == '-----BEGIN PRIVATE KEY-----' and file_lines[-1] == '-----END PRIVATE KEY-----':
        return True, 'private'
    else :
        return False, None

def get_publicKeyInfo(pem):
    pubkey = RSA.importKey(pem)
    info = {
        "modulus": pubkey.n,
        "exponent": pubkey.e
    }
    return info

def get_privateKeyInfo(pem):
    privKey = RSA.importKey(pem)
    info = {
        "modulus": privKey.n,
        "publicExponent": privKey.e,
        "privateExponent": privKey.d,
        "prime1": privKey.p,
        "prime2": privKey.q,
        "exponent1": privKey._dp,
        "exponent2": privKey._dq,
        "coefficient": privKey.u
    }
    return info





#from cryptography.hazmat.backends import default_backend
#from cryptography.hazmat.primitives import serialization

#pubkey2 = serialization.load_pem_public_key(
#    key_encoded.encode('ascii'),
#    backend=default_backend()
#)

#print(pubkey2.public_numbers().n)
#print(pubkey2.public_numbers().e)