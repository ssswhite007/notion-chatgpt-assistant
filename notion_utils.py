from notion_client import Client  
import os

class NotionAPI:  
    def __init__(self, api_key):  
        self.notion = Client(auth=api_key)  

    def fetch_database_data(self, database_id):  
        """  
        Fetch all rows (pages) from a Notion database.  
        """  

        response = self.notion.databases.query(database_id=database_id)  
        pages = response.get('results', [])  
        data = []  
        for page in pages:  
            page_content = self.extract_page_content(page)  
            data.append({  
                "id": page["id"],  
                "name": page["properties"]["Name"]["title"][0]["plain_text"],
                "tech": page["properties"]["tech"]["rich_text"][0]["plain_text"] if page["properties"]["tech"]["rich_text"] else "",
                "experience": page["properties"]["experience"]["rich_text"][0]["plain_text"] if page["properties"]["experience"]["rich_text"] else "0",
                "content": page_content,  
            })  

        return data 

    def extract_page_content(self, page):  
        """  
        Extract content from a Notion page.  
        Modify this to suit your database structure.  
        """  
        content = []  
        blocks_response = self.notion.blocks.children.list(block_id=page["id"])  
        blocks = blocks_response.get('results', [])  
        for block in blocks:  
            if block['type'] == 'paragraph':  
                content.append(block[block['type']]['text'][0]['plain_text'])  
        return "\n".join(content)  