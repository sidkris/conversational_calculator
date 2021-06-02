from chatterbot import ChatBot

bot = ChatBot(name= "Conversational Calculator (CC)", read_only = True,
logic_adapters = ["chatterbot.logic.MathematicalEvaluation"],
storage_adapter = "chatterbot.storage.SQLStorageAdapter")

print("please enter the math opertaion in words or numbers (like you normally would) that you would like me to perform!\n")

while(True):
  user_input = input("You : ")

  if user_input.lower() == "quit":
    print("Goodbye.")
    break
  
  else:
    try:
      response = bot.get_response(user_input)
      print("CC : {}".format(response))
    except:
      print("Invalid input. Please try again.")


