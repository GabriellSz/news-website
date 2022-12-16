from markupsafe import Markup

class Markup_Creator():
    def __init__(self) -> None:
        pass

    def create_resume_markup(self, identifier:int, category:str, title:str, resume:str):
        self.resume_template = Markup(
            f"""
            <article class='news_resume'>
                <a class='news_link' onclick='open_news( { identifier } )' href='./news_page.html'>
                    <div class='resume_top'>
                        <h3 class='resume_category'> { category } </h3>
                        <h3 class='resume_title'> { title } </h3>
                    </div>
                    <div class='resume_content'>
                        <p> { resume } </p>
                    </div>
                </a>
            </article>
            """
        )
        return self.resume_template

    def create_content_markup(self, identifier:int, category:str, title:str, content:str):
        self.content_template = Markup(
            f"""
            <div class='page_title'>
                <h2 id='news_category'>● { category } </h2>
                <a href='./index.html'>↩ HOME</a>
            </div>
            <section class='news'>
                <h3 class='news_title'> { title } </h3>
                <pre> { content } </pre>
            </section>
            """
        )
        return self.content_template