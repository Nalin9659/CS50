
def convert(text):
   return text.replace( ":)", "🙂").replace(":(", "🙁")

def main():

   user_input = input("Enter the unicode: ")
   print(convert(user_input))

if __name__ == "__main__":   
 main()