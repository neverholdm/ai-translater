import os
from logger import logger
from openai import OpenAI 
from dotenv import load_dotenv
load_dotenv()
api_key = os.environ.get("DEEPSEEK_API_KEY")
def translate (text,source_language,target_language):

    logger.info("开始翻译")

    try :
        client = OpenAI(
            api_key = api_key ,
            base_url="https://api.deepseek.com")
        response = client.chat.completions.create(
            model="deepseek-v4-pro",
            messages=[
                {"role": "system", "content": "你是一个专业的翻译，只输出结果，不要解释"},
                {"role": "user", "content": f"请将下面内容从{source_language}翻译成{target_language}:\n{text}"},
            ],
            stream=False,
        )
        logger.info("翻译成功")
        
        return(response.choices[0].message.content)

    except Exception as e :
        logger.error(f"翻译失败:{e}")
        return f"""翻译失败
"""

if __name__ =="__main__":
    pass