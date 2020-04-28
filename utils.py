def obfuscate_string(value):
    return ''.join(['&#{0:s};'.format(str(ord(char))) for char in value])