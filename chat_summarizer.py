from nltk.corpus import stopwords 


class AI_CLS:
    def __init__(self, chat_log):
        self.stop_words = set(stopwords.words('english'))
        self.chat_log = chat_log
        self.user_messages = []
        self.ai_messages = []
    
    def chat_log_parsing(self):
        user_messages, ai_messages = [], []
        try:
            with open(self.chat_log, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line.startswith('User:'):
                        self.user_messages.append(line[5:].strip())
                    elif line.startswith('AI:'):
                        self.ai_messages.append(line[3:].strip())
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            return 
    
    def count_messages(self):
        user_msg_count, ai_msg_count = len(self.user_messages), len(self.ai_messages)
        total_msg = user_msg_count + ai_msg_count
        print(f'Total number of conversation: {total_msg}')
        print(f"User's number of messages: {user_msg_count}")
        print(f"AI's number of messages: {user_msg_count}")
        return 
    
    

if __name__ == '__main__':
    chat_file = 'chat.txt' 
    aichat = AI_CLS(chat_file)
    aichat.chat_log_parsing()
    aichat.count_messages()
  
