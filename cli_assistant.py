from gemini_client import *

def main():
    player_input = input("Input: ")
    if player_input == "exit":
       print("Goodbye!")
       return
    client = GeminiClient()
    print(client.generate_response(player_input))

if __name__ == "__main__":
  main()