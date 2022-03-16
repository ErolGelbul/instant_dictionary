import justpy as jp
from webapp import layout, page

class Home(page.Page):
    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)

        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen p-2")
        jp.Div(a=div, text="This is the Home page!", classes="text-4xl m-2")
        jp.Div(a=div, text="""
        Welcome to Instant Dictionary!
        Please navigate to the dictionary page to search a term.
        Find out more on our about page.
        """, classes="break-normal md:break-all text-lg")

        return wp