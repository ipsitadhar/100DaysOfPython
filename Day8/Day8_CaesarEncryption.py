from Day8.art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
should_continue=True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  #What happens if the user enters a number/symbol/space?
  #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
  def caesar(text,shift,direction):
    new_text=""
    for letter in text:
      
      if letter in alphabet :
        position=alphabet.index(letter)
        if direction=="encode":
          position=position+shift
          if position>25:
            position=position-26
        if direction=="decode":
          position=position-shift
          if position<0:
            position=position+26
        new_text=new_text+alphabet[position]
      else:
        new_text=new_text+letter

    print(f"The {direction}d text is {new_text}")
    option=input("Type 'yes' if you want to go again. Otherwise type 'no'")
    if option=='no':
     should_continue=False
     print("GoodBye")
    
      
  #Can you figure out a way to ask the user if they want to restart the cipher program?
  #e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
  caesar(text,shift,direction)
