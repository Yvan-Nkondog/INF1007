
# Generate the following names from the following prefixes and suffix :
# Jack, Kack, Lack, Mack, Nack, Oack, Pack and Qack. 
# Prefixes = 'JKLMNOP' et suffix = 'ack’

def generate_name_prefix_suffix(prefixes : str, suffix: str) -> list[str]:
    result = []
    for character in prefixes:
        result.append(character + suffix)
    return result


if __name__ == "__main__":
    prefixes = 'JKLMNOP'
    suffix = 'ack'
    print(generate_name_prefix_suffix(prefixes, suffix))