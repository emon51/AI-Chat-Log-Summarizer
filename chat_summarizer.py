from nltk.corpus import stopwords 


class AI_CLS:
    def __init__(self, chat_log):
        self.stop_words = set(stopwords.words('english'))
        self.chat_log = chat_log
    
    def parse_chatting(self):
        user_messages, ai_messages = [], []
        try:
            with open(self.chat_log, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line.startswith('User:'):
                        user_messages.append(line[5:].strip())
                    elif line.startswith('AI:'):
                        ai_messages.append(line[3:].strip())
            return [user_messages, ai_messages]
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            return 
    

if __name__ == '__main__':
    chat_file = 'chat.txt' 
    aichat = AI_CLS(chat_file)
    res = aichat.parse_chatting()
    print(res)
