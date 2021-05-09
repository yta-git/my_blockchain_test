import hashlib
text = '{"difficulty":4,"index":98,"nonce":45758,"prev_block":"00008f0558bf9532ba64824758c6a4fb23eeed4d5a0db87720ae2ee1540d0880","time":1611577475,"tx":"BuMkCzj0p9s88IAW/Fr1nNkoonoEbbNYOPyiafMQ5t0Fx7Xa5Fs8bx7ahMQOuvPItPhd7Pwz9C73ag5lX6EQWg==;rJYWk8MY68HFEebNYfp4mplPeIi1gsVIS+L9dlodNQC0RHD7zS0fV9FGBY2OSJTiL/LXWFrb6aDsEmZSVAynxQ==;63;8hID2GqpHH+Vl9ybohZJUyiriBH5j2Z7ApeMO0al8WOPxUfPRqoSCv7tEMxT2dzXycw0WsHjscqIE3NgLqW5Bw=="}'

hash=hashlib.sha256(text.encode()).hexdigest()
hash=hashlib.sha256(hash.encode()).hexdigest()

print(text)
print(hash)