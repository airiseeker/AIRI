from airi.stt.listener import Listener

listener = Listener()

text = listener.listen()

print()
print("Papah berkata:")
print(text)