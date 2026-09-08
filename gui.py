import tkinter as tk
from translate import translate

window = tk.Tk()

window.title("AI 翻译器")
window.geometry("600x500")

source_label = tk.Label(window,text="请输入翻译内容")
source_label.pack()

source_text = tk.Text(window, height=8, width=60)
source_text.pack()

result_label = tk.Label(window, text="翻译结果：")
result_label.pack()

result_text = tk.Text(window, height=8, width=60)
result_text.pack()


def do_translate():
    text = source_text.get("1.0", "end-1c")

    result = translate(
        text,
        "中文",
        "英语"
    )

    result_text.delete("1.0", "end")
    result_text.insert("1.0", result)
    

# 翻译按钮
translate_button = tk.Button(
    window,
    text="开始翻译",
    command=do_translate
)
translate_button.pack()

window.mainloop()