from gemini_client import *

def main():
    player_input = input("Input: ")
    client = GeminiClient()
    while player_input != "exit":
        print(client.generate_response(player_input))
        player_input = input("Input: ")
    print("Goodbye!")

if __name__ == "__main__":
  main()