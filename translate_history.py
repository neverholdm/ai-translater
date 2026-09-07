def save_translate_history(source_language, target_language, text, result):
    with open("translation_history.txt", "a", encoding="utf-8") as f:
            f.write(f"""
源语言：{source_language}
目标语言：{target_language}
原文：{text}
译文：{result}
------------------------------
    """)

def show_translate_history ():
    try :
        with open("translation_history.txt", "r", encoding="utf-8") as f :
            content=f.read()
            print(content)
    except Exception :
        print("暂无翻译历史")
if __name__ == "__main__":
    show_translate_history()