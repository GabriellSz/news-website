const recent_news_page = document.getElementById("recent_news");

const recent_news = [];

recent_news.forEach((news) => {
  recent_news_page.innerHTML += news.resume_markup
});