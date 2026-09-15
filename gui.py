import tkinter as tk
from translate import TranslationError, translate
from  tkinter import ttk

window = tk.Tk()

window.title("AI 翻译器")
window.geometry("600x500")
# 源语言
source_label = tk.Label(window, text="源语言：")
source_label.pack()


source_language = ttk.Combobox(
    window,
    values=["中文", "英语", "日语", "韩语"],
    state="readonly"
)
source_language.set("中文")
source_language.pack()
# 输入内容
source_label = tk.Label(window,text="请输入翻译内容")
source_label.pack()

source_text = tk.Text(window, height=8, width=60)
source_text.pack()
# 目标语言
target_label = tk.Label(window, text="目标语言：")
target_label.pack()

target_language = ttk.Combobox(
    window,
    values=["中文", "英语", "日语", "韩语"],
    state="readonly"
)
target_language.set("英语")
target_language.pack()
# 翻译结果
result_label = tk.Label(window, text="翻译结果：")
result_label.pack()

result_text = tk.Text(window, height=8, width=60)
result_text.pack()


def do_translate():
    text = source_text.get("1.0", "end-1c")

    try:
        result = translate(
            text,
            source_language.get(),
            target_language.get(),
        )
    except TranslationError as exc:
        result = f"翻译失败：{exc}"

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
