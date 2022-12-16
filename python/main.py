from pathlib import Path
from markup_creator import Markup_Creator
from news_creator import News

texto = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Praesent varius, dolor in ullamcorper gravida, est risus fringilla urna, at hendrerit sapien tortor vel felis. 
Maecenas consectetur dolor fringilla ex hendrerit convallis at sit amet erat. 
Nam ut enim dapibus, hendrerit turpis quis, pharetra odio. Nunc libero ipsum, dapibus facilisis tortor sed, maximus auctor purus. 
Duis et felis vel felis auctor consectetur ut eget nulla. 
Sed mollis commodo mi, vitae tincidunt tellus facilisis eu. 
Praesent sagittis erat sed enim rutrum rhoncus. 
Pellentesque hendrerit, quam quis ullamcorper egestas, felis quam fringilla sapien, quis tincidunt sem dolor quis risus.

Sed ac mauris quis enim ornare hendrerit sed eget enim. 
In ultricies ipsum eu lacus sagittis lacinia. Nulla id maximus magna. 
Vestibulum eleifend, dolor ut molestie volutpat, sem dui facilisis nibh, vitae feugiat ipsum felis porttitor mi. 
Integer ultricies gravida est, a dictum neque imperdiet ac. 
Etiam interdum erat id ligula bibendum, sit amet pellentesque erat tempus. 
Etiam dignissim porta sapien, consequat varius orci tincidunt in. 
Mauris pulvinar velit accumsan, blandit ex et, efficitur ex. 
Vivamus non euismod est, a viverra nulla. Nullam finibus risus ut felis ornare euismod. 
Integer ut enim dictum, egestas sapien nec, auctor mauris.

Sed non augue purus. Aliquam sollicitudin tempor purus, sit amet mattis neque suscipit vitae. 
Aenean est ex, posuere sed magna et, porttitor egestas turpis. 
Aenean pellentesque dolor eu purus sodales tempus quis at tellus. 
Donec elementum sed orci sit amet aliquam. Duis eget commodo arcu. 
Integer ullamcorper, risus vitae molestie posuere, ligula justo ultrices dolor, ut auctor ex augue in ipsum. 
Quisque sed blandit magna. Morbi nec metus vitae sem pulvinar blandit in sit amet urna.
Aenean aliquam nisi tempor velit vulputate, sit amet pretium quam facilisis."""

noticia = News(1, "Esportes", "Brasil eliminado", texto)

mc = Markup_Creator()

noticia.resume_markup = mc.create_resume_markup(noticia.identifier, noticia.category, noticia.title, noticia.resume)
noticia.content_markup = mc.create_resume_markup(noticia.identifier, noticia.category, noticia.title, noticia.content)

noticia.create_dict_object()
noticia.convert_to_json(noticia.dict_object)

file_path = Path("../db.json")

if file_path.exists():
    json_file = open(file_path)
else:
    raise Exception(f"cant find {file_path}")

json_file += noticia.json_string

json_file.close()