
import textwrap 
  
value = """Thigdfkjlrjljlewrnlggwlngr
wggwwgrgwrwgnocontent."""
  
# Wrap this text. 
wrapper = textwrap.TextWrapper(width=5) 
  
word_list = wrapper.wrap(text=value) 
  
# Print each line. 
for element in word_list: 
    print(element) 
