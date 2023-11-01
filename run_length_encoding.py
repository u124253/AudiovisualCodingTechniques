def encode(message):
    """
    Function to se run length encoding to compress a message

    :param message:
    :return encoded_message:
    """
    encoded_message = ""
    i = 0

    while i <= len(message) - 1:
        count = 1
        ch = message[i]
        j = i
        while j < len(message) - 1:
            if message[j] == message[j + 1]:
                count = count + 1
                j = j + 1
            else:
                break
        encoded_message = encoded_message + str(count) + ch
        i = j + 1
    return encoded_message


run_length_encoded_message = encode("ABBBBCCCCCCCCAB")
print(run_length_encoded_message)
