def chess(token, value):
    # Assuming chess is a dictionary
    chess_dict = {
        "#b+-": "value1",
        "b-#t": "value2",
        "#c+2-p": "value3",
        # Add other token-value pairs here
    }

    if token in chess_dict:
        return chess_dict[token]
    else:
        return value

# Example usage
token = "#b+-"
value = "default_value"
result = chess(token, value)
print(result)  # This will print "value1" if "#b+-" is in the dictionary
