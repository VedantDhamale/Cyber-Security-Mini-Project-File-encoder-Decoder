import base64

def encode_input(input_data):
    encoded = base64.b64encode(input_data)
    return encoded.decode('utf-8')

def encode_file(file_in):
    with open(file_in, 'rb') as f_in:
        encoded = base64.b64encode(f_in.read())
        return encoded.decode('utf-8')

def decode_input(input_data):
    decoded = base64.b64decode(input_data.encode('utf-8'))
    return decoded

def decode_file(file_in):
    with open(file_in, 'rb') as f_in:
        decoded = base64.b64decode(f_in.read())
        return decoded

def main():
    # Accept input from user
    print('\nType the number that corresponds with the option you want.\n\nOptions:\n\n1: to encode a file\n\n2: to decode a file\n\n')
    choice = input()
    
    if choice == '1':
        file_in = input('\nEnter the name/path of the file to encode: ')
        try:
            with open(file_in, 'rb') as f:
                pass
        except FileNotFoundError:
            print("\nError: File not found")
            return
        file_out = input('\nEnter the name of the output file: ')
        encoded = encode_file(file_in)
        with open(file_out, 'w') as f_out:
            f_out.write(encoded)
    
    elif choice == '2':
        file_in = input('\nEnter the name/path of the file to decode: ')
        try:
            with open(file_in, 'rb') as f:
                pass
        except FileNotFoundError:
            print("\nError: File not found")
            return
        file_out = input('\nEnter the name of the output file: ')
        with open(file_in, 'r') as f_in:
            encoded = f_in.read()
        decoded = decode_input(encoded)
        with open(file_out, 'wb') as f_out:
            f_out.write(decoded)
    
    else:
        print('\nInvalid choice. Please try again.')

if __name__ == '__main__':
    main()
