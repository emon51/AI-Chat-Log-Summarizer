
from nltk.corpus import stopwords 
import heapq 


class AI_CLS:
    def __init__(self, chat_log):
        self.stop_words = set(stopwords.words('english'))
        self.chat_log = chat_log
        self.user_messages = []
        self.ai_messages = []
        self.non_stop_words_map = {} #Store data as key a value pair (word, frequency)
        self.non_stop_words_max_heap = [] #Store data as a pair -> (frequency, word)   

        self.chat_log_parsing()
        self._get_map_and_heap()

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
        total_msg_count = user_msg_count + ai_msg_count
        return [user_msg_count, ai_msg_count, total_msg_count]


    def _get_map_and_heap(self):
        all_messages = self.user_messages + self.ai_messages #Concatenate two list of messages.
        for line in all_messages:
            line = line.lower()
            for word in line.split():
                new_word = [ch for ch in word if ch.isalpha()]
                new_word = ''.join(new_word)
                if new_word not in self.stop_words: 
                    self.non_stop_words_map[new_word] = self.non_stop_words_map.get(new_word, 0) + 1
                    
        for word, freq in self.non_stop_words_map.items():
            heapq.heappush(self.non_stop_words_max_heap, [-freq, word])
        
    
    def get_most_used_words(self):
        five_most_used_words = []
        count = 5
        temp_arr = []
        while self.non_stop_words_map and count:
            freq, word = heapq.heappop(self.non_stop_words_max_heap)
            temp_arr.append([freq, word])
            five_most_used_words.append(word)
            count -= 1
        
        #push back all popped elements again into the heap.
        while temp_arr:
            freq, word = temp_arr.pop()
            heapq.heappush(self.non_stop_words_max_heap, [freq, word])

        return five_most_used_words
    
    
    def get_summary(self):
        user_msg_count, ai_msg_count, total_msg_count = self.count_messages()
        total_message_exchange = total_msg_count
        nature_keyword = self.non_stop_words_max_heap[0][1].capitalize()
        most_common_keywords = self.get_most_used_words()

        print('Summary: ')
        print(f"- The conversation had {total_message_exchange} exchanges; User: {user_msg_count} and AI: {ai_msg_count}.")
        print(f"- The user mainly asked about {nature_keyword}.")
        print(f"- The most common used keywords: {', '.join(most_common_keywords)}.")
    
                    





if __name__ == '__main__':
    chat_file = 'chat.txt' 
    chat = AI_CLS(chat_file)
    chat.get_summary()
  
