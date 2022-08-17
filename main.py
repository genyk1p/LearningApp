from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Combobox
from article import Article
from child_window import ChildWindow
from user import User
import datetime

article = Article()
article.load_from_db()
user = User()


def get_art_user_text(article_id):
    if user.get_from_db(int(article_id)) is not None:
        user_data = user.get_from_db(int(article_id))
        return f"In the process of studying, Learning progress = {user_data[1]}, Next show = {user_data[2][:16]}\n\n"
    else:
        return "Not studied\n\n"


class Window:

    def __init__(self, width, height, title='MyWindow'):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f'{width}x{height}+200+200')
        self.root.resizable(FALSE, FALSE)

        # Initialization all project widgets
        self.l_field_of_knowledge_studying_material = Label(self.root, text='Field of knowledge:')
        self.field_of_knowledge_list = ('Python', 'CSS')
        self.article_article_for_learning = []
        self.current_article_article_for_learning = None
        self.star_dict = {1: 3, 2: 6, 3: 12, 4: 24, 5: 48}
        self.introducing_text_en = "Hello you are in Learning application. This application will help you to learn new functions and methods. This application is made in the style of exam tickets, with the possibility of spaced repetitions of the material. When you say you know the material, it disappears for a certain amount of time and then reappears.\n1st level - will disappear for 3 days;\n2nd level - will disappear for 6 days;\n3rd level — for 12 days;\n4th level — for 24 days;\nLevel 5 — for 48 days.\n\n"
        self.introducing_text_ru = "Здравствуйте, вы находитесь в приложении Learning. Приложение поможет вам изучить новые функции и методы. Это приложение сделано по типу экзаменационных билетов, с возможностью интервальных повторений материала. Когда вы говорите, что знаете материал он исчезает на определенное время и потом снова появляется.\n1-й уровень — исчезнет на 3 дня;\n2-й уровень — исчезнет на 6 дней;\n3-й уровень — на 12 дней;\n4-й уровень — на 24 дня;\n5-й уровень — на 48 дней."

        # Initialization Adding articles widgets
        self.st_adding_articles = ScrolledText(self.root, width=104, height=28, bd=1, padx=5, pady=8, wrap=WORD)
        self.bt_add_adding_articles = Button(self.root, text='Add', command=self.add_new_article)
        self.l_description_adding_articles = Label(self.root, text='Please enter description:', justify=LEFT)
        self.l_question_adding_articles = Label(self.root, text='Please enter question:', justify=LEFT)
        self.l_success_adding_articles = Label(self.root, text='Successfully added:', justify=LEFT, wraplength=560,
                                               font='Consoles 14')
        self.ent_question_add_adding_articles = Entry(self.root, width=140, bd=1)
        self.comb_field_of_knowledge_add_art = Combobox(self.root, values=self.field_of_knowledge_list,
                                                        state='readonly')
        self.comb_field_of_knowledge_add_art.current(0)

        # Initialization Articles for learning widgets
        self.st_main_screen_articles_for_learning = ScrolledText(self.root, width=104, height=30, bd=1, padx=5, pady=8,
                                                                 wrap=WORD)
        self.st_articles_for_learning = ScrolledText(self.root, width=104, height=24, bd=1, padx=5, pady=8, wrap=WORD)
        self.bt_prev_articles_for_learning = Button(self.root, text='Prev', width=10,
                                                    command=self.action_bt_prev_articles_for_learning)
        self.bt_next_articles_for_learning = Button(self.root, text='Next', width=10,
                                                    command=self.action_bt_next_articles_for_learning)
        self.bt_add_articles_for_learning = Button(self.root, text='Add', width=10,
                                                   command=self.action_bt_add_articles_for_learning)
        self.bt_remove_articles_for_learning = Button(self.root, text='Remove', width=10,
                                                      command=self.action_bt_remove_articles_for_learning)
        self.bt_edit_articles_for_learning = Button(self.root, text='Edit', width=10,
                                                    command=self.action_bt_edit_articles_for_learning)
        self.bt_refresh_articles_for_learning = Button(self.root, text='Refresh', width=10,
                                                       command=self.action_bt_refresh_articles_for_learning)
        self.bt_delete_articles_for_learning = Button(self.root, text='Delete', width=10,
                                                      command=self.action_bt_delete_articles_for_learning)
        self.comb_field_of_knowledge = Combobox(self.root, values=self.field_of_knowledge_list, state='readonly')
        self.comb_field_of_knowledge.current(0)
        self.comb_field_of_knowledge.bind("<<ComboboxSelected>>", self.action_comb_field_of_knowledge)
        self.comb_field_of_knowledge_prev = self.comb_field_of_knowledge.current()
        self.l_lesson_progress_articles_for_learning = Label(self.root, text='Lesson_progress:', justify=LEFT)
        self.ent_lesson_progress_articles_for_learning = Entry(self.root, width=100, bd=1, state='readonly')
        self.l_question_articles_for_learning = Label(self.root, text='Question:', justify=LEFT)
        self.st_question_articles_for_learning = ScrolledText(self.root, width=104, height=2, bd=1, padx=5, pady=8,
                                                              wrap=WORD)
        self.l_description_articles_for_learning = Label(self.root, text='Description:', justify=LEFT)

        # Initialization studying the material widget
        self.l_description_studying_material = Label(self.root, text='Answer:', justify=LEFT)
        self.l_question_studying_material = Label(self.root, text='Question:', justify=LEFT)
        self.l_field_of_knowledge_studying_material = Label(self.root, text='Field of Knowledge', justify=LEFT)
        self.bt_i_know_studying_material = Button(self.root, text='Know', width=10,
                                                  command=self.action_bt_i_know_studying_material)
        self.bt_don_not_know_studying_material = Button(self.root, text="Don't know", width=10,
                                                        command=self.action_don_not_know_studying_material)
        self.bt_show_answer_studying_material = Button(self.root, text='Show answer', width=10,
                                                       command=self.action_bt_show_answer_studying_material)
        self.ent_field_of_knowledge_studying_material = Entry(self.root, width=140, bd=1, state='readonly')
        self.st_studying_material = ScrolledText(self.root, width=104, height=24, bd=1, padx=5, pady=8, wrap=WORD)
        self.st_question_studying_material = ScrolledText(self.root, width=104, height=2, bd=1, padx=5, pady=8,
                                                          wrap=WORD)

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def create_child(self, parm, width, height, title='title'):
        ChildWindow(self.root, parm, width, height, title)

    def draw_widgets(self):
        self.draw_menu()
        self.enter_screen()

    def draw_menu(self):
        menu_bar = Menu(self.root)
        menu_bar.add_command(label='Adding articles', command=self.adding_articles)
        menu_bar.add_command(label='Articles for learning', command=self.articles_for_learning)
        menu_bar.add_command(label='Studying the material', command=self.studying_the_material)
        self.root.configure(menu=menu_bar)

    # Drawing the home screen
    def enter_screen(self):
        self.st_main_screen_articles_for_learning.insert("1.0", self.introducing_text_en)
        self.st_main_screen_articles_for_learning.insert(END, self.introducing_text_ru)
        self.st_main_screen_articles_for_learning.place(x=125, y=30)
        self.st_main_screen_articles_for_learning.configure(state=DISABLED)

    # Adding a new article
    def adding_articles(self):
        # Replace all previous widgets
        self.disable_widgets_articles_for_learning()
        self.disable_widgets_studying_material()

        self.st_adding_articles.configure(state=NORMAL)
        self.st_adding_articles.delete(1.0, END)
        self.st_adding_articles.place(x=180, y=100)
        self.l_field_of_knowledge_studying_material.place(x=10, y=20)
        self.comb_field_of_knowledge_add_art.place(x=180, y=20)
        self.l_question_adding_articles.place(x=10, y=60)
        self.ent_question_add_adding_articles.place(x=180, y=60)
        self.l_description_adding_articles.place(x=10, y=100)
        self.bt_add_adding_articles.place(x=60, y=220, width=60)

    # Browse articles that you can choose to study
    def articles_for_learning(self):
        # Replace all previous widgets
        self.disable_widgets_adding_articles()
        self.disable_widgets_studying_material()

        self.draw_first_articles_for_learning()

    # Studying the material
    def studying_the_material(self):
        # Replace all previous widgets
        self.disable_widgets_articles_for_learning()
        self.disable_widgets_adding_articles()
        self.article_article_for_learning = article.article_for_learning()
        if self.article_article_for_learning == []:
            art_list = []
        else:
            art_list = self.article_article_for_learning.pop()
            self.current_article_article_for_learning = art_list
        self.draw_widget_studying_the_material(art_list, show_answer=False)


    def draw_first_articles_for_learning(self, comb_field_of_knowledge=0):
        article.load_from_db()
        self.comb_field_of_knowledge.current(comb_field_of_knowledge)
        self.st_articles_for_learning.configure(state=NORMAL)
        self.st_articles_for_learning.delete(1.0, END)
        art_list = article.get_first(self.field_of_knowledge_list[comb_field_of_knowledge])
        self.draw_widget_art_learn(art_list=art_list)

    # This function takes an article and draws widgets in the study section.
    def draw_widget_studying_the_material(self, art_list, show_answer=False):
        if art_list == []:
            self.disable_widgets_studying_material()
            self.st_studying_material.configure(state=NORMAL)
            self.st_studying_material.delete(1.0, END)
            self.st_studying_material.insert(END, 'You currently have no material to study')
            self.st_studying_material.place(x=125, y=30)
        else:
            description = art_list[1]
            self.st_studying_material.configure(state=NORMAL)
            self.st_studying_material.delete(1.0, END)
            self.st_studying_material.insert(END, description)
            self.st_question_studying_material.configure(state=NORMAL)
            self.st_question_studying_material.delete(1.0, END)
            self.st_question_studying_material.insert(END, art_list[3])
            if show_answer is True:
                self.st_studying_material.place(x=180, y=140)
            self.l_field_of_knowledge_studying_material.place(x=10, y=20)
            self.ent_field_of_knowledge_studying_material.place(x=180, y=20)
            self.ent_field_of_knowledge_studying_material.configure(textvariable=StringVar(value=art_list[2]))
            self.l_question_studying_material.place(x=10, y=60)
            self.st_question_studying_material.place(x=180, y=60)
            self.l_description_studying_material.place(x=10, y=140)
            self.st_studying_material.configure(state=DISABLED)
            self.st_question_studying_material.configure(state=DISABLED)
            self.bt_i_know_studying_material.place(x=425, y=560)
            self.bt_don_not_know_studying_material.place(x=510, y=560)
            self.bt_show_answer_studying_material.place(x=595, y=560)

    # This function takes an article and draws widgets in the article selection section to explore.
    def draw_widget_art_learn(self, art_list):
        self.l_lesson_progress_articles_for_learning.place(x=10, y=20)
        self.ent_lesson_progress_articles_for_learning.configure(textvariable=StringVar(value=get_art_user_text(art_list[0])))
        self.ent_lesson_progress_articles_for_learning.place(x=180, y=20)
        self.l_question_articles_for_learning.place(x=10, y=60)
        self.st_question_articles_for_learning.configure(state=NORMAL)
        self.st_question_articles_for_learning.delete(1.0, END)
        self.st_question_articles_for_learning.insert(END, art_list[3])
        self.st_question_articles_for_learning.place(x=180, y=60)
        self.st_question_articles_for_learning.configure(state=DISABLED)
        self.l_description_articles_for_learning.place(x=10, y=140)
        self.st_articles_for_learning.configure(state=NORMAL)
        self.st_articles_for_learning.delete(1.0, END)
        self.st_articles_for_learning.insert(END, art_list[1])
        self.st_articles_for_learning.place(x=180, y=140)
        self.st_articles_for_learning.configure(state=DISABLED)

        self.l_field_of_knowledge_studying_material.place(x=835, y=10)
        self.comb_field_of_knowledge.place(x=950, y=10)
        self.bt_prev_articles_for_learning.place(x=255, y=560)
        self.bt_next_articles_for_learning.place(x=340, y=560)
        self.bt_add_articles_for_learning.place(x=425, y=560)
        self.bt_remove_articles_for_learning.place(x=510, y=560)
        self.bt_edit_articles_for_learning.place(x=595, y=560)
        self.bt_delete_articles_for_learning.place(x=680, y=560)
        self.bt_refresh_articles_for_learning.place(x=765, y=560)

        self.st_articles_for_learning.configure(state=DISABLED)

    # Displays the previous article in the select article to study section if the user clicks on the button prev
    def action_bt_prev_articles_for_learning(self):
        art_list = article.get_prev(
            field_of_knowledge=self.field_of_knowledge_list[self.comb_field_of_knowledge.current()])
        self.draw_widget_art_learn(art_list)

    def action_bt_next_articles_for_learning(self):
        art_list = article.get_next(
            field_of_knowledge=self.field_of_knowledge_list[self.comb_field_of_knowledge.current()])
        self.draw_widget_art_learn(art_list)

    # Adds an article to study
    def action_bt_add_articles_for_learning(self):
        art_list = article.get_current()
        if user.get_from_db(int(art_list[0])) is None:
            data = {
                'article_id': int(art_list[0]),
                'counter': 1,
                'next_show': datetime.datetime.now(),
            }
            user.add_to_db(data)
        self.draw_widget_art_learn(art_list=art_list)

    # Removes an article from the list of articles to study.
    def action_bt_remove_articles_for_learning(self):
        if user.delete_from_db(('article_id', article.get_current()[0]))[0] is True:
            user.load_from_db()
            art_list = article.get_current()
            self.draw_widget_art_learn(art_list=art_list)

    # Opens a new window for editing the article
    def action_bt_edit_articles_for_learning(self):
        self.create_child(article, 1100, 600, 'EditArticle')

    # After the article has been edited, updates the article class instance and re-renders the updated article
    def action_bt_refresh_articles_for_learning(self):
        index = article.counter
        article.load_from_db()
        article.counter = index
        self.st_articles_for_learning.configure(state=NORMAL)
        self.st_articles_for_learning.delete(1.0, END)
        art_list = article.get_current()
        for index, value in enumerate(self.field_of_knowledge_list):
            if value == art_list[3]:
                self.comb_field_of_knowledge.current(index)
        self.draw_widget_art_learn(art_list=art_list)

    # Deletes an article and displays the closest article in its place.
    def action_bt_delete_articles_for_learning(self):
        field_of_knowledge = self.field_of_knowledge_list[self.comb_field_of_knowledge.current()]
        index = article.counter
        current_article = article.get_current()
        article1 = None
        for i in range(0, article.max_counter):
            value = article.get_prev(field_of_knowledge=field_of_knowledge)
            if value[3] == field_of_knowledge:
                if value != current_article:
                    article1 = value
                    break
        if article1 is None:
            article.counter = index
            for i in range(0, article.max_counter):
                value = article.get_next(field_of_knowledge=field_of_knowledge)
                if value[3] == field_of_knowledge:
                    if value != current_article:
                        article1 = value
                        break
        if article1 is None:
            article1 = (0, '', '', '', '', 0)
        if user.delete_from_db(('article_id', current_article[0]))[0] is True:
            result = article.delete_from_db(('rowid', current_article[0]))
            if result[0] is True:
                article.load_from_db()
                for i in article.data:
                    if i[3] == article1[3]:
                        article.counter += 1
                art_list = article1
                self.draw_widget_art_learn(art_list=art_list)
        else:
            print('Error')

    def add_new_article(self):
        if self.st_adding_articles.get(1.0, END) == '\n' or self.ent_question_add_adding_articles.get() == '':
            self.l_success_adding_articles.configure(text="Please fill all field!")
        else:
            article_dict = {
                'full_text': self.st_adding_articles.get(1.0, END),
                'field': self.field_of_knowledge_list[self.comb_field_of_knowledge.current()],
                'question': self.ent_question_add_adding_articles.get()
            }
            result = article.add_to_db(article_dict)
            if result[0] is True:
                self.l_success_adding_articles.configure(text='Successfully added:')
                self.st_adding_articles.delete(1.0, END)
                self.ent_question_add_adding_articles.delete(0, END)
            else:
                self.l_success_adding_articles.configure(text="Error while working with SQLite " + str(result[1]))
        self.l_success_adding_articles.place(x=180, y=565)
        article.load_from_db()

    def action_comb_field_of_knowledge(self, event):
        if self.comb_field_of_knowledge_prev != self.comb_field_of_knowledge.current():
            self.comb_field_of_knowledge_prev = self.comb_field_of_knowledge.current()
            self.draw_first_articles_for_learning(self.comb_field_of_knowledge.current())

    def action_bt_i_know_studying_material(self):
        user_data = user.get_from_db(self.current_article_article_for_learning[0])
        new_time = datetime.datetime.strptime(user_data[2], "%Y-%m-%d %H:%M:%S.%f") + datetime.timedelta(days=self.star_dict[user_data[1]])
        new_user_data = {
            'article_id': user_data[0],
            'counter': user_data[0] + 1,
            'next_show': str(new_time),
        }
        if user.update_in_db(new_user_data, ('article_id', user_data[0]))[0] is True:
            if self.article_article_for_learning == []:
                self.article_article_for_learning = article.article_for_learning()
                if self.article_article_for_learning == []:
                    art_list = []
            if self.article_article_for_learning != []:
                art_list = self.article_article_for_learning.pop()
                self.current_article_article_for_learning = art_list
            self.draw_widget_studying_the_material(art_list, show_answer=False)
        else:
            print('error')

    def action_don_not_know_studying_material(self):
        if self.article_article_for_learning == []:
            self.article_article_for_learning = article.article_for_learning()
            if self.article_article_for_learning == []:
                art_list = []
        if self.article_article_for_learning != []:
            art_list = self.article_article_for_learning.pop()
            self.current_article_article_for_learning = art_list
        self.draw_widget_studying_the_material(art_list, show_answer=False)

    def action_bt_show_answer_studying_material(self):
        art_list = self.current_article_article_for_learning
        self.draw_widget_studying_the_material(art_list, show_answer=True)

    # Removes widgets from a section adding_articles
    def disable_widgets_adding_articles(self):
        self.st_main_screen_articles_for_learning.place_forget()
        self.st_adding_articles.place_forget()
        self.comb_field_of_knowledge.place_forget()
        self.l_field_of_knowledge_studying_material.place_forget()
        self.l_question_adding_articles.place_forget()
        self.ent_question_add_adding_articles.place_forget()
        self.l_description_adding_articles.place_forget()
        self.bt_add_adding_articles.place_forget()
        self.l_success_adding_articles.place_forget()
        self.comb_field_of_knowledge_add_art.place_forget()

    # Removes widgets from a section articles_for_learning
    def disable_widgets_articles_for_learning(self):
        self.st_main_screen_articles_for_learning.place_forget()
        self.l_field_of_knowledge_studying_material.place_forget()
        self.comb_field_of_knowledge.place_forget()
        self.l_lesson_progress_articles_for_learning.place_forget()
        self.st_articles_for_learning.place_forget()
        self.bt_prev_articles_for_learning.place_forget()
        self.bt_next_articles_for_learning.place_forget()
        self.bt_add_articles_for_learning.place_forget()
        self.bt_edit_articles_for_learning.place_forget()
        self.bt_refresh_articles_for_learning.place_forget()
        self.bt_delete_articles_for_learning.place_forget()
        self.bt_remove_articles_for_learning.place_forget()
        self.ent_lesson_progress_articles_for_learning.place_forget()
        self.l_question_articles_for_learning.place_forget()
        self.st_question_articles_for_learning.place_forget()
        self.l_description_articles_for_learning.place_forget()

    # Removes widgets from a section studying_material
    def disable_widgets_studying_material(self):
        self.l_description_studying_material.place_forget()
        self.l_question_studying_material.place_forget()
        self.bt_i_know_studying_material.place_forget()
        self.bt_don_not_know_studying_material.place_forget()
        self.bt_show_answer_studying_material.place_forget()
        self.st_question_studying_material.place_forget()
        self.st_studying_material.place_forget()
        self.l_field_of_knowledge_studying_material.place_forget()
        self.ent_field_of_knowledge_studying_material.place_forget()


if __name__ == "__main__":
    window = Window(1100, 600, 'LearningApp')
    window.run()
