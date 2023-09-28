from pathlib import Path
from llama_index import VectorStoreIndex, SimpleDirectoryReader
from llama_index import download_loader
import openai
import pandas as pd

 
class property_loop():

    def read_data(self):
        try:
            holdings_data = "https://raw.githubusercontent.com/Praveen3ravi/CHATBOT/main/holdings.csv"
            trades_data = "https://raw.githubusercontent.com/Praveen3ravi/CHATBOT/main/trades.csv"
        
            holdings_df = pd.read_csv(holdings_data)
            trade_df = pd.read_csv(trades_data)

            # 3 Date fields:
            final_df = holdings_df.merge(trade_df, on = "SecurityId", how="inner")
            final_df['AsOfDate'] = pd.to_datetime(final_df['AsOfDate'], format='%d-%m-%Y')
            final_df['OpenDate'] = pd.to_datetime(final_df['OpenDate'], format='%d-%m-%Y')
            final_df['CloseDate'] = pd.to_datetime(final_df['CloseDate'], format='%d-%m-%Y')

            # Since all the column name are in Pascal case i have created in same format:
            final_df['OpenYear'] = final_df['OpenDate'].dt.year

            # Droping columns which make no sense and which can possibly impact the context of the data:
            final_df = final_df.drop('TradeDate', axis=1)
            final_df = final_df.drop('SettleDate', axis=1)


            # 22 Categorical Variables and 30 numberical variables: 
            final_df = final_df.drop_duplicates()
            final_df.to_csv("data.csv",index=False)
        
        except Exception as e:
            print(f"""There is some issue while reading the data.
Error: {e}""")             

        
    def bot_response(self, key, query):
        self.read_data()

        openai.api_key = key
        # os.environ["OPENAI_API_KEY"] = ""
        SimpleCSVReader = download_loader("SimpleCSVReader")
        loader = SimpleCSVReader(encoding="utf-8")
        
        self.script_dir = str(Path( __file__ ).parent.absolute())
        data =  self.script_dir +"/"+'data.csv'
        data = data.replace("\\", "/")
        doc = loader.load_data(file=data)

        index = VectorStoreIndex.from_documents(doc)
        query_engine = index.as_query_engine()
         
        for i in query:
            response = query_engine.query(i)
            print(response)