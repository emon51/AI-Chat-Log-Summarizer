from nltk.corpus import stopwords 
import heapq 


class AI_CLS:
    def __init__(self, chat_log):
        self.stop_words = set(stopwords.words('english'))
        self.chat_log = chat_log
        self.user_messages = []
        self.ai_messages = []
        self.non_stop_words_map = {} #Store data as key value pair (word, frequency)
        self.non_stop_words_max_heap = [] #Store data as (frequency, word)
    
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


    def _get_map_and_heap(self):
        all_messages = self.user_messages + self.ai_messages
        for line in all_messages:
            line = line.lower()
            for word in line.split():
                new_word = [ch for ch in word if ch.isalpha()]
                new_word = ''.join(new_word)
                #print(new_word)
                if new_word not in self.stop_words: 
                    self.non_stop_words_map[new_word] = self.non_stop_words_map.get(new_word, 0) + 1
        #print(self.non_stop_words_map)
        for word, freq in self.non_stop_words_map.items():
            heapq.heappush(self.non_stop_words_max_heap, [-freq, word])
        
    
    def get_common_used_words(self):
        self._get_map_and_heap()
        five_most_used_words = []
        count = 5
        while self.non_stop_words_map and count:
            _, word = heapq.heappop(self.non_stop_words_max_heap)
            five_most_used_words.append(word)
            count -= 1
        return five_most_used_words
    
                    




                    

    


if __name__ == '__main__':
    chat_file = 'chat.txt' 
    aichat = AI_CLS(chat_file)
    aichat.chat_log_parsing()
    #aichat.count_messages()
    print(aichat.get_common_used_words())
  
