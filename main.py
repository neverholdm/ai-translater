from translate import TranslationError, translate
from translate_history import show_translate_history,save_translate_history

def once_translate ():
    source_language=input("请输入源语言\n")
    target_language=input("请输入目标语言\n")
    while True:
        text=input("请输入翻译内容\n")
        if text :
            break
        print("内容不能为空")
    try:
        result = translate(
            text,
            source_language,
            target_language,
        )
    except TranslationError as exc:
        print(f"翻译失败：{exc}")
        return

    print(f"翻译结果:\n{result}")

    save_translate_history(
        source_language,
        target_language,
        text,
        result,
)

def main () :
    while True :
        a=input("""
========ai翻译器========       

1. 开始翻译
2. 查看历史记录
3. 退出

"""
)

        if a=="1" :
            once_translate ()       
            
        elif a=="2" :
            show_translate_history ()
        elif a=="3" :
            break
        else :
            print("请输入1-3之间的数字")
if __name__ =="__main__" :
    main ()