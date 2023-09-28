Create a chatbot trained on the two files below. The bot should be able to answer questions related to the data from the provided files. If the answer is not found in the given files then it should respond with “Sorry can not find the answer’ instead of getting an answer from the internet.

Example Questions
   * Total number of holdings or trades for a given fund?
   * Which funds performed better depending on the yearly Profit and Loss of that fund?
Feel free to use any LLM. Share your notebook within 3 days.

If you have any doubts then feel free to ask them over email.

======================================================================
**STEP 1:**
Download python. 
RUN: ".\venv\Scripts\Activate.ps1" to activate the virtual environment.
RUN: "pip install -r requirements.txt" to download all libraries from requirements.txt

**STEP 2:**
RUN:  "uvicorn main:app --reload --host 0.0.0.0 --port 8000"

**STEP 3:**
API params: 
{
  "ChatGPT_key": "", #provide the key here
  "query": ["What is the SecurityTypeName for the SecName 'EJ0445951'?", 
             "What is the StartFXRate on OpenDate 04-03-2020?",
             "List all unique TradeTypeName?",
             "Which type of TradeTypeName has more Qty?",
             "How many numbers of unique types of 'SecurityType'?",
             "What is the StartPrice on '13-01-2023'?",
             "What is the highest TotalCash for TradeTypeName Buy?",
             "Total number of holdings or trades for a given fund?",
             "Which OpenYear has the highest TotalCash?"]
}
