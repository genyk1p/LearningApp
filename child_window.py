from tkinter import *
from tkinter.ttk import Combobox
from tkinter.scrolledtext import ScrolledText


class ChildWindow:

    def __init__(self, parent, article, width, height, title='MyWindow'):
        self.root = Toplevel(parent)
        self.root.title(title)
        self.root.geometry(f'{width}x{height}+200+200')
        self.root.resizable(FALSE, FALSE)
        self.article = article
        self.grab_focus()
        self.field = ('Python', 'CSS')

        self.save_btn = Button(self.root, text='Save', command=self.edit)
        self.l1 = Label(self.root, text='Field of knowledge:')
        self.field_of_knowledge = Combobox(self.root, values=self.field, state='readonly')
        self.l3_description = Label(self.root, text='Description:', justify=LEFT)
        self.l4_question = Label(self.root, text='Question:', justify=LEFT)
        self.ent2_question = Entry(self.root, width=140, bd=1)
        self.st = ScrolledText(self.root, width=104, height=25, bd=1, padx=5, pady=8, wrap=WORD)
        self.l5_success = Label(self.root, text='Successfully added:', justify=LEFT, wraplength=560, font='Consolas 14')
        self.draw_widgets()

    def draw_widgets(self):
        text_list = self.article.get_current()
        self.ent2_question.configure(textvariable=StringVar(value=str(text_list[3])))
        self.st.insert(END, text_list[1])
        self.l1.place(x=10, y=20)
        self.field_of_knowledge.place(x=140, y=20)
        self.l4_question.place(x=10, y=60)
        self.ent2_question.place(x=140, y=60)
        self.l3_description.place(x=10, y=100)
        self.st.place(x=140, y=100)
        self.save_btn.place(x=40, y=180, width=60)

    def grab_focus(self):
        self.root.grab_set()

    def edit(self):
        text = self.st.get(1.0, END)
        fk = self.field_of_knowledge.current()
        question = self.ent2_question.get()
        if text != '' and str(fk) != "-1" and question != '':
            request_dict = {
                'full_text': self.st.get(1.0, END)[:-2],
                'field': self.field[self.field_of_knowledge.current()],
                'question': self.ent2_question.get(),
            }
            result = self.article.update_in_db(request_dict=request_dict,
                                               condition=('rowid', int(self.article.get_current()[0])))
            if result[0] is True:
                self.l5_success.configure(text="You successfully update you article")
            if result[0] is False:
                self.l5_success.configure(text=result[1])
        else:
            self.l5_success.configure(text="Please fill all field!")
        self.l5_success.place(x=136, y=565)
