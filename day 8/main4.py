def decrypt(plain_text, shift_ampubt):
  encrypted_text =  []
  for letter in plain_text:
    
    index = alphabet.index(letter)
    # print (index)
    index_new = index - shift
    # print (index_new)
    # index = 0
    # print (alphabet[index_new])
    if index_new > 25:
      index_new = index_new + 25
    encrypted_text += alphabet[index_new]
  print ("".join(encrypted_text))


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
decrypt (text, shift)

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
